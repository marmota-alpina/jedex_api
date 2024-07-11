from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.company_service import CompanyService
from app.services.contract_service import ContractService
from app.services.freight_service import FreightService


def get_company_service(db: Session = Depends(get_db)) -> CompanyService:
    return CompanyService(session=db)


def get_contract_service(db: Session = Depends(get_db), company_service: CompanyService = Depends(get_company_service)
                         ) -> ContractService:
    return ContractService(session=db, company_service=company_service)


def get_freight_service(contract_service: ContractService = Depends(get_contract_service)) -> FreightService:
    return FreightService(contract_service)
