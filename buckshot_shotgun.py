from random import randint

class BuckShot_Shotgun:
  def __init__(self):
    self.shell_arr = list()
    self.dmg = 1

  def get_damage(self) -> int:
    return self.dmg


  def get_shell_array(self) -> list:
    return self.shell_arr
  
  def get_shell_count(self) -> int:
    return len(self.get_shell_array())
  

  def add_shell(self, shell) -> None:
    self.get_shell_array().append(shell)
  
  def eject_shell(self) -> None:
    self.get_shell_array().pop(0)
  

  def count_shells(self, x) -> int:
    return self.get_shell_array().count(x)

  def current_bullet(self) -> int:
    return self.get_shell_array()[0]

  def fire_shotgun(self, tgt) -> None:
    if (self.current_bullet() == 1):
      tgt.take_damage(self.get_damage())
    self.eject_shell()


  def calc_probability(self):
    if self.count_shells(1) == 0:
      return 0
    else:
      prob = float(
        (self.count_shells(1)) / (self.get_shell_count())
      )
      return prob*100
    
  # I know for a fact this isn't how Buckshot Roulette
  # generates shell arrays, but it will do for now.
  def gen_shell_array(self, size):
    for L in range(size):
      self.add_shell(randint(0, 1))
