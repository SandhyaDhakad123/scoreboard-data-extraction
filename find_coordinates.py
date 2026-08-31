import cv2

# Apni final_scoreboard.jpg image kholo
img = cv2.imread("final_scoreboard.jpg")

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"X = {x}, Y = {y}")

cv2.imshow("Click on row boundaries - Press ESC to exit", img)
cv2.setMouseCallback("Click on row boundaries - Press ESC to exit", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()