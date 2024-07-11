from fastapi import APIRouter, HTTPException, Depends

from app.core.dependencies import get_freight_service
from app.schemas.freight import FreightResponse, FreightRequest
from app.services.freight_service import FreightService

router = APIRouter()


@router.post("/", response_model=FreightResponse)
def calculate_freight(request: FreightRequest, contract_service: FreightService = Depends(get_freight_service)):

    try:
        freight = contract_service.calculate_freight(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return freight
