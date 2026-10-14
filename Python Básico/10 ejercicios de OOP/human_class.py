"""COCNECTANDO LAS CLASES DE MANERA LÓGICA"""


# ESTA CLASE ES PARA REPRESENTAR LAS MANOS  
class Hand:
    pass

right_hand = Hand()
left_hand = Hand()

# ESTA ES PARA REPRESENTAR LOS BRAZOS 
class Arm:
    def __init__(self,hand):
        self.hand = hand

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

# ESTA REPRESENTA LOS PIES Y SE HACE LO MISMO A LO ANTERIOR
class Feet:
    pass

right_foot = Feet()
left_foot = Feet()

class Leg:
    def __init__(self, foot):
        self.foot = foot

right_leg = Leg(right_foot)
left_leg = Leg(left_foot)


class Head:
    pass

head = Head()

class Torso:
    def __init__(self,head_1,right_arm_1,left_arm_1):
        self.head = head_1
        self.right_arm = right_arm_1
        self.left_arm = left_arm_1

torso = Torso(head,right_arm,left_arm)

class Human:
    def __init__(self,torso_1,right_leg_1,left_leg_1):
        self.torso = torso_1
        self.right_leg = right_leg_1
        self.left_leg = left_leg_1

human = Human(torso,right_leg,left_leg)
