from ultralytics import YOLO
import cv2

model = YOLO('../model/yolov8n.pt')
results = model("Images/img.png", show=True)
cv2.waitKey(0)
