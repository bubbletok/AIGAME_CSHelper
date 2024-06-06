import HPBarProcessor
import MinionHPCaculator
import PIL.Image
import MinionHPBarConnector

def IsLastHit(minion:MinionHPBarConnector.Minion, attackDamage:int, currentTime:float)->bool:
    isLastHit = False

    hpByTime = MinionHPCaculator.CaculateHP(minion.type, currentTime)
    hpRatio = HPBarProcessor.CaculateHpRatio(minion.hpBar.img)

    hp = round(hpByTime * hpRatio)

    print(hpByTime)
    print(hpRatio)
    print(hp)

    isLastHit = (hp < attackDamage)

    return isLastHit

if __name__ == '__main__':
    testImg = PIL.Image.open("Data/HPBar_test.png")

    testHPBar = MinionHPBarConnector.HPBar(testImg, (0,0,0,0))
    testMinion = MinionHPBarConnector.Minion(0, (0,0,0,0), testHPBar)

    print(IsLastHit(testMinion, 600, 300))