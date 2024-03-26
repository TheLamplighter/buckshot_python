from abc import ABC, abstractmethod
from random import randint
from copy import deepcopy

class BuckShot_Item(ABC):
  @abstractmethod
  def __init__(self) -> None:
    self.id = -1

  @abstractmethod
  def use(actor, env):
    pass
  
  def get_id(self):
    return self.id



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
  
  def use(actor, env):
    actor.heal_damage(1)

class Handcuffs(Debuff_Item):
  def __init__(self):
    self.id = 1

  def cuff(tgt):
    pass

  def use(actor, env):
    if (actor == env.Dealer):
      Handcuffs.cuff(env.Player)
    else:
      Handcuffs.cuff(env.Dealer)

class Handsaw(Damage_Item):
  def __init__(self):
    self.id = 2

  def use(actor, env):
    env.Shotgun.dmg = 2
  pass

class Spyglass(Info_Item):
  def __init__(self):
    self.id = 3

  def use(actor, env):
    actor.probability = env.Shotgun.current_bullet()
  pass

class Beer(Info_Item):
  def __init__(self):
    self.id = 4

  def use(actor, env):
    env.Shotgun.eject_shell()
  pass


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
def get_list_item_id():
  return item_id

@classmethod
def get_item_id_size():
  return len(item_id)

@classmethod
def count_items(itemset) -> list:
  counter = list()

  for L in len(item_id):
    counter.append(itemset.count(item_id[L]))

  return counter


def item_by_id(id) -> object:
  return deepcopy(item_id[id])

def gen_item() -> object:
  rng = randint(0, len(item_id)-1)
  return item_by_id(rng)

@classmethod
def gen_itemset(number) -> list:
  itemset = list()

  for L in range(number):
    itemset.append(gen_item())

  return itemset

@classmethod
def gen_alt_itemset(actor, number):
  for L in range(number):

    x = randint(0, get_item_id_size-1)

    # TODO: Generalize this to all no-no items.
    while (x == 0) and (actor.get_itemcount(x) >= 2):
      x = randint(0, get_item_id_size-1)
    
    if (actor.get_inventory_size == actor.get_inventory_max):
      break
    actor.add_item(x)