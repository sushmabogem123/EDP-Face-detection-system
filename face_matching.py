import cv2
import os
import numpy as np
import csv
from datetime import datetime

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

person_name = "Sushma"

# Load known faces
for filename in os.listdir("known_faces"):

    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        path = os.path.join("known_faces", filename)
        image = cv2.imread(path)

        if image is None:
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        detected_faces = face_cascade.detectMultiScale(
            gray,
            1.1,
            5
        )

        for (x, y, w, h) in detected_faces:
            face = gray[y:y+h, x:x+w]
            faces.append(face)
            labels.append(0)

if len(faces) == 0:
    print("No faces found in known images.")
    exit()

# Train recognizer
recognizer.train(faces, np.array(labels))

print("Known face loaded successfully!")
print("Starting webcam...")

# Create attendance file if it doesn't exist
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time", "Status"])

# Prevent repeated attendance
attendance_marked = False

# Open webcam
camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        print("Could not access webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(
        gray,
        1.1,
        5
    )

    for (x, y, w, h) in detected_faces:

        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)

        if confidence < 100:

            text = f"{person_name} - Matched"

            # Mark attendance only once
            if not attendance_marked:

                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                with open(attendance_file, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [person_name, date, time, "Present"]
                    )

                attendance_marked = True

                print("Attendance marked successfully!")

        else:
            text = "Unknown"

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()