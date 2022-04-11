import numpy as np
import cv2
import tensorflow as tf
def crop_square(img, size, interpolation=cv2.INTER_AREA):
    h, w = img.shape[:2]
    min_size = np.amin([h,w])

    # Centralize and crop
    crop_img = img[int(h/2-min_size/2):int(h/2+min_size/2), int(w/2-min_size/2):int(w/2+min_size/2)]
    resized = cv2.resize(crop_img, (size, size), interpolation=interpolation)

    return resized
model = tf.keras.models.load_model(r"C:\Users\DELL\Downloads\my_model (2).h5")

def img_class(model, img):
    img_arr = np.asarray(img)
    
    pred_probab = model.predict(img_arr)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class


# Initializing Video Frame
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    # Displaying border in frame
    frame = cv2.rectangle(frame, (40,100), (240,300), (0,255,0), thickness = 1)
    
    # Cropping Hand Region
    crop = frame[100:300, 40:240]
    
    # Converting to GRAY
#     img_gry = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    # Applying Gaussian BLur                       
#     img_gry_blr = cv2.blur(img_gry,(1,1))
    # Resizing
    temp_img = crop
    temp_img = cv2.resize(temp_img, (64,64))
    images=[]
    images.append(temp_img)
    images = np.array(images)
    images = images.astype('float32')/255.0
    pred_probab, pred_class = img_class(model, images)
    classes = ['Q',
 'del',
 'V',
 'F',
 'I',
 'U',
 'Y',
 'S',
 'P',
 'T',
 'H',
 'space',
 'O',
 'K',
 'E',
 'N',
 'W',
 'A',
 'B',
 'R',
 'nothing',
 'L',
 'C',
 'M',
 'J',
 'D',
 'Z',
 'G',
 'X']
    
    char_op = classes[pred_class]

    cv2.putText(frame, char_op, (580,420), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 2)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('pic',crop)
#     cv2.imshow('gry',img_gry)
#     cv2.imshow('blur',img_gry_blr)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
