import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, contents=None, **ball):
        self.contents = []
        for k, v in ball.items():
            for i in range(v):
                self.contents.append(k)
        for color in ball.keys():
            self.__dict__[color] = ball[color]
        if len(self.__dict__) < 1:
            raise TypeError('At least one positional argument is required.')


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__ == '__main__':
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    print(hat1.contents)
    print(hat2.contents)
    # print(hat1.__dict__)
    # print(hat2.__dict__)
    # print(hat3.__dict__)
