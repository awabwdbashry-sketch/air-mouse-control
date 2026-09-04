import cv2
import mediapipe as mp
import numpy as np

# =========================
# MediaPipe
# =========================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# =========================
# Camera
# =========================
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# =========================
# Canvas
# =========================
canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

draw_color = (0, 0, 255)
brush = 8
eraser = 40

xp, yp = 0, 0

# =========================
# Colors
# =========================
buttons = [
    ("RED",    (10,10,90,70),    (0,0,255)),
    ("GREEN",  (100,10,180,70),  (0,255,0)),
    ("BLUE",   (190,10,270,70),  (255,0,0)),
    ("YELLOW", (280,10,360,70),  (0,255,255)),
    ("BLACK",  (370,10,450,70),  (0,0,0)),
    ("ERASE",  (460,10,560,70),  (255,255,255)),
    ("CLEAR",  (570,10,680,70),  (120,120,120)),
    ("SAVE",   (690,10,790,70),  (80,180,255))
]

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    # =========================
    # Draw Toolbar
    # =========================
    for text, rect, color in buttons:

        x1,y1,x2,y2 = rect

        cv2.rectangle(frame,(x1,y1),(x2,y2),color,-1)

        txt = (0,0,0)

        if text in ["BLACK","CLEAR"]:
            txt = (255,255,255)

        cv2.putText(
            frame,
            text,
            (x1+5,y1+40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            txt,
            2
        )
            # =========================
    # Hand Detection
    # =========================
    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        h, w, _ = frame.shape

        # السبابة
        index = hand.landmark[8]

        ix = int(index.x * w)
        iy = int(index.y * h)

        # الوسطى
        middle = hand.landmark[12]

        mx = int(middle.x * w)
        my = int(middle.y * h)

        cv2.circle(frame, (ix, iy), 10, (255,255,255), -1)

        # =========================
        # Toolbar
        # =========================
        if iy < 80:

            xp, yp = 0, 0

            for text, rect, color in buttons:

                x1, y1, x2, y2 = rect

                if x1 < ix < x2 and y1 < iy < y2:

                    if text == "RED":
                        draw_color = (0,0,255)

                    elif text == "GREEN":
                        draw_color = (0,255,0)

                    elif text == "BLUE":
                        draw_color = (255,0,0)

                    elif text == "YELLOW":
                        draw_color = (0,255,255)

                    elif text == "BLACK":
                        draw_color = (0,0,0)

                    elif text == "ERASE":
                        draw_color = (255,255,255)

                    elif text == "CLEAR":
                        canvas[:] = 0

                    elif text == "SAVE":
                        cv2.imwrite("drawing.png", canvas)
                        print("✅ Saved as drawing.png")

        else:

            # السبابة مرفوعة والوسطى نازلة = رسم
            index_up = iy < hand.landmark[6].y * h
            middle_down = my > hand.landmark[10].y * h

            if index_up and middle_down:

                if xp == 0 and yp == 0:
                    xp, yp = ix, iy

                thickness = eraser if draw_color == (255,255,255) else brush

                cv2.line(
                    canvas,
                    (xp, yp),
                    (ix, iy),
                    draw_color,
                    thickness
                )

                xp, yp = ix, iy

            else:

                xp, yp = 0, 0
                    # =========================
    # دمج لوحة الرسم مع الكاميرا
    # =========================
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    _, inv = cv2.threshold(
        gray,
        20,
        255,
        cv2.THRESH_BINARY_INV
    )

    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)

    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("Air Draw Pro", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        canvas[:] = 0

    if key == ord("s"):
        cv2.imwrite("drawing.png", canvas)
        print("✅ Drawing Saved!")

    if key == ord("q"):
        break

# =========================
# Cleanup
# =========================
cap.release()
cv2.destroyAllWindows()