from fastapi import APIRouter
from app.api.v1.endpoints import calculate_freight, company, contract

response_status = {
    200: {"description": "Success"},
    422: {"description": "Validation Error"},
    404: {"description": "Not found"},
    500: {"description": "Internal server error"},
}
api_router = APIRouter(responses=response_status)
api_router.include_router(calculate_freight.router, prefix="/freight", tags=["Freight"])
api_router.include_router(company.router, prefix="/company", tags=["Company"])
api_router.include_router(contract.router, prefix="/contract", tags=["Contract"])
