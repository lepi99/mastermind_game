from ultralytics import YOLO

model = YOLO("best.pt")
results = model.predict("images/Mastermind_cover1.jpg")
result = results[0]
print("aaaaaaaaaaaaaaaaaaaaa")
print(len(result.boxes))
box = result.boxes[0]

print("Object type:", box.cls)
print("Coordinates:", box.xyxy)
print("Probability:", box.conf)

cords = box.xyxy[0].tolist()
class_id = box.cls[0].item()
conf = box.conf[0].item()
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)

print(result.names)

for box in result.boxes:
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  print("Object type:", class_id)
  print("Coordinates:", cords)
  print("Probability:", conf)
  print("---")