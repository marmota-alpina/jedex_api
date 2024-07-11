import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import Optional, Type
from app.models.contract import Contract
from app.models.postal_code_range import PostalCodeRange
from app.schemas.contract import ContractCreate, ContractUpdate
from app.services.company_service import CompanyService


class ContractService:
    def __init__(self, session: Session, company_service: CompanyService):
        self.session = session
        self.company_service = company_service

    def create_contract(self, contract_data: ContractCreate) -> Contract:
        company = self.company_service.get_company(contract_data.company_id)
        if not company:
            raise ValueError(f"Company with id {contract_data.company_id} not found")

        contract = Contract(contract_id=str(uuid.uuid4()), **contract_data.dict(exclude={'ranges'}))

        try:
            with self.session.begin_nested():
                self.session.add(contract)
                self.session.flush()  # Force commit to get the contract ID

                if contract_data.ranges:
                    for range_data in contract_data.ranges:
                        postal_code_range = PostalCodeRange(
                            postal_code_range_id=str(uuid.uuid4()),
                            contract_id=contract.id,
                            **range_data.dict()
                        )
                        self.session.add(postal_code_range)

                self.session.commit()
        except IntegrityError as e:
            self.session.rollback()
            raise IntegrityError(f"Integrity error creating contract", params=e.params, orig=e.orig)
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Internal error creating contract")

        return contract

    def get_contracts(self) -> list[Type[Contract]]:
        return self.session.query(Contract).all()

    def get_contract_by_id(self, contract_id: str) -> Optional[Contract]:
        return self.session.query(Contract).filter(contract_id == Contract.id).first()

    def update_contract(self, contract_id: str, contract_data: ContractUpdate) -> Optional[Contract]:
        contract = self.get_contract_by_id(contract_id)
        if not contract:
            return None

        for key, value in contract_data.dict(exclude_unset=True).items():
            setattr(contract, key, value)

        postal_code_ranges = self.session.query(PostalCodeRange).filter(
            contract_id == PostalCodeRange.contract_id,
        ).all()

        for range_data in contract_data.ranges or []:
            postal_code_range = next((r for r in postal_code_ranges if
                                      range_data.start_postal_code == r.start_postal_code
                                      and range_data.end_postal_code == r.end_postal_code), None)
            if postal_code_range:
                for key, value in range_data.dict(exclude_unset=True).items():
                    setattr(postal_code_range, key, value)
            else:
                postal_code_range = PostalCodeRange(
                    postal_code_range_id=str(uuid.uuid4()),
                    contract_id=contract.id,
                    **range_data.dict()
                )
                self.session.add(postal_code_range)
        self.session.flush()
        self.session.commit()

        return contract

    def delete_contract(self, contract_id: str) -> bool:
        contract = self.session.query(Contract).filter(contract_id == Contract.id).first()
        if not contract:
            return False

        self.session.query(PostalCodeRange).filter(contract_id == PostalCodeRange.contract_id).delete()
        self.session.delete(contract)
        self.session.commit()

        return True
