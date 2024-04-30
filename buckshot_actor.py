from abc import ABC, abstractmethod
from buckshot_inventory import BuckShot_Inventory
from buckshot_shotgun import BuckShot_Shotgun
from buckshot_actor import BuckShot_Actor
from buckshot_env import BuckShot_Environment
from buckshot_item import item_id, BuckShot_Item
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
  
  def is_full_health(self) -> bool:
    if self.get_cur_health == self.get_max_health:
      return True
    return False
  
  def get_hp_percent(self) -> int: #Is this necessary?
    per = self.get_cur_health / self.get_max_health
    return per*100  

  

  def get_env(self) -> BuckShot_Environment:
    return self.env
  
  def get_other_guy(self) -> BuckShot_Actor:
    return self.other_guy
  
  def get_shotgun(self) -> BuckShot_Shotgun:
    return self.env.Shotgun
  

  def count_item(self, item) -> int:
    self.inventory.count_item(item)

  def has_item(self, item) -> bool:
    self.inventory.has_item(item)
  

  def does_he_know(self) -> bool:
    count = self.get_shotgun.get_shell_count()

    if count == 1:
      return True
    else:
      return self.knower

  def get_cuffed_status(self) -> bool:
    return self.cuffed
  

  def the_other_guy(self, env: BuckShot_Environment) -> BuckShot_Actor:
    if self == env.get_dealer:
      return env.get_player
    else:
      return env.get_dealer
  


  #Setters
  def set_max_health(self, value) -> None:
    self.max_health = value
  
  def set_cur_health(self, value) -> None:
    self.cur_health = clip(0, value, self.max_health)

  def take_damage(self, dmg) -> None:
    self.set_cur_health(self.cur_health - dmg)
  
  def heal_damage(self, heal) -> None:
    self.set_cur_health(self.cur_health + heal)
  
  
  def set_cuffed(self) -> None:
    self.cuffed = True
  
  def set_uncuffed(self) -> None:
    self.cuffed = False
  

  def stop_knowing(self):
    self.knower = False

  def start_knowing(self):
    self.knower = True
  

  def set_env(self, env) -> None:
    self.env = env
  

  def add_item(self, item) -> None:
    self.inventory.add(item)

  def remove_item(self, item) -> None:
    self.inventory.remove(item)

  def clear_inventory(self) -> None:
    self.inventory.clear()



  # Actions
  def shoot_shotgun(self, tgt):
    self.get_shotgun.fire_shotgun(tgt)
    self.knower = False
  
  def shoot_enemy(self):
    self.shoot_shotgun(self.other_guy)
  
  def shoot_self(self):
    self.shoot_shotgun(self)
  
  def use_item(self, item) -> None:
    item_id()[item].use(self, self.env)



  # Decision Logic
  @abstractmethod
  def make_choice(self, env) -> None:
    pass


  def take_turn(self) -> None:
    if self.cuffed:
      self.set_uncuffed()
      return

    choice = -5

    while(choice not in {-1, -2}):
      choice = self.make_choice()
      
      if choice in {-1, -2}:
        if choice == -2:
          self.shoot_self
        if choice == -1:
          self.shoot_enemy
      else:
        if self.inventory.has_item(choice):
          self.use_item(choice)