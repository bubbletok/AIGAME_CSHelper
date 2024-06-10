import HPBarProcessor
import MinionHPCaculator
import PIL.Image
import MinionHPBarConnector

def IsLastHit(minion:MinionHPBarConnector.Minion, attackDamage:int, currentTime:float)->bool:
    isLastHit = False

    hpByTime = MinionHPCaculator.CaculateHP(minion.type, currentTime)
    # print(f"hpByTime: {hpByTime}")
    hpRatio = HPBarProcessor.CaculateHpRatio(minion.hpBar.img)
    # print(f"hpRatio: {hpRatio}")
    hpRatio = 1.0 if hpRatio > 1.0 else hpRatio
    hp = round(hpByTime * hpRatio)

    # print(f"hp: {hp}, attackDamage: {attackDamage}")
    isLastHit = (hp < attackDamage)

    return isLastHit

if __name__ == '__main__':
    testImg = PIL.Image.open("Data/HPBar_test.png")

    testHPBar = MinionHPBarConnector.HPBar(testImg, (0,0,0,0))
    testMinion = MinionHPBarConnector.Minion(0, (0,0,0,0), testHPBar)

    print(IsLastHit(testMinion, 600, 300))