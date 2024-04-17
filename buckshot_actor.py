from abc import ABC, abstractmethod
from buckshot_inventory import BuckShot_Inventory
from buckshot_item import item_id
from copy import deepcopy
from numpy import clip

class BuckShot_Actor():
  def __init__(self, max_health=2) -> None:
    # Essential Stats
    self.max_health = max_health
    self.cur_health = max_health

    self.max_inventory = 8
    self.inventory = BuckShot_Inventory(self, self.max_inventory)
    
    # Senses
    self.env = object
    self.probability = 0.5
    self.cuffed = False
    self.other_guy = object
    self.knower = False
  


  #Getters
  def get_max_health(self) -> int:
    return self.max_health
  
  def get_cur_health(self) -> int:
    return self.cur_health
  
  def get_hp_percent(self) -> int:
    per = self.cur_health / self.max_health
    return per*100  

  

  def get_env(self) -> object:
    return self.env
  
  def get_other_guy(self) -> object:
    return self.other_guy
  
  def get_shotgun(self) -> object:
    return self.env.Shotgun
  

  def get_cuffed_status(self) -> bool:
    return self.cuffed
  
  def the_other_guy(self):
    if self == self.env.Dealer:
      return self.env.Player
    else:
      return self.env.Dealer
  


  #Setters
  def set_max_health(self, value) -> None:
    self.max_health = value
    return
  
  def set_cur_health(self, value) -> None:
    self.cur_health = clip(0, value, self.max_health)
    return

  def take_damage(self, dmg) -> None:
    self.set_cur_health(self.cur_health - dmg)
    return
  
  def heal_damage(self, heal) -> None:
    self.set_cur_health(self.cur_health + heal)
    return
  
  def set_cuffed(self) -> None:
    self.cuffed = True
    return
  
  def set_uncuffed(self) -> None:
    self.cuffed = False
    return
  

  def set_env(self, env) -> None:
    self.env = env
    return

  def add_item(self, item) -> None:
    self.inventory.add(item)

  def remove_item(self, item) -> None:
    self.inventory.remove(item)

  def count_item(self, item) -> int:
    self.inventory.count_item(item)

  def has_item(self, item) -> bool:
    self.inventory.has_item(item)

  def clear_inventory(self) -> None:
    self.inventory.clear()


  # Actions
  def shoot_shotgun(self, tgt):
    self.get_shotgun.fire_shotgun(tgt)
    self.knower = False
    return
  
  def shoot_enemy(self):
    self.shoot_shotgun(self.other_guy)
    return
  
  def shoot_self(self):
    self.shoot_shotgun(self)
    return
  
  def use_item(self, item) -> None:
    item.use(self, self.env)
    return



  # Decision Logic
  @abstractmethod
  def make_choice(self, env):
    pass


  def take_turn(self):
    if self.cuffed:
      self.set_uncuffed()
      return

    choice = -5

    while(choice not in {-1, -2}):
      choice = self.make_choice()
      
      if choice in {-1, -2}:
        if choice == -2:
          tgt = self
        if choice == -1:
          tgt = self.the_other_guy()
        self.env.Shotgun.fire_shotgun(tgt)
      else:
        if self.inventory[choice] >= 0:
          item_id()[choice].use(self, self.env)
          self.inventory[choice] += -1



      