import copy
import random

# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _count in range(value):
        self.contents.append(key)

  def draw(self, n):
    draw_balls = []
    if n > len(self.contents):
      n = len(self.contents)
    for _ in range(n):
      pos_ball = random.randrange(0,len(self.contents))
      draw_balls.append(self.contents[pos_ball])
      del(self.contents[pos_ball])
    return draw_balls
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for _ in range(num_experiments):
    another_hat = copy.deepcopy(hat)
    balls_drawn = another_hat.draw(num_balls_drawn)
    count = 0
    for k, v in expected_balls.items():
      if balls_drawn.count(k) >= v:
        count += 1
    if count == len(expected_balls):
      m += 1
      
  return m/num_experiments
