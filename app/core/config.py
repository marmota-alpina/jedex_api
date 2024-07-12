from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str
    address_service_url: str

    def __init__(self):
        super().__init__()

    class Config:
        env_file = ".env"


settings = Settings()
