import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/train/A")
    os.makedirs("data/train/B")
    os.makedirs("data/train/G")
    os.makedirs("data/train/OK")
    os.makedirs("data/train/THUMBUP")
    os.makedirs("data/train/THUMBDOWN")
    os.makedirs("data/train/NONE")
    os.makedirs("data/train/DOUBT")
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/test/A")
    os.makedirs("data/test/B")
    os.makedirs("data/test/G")
    os.makedirs("data/test/OK")
    os.makedirs("data/test/THUMBUP")
    os.makedirs("data/test/THUMBDOWN")
    os.makedirs("data/test/NONE")
    os.makedirs("data/test/DOUBT")


# Train or test 
mode = 'tRAIN'
directory = 'data/'+mode+'/'

# Use 0 for Default Camera or 1 ,2 ... for external camera
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # mirror image
    frame = cv2.flip(frame, 1)

    count = {'zero': len(os.listdir(directory+"/0")),
             'one': len(os.listdir(directory+"/1")),
             'two': len(os.listdir(directory+"/2")),
             'three': len(os.listdir(directory+"/3")),
             'four': len(os.listdir(directory+"/4")),
             'five': len(os.listdir(directory+"/5")),
             'A': len(os.listdir(directory+"/A")),
             'L': len(os.listdir(directory+"/L")),
             'B': len(os.listdir(directory + "/B")),
             'OK': len(os.listdir(directory+"/OK")),
             'THUMBUP': len(os.listdir(directory + "/THUMBUP")),
             'THUMBDOWN': len(os.listdir(directory + "/THUMBDOWN")),
             'NONE': len(os.listdir(directory + "/NONE")),
             'DOUBT': len(os.listdir(directory + "/DOUBT"))

             }

    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ZERO : "+str(count['zero']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "ONE : "+str(count['one']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "TWO : "+str(count['two']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "THREE : "+str(count['three']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FOUR : "+str(count['four']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "FIVE : " + str(count['five']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "C : " + str(count['A']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "B : " + str(count['B']), (120, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "L : " + str(count['L']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "OK : " + str(count['OK']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "THUMBUP : " + str(count['THUMBUP']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "THUMBDOWN : " + str(count['THUMBDOWN']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "NONE : " + str(count['NONE']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.putText(frame, "DOUBT : " + str(count['DOUBT']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)

    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    ##############################################

    #  ROI
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (128, 128))
 
    cv2.imshow("Frame", frame)

    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)

    ##########################################

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['zero'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['one'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['two'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['three'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['four'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['five'])+'.jpg', roi)
    if interrupt & 0xFF == ord('A'):
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('B'):
        cv2.imwrite(directory + 'B/' + str(count['B']) + '.jpg', roi)
    if interrupt & 0xFF == ord('L'):
        cv2.imwrite(directory + 'L/' + str(count['L']) + '.jpg', roi)
    if interrupt & 0xFF == ord('O'):
        cv2.imwrite(directory + 'OK/' + str(count['OK']) + '.jpg', roi)
    if interrupt & 0xFF == ord('T'):
        cv2.imwrite(directory + 'THUMBUP/' + str(count['THUMBUP']) + '.jpg', roi)
    if interrupt & 0xFF == ord('D'):
        cv2.imwrite(directory + 'THUMBDOWN/' + str(count['THUMBDOWN']) + '.jpg', roi)
    if interrupt & 0xFF == ord('N'):
        cv2.imwrite(directory + 'NONE/' + str(count['NONE']) + '.jpg', roi)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(directory + 'DOUBT/' + str(count['DOUBT']) + '.jpg', roi)
# Exit
cap.release()
cv2.destroyAllWindows()

