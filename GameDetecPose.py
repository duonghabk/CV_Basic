import cv2
import mediapipe as mp
import time
import poseDetector as poseDt

def main():

    DIR = 'Video/'
    file = '2.mp4'
    cap = cv2.VideoCapture(DIR + file)
    detector = poseDt.poseDetector()

    pTime = 0
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        detector.findPosition(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
