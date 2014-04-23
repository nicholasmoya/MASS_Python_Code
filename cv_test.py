import cv2

frame = cv2.imread("./chimp.jpg")
cv2.imwrite("./chimpy_dimpy.jpg", frame)
# cv2.imshow("frame", frame)
# key = cv2.waitKey(1) & 0xFF
frame = cv2.resize(frame, (320, 240))
cv2.imwrite("./resize.jpg", frame)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./gray.jpg", gray)
gray = cv2.GaussianBlur(gray, (21, 21), 0)
cv2.imwrite("./blur.jpg", gray)
firstFrame = gray

frameDelta = cv2.absdiff(firstFrame, gray)
# cv2.imshow("Diff", frameDelta)
cv2.imwrite("./diff.jpg", frameDelta)
thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("./thresh.jpg", thresh)
# cv2.imshow("Thresh", thresh)

# dilate the thresholded image to fill in holes, then find contours
# on thresholded image
thresh = cv2.dilate(thresh, None, iterations=2)
cv2.imwrite("./dilate.jpg", thresh)
# cv2.imshow("Dilate", thresh)
"""
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for c in cnts:
        # if the contour is too small, ignore it
        # if cv2.contourArea(c) < args["min_area"]:
                # continue

        if cv2.contourArea(c) < 50:
                continue

        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"

# show the frame and record if the user presses a key
# cv2.imshow("Security Feed", frame)
# cv2.imshow("Thresh", thresh)
# cv2.imshow("Frame Delta", frameDelta)
# key = cv2.waitKey(1) & 0xFF
"""
