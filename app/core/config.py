import os 

class Settings:
    APP_NAME: str = "MeterFlow API"
    SECRET_KEY: str = os.getenv("METERFLOW_SECRET_KEY","dev-secret-change-in-prod")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DB_PATH: str = os.getenv("METERFLOW_DB_PATH","meterflow.db")

    INITIAL_FREE_CREDITS: int = 100
    PRO_UPGRADE_CREDITS: int = 5000

    FEATURE_COSTS: dict[str,int] = {
        "sms_sent": 1,
        "email_sent": 1,
        "ai_reference": 5,
    }

    RATE_LIMITS_PER_MINUTE: dict[str,int] = {
        "FREE": 10,
        "PRO": 100,
    }

settings = Settings()
