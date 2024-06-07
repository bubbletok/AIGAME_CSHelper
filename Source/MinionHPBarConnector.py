import MinionHPCaculator
import PIL.Image
import math

connectionThreshold = 50

class HPBar:
    def __init__(self, image:PIL.Image, box:list):
        self.img = image

        self.x = box[0]
        self.y = box[1]
        self.w = box[2] - box[0]
        self.h = box[3] - box[1]
        self.pos = (self.x+self.w/2, self.y+self.h/2)

class Minion:
    def __init__(self, type:MinionHPCaculator.MinionType, box:list, hpBar:HPBar = None):
        self.type = type
        self.hpBar = hpBar

        self.x = box[0]
        self.y = box[1]
        self.w = box[2] - box[0]
        self.h = box[3] - box[1]
        self.pos = (self.x+self.w/2, self.y+self.h/2)


def DistanceBetween(pos1:list[float,float], pos2:list[float,float]):
    return math.sqrt(math.pow(pos1[0]-pos2[0], 2) + math.pow(pos1[1] - pos2[1]))

def FindHpBar(minion:Minion, hpBarList:list[HPBar]):
    nearestDistance = 9999
    nearestBar = None
    for bar in hpBarList:
        if DistanceBetween(minion.pos, bar.pos) < connectionThreshold:
            if DistanceBetween < nearestDistance:
                nearestBar = bar
            else:
                continue
    minion.hpBar = nearestBar

def Connect(minionList:list[Minion], hpBarList:list[HPBar]):
    for elem in minionList:
        if elem.hpBar == None:
            FindHpBar(elem, hpBarList)