from abc import ABC, abstractmethod
from buckshot_item import get_list_item_id

class BuckShot_Actor():
  def __init__(self, max_health=2) -> None:
    self.max_health = max_health
    self.cur_health = max_health
    #self.inventory = list()
    self.alt_inventory = [0]*len(get_list_item_id())
    
    self.probability = 0.5
    self.env = object
    self.cuffed = False

  def set_env(self, env) -> None:
    self.env = env
    
  def set_max_health(self, value) -> None:
    self.max_health = value
    return

  def take_damage(self, dmg) -> None:
    if (self.cur_health >= dmg):
      self.cur_health = self.cur_health - dmg
    else:
      self.cur_health = 0
    return
  
  def heal_damage(self, heal) -> None:
    self.cur_health = self.cur_health + heal

    if (self.cur_health > self.max_health):
      self.cur_health = self.max_health
    
    return


  '''def get_inventory(self) -> list:
    return self.inventory'''
  
  def get_alt_inventory(self) -> list:
    return self.alt_inventory
  
  def use_item(self, item) -> None:
    item.use(self, self.env)

  '''def clear_inventory(self):
    self.inventory = list()
    return'''
  
  def clear_alt_inventory(self):
    self.alt_inventory = [0]*len(get_list_item_id())
  

  '''def add_item(self, new_item):
    if len(self.items) >= 8:
      return
    else:
      self.inventory.append(self.inventory, new_item)
      return'''

  def the_other_guy(self):
    if self == self.env.Dealer:
      return self.env.Player
    else:
      return self.env.Dealer

  
  '''def add_itemset(self, new_items):
    for i in new_items:
      if len(self.inventory) >= 8:
        break
      else:
        self.add_item(i)

  def update_senses(self, env):
    if self == env.Dealer:
      self.enemy_inventory = env.Player.inventory
    else:
      self.enemy_inventory = env.Dealer.inventory

    self.shell_array = env.Shotgun.get_shell_array()
    self.probability = env.Shotgun.calc_probability()'''

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
        if self.alt_inventory[choice] >= 0:
          get_list_item_id()[choice].use(self, self.env)
          self.alt_inventory[choice] += -1



      