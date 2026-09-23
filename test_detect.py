import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# warm up camera
for _ in range(30):
    cap.read()

ret, frame = cap.read()
cap.release()

if not ret:
    print("ERROR: Cannot read from camera 0")
else:
    print("Frame shape:", frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for neighbors in [5, 3, 2, 1]:
        faces = cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=neighbors, minSize=(30, 30)
        )
        count = len(faces) if len(faces) > 0 else 0
        print(f"minNeighbors={neighbors}: faces found = {count}")
        if count > 0:
            print(f"  Face box: {faces[0]}")

    # show the frame with any detections
    faces = cascade.detectMultiScale(gray, 1.1, 1, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.imshow("Detection Test - press any key", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
