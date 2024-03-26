from abc import ABC, abstractmethod
from numpy import clip
from buckshot_item import get_list_item_id

class BuckShot_Actor():
  def __init__(self, max_health=2) -> None:
    # Essential Stats
    self.max_health = max_health
    self.cur_health = max_health
    self.max_inventory = 8
    self.inventory = [0]*len(get_list_item_id())
    
    # Senses
    self.env = object
    self.probability = 0.5
    self.cuffed = False
    self.other_guy = object
  


  #Getters
  def get_max_health(self) -> int:
    return self.max_health
  
  def get_cur_health(self) -> int:
    return self.cur_health
  
  def get_hp_percent(self) -> int:
    per = self.cur_health / self.max_health
    return per*100
  

  def get_inventory(self) -> list:
    return self.inventory
  
  def get_inventory_max(self) -> int:
    return self.max_inventory
  
  def get_inventory_size(self) -> int:
    return sum(self.inventory)
  
  def get_itemcount(self, item_index) -> int:
    return self.inventory[item_index]
  
  def has_item(self, item_index) -> bool:
    return (self.get_itemcount(item_index) > 0)
  

  def get_env(self) -> object:
    return self.env
  
  def get_other_guy(self) -> object:
    return self.other_guy
  
  def get_shotgun(self) -> object:
    return self.env.Shotgun
  

  def get_cuffed_status(self) -> bool:
    return self.cuffed
  


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
  

  def set_env(self, env) -> None:
    self.env = env
    return


  def clear_inventory(self) -> None:
    self.inventory = [0]*len(get_list_item_id)
    return

  def set_item_qty(self, item, qty) -> None:
    if clip(0, item, len(self.inventory)-1) == item:
      self.inventory[item] = clip(0, qty, len(get_list_item_id))
    else:
      # TODO: something. idk.
      pass
    return

  def add_item(self, item) -> None:
    self.set_item_qty(item, self.inventory[item]+1)
    return
  
  def rmv_item(self, item) -> None:
    self.set_item_qty(item, self.inventory[item]-1)
    return
  
  
  def the_other_guy(self):
    if self == self.env.Dealer:
      return self.env.Player
    else:
      return self.env.Dealer



  # Actions
  def shoot_shotgun(self, tgt):
    self.env.Shotgun.fire_shotgun(tgt)
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
    if self.cuffed == True:
      self.cuffed = False
      return

    choice = -5

    while(choice not in {-1, -2}):
      choice = self.make_choice()
      
      if choice in {-1, -2}:
        if choice == -1:
          tgt = self
        if choice == -2:
          tgt = self.the_other_guy()
        self.env.Shotgun.fire_shotgun(tgt)
      else:
        if self.inventory[choice] >= 0:
          get_list_item_id()[choice].use(self, self.env)
          self.inventory[choice] += -1



      