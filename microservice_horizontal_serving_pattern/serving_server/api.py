import io
import datetime
import os

from fastapi import APIRouter, File
from PIL import Image
import requests

router = APIRouter()
inference_server_info = {
    "ip": ["15.164.49.19", "15.164.49.19"],
    "port": ["8001", "8002"]
}
os.makedirs("./data", exist_ok=True)

@router.post("/predict")
async def predict_results(
    file: bytes = File(...)
):
    input_image = Image.open(io.BytesIO(file)).convert("RGB")

    file_name = f"./data/{datetime.date.today().isoformat()}_image.jpg"
    input_image.save(file_name)

    responses = []
    for ip, port in zip(inference_server_info["ip"], inference_server_info["port"]):
        headers = {'accept': 'application/json',}
        files = {'file': open(file_name, 'rb')}
        response = requests.post(f'http://{ip}:{port}/api/predict', headers=headers, files=files)
        responses.append(response.json())

    return responses