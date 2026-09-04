# 🖱️ Air Mouse Control

A computer vision project that allows users to control the computer mouse using hand gestures captured through a webcam.

The project uses **MediaPipe** to track hand landmarks and **OpenCV** to process the webcam feed. The index finger controls the mouse cursor, while specific hand movements can be used to perform mouse clicks.

## ✨ Features

* 🖐️ Real-time hand tracking
* 🖱️ Control the mouse cursor using the index finger
* 👆 Pinch gesture for mouse clicking
* ✋ Open-palm gesture for disabling mouse control
* 🎥 Real-time webcam processing
* 🎯 Smooth cursor movement
* ⚡ Fast and responsive gesture detection
* 💻 Direct interaction with the computer mouse

## 🛠️ Technologies Used

* 🐍 Python
* 👁️ OpenCV
* ✋ MediaPipe
* 🔢 NumPy
* 🖱️ PyAutoGUI

## ⚙️ How It Works

The project captures live video from the webcam and detects the user's hand using MediaPipe.

MediaPipe identifies the hand landmarks, including the position of the index finger and other important points.

The index finger position is then converted from the webcam coordinates into screen coordinates. PyAutoGUI uses these coordinates to move the system mouse cursor.

A pinch gesture between the fingers is detected and interpreted as a mouse click.

An open-palm gesture can be used to temporarily disable mouse control.

## 🔄 Processing Pipeline

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Detection
   ↓
Hand Landmark Detection
   ↓
Gesture Recognition
   ↓
Cursor / Click Control
   ↓
Computer Mouse
```

## 🖱️ Mouse Controls

| Gesture         | Action                |
| --------------- | --------------------- |
| ☝️ Index Finger | Move the mouse cursor |
| 🤏 Pinch        | Mouse click           |
| ✋ Open Palm     | Disable mouse control |

> ⚠️ **Important:** This project controls the actual system mouse. Make sure your hand is positioned correctly before running it.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/awabwdbashry-sketch/air-mouse-control.git
cd air-mouse-control
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 📋 Requirements

* Python 3.9 or newer
* Webcam
* Windows, Linux, or macOS
* Working internet connection for installing dependencies

### Python Dependencies

```text
opencv-python
mediapipe
numpy
pyautogui
```

## ▶️ Usage

Run the main Python file:

```bash
python air_mouse.py
```

Position your hand in front of the webcam and use the supported gestures to control the mouse.

Press the appropriate exit key defined by the application to stop the program.

## 📁 Project Structure

```text
air-mouse-control/
│
├── air_mouse.py
├── requirements.txt
├── README.md
├── README_AR.md
└── .gitignore
```

## 💡 Applications

This project demonstrates how computer vision can be used to create touchless human-computer interaction.

Possible applications include:

* 🖥️ Touchless computer control
* ♿ Accessibility interfaces
* 🎓 Computer vision education
* 🧪 Human-computer interaction experiments
* 🖐️ Gesture-based interfaces
* 🚀 Future smart-device interfaces

## ⭐ Advantages

* Simple and interactive
* Real-time performance
* Uses a normal webcam
* No special hardware required
* Demonstrates practical computer vision
* Provides hands-free mouse interaction

## 🚀 Future Improvements

Possible future improvements include:

* 🎯 More accurate cursor smoothing
* 🖱️ Left and right click gestures
* 🖱️ Double-click gesture
* 📜 Scroll gestures
* 🖐️ Multi-hand interaction
* ⚙️ Customizable gesture settings
* 🎚️ Adjustable cursor sensitivity
* 🔊 Voice and gesture combination

## 🎯 Project Purpose

The main goal of this project is to demonstrate how **hand tracking and gesture recognition** can be combined with system-level mouse control to create a touchless computer interface.

## 📄 License

This project is available for educational and personal use.

---

⭐ If you find this project useful, consider giving the repository a star!

**GitHub:** `https://github.com/awabwdbashry-sketch/air-mouse-control`
## 👨‍💻 Developer

**Awab Bashary | AwabBuilds**

GitHub: **awabwdbashry-sketch**
