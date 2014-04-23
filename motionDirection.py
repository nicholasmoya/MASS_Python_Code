import datetime
import time
import cv2

def motionDirection():
    camera = cv2.VideoCapture(0)
    time.sleep(3.25)

    firstFrame = None

    bgRestart = 10
    countFramesWithMotion = 0
    largeContourArea = 0

    while True:
            (grabbed, frame) = camera.read()
            text = "Unoccupied"

            if not grabbed:
                break

            # resize the frame, convert it to grayscale, and blur it
            frame = cv2.resize(frame, (320, 240))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)
            cv2.imshow("Blur", gray)

            if firstFrame is None:
                firstFrame = gray
                continue

            # compute the absolute difference between the current frame and
            # first frame
            frameDelta = cv2.absdiff(firstFrame, gray)
            cv2.imshow("Diff", frameDelta)
            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
            # cv2.imshow("Thresh", thresh)

            # dilate the thresholded image to fill in holes, then find contours
            # on thresholded image
            thresh = cv2.dilate(thresh, None, iterations=15)
            # thresh1 = cv2.dilate(thresh, None, iterations=5)
            # thresh2 = cv2.dilate(thresh, None, iterations=10)
            # thresh3 = cv2.dilate(thresh, None, iterations=20)
            # thresh4 = cv2.dilate(thresh, None, iterations=40)
            cv2.imshow("Dilate", thresh)
            # cv2.imshow("Dilate 1", thresh1)
            # cv2.imshow("Dilate 2", thresh2)
            # cv2.imshow("Dilate 3", thresh3)
            # cv2.imshow("Dilate 4", thresh4)
            (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            countContoursInFrame = 0 

            # loop over the contours in this frame
            for c in cnts:
                print cv2.contourArea(c)

                if cv2.contourArea(c) < 50:
                        continue

                countContoursInFrame += 1

                # compute the bounding box for the contour, draw it on the frame,
                # and update the text
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Occupied"
                
                # If the current contour is larger than the current largest,
                # make it the new largest contour for this frame
                if cv2.contourArea(c) > largeContourArea:
                    largeContour = c
                    largeContourArea = cv2.contourArea(largeContour)
                    largeContourCenter = (x + 0.5*w, y + 0.5*h)
                
            if (countContoursInFrame > 0):
                countFramesWithMotion += 1
            elif (countContoursInFrame <= 0):
                countFramesWithMotion = 0

            print "Frames with motion: ", countFramesWithMotion

            # If the current frame is the first with motion,
            # set its largest contour to be the start of motion path
            if (countFramesWithMotion == 1):
                largeContourCenter0 = largeContourCenter
        
            if (countFramesWithMotion > 3):
                xMotion = largeContourCenter[0] - largeContourCenter0[0]
                if xMotion == 0: xMotion = 1 # prevent division by zero
                print "Initial x-position: ", largeContourCenter0[0]
                print "Final x-position: ", largeContourCenter[0]
                print "X Motion: ", xMotion/abs(xMotion)
                return xMotion/abs(xMotion)

            # draw the text and timestamp on the frame
            cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            # show the frame and record if the user presses a key
            cv2.imshow("Security Feed", frame)
            # cv2.imshow("Thresh", thresh)
            # cv2.imshow("Frame Delta", frameDelta)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key is pressed, break from the lop
            if key == ord("q"):
                cv2.imwrite("./blur.jpg", gray)
                cv2.imwrite("./diff.jpg", frameDelta)
                # cv2.imwrite("./thresh.jpg", thresh)
                cv2.imwrite("./dilate.jpg", thresh)
                # break

            # Capture a new background image every after a number of iterations
            bgRestart = bgRestart - 1
            if bgRestart == 0:
                firstFrame = None
                bgRestart = 10
            print bgRestart

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
