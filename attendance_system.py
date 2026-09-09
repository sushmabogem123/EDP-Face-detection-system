import cv2
import csv
import os
import numpy as np
from datetime import datetime

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()

known_faces_folder = "known_faces"

faces = []
labels = []

for filename in os.listdir(known_faces_folder):

    path = os.path.join(known_faces_folder, filename)

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        continue

    faces.append(image)
    labels.append(0)

if len(faces) == 0:
    print("No known faces found!")
    exit()

recognizer.train(faces, np.array(labels, dtype=np.int32))

print("Face database loaded successfully.")



attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):

    with open(attendance_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Date",
            "Time",
            "Status"
        ])


def mark_attendance(name):

    today = datetime.now().strftime("%Y-%m-%d")

    with open(attendance_file, "r", newline="") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            if len(row) >= 2:

                if row[0] == name and row[1] == today:

                    return

    current_time = datetime.now().strftime("%H:%M:%S")

    with open(attendance_file, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            today,
            current_time,
            "Present"
        ])

    print("Attendance marked for:", name)



camera = cv2.VideoCapture(0)

if not camera.isOpened():

    print("Camera could not be opened.")
    exit()

print("Camera started.")
print("Press Q to exit.")


while True:

    ret, frame = camera.read()

    if not ret:

        print("Unable to read camera.")
        break

   
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.equalizeHist(gray)

   
    detected_faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    
    for (x, y, w, h) in detected_faces:

        face = gray[y:y+h, x:x+w]

        try:

            label, confidence = recognizer.predict(face)

            # Lower confidence = better match
            if confidence < 100:

                name = "Sushma"
                status = "Present"

                mark_attendance(name)

            else:

                name = "Unknown"
                status = "Not Recognized"

        except:

            name = "Unknown"
            status = "Not Recognized"

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # Display status
        cv2.putText(
            frame,
            status,
            (x, y + h + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        "Faces detected: " + str(len(detected_faces)),
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Week 6-7 Attendance System",
        frame
    )

    # Press Q in webcam window
    if cv2.waitKey(1) & 0xFF == ord("q"):

        break



camera.release()

cv2.destroyAllWindows()

print("Attendance system stopped.")