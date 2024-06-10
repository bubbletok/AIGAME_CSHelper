import numpy as np
import cv2
import pyscreenshot as ImageGrab
import os
import torch
import shutil # to delete directory
import time
import pyautogui
import mss

WIDTH = 1920
HEIGHT = 1080

detect_path = os.path.join('Source','yolov5','detect.py')
weight_path = os.path.join('Data','Weights','best.pt')
source_path = os.path.join('Data','Images','image.png')
data_path = os.path.join('Data','custom.yaml')
project_path = os.path.join('Data','Results')
name_path = os.path.join('results')
results_path = os.path.join(project_path, name_path)
def detect():
    delete_results()
    # image = pyautogui.screenshot()
    # print(type(image))
    with mss.mss() as sct:
        img=sct.shot(mon=1, output="main_mon.png")

    os.system(f"python {detect_path} --weights {weight_path} --source screen --data {data_path} --nosave --save-txt --project {project_path} --name {name_path} --device 0")
    
    
def delete_results():
    if os.path.exists(results_path):
        shutil.rmtree(results_path)
if __name__ == '__main__':
    detect()