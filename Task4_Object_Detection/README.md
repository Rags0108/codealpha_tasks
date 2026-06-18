# 🚀 CodeAlpha AI Internship - Task 4

# 🎯 AI-Powered Object Detection and Tracking

## 📌 Project Description

This project implements a real-time Object Detection and Multi-Object Tracking system using Ultralytics YOLO and ByteTrack. The system detects objects from a webcam or video stream, assigns unique tracking IDs, performs object counting, calculates total detected objects, and saves the processed output video with annotations.

---

## 🎯 Objectives

* Perform real-time object detection using YOLO.
* Track detected objects using ByteTrack.
* Assign unique tracking IDs to each object.
* Display object labels and confidence scores.
* Count detected objects by class.
* Calculate total object count.
* Save the processed video output.

---

## 🛠 Technologies Used

* Python 3.12
* OpenCV
* Ultralytics YOLO
* ByteTrack
* NumPy

---

## 📂 Project Structure

Task4_Object_Detection/

├── models/

│ └── yolo11n.pt

├── videos/

│ └── output.mp4

├── task4.ipynb

├── requirements.txt

├── README.md

└── main.py

---

## 🔄 Workflow

### Step 1: Install Libraries

Install all required dependencies from requirements.txt.

### Step 2: Import Libraries

Import OpenCV, Ultralytics YOLO, and other required packages.

### Step 3: Load YOLO Model

Load the pre-trained YOLO model.

### Step 4: Open Webcam or Video

Capture frames from webcam or video source.

### Step 5: Object Detection

Detect objects using the YOLO model.

### Step 6: Object Tracking

Track detected objects using ByteTrack and assign unique IDs.

### Step 7: Object Counting

Count detected objects for each class.

### Step 8: Total Object Count

Calculate the total number of detected objects.

### Step 9: Display Results

Display bounding boxes, labels, confidence scores, tracking IDs, and object counts.

### Step 10: Save Output Video

Store the processed video in MP4 format.

---

## ✨ Features

* Real-Time Object Detection
* Multi-Object Tracking
* Unique Tracking IDs
* Object Counting
* Total Object Count
* Confidence Score Display
* Bounding Box Visualization
* Output Video Saving
* Webcam and Video File Support

---

## 📊 Sample Output

Detected Objects:

* Person
* Remote
* Cell Phone
* Clock
* Teddy Bear
* Traffic Light

Output Display:

* Bounding Boxes
* Class Labels
* Confidence Scores
* Tracking IDs
* Object Counts
* Total Object Count

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python main.py
```

Or run:

```bash
task4.ipynb
```

inside Jupyter Notebook.

---

## 📈 Results

The system successfully:

* Detects multiple objects in real time.
* Tracks objects using ByteTrack.
* Maintains persistent object IDs across frames.
* Counts detected objects.
* Displays total object count.
* Saves annotated output video.

---

## 📚 References

* Ultralytics YOLO Documentation
* ByteTrack Multi-Object Tracking
* OpenCV Documentation

---

## 👨‍💻 By

Ragavan S

CodeAlpha AI Intern

B.Tech Artificial Intelligence & Data Science

* GitHub: https://github.com/Rags0108
* LinkedIn: https://www.linkedin.com/in/s-ragavan/

---

## 📜 License

This project is developed for educational and internship purposes under the CodeAlpha AI Internship Program.

---

## ⭐ Acknowledgement

Thanks to CodeAlpha for providing the opportunity to work on practical Artificial Intelligence and Object Detection projects.
