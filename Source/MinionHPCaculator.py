from enum import IntEnum
import datetime
import math

class MinionType(IntEnum):
    Melee = 0
    Caster = 1
    Siege = 2

minionInitialHP = [477,296,912] # HP of minions when spawned first
meleeMinionHPPlus= [33,34,35,34,35,36,35,36,36,37,36,37,38,37,38,39,38,39,39,40]

class WrongMinionTypeError(Exception):
    def __init__(self):
        self.msg = "minion type must be Melee(0), Caster(1), or Seige(2)"
    def __str__(self):
        return self.msg

def CaculateHP(type:MinionType, time:float) -> float:
    hp = 0
    if(type == MinionType.Melee):
        hp = CaculateMeleeHP(time)
    elif(type == MinionType.Caster):
        hp = CaculateCasterHP(time)
    elif(type == MinionType.Siege):
        hp = CaculateSiegeHP(time)
    else:
        raise WrongMinionTypeError()

    hp = math.floor(hp)
    return hp

def CaculateMeleeHP(time:float) -> float:
    hp = minionInitialHP[MinionType.Melee]
    waveNum = 1
    targetWaveNum = TimeToWave(time)

    while(waveNum < targetWaveNum):
        print(waveNum)
        if(waveNum>=4 and (waveNum-1)%3==0):
            if((waveNum) <= 15):
                hp = round(hp+22+((waveNum-1)/3)*0.3, 1)
            else:
                hp += meleeMinionHPPlus[int((waveNum-1)/3 - 5)]
        waveNum += 1

    return hp
def CaculateCasterHP(time:float) -> float:
    hp = minionInitialHP[MinionType.Caster]
    waveNum = 1
    targetWaveNum = TimeToWave(time)

    while(waveNum < targetWaveNum):
        if(waveNum>=4 and (waveNum-1)%3==0):
            if((waveNum) <= 15):
                hp += 6
            else:
                hp += 8.25
        waveNum += 1

    return hp
def CaculateSiegeHP(time:float) -> float:
    hp = minionInitialHP[MinionType.Siege]
    waveNum = 1
    targetWaveNum = TimeToWave(time)
    while(waveNum < targetWaveNum):
        if(waveNum>=4 and (waveNum-1)%3==0):
            if((waveNum) <= 15):
                hp += 62
            else:
                hp += 87
        waveNum += 1

    return hp

def TimeToWave(time:float) -> int:
    return (time-35)//30

def PrintAllHP():
    hp = [0,0,0]
    hp[0] = minionInitialHP[MinionType.Melee]
    hp[1] = minionInitialHP[MinionType.Caster]
    hp[2] = minionInitialHP[MinionType.Siege]

    waveNum = 1
    time = 65

    spawnSiege = False

    #HPsheet = open('Data/MinionHPSheet.txt','w')

    while True:
        if time>2235:
            break
        
        if(3 <= waveNum <= 26):
            if(waveNum%3==0):
                spawnSiege = True
            else:
                spawnSiege = False
        elif(27 <= waveNum <= 48):
            if((waveNum-1)%2==0):
                spawnSiege = True
            else:
                spawnSiege = False
        elif(49 <= waveNum):
            spawnSiege = True
        
        if(waveNum>=4 and (waveNum-1)%3==0):
            if((waveNum) <= 15):
                hp[0] = round(hp[0]+22+((waveNum-1)/3)*0.3, 1)
                hp[1] += 6
                hp[2] += 62
            else:
                hp[0] += meleeMinionHPPlus[int((waveNum-1)/3 - 5)]
                hp[1] += 8.25
                hp[2] += 87

        if(spawnSiege == False):
            print('Wave {0:02d} | {1} - {2:6.1f}, {3:6.2f}, {4:>4}'.format(waveNum,str(datetime.timedelta(seconds=time)), hp[0],hp[1],-1))
            #HPsheet.write('Wave {0:02d} | {1} - {2:6.1f}, {3:6.2f}, {4:>4}\n'.format(waveNum,str(datetime.timedelta(seconds=time)), hp[0],hp[1],"X"))
        else:
            print('Wave {0:02d} | {1} - {2:6.1f}, {3:6.2f}, {4:4}'.format(waveNum,str(datetime.timedelta(seconds=time)), hp[0],hp[1],hp[2]))
            #HPsheet.write('Wave {0:02d} | {1} - {2:6.1f}, {3:6.2f}, {4:4}\n'.format(waveNum,str(datetime.timedelta(seconds=time)), hp[0],hp[1],hp[2]))

        waveNum += 1
        time += 30

    #HPsheet.close()

'''Test'''
#print(CaculateHP(MinionType.Caster, 1290))
#PrintAllHP()