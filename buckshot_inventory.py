from random import randint
from buckshot_item import item_id, item_id_size
from copy import deepcopy



class BuckShot_Inventory():
  def __init__(self, actor, max_inventory=8) -> None:
    self.actor = actor
    self.max_inventory = max_inventory

    self.inventory = [None]*max_inventory
    self.itemcount = [0]*item_id_size


  #Getters
  def itemslot(self, slot) -> object:
    return self.inventory[slot]


  def max_size(self) -> int:
    return self.max_inventory

  def size(self) -> int:
    return sum(self.itemcount)
  
  
  def is_empty(self) -> bool:
    if (self.size > 0): return True
    return False
  
  def not_empty(self) -> bool:
    return not self.is_empty
  

  def count_item(self, item) -> int:
    return self.itemcount[item]
  
  def has_item(self, item_index) -> bool:
    return (self.count_item(item_index) > 0)
  

  def item_by_id(self, item) -> object:
    return deepcopy(item_id[item])
  

  def find(self, item) -> int:
    for L in range(len(self.inventory)):
      if self.inventory[L] == item: return L
    return -1
  


  #Setters
  def set_actor(self, actor) -> None:
    self.actor = actor


  def place_item(self, item, slot) -> None:
    self.inventory[slot] = self.item_by_id(item)


  def add(self, item) -> None:
    slot = self.find(None)
    if(self.size < self.max_size) and (slot >= 0):
      self.place_item(item, slot)
      self.itemcount[item] += 1

  def remove(self, item) -> None:
    if(self.not_empty) and (self.has_item(item)):
      slot = self.find(item_id[item])
      self.inventory[slot] = None
      self.itemcount[item] += -1

  def clear(self) -> None:
    self.inventory = [None]*self.max_inventory
    self.itemcount = [0]*item_id_size
    return
  


  #Itemset Logic --- Kill me.
  def get_item_load(self, number) -> None:
    for L in range(number):
      x = randint(0, item_id_size-1)

      while (not item_id[x].check_valid(self.actor)):
        x = randint(0, item_id_size-1)
      
      if (self.size == self.max_size): break
      self.add(x)