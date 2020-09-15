# # Class

# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 6 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, loccation, damage):
#   print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, loccation, damage))

# attack(name, "1시", damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank_name,"1시",tank2_damage)

class Unit:
  def __init__(self, name, hp, damage): #__init__ 파이썬에서 쓰이는 생성자. 마린이나 탱크와 같은 객체가 만들어질 때, 자동으로 호출되는 부분
    self.name = name
    self.hp = hp                # 멤버 변수
    self.damage = damage
    print("{0} 유닛이 생성 되었습니다.".format(self.name))
    print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

class AttackUnit:
  def __init__(self, name, hp, damage): 
      self.name = name
      self.hp = hp
      self.damage = damage

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank1 = Unit("탱크",150,35)

# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name, wraith1.damage)) # .멤버변수명 으로 접근 가능

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#   print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# # if wraith1.clocking == True:
#   print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name)) 클래스 외부에서 원하는 변수에 대해 확장을 할 수 있고, 확장된 변수는 확장을 한 객체에 대해서만 적용되고, 기존에 있던 다른 객체들에는 적용이 안된다.

