from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_company_service
from app.schemas.company import CompanyResponse, CompanyCreate, CompanyUpdate
from app.services.company_service import CompanyService

router = APIRouter()


@router.post("/", response_model=CompanyResponse)
def create_company(company_data: CompanyCreate, company_service: CompanyService = Depends(get_company_service)):
    return company_service.create_company(company_data)


@router.get("/", response_model=list[CompanyResponse])
def read_companies(company_service: CompanyService = Depends(get_company_service)):
    return company_service.get_companies()


@router.get("/{company_id}", response_model=CompanyResponse)
def read_company(company_id: str, company_service: CompanyService = Depends(get_company_service)):
    company = company_service.get_company(company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(company_id: str, company_data: CompanyUpdate,
                   company_service: CompanyService = Depends(get_company_service)):
    company = company_service.update_company(company_id, company_data)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.delete("/{company_id}", response_model=bool)
def delete_company(company_id: str, company_service: CompanyService = Depends(get_company_service)):
    success = company_service.delete_company(company_id)
    if not success:
        raise HTTPException(status_code=404, detail="Company not found")
    return success
