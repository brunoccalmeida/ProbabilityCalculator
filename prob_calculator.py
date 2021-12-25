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
    times_expected_balls_in_draw = 0
    hat_draw = copy.copy(hat.draw(num_balls_drawn))
    # print(hat_draw)
    # print(expected_balls)
    print(hat.contents)
    # for i in range(num_experiments):
    #     for element in hat_draw:
    #         print(element)

    #         if element not in hat_draw:
    #             all_elements_in = False
    #         else:
    #             all_elements_in = True
    #     if all_elements_in:
    #         times_expected_balls_in_draw += 1
    #
    # return times_expected_balls_in_draw/num_experiments


if __name__ == '__main__':
    hat1 = Hat(yellow=2, blue=2, green=2)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    hat4 = Hat(red=1)
    print(experiment(hat=hat1,
                     expected_balls={"yellow": 3, "green": 1},
                     num_balls_drawn=5,
                     num_experiments=1))
    # print(hat1.__dict__)
    # print(hat2.__dict__)
    # print(hat3.__dict__)
