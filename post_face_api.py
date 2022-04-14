from imutils import paths
import face_recognition
import argparse
import cv2
import os
import sys
import json
import copy
from PIL import Image
import numpy as np
import io
def process_json(image):
    # results = []
    # empty_results = []

    # for i,json_object in enumerate(json_input_list):
    try:
        # image = cv2.imread(json_object["image_path"])
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception:
        return []
    boxes = face_recognition.face_locations(rgb,model='hog')
    if boxes:
        encodings = face_recognition.face_encodings(rgb, boxes)
        for i,enc in enumerate(encodings):
            return  enc.tolist()
            # new_obj= copy.deepcopy(json_object)
            # new_obj['features'] = enc.tolist()
            # new_obj['id'] = new_obj['id'] +"_"+str(i)
            # results.append(new_obj)
    # else:
    #     empty_results.append(json_object)
    # return results,empty_results
def get_output():
    raw_input_binary = sys.stdin.buffer.read()
    # img = Image.open(io.BytesIO(raw_input_binary))

 
    # img_resized = img.resize((224, 224))
    img = Image.open(io.BytesIO(raw_input_binary))
    arr = np.asarray(img)
    print(json.dumps(process_json(arr)))

    # output = {}
    # if len(results)>0:
    #     output["results"]=results
    # if len(results)>0:
    #     output["empty_results"]=empty_results
        

    # # print(results)
    # print(json.dumps(output,indent=4)) 
           

get_output()