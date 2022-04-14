from imutils import paths
import face_recognition
import argparse
import cv2
import os
import sys
import json
import copy


def process_json(json_input_list):
    results = []
    empty_results = []

    for i,json_object in enumerate(json_input_list):
        try:
            image = cv2.imread(json_object["image_path"])
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception:
            empty_results.append(json_object)
            continue
        boxes = face_recognition.face_locations(rgb,model='hog')
        if boxes:
            encodings = face_recognition.face_encodings(rgb, boxes)
            for i,enc in enumerate(encodings):
                new_obj= copy.deepcopy(json_object)
                new_obj['features'] = enc.tolist()
                new_obj['id'] = new_obj['id'] +"_"+str(i)
                results.append(new_obj)
        else:
            empty_results.append(json_object)
    return results,empty_results
def get_output():
    raw_input_str = sys.stdin.read()
#     raw_input_str="""[{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909964","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909964.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909887","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909887.png"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910101","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910101.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909890","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909890.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909841","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909841.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910153","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910153.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910039","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910039.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909766","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909766.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909861","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909861.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909804","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909804.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910210","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910210.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910116","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910116.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910160","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910160.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910080","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910080.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909856","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909856.png"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910054","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910054.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909851","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909851.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910170","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910170.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910102","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910102.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909947","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909947.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910035","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910035.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909772","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909772.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909929","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909929.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909830","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909830.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909918","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909918.png"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909895","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909895.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909776","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909776.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909884","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909884.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909876","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909876.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910205","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910205.png"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909941","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909941.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910018","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910018.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910096","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910096.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910189","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910189.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909800","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909800.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909764","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909764.png"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909995","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909995.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909901","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909901.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910110","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910110.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910135","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910135.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909910","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909910.png"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910065","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910065.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19910147","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910147.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910007","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910007.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910058","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910058.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19910183","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910183.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Twiter","id":"19909794","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909794.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19909768","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909768.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Linkedin","id":"19910005","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19910005.jpg"},{"time_stamp":"2021-06-16 12:32:08","source":"Facebook","id":"19909815","image_path":"/home/ahmed/projects/Image_Similarity-main/SubImages/19909815.jpg"}]
# """
    json_input = json.loads(raw_input_str)
    results,empty_results= process_json(json_input)
    output = {}
    if len(results)>0:
        output["results"]=results
    if len(results)>0:
        output["empty_results"]=empty_results
        

    # print(results)
    print(json.dumps(output,indent=4)) 
           

get_output()