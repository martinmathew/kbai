from collections import Set
from xml.dom import INVALID_STATE_ERR

from src.com.martin.png.Bank import Bank
from src.com.martin.png.River import River
from src.com.martin.png import SmartGenerator


class SmartGenerator:

    def __init__(self):
        self.prev_state: set = set()

    def gernerate(self, initial: River, leftToRight: bool):
        if initial == River.INVALID_STATE or initial in self.prev_state:
            return River.INVALID_STATE
        elif initial.isFinal():
            return initial
        else:
            self.prev_state.add(initial)
            if leftToRight:
                leftToRight = initial.moveFromLeftToRight(2, 0)
                new_state = self.gernerate(leftToRight, False)
                if new_state == River.INVALID_STATE:
                    leftToRight = initial.moveFromLeftToRight(0, 2)
                    new_state = self.gernerate(leftToRight, False)
                    if new_state == River.INVALID_STATE:
                        leftToRight = initial.moveFromLeftToRight(1, 1)
                        new_state = self.gernerate(leftToRight, False)
                        if new_state == River.INVALID_STATE:
                            leftToRight = initial.moveFromLeftToRight(1, 0)
                            new_state = self.gernerate(leftToRight, False)
                            if new_state == River.INVALID_STATE:
                                leftToRight = initial.moveFromLeftToRight(0, 1)
                                new_state = self.gernerate(leftToRight, False)
                                self.prev_state.remove(initial)
                                return new_state
                            else:
                                self.prev_state.remove(initial)
                                return new_state
                        else:
                            self.prev_state.remove(initial)
                            return new_state
                    else:
                        self.prev_state.remove(initial)
                        return new_state
                else:
                    self.prev_state.remove(initial)
                    return new_state
            else:
                rightToLeft = initial.moveFromRightToLeft(1, 0)
                new_state = self.gernerate(rightToLeft, True)
                if new_state == River.INVALID_STATE:
                    rightToLeft = initial.moveFromRightToLeft(0, 1)
                    new_state = self.gernerate(rightToLeft, True)
                    if new_state == River.INVALID_STATE:
                        rightToLeft = initial.moveFromRightToLeft(1, 1)
                        new_state = self.gernerate(rightToLeft, True)
                        if new_state == River.INVALID_STATE:
                            rightToLeft = initial.moveFromRightToLeft(2, 0)
                            new_state = self.gernerate(rightToLeft, True)
                            if new_state == River.INVALID_STATE:
                                rightToLeft = initial.moveFromRightToLeft(0, 2)
                                new_state = self.gernerate(rightToLeft, True)
                                self.prev_state.remove(initial)
                                return new_state
                            else:
                                self.prev_state.remove(initial)
                                return new_state
                        else:
                            self.prev_state.remove(initial)
                            return new_state
                    else:
                        self.prev_state.remove(initial)
                        return new_state
                else:
                    self.prev_state.remove(initial)
                    return new_state

    def generateIter(self,initial:River):
        stk = [initial]
        left_to_right = True
        min = 99999999
        while stk.__len__() > 0:
            if left_to_right:
                lr = initial.moveFromLeftToRight(2, 0)
                if lr == River.INVALID_STATE or lr in stk :
                    lr = initial.moveFromLeftToRight(0,2)
                elif lr.isFinal():
                    stk.append(lr)
                    print(stk)
                    stk.pop()
                    if lr == River.INVALID_STATE or lr in stk:
                        lr = initial.moveFromLeftToRight(1,1)
                    elif lr.isFinal():
                        stk.append(lr)
                        print(stk)
                        stk.pop()
                        if lr == River.INVALID_STATE or lr in stk:
                            lr = initial.moveFromLeftToRight(1,0)
                        elif lr.isFinal():
                            stk.append(lr)
                            print(stk)
                            stk.pop()
                            if lr == River.INVALID_STATE or lr in stk:
                                lr = initial.moveFromLeftToRight(0,1)
                            elif lr.isFinal():
                                stk.append(lr)
                                print(stk)
                                stk.pop()
                                if lr == River.INVALID_STATE or lr in stk:
                                    stk.pop()
                                    initial = stk.pop()
                                elif lr.isFinal():
                                    stk.append(lr)
                                    print(stk)
                                    stk.pop()
                                else:
                                    stk.append(lr)
                                    initial = lr
                            else:
                                stk.append(lr)
                                initial = lr;
                        else:
                            stk.append(lr)
                            initial = lr
                    else:
                        stk.append(lr)
                        initial = lr
                else:
                    stk.append(lr)
                    initial = lr

            else:
                rl = initial.moveFromRightToLeft(1,0)
                if rl == River.INVALID_STATE:
                    rl = initial.moveFromRightToLeft(0,1)
                    if rl == River.INVALID_STATE:
                        rl = initial.moveFromRightToLeft(1,1)
                        if rl == River.INVALID_STATE:
                            rl = initial.moveFromRightToLeft(2,0)
                            if rl == River.INVALID_STATE:
                                rl = initial.moveFromRightToLeft(0,2)
                                if rl == River.INVALID_STATE:
                                    stk.pop()
                                    initial = stk.pop()
                                else:
                                    stk.append(rl)
                                    initial = rl
                            else:
                                stk.append(rl)
                                initial = rl
                        else:
                            stk.append(rl)
                            initial = rl
                    else:
                        stk.append(rl)
                        initial = rl
                else:
                    stk.append(rl)
                    initial = rl
            left_to_right = not left_to_right








if __name__ == "__main__":
    initial_state = River(Bank(3, 3, 3, 3), Bank(3, 3, 0, 0),True)
    gen = SmartGenerator()
    final_state = gen.gernerate(initial_state, True)
    print(final_state)
