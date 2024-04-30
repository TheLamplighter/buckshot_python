from buckshot_actor import BuckShot_Actor
from buckshot_shotgun import BuckShot_Shotgun
from buckshot_item import gen_alt_itemset
from random import randint

class BuckShot_Environment:
  def __init__(self, stage=1, round=0, turn=0) -> None:
    self.stage = stage
    self.round = round
    self.turn = turn

  Shotgun = BuckShot_Shotgun()
  Dealer = BuckShot_Actor()
  Player = BuckShot_Actor()

  def get_player(self) -> BuckShot_Actor:
    return self.Player

  def get_dealer(self) -> BuckShot_Actor:
    return self.Dealer

  def get_shotgun(self) -> BuckShot_Shotgun:
    return self.Shotgun

  # Probably Unnecessary, but I don't
  # Know how Python works.
  def update_env(self) -> None:
    self.Player.set_env(self)
    self.Dealer.set_env(self)

  def stage_up(self) -> None:
    self.stage += 1


  #Game Logic Methods
  def turn(self, actor: BuckShot_Actor) -> None:
    actor.take_turn()
    self.Shotgun.dmg = 1


  def round(self) -> None:
    self.Player.inventory.get_item_load()
    self.Dealer.inventory.get_item_load()
    self.Shotgun.gen_shell_array()

    while(self.Shotgun.shotty_empty() == False):
      self.turn(self.Player)

      if (self.Shotgun.shotty_empty()):
        break

      self.turn(self.Dealer)
    pass


  def stage(self, max_hp=2, threshold=0) -> None:
    pass


# Running Logic starts HERE 

