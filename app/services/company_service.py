import uuid
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyService:
    def __init__(self, session: Session):
        self.session = session

    def create_company(self, company_data: CompanyCreate) -> Company:
        company = Company(company_id=str(uuid.uuid4()), **company_data.dict())
        self.session.add(company)
        self.session.commit()
        return company

    def get_company(self, company_id: str) -> Company | None:
        return self.session.query(Company).filter(company_id == Company.id).first()

    def update_company(self, company_id: str, company_data: CompanyUpdate) -> Company:
        company = self.get_company(company_id)
        if company:
            for key, value in company_data.dict(exclude_unset=True).items():
                setattr(company, key, value)
            self.session.commit()
        return company

    def delete_company(self, company_id: str) -> bool:
        company = self.get_company(company_id)
        if company:
            self.session.delete(company)
            self.session.commit()
            return True
        return False

    def get_companies(self):
        return self.session.query(Company).all()
