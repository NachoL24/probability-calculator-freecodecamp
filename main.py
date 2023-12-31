# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

import prob_calculator

#prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=3, red=2, green=6)
#hat.draw(4)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "green": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability: ", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
