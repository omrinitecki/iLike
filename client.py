import requests
import cv2
from datetime import datetime


def main():
    image = cv2.imread("avocado.jpg")
    while True:
        cv2.imshow("avocado", image)
        key = cv2.waitKey(0)
        if key == ord(" "):
            requests.post("http://127.0.0.1:5000", json={"omri": str(datetime.now())})
            response = requests.get("http://127.0.0.1:5000")
            print(response.json())
        elif key == ord("q"):
            break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()