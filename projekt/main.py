import cv2 as cv
import os

# Sprawdzenie czy pliki istnieją w folderze
print(f"Plik PB: {os.path.exists('frozen_inference_graph.pb')}")
print(f"Plik PBTXT: {os.path.exists('ssd_mobilenet_v2_coco_2018_03_29.pbtxt')}")

try:
    # Próba wczytania sieci
    net = cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
    print("Sukces! Model załadowany poprawnie.")
except Exception as e:
    print(f"Błąd ładowania: {e}")