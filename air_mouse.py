import cv2
import mediapipe as mp
import pyautogui
import math


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils


screen_w, screen_h = pyautogui.size()

cap = cv2.VideoCapture(0)


control = True
clicked = False


while True:

    success, frame = cap.read()

    if not success:
        break


    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)


    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            lm = hand.landmark


            # نقاط الأصابع
            index_x = int(lm[8].x * w)
            index_y = int(lm[8].y * h)

            thumb_x = int(lm[4].x * w)
            thumb_y = int(lm[4].y * h)


            # حساب المسافة بين السبابة والإبهام
            distance = math.hypot(
                index_x - thumb_x,
                index_y - thumb_y
            )


            # معرفة اليد مفتوحة
            fingers = []

            tips = [8,12,16,20]

            for tip in tips:
                if lm[tip].y < lm[tip-2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)


            # ✋ كف مفتوح = إيقاف
            if sum(fingers) == 4:
                control = False


            # 👊 أي وضع آخر = تشغيل
            else:
                control = True



            if control:

                mouse_x = int(lm[8].x * screen_w)
                mouse_y = int(lm[8].y * screen_h)

                pyautogui.moveTo(
                    mouse_x,
                    mouse_y
                )


                 
                if distance < 40 and not clicked:

                    pyautogui.click()
                    clicked = True


                if distance > 60:
                    clicked = False



            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )


            text = "ON" if control else "OFF"


            cv2.putText(
                frame,
                "Mouse: " + text,
                (30,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0,255,0),
                3
            )


    cv2.imshow(
        "AI Mouse",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()