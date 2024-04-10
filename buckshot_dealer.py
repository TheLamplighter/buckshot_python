from buckshot_actor import BuckShot_Actor
from random import randint

class Dealer(BuckShot_Actor):
  the_knower = False

  def shoot_random():
    coin_flip = randint(0, 1)
    return coin_flip -2
  
  def full_health(self) -> bool:
    if self.cur_health == self.max_health:
      return True
    return False
  
  def does_he_know(self, env) -> bool:
    count = env.Shotgun.get_shell_count()

    if count == 1:
      return True
    else:
      return False



  def make_choice(self, env) -> int:
    pass