from fastapi import APIRouter, UploadFile, File, HTTPException
from app.service.yoloService import *
from app.service.fileService import *

router = APIRouter()

# @router.post("/predict")
@router.post("/predict")
async def post_predict(file: UploadFile = File(...)):
    return await YoloService().service_yolo(file)

@router.get("/download/{filename}")
async def post_download(filename: str):
    # filename = UUID_label_x_y_w_h_conf.jpg
    # 서버에 저장된 파일을 클라이언트에게 반환합니다.
    return service_file(filename)
