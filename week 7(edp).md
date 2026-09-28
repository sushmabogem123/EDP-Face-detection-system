# Face Recognition Attendance System
## Week 7 and Week 8
# Week 7 - Logging and Edge Case Handling
## Objective
To implement attendance logging and test the system under different conditions such as multiple faces, unknown faces and varying lighting conditions.
## Work Done
- Implemented face detection using OpenCV Haar Cascade.
- Implemented face recognition using LBPH face recognition.
- Implemented attendance logging.
- Recorded Student ID, Name, Date and Time.
- Stored attendance records in CSV format.
- Tested the system with multiple faces.
- Tested the system with unknown/unregistered faces.
- Tested the system under different lighting conditions.
- Used duplicate removal to avoid repeated attendance entries for the same student.
## Result
The system detects faces through the webcam and generates attendance records in CSV format. Different edge cases such as multiple faces and unknown faces were tested.
# Week 8 - Testing and Documentation
## Objective
To test the complete Face Recognition Attendance System and prepare the project documentation and final demonstration.
## Work Done
- Tested webcam functionality.
- Tested face detection.
- Tested face recognition.
- Tested multiple-face detection.
- Tested unknown-face handling.
- Tested attendance logging.
- Verified attendance records stored in CSV format.
- Documented the project workflow.
- Prepared the project for final demonstration.
## Testing
| Test Case | Expected Result |
|---|---|
| Webcam test | Webcam opens successfully |
| Face detection | Face is detected |
| Face recognition | System attempts to identify the face |
| Unknown face | Unknown status is displayed |
| Multiple faces | Multiple faces are detected |
| Attendance logging | Attendance is stored in CSV |
| Duplicate attendance | Duplicate ID is removed |
## Technologies Used
- Python
- OpenCV
- Haar Cascade
- LBPH Face Recognition
- Pandas
- CSV
## Project Outcome
The Face Recognition Attendance System detects faces through a webcam and performs face-recognition-based attendance recording. Attendance details are stored in CSV format with Student ID, Name, Date and Time.