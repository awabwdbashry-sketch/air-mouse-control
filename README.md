# Air Mouse Control 🖱️✋

A computer vision project that turns hand gestures into mouse controls using a webcam.

The project uses **MediaPipe Hands** to track hand landmarks and **PyAutoGUI** to control the system mouse through natural hand movements.

## ✨ Features

* Real-time hand tracking
* Move the mouse using the index finger
* Click using a thumb/index finger pinch gesture
* Open-palm detection to disable mouse control
* Webcam-based interaction
* Real-time visual feedback

## 🛠️ Technologies

* Python
* OpenCV
* MediaPipe
* NumPy
* PyAutoGUI

## ⚙️ How It Works

The webcam captures the user's hand in real time.

MediaPipe detects the hand landmarks and provides the coordinates of the fingers.

The project then uses these landmarks to:

1. Detect the user's hand.
2. Track the index finger.
3. Map finger movement to the computer screen.
4. Detect a pinch between the thumb and index finger.
5. Trigger a mouse click.
6. Disable interaction when an open palm is detected.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/awabwdbashry-sketch/air-mouse-control.git
cd air-mouse-control
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run:

```bash
python air_mouse.py
```

Make sure your webcam is connected and accessible.

Move your index finger to control the mouse.

Use the supported pinch gesture to perform a click.

## 📋 Requirements

* Python 3.9+
* Webcam
* Windows, macOS, or Linux
* Working internet connection during dependency installation

## 📁 Project Structure

```text
air-mouse-control/
├── air_mouse.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚠️ Notes

PyAutoGUI controls the operating system mouse, so the application should be used carefully.

The exact interaction behavior depends on the gesture detection logic implemented in `air_mouse.py`.

## 📄 License

This project is available for educational and personal use.
