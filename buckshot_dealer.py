from buckshot_actor import BuckShot_Actor
from random import randint
from buckshot_item import item_id

# Typing Imports
from buckshot_env import BuckShot_Environment



class Dealer(BuckShot_Actor):
  def __init__(self, max_health=2) -> None:
    super().__init__(max_health)

    self.current_slot = 0
    self.item_phase = True


  def shoot_correct(self) -> int:
    return self.get_shotgun.current_shell()-2

  def shoot_random() -> int:
    coin_flip = randint(0, 1)
    return coin_flip -2
  
  def shoot_already(self) -> int:
    # Dealer shoots randomly unless he knows the current shell.
    if(self.does_he_know): choice = self.shoot_correct
    else: choice = self.shoot_random
    return choice
  

  # Dealer AI
  # He uses every usable item in Itemslot order, then shoots.
  # He shoots randomly unless he knows the current shell
  # And he always knows the last shell in a load.
  
  # @log_action
  def make_choice(self, env: BuckShot_Environment) -> int:
    if(self.item_phase):
      # He cycles through inventory looking for a usable item
      while(self.current_slot < self.max_inventory):
        slot = self.inventory.itemslot(self.current_slot)
        self.current_slot += 1
        
        # Exits loop when it finds one or runs out of inventory
        if(slot == None) or (slot.check_usable() == False): continue
        else: break

      # If it can't use any items, it'll exit the item phase
      if(slot == None) or (slot.check_usable() == False):
        self.item_phase = False
        self.current_slot = 0
      else: # Otherwise, it'll use that item.
        choice = slot.get_id()

    # When it leaves the item phase, it chooses to shoot.
    if(self.item_phase == False):
      choice = self.shoot_already()
      self.item_phase = True

    return choice

