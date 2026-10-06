from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Purchase Predictor"
    backend_port: int = 8080
    frontend_origin: str = "http://localhost:5173"

    class Config:
        env_file = ".env"


settings = Settings()
