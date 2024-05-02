from buckshot_actor import BuckShot_Actor
from random import randint
from buckshot_item import item_id
from buckshot_env import BuckShot_Environment

class Dealer(BuckShot_Actor):
  def __init__(self, max_health=2) -> None:
    super().__init__(max_health)

    self.current_slot = 0
    self.item_phase = True


  def shoot_correct(self) -> int:
    return self.get_shotgun.current_bullet()-2

  def shoot_random() -> int:
    coin_flip = randint(0, 1)
    return coin_flip -2
  
  def shoot_already(self) -> int:
    if(self.does_he_know):
      choice = self.shoot_correct
    else:
      choice = self.shoot_random
    return choice
  

  def make_choice(self, env: BuckShot_Environment) -> int:
    choice = -5

    slot = self.inventory.itemslot(self.current_slot)

    if(self.item_phase):
      while(self.current_slot < self.max_inventory):
        slot = self.inventory.itemslot(self.current_slot)
        self.current_slot += 1
        
        if(slot == None) or (slot.check_usable() == False):
          continue

      if(slot == None) or (slot.check_usable() == False):
        self.item_phase = False
        self.current_slot = 0
      else:
        choice = slot.get_id()


    if(self.item_phase == False):
      choice = self.shoot_already()
      self.item_phase = True
      self.stop_knowing

    return choice

