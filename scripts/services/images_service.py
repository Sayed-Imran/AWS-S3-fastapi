from fastapi import APIRouter, status, UploadFile, File
from scripts.utils.s3_image_util import S3
from scripts.core.handlers.image_handler import ImageHandler

image_router = APIRouter(prefix='/api')


@image_router.post('/upload', status_code=status.HTTP_200_OK)
def upload_image(file: UploadFile = File(...)):
    image_handler = ImageHandler()
    resp = image_handler.upload_image(file,file.filename)
    print(resp)
    return {"success": True, 'url': resp}

@image_router.delete('/delete',status_code=status.HTTP_202_ACCEPTED)
def delete_image(filename: str):
    image_handler = ImageHandler()
    resp = image_handler.delete_image(filename)
    return resp
