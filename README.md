# Week 6 Attendance Logging and Edge Cases

## Topics Learned
- Attendance logging
- Handling low-light conditions
- Multiple face detection
- Duplicate attendance prevention
- CSV file handling

## Objective

To improve the face recognition attendance system by handling
different real-world conditions and maintaining an attendance log.

## Implementation

The system uses OpenCV Haar Cascade for face detection and
LBPH face recognition for matching known faces.

The system:
- Detects faces using a webcam
- Handles multiple faces
- Improves grayscale images in low-light conditions
- Recognizes known faces
- Identifies unknown faces
- Records attendance automatically
- Stores Name, Date, Time and Status in a CSV file
- Prevents duplicate attendance for the same person on the same day

## Technologies Used

- Python
- OpenCV
- NumPy
- CSV
- Haar Cascade
- LBPH Face Recognition

## Output

The system displays the detected person's name and attendance
status on the webcam screen.

Attendance is stored in `attendance.csv`.

## Technical Skills Learned

I learned how to implement attendance logging using Python and
CSV files. I also learned how to handle edge cases such as
low lighting, multiple faces, unknown faces and duplicate
attendance records using OpenCV.