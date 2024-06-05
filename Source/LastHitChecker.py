import HPBarProcessor
import MinionHPCaculator
import PIL.Image

def IsLastHit(hpBarImg:PIL.Image, attackDamage:float, minionType:MinionHPCaculator.MinionType, currentTime:float)->bool:
    isLastHit = False

    hpByTime = MinionHPCaculator.CaculateHP(minionType, currentTime)
    hpRatio = HPBarProcessor.CaculateHpRatio(hpBarImg)

    hp = round(hpByTime * hpRatio)

    print(hpByTime)
    print(hpRatio)
    print(hp)

    isLastHit = (hp < attackDamage)

    return isLastHit

testImg = PIL.Image.open("Data/HPBar_test.png")

print(IsLastHit(testImg, 600, MinionHPCaculator.MinionType.Melee, 300))