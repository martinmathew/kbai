from src.com.martin.png import Bank


class Bank:


    def __init__(self, maxGuard, maxPrison, guard, prison):
        self.guard = guard
        self.prison = prison
        self.maxGuard = maxGuard
        self.maxPrison = maxPrison;

    def add(self, prison, guard):
        if ((self.prison + prison <= self.maxPrison) and (self.guard + guard <= self.maxGuard) and (self.guard+guard == 0 or
                self.guard + guard >= self.prison + prison)):
            return Bank(self.maxGuard, self.maxPrison, self.guard + guard, self.prison + prison)
        else:
            return Bank.INVALID_STATE

    def remove(self, prison, guard):
        if ((self.prison - prison >= 0) and (self.guard - guard >= 0) and (self.guard-guard == 0 or self.guard - guard >= self.prison - prison)):
            return Bank(self.maxGuard, self.maxPrison, self.guard-guard, self.prison - prison)
        else:
            return Bank.INVALID_STATE

    def isValidState(self):
        return (self.prison <= self.maxPrison or self.prison >= 0) and (
                    self.guard <= self.maxGuard or self.guard >= 0) and (self.guard >= self.prison)

    def isEmpty(self):
        return (self.prison == 0 and self.guard == 0)

    def isFull(self):
        return (self.prison == self.maxPrison and self.guard == self.maxGuard)

    def __eq__(self, o: object) -> bool:
        return self.prison == o.prison and self.guard == o.guard

    def __hash__(self) -> int:
        return self.guard*pow(2,2)+self.prison*pow(2,1)

    def __str__(self) -> str:
        return "Prison:"+self.prison+"\nGuard:"+self.guard

    def __repr__(self) -> str:
        return self.__str__()


Bank.INVALID_STATE = Bank(-1, -1, -1, -1)