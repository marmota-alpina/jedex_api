from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str

    def __init__(self):
        super().__init__()
        print(self.database_url)

    class Config:
        env_file = ".env"


settings = Settings()
