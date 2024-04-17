from buckshot_actor import BuckShot_Actor
from random import randint
from buckshot_item import get_list_item_id

class Dealer(BuckShot_Actor):
  def __init__(self, max_health=2) -> None:
    super().__init__(max_health)
    self.alt_inventory = []*(self.max_inventory)

    self.current_slot = 0
    self.item_phase = True
    self.knower = False

  
  def stop_knowing(self):
    self.knower = False

  def start_knowing(self):
    self.knower = True

  def shoot_correct(self) -> int:
    return self.env.Shotgun.current_bullet()-2

  def shoot_random() -> int:
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
      return self.knower



  def make_choice(self, env) -> int:

    choice = -5

    while(self.item_phase and (self.current_slot < self.inventory.size)):
      slot = self.inventory.itemslot(self.current_slot)
      
      # Item phase logic

    else:
      if(self.does_he_know):
        choice = self.shoot_correct
      else:
        choice = self.shoot_random
      self.item_phase = True
  
    return choice

