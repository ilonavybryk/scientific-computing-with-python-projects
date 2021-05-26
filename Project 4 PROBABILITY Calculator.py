import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for argument in kwargs.keys():
            for key in range(kwargs[argument]):
                self.contents.append(argument)

    def draw(self, n_of_draws):
        n_of_draws = min(n_of_draws, len(self.contents))
        balls = list()
        for draw in range(n_of_draws):
            index = random.randint(0, len(self.contents)-1)
            balls.append(self.contents.pop(index))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    result = 0
    for draw in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        balls = experiment_hat.draw(num_balls_drawn)
        num_of_colors = 0
        for color in expected_balls.keys():
            if balls.count(color) >=expected_balls[color]:
                num_of_colors = num_of_colors + 1
        if num_of_colors == len(expected_balls):
            result += 1
    probability = float(result)/num_experiments
    return(probability)