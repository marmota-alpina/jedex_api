from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from app.core.dependencies import get_contract_service
from app.schemas.contract import ContractCreate, ContractUpdate, Contract
from app.services.contract_service import ContractService

router = APIRouter()


@router.post("/", response_model=Contract, status_code=status.HTTP_201_CREATED)
def create_contract(
        contract_data: ContractCreate,
        contract_service: ContractService = Depends(get_contract_service)
):
    try:
        created_contract = contract_service.create_contract(contract_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return created_contract


@router.get("/", response_model=List[Contract])
def get_contracts(
        contract_service: ContractService = Depends(get_contract_service)
):
    contracts = contract_service.get_contracts()
    return contracts


@router.get("/{contract_id}", response_model=Contract)
def get_contract(
        contract_id: str,
        contract_service: ContractService = Depends(get_contract_service)
):
    contract = contract_service.get_contract_by_id(contract_id)
    if not contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")
    return contract


@router.put("/{contract_id}", response_model=Contract)
def update_contract(
        contract_id: str,
        contract_data: ContractUpdate,
        contract_service: ContractService = Depends(get_contract_service)
):
    updated_contract = contract_service.update_contract(contract_id, contract_data)
    if not updated_contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")
    return updated_contract


@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contract(
        contract_id: str,
        contract_service: ContractService = Depends(get_contract_service)
):
    success = contract_service.delete_contract(contract_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found")
    return None
