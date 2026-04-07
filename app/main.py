import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import config

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def check_health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=config.app_connection.HOST,
        port=config.app_connection.PORT,
        reload=True,
    )
