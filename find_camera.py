import cv2

print("Checking cameras 0, 1, 2 one by one.")
print("A window will open for each. Press ANY KEY to go to the next one.")
print("Remember which index shows your USB external camera.\n")

for i in [0, 1, 2]:
    cap = cv2.VideoCapture(i)
    if not cap.isOpened():
        print(f"Index {i}: not available")
        continue

    # warm up
    for _ in range(10):
        cap.read()

    ret, frame = cap.read()
    cap.release()

    if not ret or frame is None:
        print(f"Index {i}: opened but no frame")
        continue

    label = f"INDEX {i}  |  Press any key for next"
    cv2.putText(frame, label, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.imshow(f"Camera Index {i}", frame)
    print(f"Showing index {i} - press any key in the window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("\nDone. Tell Kiro which index was your USB external camera.")
