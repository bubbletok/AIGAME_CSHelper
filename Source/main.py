from text_recognintion import *
from DetectByYolov5 import *
from ultralytics import YOLO
import pyautogui
import torch
import os
from PIL import Image
import pathlib
from pathlib import Path
from draw import *
import re
from MinionHPBarConnector import *
from MinionHPCaculator import *
from LastHitChecker import *

pathlib.PosixPath = pathlib.WindowsPath
result_path = 'runs/detect'
hp_bar_path = 'runs/detect/exp/crops/HpBar'

model = torch.hub.load('ultralytics/yolov5','custom',path='Data/Weights/best.pt', force_reload=True, trust_repo=True)
draw_cls = draw()

time_num = 0
attack_num = 0

while True:

    # 지난 결과 이미지 삭제
    if os.path.exists(result_path):
        shutil.rmtree(result_path)

    # 공격력, 게임시간 추출
    box1 = (430,910,465,940) # attack
    box2 = (1855,32,1900,50) # time

    attack_text = text_recognition(*box1)
    time_text = text_recognition(*box2)

    if time_text != None and time_text != '': # 잘 인식 된 경우
        # 잘못 인식된 기호 삭제
        time_text = re.findall(r'\d+',time_text)
        time_text = ''.join(time_text)
        time_text = int(time_text)
        time_text = (time_text//100)*60 + time_text%60
        if time_num == 0:
            time_num = time_text
            
        # 숫자 잘 인식된 경우
        elif time_text-time_num < 10:
            time_num = time_text
            
    if attack_text != None and attack_text!='': # 잘 인식 된 경우
        # 잘못 인식된 기호 삭제
        attack_text = re.findall(r'\d+',attack_text)
        attack_text = ''.join(attack_text)
        attack_num = int(attack_text)
    
    # draw_cls.rect(*box1)
    # draw_cls.rect(*box2)




    # 주 모니터 캡처
    with mss.mss() as sct:
        image=sct.shot(mon=1, output="obj.png")

    # 모델에 캡처 이미지 input
    results = model(image)
    pd = results.pandas().xyxy
    results.crop()
    pd = pd[0] # 결과 pandas

    minion_lst = []
    hp_bar_image_lst = []
    hp_bar_lst = []


    # connect minion and HPbar
    # hp bar lst 만들기
    try:
        for filename in os.listdir(hp_bar_path):
            # 파일의 전체 경로 생성
            file_path = os.path.join(hp_bar_path, filename)
            
            
            # 이미지 파일 열기
            with Image.open(file_path) as img:
                # 이미지 객체를 리스트에 추가
                hp_bar_image_lst.append(img.copy())  # .copy()를 사용하여 파일을 닫은 후에도 이미지 객체를 유지
    except (IOError, SyntaxError) as e:
        print(f"there's no obj")


    # 모든 객체에 대해
    hp_bar_var = 0
    for i in range(len(pd)): 

        if pd.iloc[i,5] != 3: # 미니언
            minion = Minion(type=MinionType(pd.iloc[i,5]),box=list(pd.iloc[i,:4].astype(int)))
            minion_lst.append(minion)

        else: # hp_bar
            hp_bar = HPBar(image=hp_bar_image_lst[hp_bar_var],box=list(pd.iloc[i,:4].astype(int)))
            hp_bar_lst.append(hp_bar)
            hp_bar_var += 1

        # x1,y1,x2,y2 = pd.iloc[i,:4].astype(int) # box xy
        # draw_cls.rect(x1,y1,x2,y2) # box그리기
        
    
    Connect(minion_lst,hp_bar_lst)

    

    attack_num = 200
    time_num = 200
    # check islastattack
    for i in minion_lst:
        if i.hpBar != None: # hpbar 인식 되었다면
            # print("lower hp")
            if IsLastHit(i,attack_num,time_num): # 막타 타이밍 이면
                x1,y1=i.x,i.y
                x2 = i.w + x1
                y2 = i.h + y1
                draw_cls.rect(x1,y1,x2,y2)




    # time.sleep(0.1)
        
