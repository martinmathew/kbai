from xml.dom import INVALID_STATE_ERR

from src.com.martin.png import Bank
from src.com.martin.png.Bank import *
from src.com.martin.png.River import *
from src.com.martin.png import River


class River:


    def __init__(self, left: Bank, right: Bank,boat_at_left:bool):
        self.left = left
        self.right = right
        self.boat_at_left = boat_at_left

    def moveFromLeftToRight(self, guard, prison):
        if (self.left.remove(prison, guard) == Bank.INVALID_STATE or self.right.add(prison, guard) == Bank.INVALID_STATE):
            return River.INVALID_STATE
        else:
            return River(self.left.remove(prison, guard), self.right.add(prison, guard),False)

    def moveFromRightToLeft(self, guard, prison):
        if (self.right.remove(prison, guard) == Bank.INVALID_STATE or self.left.add(prison, guard) == Bank.INVALID_STATE):
            return River.INVALID_STATE
        else:
            return River(self.left.add(prison, guard), self.right.remove(prison, guard),True)

    def isValid(self):
        return self.left.isValidState() and self.right.isValidState()

    def isFinal(self):
        return self.left.isEmpty() and self.right.isFull();

    def __eq__(self, o: object) -> bool:
        return self.left.__eq__(o.left) and self.right.__eq__(o.right) and self.boat_at_left == o.boat_at_left

    def __hash__(self) -> int:
        return self.left.__hash__()*pow(2,2)+self.right.__hash__()*pow(2,1)+ (13 if self.boat_at_left else 7)

    def __str__(self) -> str:
        return "left,{"+self.left.__str__()+"} right {"+self.right.__str__()+"}"

    def __repr__(self) -> str:
        return self.__str__()


River.INVALID_STATE = River(Bank.INVALID_STATE, Bank.INVALID_STATE,False)

