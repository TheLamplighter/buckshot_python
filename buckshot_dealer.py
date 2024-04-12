from buckshot_actor import BuckShot_Actor
from random import randint
from buckshot_item import get_list_item_id

class Dealer(BuckShot_Actor):
  def __init__(self, max_health=2) -> None:
    super().__init__(max_health)
    self.alt_inventory = []*(self.max_inventory)

    




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
    choice = randint(0, len(get_list_item_id))





    if(self.does_he_know or self.used_item[3]):
      pass
    else:
      pass
    pass