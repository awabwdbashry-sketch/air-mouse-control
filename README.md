# Finger Counter ✋🔢

A real-time computer vision project that detects and counts raised fingers using a webcam.

The project uses **MediaPipe Hands** to track hand landmarks and **OpenCV** to process and display the result.

## ✨ Features

* Real-time hand tracking
* Detects up to two hands
* Counts raised fingers on each hand
* Displays the total finger count
* Supports counting from 0 to 10 fingers
* Live webcam visualization

## 🛠️ Technologies

* Python
* OpenCV
* MediaPipe
* NumPy

## ⚙️ How It Works

The webcam captures the user's hand in real time.

MediaPipe detects the hand landmarks and provides the coordinates of the fingers.

The project analyzes the landmark positions to determine which fingers are raised and calculates the total number of raised fingers.

The application can detect:

* Left hand
* Right hand
* Individual raised fingers
* Total raised fingers

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/awabwdbashry-sketch/finger-counter.git
cd finger-counter
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the application:

```bash
python finger_counter.py
```

Make sure your webcam is connected and accessible.

Place your hand(s) in front of the camera and raise or lower your fingers to see the detected count.

## 📋 Requirements

* Python 3.9+
* Webcam
* Windows, macOS, or Linux
* Internet connection for installing dependencies

## 📁 Project Structure

```text
finger-counter/
├── finger_counter.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔢 Supported Range

The project can detect up to **10 raised fingers** when two hands are visible.

## 📄 License

This project is available for educational and personal use.
