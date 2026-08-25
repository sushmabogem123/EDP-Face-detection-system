# EDP AI/ML Internship - Week 4

## Project
Face Detection Attendance System

## Week 4 Topics
- OpenCV
- Haar Cascades

## Objective
The objective of Week 4 is to detect human faces in real time using a webcam with OpenCV and Haar Cascade Classifier.

## Implementation

The program captures live video from the webcam and processes each frame using OpenCV.

A Haar Cascade Classifier is used to detect faces in the video frames.

When a face is detected:
- A rectangle is drawn around the face.
- "Face Detected" is displayed.
- The number of detected faces is displayed.

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier
- Webcam
- Visual Studio Code

## Steps Performed

1. Installed OpenCV using `opencv-python`.
2. Loaded the Haar Cascade face detection model.
3. Accessed the computer webcam using OpenCV.
4. Captured video frames continuously.
5. Converted frames to grayscale.
6. Detected faces using Haar Cascade.
7. Drew bounding boxes around detected faces.
8. Displayed the number of detected faces.
9. Tested real-time face detection using the webcam.

## Technical Skills Learned

- OpenCV
- Haar Cascade Classifier
- Computer Vision Basics
- Real-time Webcam Processing
- Image and Video Processing
- Face Detection
- Grayscale Image Conversion
- Bounding Box Detection
- Python Programming


## How to Run

Install OpenCV:

```bash
pip install opencv-python