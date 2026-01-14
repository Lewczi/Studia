from fastapi import FastAPI, UploadFile, File
from tasks import analyze_image_task
from celery.result import AsyncResult
import requests
import uuid
import os

app = FastAPI()


UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 3 - GET: Zdjęcie z dysku lokalnego
@app.get("/analyze")
async def analyze(path: str):
    task = analyze_image_task.delay(path)
    return {"task_id": str(task.id), "status": "Zakolejkowano (Lokalne)"}

# 4 - GET: Zdjęcie z Internetu (URL)
@app.get("/analyze_url")
async def analyze_url(url: str):
    # Pobieranie zdjęcia z sieci
    response = requests.get(url)
    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.jpg")
    with open(file_path, "wb") as f:
        f.write(response.content)
    
    task = analyze_image_task.delay(file_path)
    return {"task_id": str(task.id), "status": "Zakolejkowano (URL)"}

# 5 - POST: Przesyłanie zdjęcia przez klienta
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    task = analyze_image_task.delay(file_path)
    return {"task_id": str(task.id), "status": "Zakolejkowano (Upload)"}


@app.get("/status/{task_id}")
async def get_status(task_id: str):
    res = AsyncResult(task_id)
    return {
        "id": task_id, 
        "status": res.status, 
        "result": res.result if res.ready() else "Przetwarzanie..."
    }