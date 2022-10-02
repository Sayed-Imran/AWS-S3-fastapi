from scripts.services.images_service import image_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(image_router)
