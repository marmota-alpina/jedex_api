import requests

from app.core.config import settings
from app.schemas.distance import DistanceResponse


class AddressService:
    @staticmethod
    def get_distance(origin: str, destination: str) -> DistanceResponse | None:
        address_service_url = settings.address_service_url
        print(f"{address_service_url}/geolocation/distance/from/{origin}/to/{destination}")
        response = requests.get(f"{address_service_url}/geolocation/distance/from/{origin}/to/{destination}")
        if response.status_code == 200:
            data = response.json()
            return DistanceResponse(
                origin=data['from_address']['postal_code'],
                destination=data['to_address']['postal_code'],
                distance=data['distance'],
                distance_unit=data['unit']

            )
        return None
