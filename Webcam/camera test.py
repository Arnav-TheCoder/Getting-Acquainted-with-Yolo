import cv2

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        print("Couldn't access webcam.")
        break

    cv2.imshow("Laptop Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()