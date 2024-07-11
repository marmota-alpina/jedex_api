from app.core.constants import TRANSPORT_DURATION_DEFAULT
from app.core.enums import DurationUnit, WeightUnit
from app.schemas.freight import FreightRequest, FreightResponse
from app.services.address_service import AddressService
from app.services.contract_service import ContractService


class FreightService:
    def __init__(self, contract_service: ContractService):
        self.contract_service = contract_service

    def calculate_freight(self, freight_data: FreightRequest) -> FreightResponse:
        # Get the distance between the origin and destination postal codes
        distance_response = AddressService.get_distance(
            freight_data.origin_postal_code, freight_data.destination_postal_code)
        if distance_response is None:
            raise ValueError("Distance could not be estimated")

        # Retrieve the contract by its ID
        contract = self.contract_service.get_contract_by_id(freight_data.contract_id)
        if contract is None:
            raise ValueError("Contract could not be retrieved")

        # Check if there's a postal code range that matches the origin and destination postal codes
        postal_code_range = next(
            (postal_range for postal_range in contract.postal_code_ranges if
             postal_range.start_postal_code <= freight_data.destination_postal_code <= postal_range.end_postal_code),
            None
        )

        if postal_code_range is None:
            raise ValueError("No matching postal code range found in the contract")

        # Calculate dimensional weight
        volume = freight_data.dimensions.length * freight_data.dimensions.width * freight_data.dimensions.height
        dimensional_weight = volume / contract.dimensional_factor

        # Use the greatest of the actual weight or dimensional weight
        chargeable_weight = max(freight_data.weight, dimensional_weight)

        # Calculate the freight value using the distance and rate per km
        freight_value = distance_response.distance * postal_code_range.delivery_rate_per_kg * chargeable_weight

        return FreightResponse(
            shipment_type=freight_data.shipment_type,
            freight_cost=round(freight_value, 2),
            duration=TRANSPORT_DURATION_DEFAULT,
            duration_unit=DurationUnit.days,
            chargeable_weight=chargeable_weight,
            weight_unit=WeightUnit.kg,
            distance=distance_response
        )
