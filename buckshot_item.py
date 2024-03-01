from abc import ABC, abstractmethod

class buckshot_item(ABC):

  @abstractmethod
  def __init__(self, id) -> None:
    self.id = id
    pass

  @abstractmethod
  def use():
    pass
  
  def get_id(self):
    return self.id


# Probably unnecessary, but I think having items inherit from
# 'category' subclasses might allow the AI to better respond to
# new/unpredictable objects.
# e.g. if we had a 'Comically Big Cigar' item that heals 2 instead of 1
# the AI would know to treat them both as healing items, and not just
# be completely clueless about how to use it.
  

class healing_item(buckshot_item):
  pass

class info_item(buckshot_item):
  pass

class damage_item(buckshot_item):
  pass

class debuff_item(buckshot_item):
  pass