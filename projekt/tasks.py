import cv2 as cv
import os
from celery import Celery


app = Celery(
    'tasks', 
    broker='pyamqp://guest@rabbitmq//', 
    backend='rpc://')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
net = cv.dnn.readNetFromTensorflow(
    os.path.join(BASE_DIR, 'frozen_inference_graph.pb'),
    os.path.join(BASE_DIR, 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
)

@app.task
def analyze_image_task(image_path):
    img = cv.imread(image_path)
    if img is None: 
        return "Błąd: Nie wczytano obrazu"
    
    blob = cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True)
    net.setInput(blob)
    detections = net.forward()

    count = 0
    for i in range(detections.shape[2]):
        score = float(detections[0, 0, i, 2])
        if score > 0.4 and int(detections[0, 0, i, 1]) == 1:
            count += 1
            
    return count 