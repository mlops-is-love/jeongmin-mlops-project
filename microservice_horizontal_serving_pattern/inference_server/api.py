import io

from fastapi import APIRouter, File
import mlflow
import cv2
import numpy as np
from PIL import Image
from scipy.spatial import distance

default_model_uri = "runs:/8c76d321faa24dfd9d3c1d9a3e7d0d4d/tensorflow-model"
haarcascade_frontalface_default_path = '/workspace/haarcascade_frontalface_default.xml'

router = APIRouter()
model = mlflow.keras.load_model(default_model_uri)
face_model = cv2.CascadeClassifier(haarcascade_frontalface_default_path)

@router.get("/model/{run_id}/{model_name}")
def select_model(
    run_id: str,
    model_name: str,
):
    model_uri = f"runs:/{run_id}/{model_name}"
    model = mlflow.keras.load_model(model_uri)
    return "select model successful!"

@router.post("/predict")
async def predict_results(
    file: bytes = File(...)
):
    input_image = Image.open(io.BytesIO(file)).convert("RGB")

    img = cv2.cvtColor(np.array(input_image), cv2.IMREAD_GRAYSCALE)
    faces = face_model.detectMultiScale(img,scaleFactor=1.1, minNeighbors=4) #returns a list of (x,y,w,h) tuples
    
    mask_label = {0:'MASK',1:'NO MASK'}
    dist_label = {0:(0,255,0),1:(255,0,0)}

    results = {"is_mask": [], "bbox": []}
    if len(faces) >= 1:
        label = [0 for i in range(len(faces))]
        new_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #colored output image
        for i in range(len(faces)):
            (x,y,w,h) = faces[i]
            crop = new_img[y:y+h,x:x+w]
            crop = cv2.resize(crop,(128,128))
            crop = np.reshape(crop,[1,128,128,3])/255.0
            mask_result = model.predict(crop)
            # cv2.putText(new_img,mask_label[mask_result.argmax()],(x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,dist_label[label[i]],2)
            # cv2.rectangle(new_img,(x,y),(x+w,y+h),dist_label[label[i]],1)

            results["is_mask"].append(mask_label[mask_result.argmax()])
            results["bbox"].append([int(x), int(y), int(x+w), int(y+h)])

    return results
