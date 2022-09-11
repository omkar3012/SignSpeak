import cv2
import imutils
import numpy as np
from keras.models import model_from_json
import operator
import pyttsx3
import sys, os

# model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)

loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

# #########################################################################################
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# is_voice_on = True
#
# def say_text(text):
# 	if not is_voice_on:
# 		return
# 	while engine._inLoop:
# 		pass
# 	engine.say(text)
# 	engine.runAndWait()
#
#
cap = cv2.VideoCapture(0)
# #####################################################################################

# Category dictionary
categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', "C": 'C',"L":'L',"OK":'OK',"THUMBUP":'THUMBUP',"THUMBDOWN":'THUMBDOWN',"NONE":'NONE',"DOUBT":'DOUBT',"B":'B',"O":'O',"U":'U'}
#  B": 'B',
#               "C": 'C', "D": 'D', "E": 'E', "F": 'F', "G": 'G', "H": 'H', "I": 'I', "J": 'J', "K": 'K',
#               "L": 'L', "M": 'M', "N": 'N', "O": 'O', "P": 'P', "Q": 'Q', "R": 'R', "S": 'S', "T": 'T',
#               "U": 'U', "V": 'V', "W": 'W', "X": 'X', "Y": 'Y', "Z": 'Z'#}

while True:
    _, frame = cap.read()
    # frame =imutils.resize(frame,width=320)

    frame = cv2.flip(frame, 1)

    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # ROI
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)

    roi = frame[y1:y2, x1:x2]

    roi = cv2.resize(roi, (64, 64))
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    print(roi)
    _, test_image = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)


    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    prediction = {'ZERO': result[0][0],
                  'ONE': result[0][1],
                  'TWO': result[0][2],
                  'THREE': result[0][3],
                  'FOUR': result[0][4],
                  'FIVE': result[0][5],
                   'C': result[0][6],
                  'L':result[0][7],
                  # 'OK':result[0][8],
                  # 'THUMBUP':result[0][9],
                  # 'THUMBDOWN':result[0][10],
                  'NONE':result[0][11],
                  # 'CALL':result[0][12]
                  'B':result[0][13],
                  'O':result[0][14],
                  'U':result[0][15]
                  }


    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)

    # ###################################################################################
    # text = ""
    # word = ""
    # count_same_frame = 0
    # while True:
    #
    #     old_text = text
    #     if len() > 0:
    #         contour = max(10, key=cv2.contourArea)
    #         if cv2.contourArea(contour) > 10000:
    #             text = get_pred_from_contour(contour, thresh)
    #             if old_text == text:
    #                 count_same_frame += 1
    #             else:
    #                 count_same_frame = 0
    #
    #             if count_same_frame > 20:
    #                 if len(text) == 1:
    #                     Thread(target=say_text, args=(text,)).start()
    #                 word = word + text
    #                 if word.startswith('I/Me '):
    #                     word = word.replace('I/Me ', 'I ')
    #                 elif word.endswith('I/Me '):
    #                     word = word.replace('I/Me ', 'me ')
    #                 count_same_frame = 0
    #
    #         elif cv2.contourArea(contour) < 1000:
    #             if word != '':
    #                 # print('yolo')
    #                 # say_text(text)
    #                 Thread(target=say_text, args=(word,)).start()
    #             text = ""
    #             word = ""
    #     else:
    #         if word != '':
    #             # print('yolo1')
    #             # say_text(text)
    #             Thread(target=say_text, args=(word,)).start()
    #         text = ""
    #         word = ""
    #     blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
    #     cv2.putText(blackboard, "Text Mode", (180, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 0, 0))
    #     cv2.putText(blackboard, "Predicted text- " + text, (30, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 0))
    #     cv2.putText(blackboard, word, (30, 240), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255))
    #     if is_voice_on:
    #         cv2.putText(blackboard, "Voice on", (450, 440), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 127, 0))
    #     else:
    #         cv2.putText(blackboard, "Voice off", (450, 440), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 127, 0))
    # ####################################################################################


    cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 2)
    cv2.imshow("Frame", frame)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break


cap.release()
cv2.destroyAllWindows()

# import cv2
# import imutils
# import numpy as np
# from keras.models import model_from_json
# import operator
# import pyttsx3
# import sys, os
#
# # model
# json_file = open("model-bw.json", "r")
# model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(model_json)
#
# loaded_model.load_weights("model-bw.h5")
# print("Loaded model from disk")
#
# #########################################################################################
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# is_voice_on = True
#
#
# def say_text(text):
#     if not is_voice_on:
#         return
#     while engine._inLoop:
#         pass
#     engine.say(text)
#     engine.runAndWait()
#
# def get_img_contour_thresh(img):
# 	img = cv2.flip(img, 1)
# 	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 	contours = cv2.findContours(test_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
# 	return img, contours
#
# cap = cv2.VideoCapture(0)
# #####################################################################################
#
# # Category dictionary
# categories = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', "A": 'A', "L": 'L'}
# #  B": 'B',
# #               "C": 'C', "D": 'D', "E": 'E', "F": 'F', "G": 'G', "H": 'H', "I": 'I', "J": 'J', "K": 'K',
# #               "L": 'L', "M": 'M', "N": 'N', "O": 'O', "P": 'P', "Q": 'Q', "R": 'R', "S": 'S', "T": 'T',
# #               "U": 'U', "V": 'V', "W": 'W', "X": 'X', "Y": 'Y', "Z": 'Z'#}
#
# while True:
#     _, frame = cap.read()
#     # frame =imutils.resize(frame,width=320)
#
#     frame = cv2.flip(frame, 1)
#
#     x1 = int(0.5 * frame.shape[1])
#     y1 = 10
#     x2 = frame.shape[1] - 10
#     y2 = int(0.5 * frame.shape[1])
#     # ROI
#     cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
#
#     roi = frame[y1:y2, x1:x2]
#
#     roi = cv2.resize(roi, (64, 64))
#     roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     print(roi)
#     _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
#     cv2.imshow("test", test_image)
#
#     result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
#     prediction = {'ZERO': result[0][0],
#                   'ONE': result[0][1],
#                   'TWO': result[0][2],
#                   'THREE': result[0][3],
#                   'FOUR': result[0][4],
#                   'FIVE': result[0][5],
#                   'C': result[0][6],
#                   'L': result[0][7]
#                   }
#
#     prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
#
#     ###################################################################################
#     # text = ""
#     # word = ""
#     # count_same_frame = 0
#     # while True:
#     #
#     #     old_text = text
#     #     if 1 > 0:
#     #         contour = max(0, key=cv2.contourArea)
#     #         if cv2.contourArea(contour) > 10000:
#     #             text = get_pred_from_contour(contour, thresh)
#     #             if old_text == text:
#     #                 count_same_frame += 1
#     #             else:
#     #                 count_same_frame = 0
#     #
#     #             if count_same_frame > 20:
#     #                 if len(text) == 1:
#     #                     Thread(target=say_text, args=(text,)).start()
#     #                 word = word + text
#     #                 if word.startswith('I/Me '):
#     #                     word = word.replace('I/Me ', 'I ')
#     #                 elif word.endswith('I/Me '):
#     #                     word = word.replace('I/Me ', 'me ')
#     #                 count_same_frame = 0
#     #
#     #         elif cv2.contourArea(contour) < 1000:
#     #             if word != '':
#     #                 # print('yolo')
#     #                 # say_text(text)
#     #                 Thread(target=say_text, args=(word,)).start()
#     #             text = ""
#     #             word = ""
#     #     else:
#     #         if word != '':
#     #             # print('yolo1')
#     #             # say_text(text)
#     #             Thread(target=say_text, args=(word,)).start()
#     #         text = ""
#     #         word = ""
#         blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
#         cv2.putText(blackboard, "Text Mode", (180, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 0, 0))
#
#         cv2.putText(blackboard, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
#         if is_voice_on:
#             cv2.putText(blackboard, "Voice on", (450, 440), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 127, 0))
#         else:
#             cv2.putText(blackboard, "Voice off", (450, 440), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 127, 0))
#     ####################################################################################
#
#     cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
#     cv2.imshow("Frame", frame)
#
#     interrupt = cv2.waitKey(10)
#     if interrupt & 0xFF == 27:  # esc key
#         break
#
# cap.release()
# cv2.destroyAllWindows()
