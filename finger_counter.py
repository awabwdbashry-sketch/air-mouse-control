import cv2
import mediapipe as mp

# إعداد MediaPipe
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # قلب الصورة
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    total_fingers = 0

    if results.multi_hand_landmarks and results.multi_handedness:

        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            lm = hand_landmarks.landmark

            hand_label = handedness.classification[0].label  # Right أو Left

            fingers = 0

            # -------------------------
            # الإبهام
            # -------------------------
            if hand_label == "Right":
                if lm[4].x < lm[3].x:
                    fingers += 1
            else:  # Left
                if lm[4].x > lm[3].x:
                    fingers += 1

            # -------------------------
            # باقي الأصابع
            # -------------------------
            tips = [8, 12, 16, 20]

            for tip in tips:
                if lm[tip].y < lm[tip - 2].y:
                    fingers += 1

            total_fingers += fingers

            # رسم اليد
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(
                    color=(0, 255, 0),
                    thickness=2,
                    circle_radius=3
                ),
                mp_draw.DrawingSpec(
                    color=(255, 0, 255),
                    thickness=2
                )
            )

            # عرض عدد أصابع كل يد
            cv2.putText(
                frame,
                f"{hand_label}: {fingers}",
                (
                    int(lm[0].x * frame.shape[1]),
                    int(lm[0].y * frame.shape[0]) - 20
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

    # عرض المجموع
    cv2.putText(
        frame,
        f"Total Fingers: {total_fingers}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 255),
        3
    )

    cv2.imshow("Finger Counter (0-10)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()