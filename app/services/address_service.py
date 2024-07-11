import requests

from app.schemas.distance import DistanceResponse


class AddressService:

    @staticmethod
    def get_distance(origin: str, destination: str) -> DistanceResponse | None:
        response = requests.get(f"http://0.0.0.0/geolocation/distance/from/{origin}/to/{destination}")
        if response.status_code == 200:
            data = response.json()
            return DistanceResponse(
                origin=data['from_address']['postal_code'],
                destination=data['to_address']['postal_code'],
                distance=data['distance'],
                distance_unit=data['unit']

            )
        return None
