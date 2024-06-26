from abc import ABC, abstractmethod
from copy import deepcopy
from numpy import clip
from buckshot_inventory import BuckShot_Inventory
from buckshot_item import item_id, BuckShot_Item

# Typing Imports
from buckshot_shotgun import BuckShot_Shotgun
from buckshot_actor import BuckShot_Actor # ??? ??? ???
from buckshot_env import BuckShot_Environment



class BuckShot_Actor():
  def __init__(self, max_health=2) -> None:
    # Essential Stats
    self.max_health = max_health
    self.cur_health = max_health
    self.threshold = 0

    self.max_inventory = 8
    self.inventory = BuckShot_Inventory(self, self.max_inventory)
    
    # Senses
    self.env = object
    self.other_guy = object
    self.probability = 0.5
    self.cuffed = False
    self.knower = False
  


  # Getters
  def get_max_health(self) -> int:
    return self.max_health
  
  def get_cur_health(self) -> int:
    return self.cur_health
  
  def get_cur_threshold(self) -> int:
    return self.threshold
  
  
  def is_full_health(self) -> bool:
    if (self.get_cur_health == self.get_max_health): return True
    else: return False
  
  def is_dead(self) -> bool:
    return (self.get_cur_health + self.get_cur_threshold) <= 0
  

  def get_hp_percent(self) -> int: #Is this necessary?
    per = (self.get_cur_health / self.get_max_health)
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
    if (self.get_shotgun.get_shell_count() == 1): return True
    else: return self.knower

  # @log_action
  def get_cuffed_status(self) -> bool:
    return self.cuffed
  

  def the_other_guy(self, env: BuckShot_Environment) -> BuckShot_Actor:
    if (self == env.get_dealer): return env.get_player
    else: return env.get_dealer


  
  def actor_state(self):
    # HP Max
    # HP
    # inventory state
    # The Knower
    pass
  def enemy_state(self):
    return self.actor_state(self.the_other_guy)
    pass
  def shotgun_state(self):
    # Live Rounds
    # Blank rounds
    pass
  


  # Setters
  def set_max_health(self, value) -> None:
    self.max_health = value
  
  def set_cur_health(self, value) -> None:
    self.cur_health = value

  def set_threshold(self, value) -> None:
    self.threshold = value


  # Damages 'Defibrilators' first and 'Transfusions' second.
  # Just like in the game.
  # @log_action
  def take_damage(self, dmg) -> None:
    self.set_cur_health(self.get_cur_health - dmg)
    if(self.get_cur_health < 0):
      self.set_threshold(self.get_cur_threshold - self.get_cur_health)
      self.set_cur_health(0)
  
  # @log_action
  def heal_damage(self, heal) -> None:
    self.set_cur_health(self.cur_health + heal)
  
  # @log_action
  def set_cuffed(self) -> None:
    self.cuffed = True
  
  # @log_action
  def set_uncuffed(self) -> None:
    self.cuffed = False
  
  # @log_action
  def stop_knowing(self):
    self.knower = False

  # @log_action
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
  def shoot_shotgun(self, tgt) -> int:
    self.stop_knowing
    return self.get_shotgun.fire_shotgun(tgt)
  
  # @log_action
  def shoot_enemy(self) -> int:
    return self.shoot_shotgun(self.other_guy)
  
  # @log_action
  def shoot_self(self) -> int:
    return self.shoot_shotgun(self)

  # @log_action
  def use_item(self, item) -> None: # TODO: This is kind of ugly. Have a look.
    item_id[item].use(self, self.env)



  # Decision Logic
  @abstractmethod
  # @log_action
  def make_choice(self, env) -> int:
    # Left to the Player and Dealer classes
    pass


  # Handles actor input, Dealer or Player.
  # @log_action
  def take_turn(self) -> None:
    if self.get_cuffed_status:
      # If cuffed, skip turn and uncuff.
      self.set_uncuffed
      return

    choice = -5

    while(choice not in {-1, -2} and (not self.get_shotgun.shotty_empty())):
      # Gets input from Player/Dealer
      choice = self.make_choice()

      # Makes sure it's correct, just in case
      if(choice >= len(item_id)) or (choice < -2): continue
      
      if choice in {-1, -2}: # If it's negative, that means 'Shoot'
        if (choice == -1): self.shoot_enemy
        if (choice == -2) and (self.shoot_self == 0): continue
        # Shooting yourself with a blank lets you go again.
        return
      else: # 0 and up means 'Item'
        if self.inventory.has_item(choice) and item_id[choice].check_usable():
          self.use_item(choice)
        # Turn doesn't end on item use, unless shotgun empties.
        continue