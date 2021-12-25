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
        if len(self.__dict__) < 2:
            raise TypeError(f'At least one positional argument in "Key=Value" format is required.')

    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        list_of_random_balls = []
        for balls in range(number_of_balls):
            chose_ball = random.choice(self.contents)
            list_of_random_balls.append(chose_ball)
            self.contents.remove(chose_ball)
        return list_of_random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    hat_contents = copy.deepcopy(hat)
    hat_draw = copy.deepcopy(hat.draw(num_balls_drawn))
    expected_balls_dict = copy.deepcopy(expected_balls)
    for k, v in expected_balls_dict.items():
        expected_balls_dict[k] = 0
    print(hat_draw)

    for element in hat_draw:
        try:
            expected_balls_dict[element] += 1
        except:
            continue
    print(expected_balls_dict)
    print(expected_balls)
    count = 0
    for k, v in expected_balls_dict.items() and expected_balls.items():
        if expected_balls_dict[k] >= expected_balls[k]:
            count += 1

    return count/num_experiments


if __name__ == '__main__':
    hat1 = Hat(yellow=4, blue=3, green=5)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    hat4 = Hat(red=1)
    print(experiment(hat=hat1,
                     expected_balls={"yellow": 2, "green": 1},
                     num_balls_drawn=5,
                     num_experiments=2000))
    # print(hat1.__dict__)
    # print(hat2.__dict__)
    # print(hat3.__dict__)
