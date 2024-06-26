from abc import ABC, abstractmethod
from random import randint
from copy import deepcopy

#Typing imports
from buckshot_actor import BuckShot_Actor
from buckshot_env import BuckShot_Environment



class BuckShot_Item(ABC):
  @abstractmethod
  def __init__(self) -> None:
    self.id = -1

  def __eq__(self, other) -> bool:
    return type(self) == type(other)
  
  
  def get_id(self):
    return self.id
  
  # @log_action
  def use(self, actor: BuckShot_Actor, env: BuckShot_Environment):
    actor.remove_item(self.get_id)

  # @log_action
  def check_usable(self, actor: BuckShot_Actor, env: BuckShot_Environment):
    return True
  
  def check_valid(self, actor: BuckShot_Actor, env: BuckShot_Environment):
    return True



# Probably unnecessary, but I think having items inherit from
# 'category' subclasses might allow the AI to better respond to
# new/unpredictable objects.
# e.g. if we had a 'Comically Big Cigar' item that heals 2 instead of 1
# the AI would know to treat them both as healing items, and not just
# be completely clueless about how to use it.
class Healing_Item(BuckShot_Item):
  pass

class Info_Item(BuckShot_Item):
  pass

class Damage_Item(BuckShot_Item):
  pass

class Debuff_Item(BuckShot_Item):
  pass


# Actual Item Classes Below
class Cigarrette(Healing_Item):
  def __init__(self):
    self.id = 0
  
  def use(self, actor, env):
    super().use(self, actor, env)
    actor.heal_damage(1)
  
  def check_usable(self, actor, env):
    if (actor.get_cur_health() < actor.get_max_health()): return True
    else: return False

  def check_valid(self, actor, env):
    if actor.count_item(self.id) >= 2: return False
    else: return True


class Handcuffs(Debuff_Item):
  def __init__(self):
    self.id = 1

  def use(self, actor, env):
    super().use(self, actor, env)
    Handcuffs.cuff(actor.other_guy)
    return
  
  def check_usable(self, actor, env):
    return not actor.get_other_guy.get_cuffed_status
    
  def check_valid(self, actor, env):
    return super().check_valid(self, actor, env)

  def cuff(tgt: BuckShot_Actor):
    tgt.set_cuffed()
    return


class Handsaw(Damage_Item):
  def __init__(self):
    self.id = 2

  def use(self, actor, env):
    super().use(self, actor, env)
    env.Shotgun.dmg = 2
    return
  
  def check_usable(self, actor, env):
    if env.Shotgun.dmg == 2: return False
    return True

  def check_valid(self, actor, env):
    return super().check_valid(self, actor, env)


class Spyglass(Info_Item):
  def __init__(self):
    self.id = 3

  def use(self, actor, env):
    super().use(self, actor, env)
    actor.probability = env.Shotgun.current_shell()
    actor.start_knowing()
    return
  
  def check_usable(self, actor, env):
    return not actor.does_he_know()
  
  def check_valid(self, actor, env):
    return super().check_valid(self, actor, env)


class Beer(Info_Item):
  def __init__(self):
    self.id = 4

  def use(self, actor, env):
    super().use(self, actor, env)
    env.Shotgun.eject_shell()
    actor.stop_knowing()
    return
  
  def check_usable(self, actor, env):
    return super().check_usable(self, actor, env)
  
  def check_valid(self, actor, env):
    return super().check_valid(self, actor, env)



# THIS is where all the Item IDs are stored.
# To add a new item to the game, just make the class
# and add the object to this list.
# ...It would probably be smart to move this to another file later.
item_id = list(
  Cigarrette(), #0 
  Handcuffs(), #1
  Handsaw(), #2
  Spyglass(), #3
  Beer(), #4
)


@classmethod
def item_id() -> list:
  return item_id

@classmethod
def item_id_size():
  return len(item_id)