from django.shortcuts import render
import json
import base64
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from PIL import Image
from io import BytesIO
import numpy as numpy
from rest_framework import status
import tensorflow as tensorflow
import cv2
# Create your views here.
model = tensorflow.keras.models.load_model(r"C:\Users\DELL\Documents\GitHub\SignLanguageToText\app\my_model (2).h5")
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

y=0
x=0
h=300
w=300

def img_class(model, img):
    img_arr = numpy.asarray(img)
    
    pred_probab = model.predict(img_arr)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return max(pred_probab), pred_class

@api_view(['POST'])
def AslToText(request):
    if request.method == "POST":
        char_op=""
        b = request.data['text']
        im = Image.open(BytesIO(base64.b64decode(b)))
        left =35
        top = 35
        right = 175
        bottom = 175
        width, height = im.size

        # Cropped image of above dimension
        # (It will not change orginal image)
        im = im.transpose(Image.ROTATE_180)
        im1 = im.crop((0, 0, width, height/2))
        temp_img2 = cv2.rotate(numpy.array(im1), cv2.ROTATE_90_COUNTERCLOCKWISE)
        temp_img =  cv2.cvtColor(numpy.asarray(temp_img2), cv2.COLOR_RGB2BGR)
        # crop = temp_img[y:y+h,x:x+w]

        temp_img = cv2.resize(temp_img, (64,64))
        images=[]
        images.append(temp_img)
        images = numpy.array(images)
        images = images.astype('float32')/255.0
        pred_probab, pred_class = img_class(model, images)
        char_op = classes[pred_class]
    return Response( {'value':char_op},200)

@api_view(['POST'])
def textToAsl(request):
    if request.method == 'POST':
        text = request.data['text']  #Extracting text
        print(text)
        arr = text.split()
        data = {}
        count = 0       #number of ele in dict
        for i in range(0,len(arr)):
            nesteddata = {}
            flag = 0                #flag to avoid empty nested dict
            for j in range(0,len(arr[i])):
                asci = ord(arr[i][j])
                if asci <=90 and asci >=65:           #converting to lower case
                    asci = asci + 32
                if  asci>= 97 and asci <=122: 
                    flag = 1
                    alphabet = chr(asci)       
                    with open('./split/'+alphabet+'.png', mode='rb') as file:
                        byte_img = file.read()

                    base64_bytes = base64.b64encode(byte_img)       #in byte base64 format
                    nesteddata[j] = base64_bytes.decode('utf-8')   #converting to string format
            if flag ==1:
                data[count] = nesteddata     #main dict
                count += 1
        print(json.dumps(data))          #conv to json
