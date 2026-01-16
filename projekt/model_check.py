import cv2 as cv
import os


image_path = 'osoby.jpg'
model_pb = 'frozen_inference_graph.pb'
model_pbtxt = 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt'

def main():
    if not os.path.exists(image_path):
        print(f"BŁĄD: Nie znaleziono pliku {image_path}")
        return
    if not os.path.exists(model_pb) or not os.path.exists(model_pbtxt):
        print("BŁĄD: Nie znaleziono plików modelu (.pb lub .pbtxt)")
        return

    print("Wczytywanie modelu...")
    net = cv.dnn.readNetFromTensorflow(model_pb, model_pbtxt)
    
    img = cv.imread(image_path)
    rows, cols = img.shape[:2]
    print(f"Wczytano obraz: {cols}x{rows} px")

    blob = cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True)
    net.setInput(blob)
    
    print("Analizowanie...")
    detections = net.forward()

 
    count = 0
    for i in range(detections.shape[2]):
        confidence = float(detections[0, 0, i, 2])
        class_id = int(detections[0, 0, i, 1])

        
        if confidence > 0.4 and class_id == 1:
            count += 1
            
            left = int(detections[0, 0, i, 3] * cols)
            top = int(detections[0, 0, i, 4] * rows)
            right = int(detections[0, 0, i, 5] * cols)
            bottom = int(detections[0, 0, i, 6] * rows)

           
            cv.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

            
            label = f"Osoba: {confidence * 100:.1f}%"
            label_size, base_line = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            
           
            y_label = max(top, label_size[1] + 10)
            cv.rectangle(img, (left, y_label - label_size[1] - 10), (left + label_size[0], y_label + base_line - 10), (255, 255, 255), cv.FILLED)
            cv.putText(img, label, (left, y_label - 7), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    print(f"--- SUKCES! ---")
    print(f"Znaleziono obiektów: {count}")

    
    output_file = 'model_wynik.jpg'
    cv.imwrite(output_file, img)
    print(f"Wynik zapisano jako: {output_file} (sprawdź folder projektu)")

    
    try:
        cv.imshow('Wynik detekcji', img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except:
        pass 

if __name__ == '__main__':
    main()