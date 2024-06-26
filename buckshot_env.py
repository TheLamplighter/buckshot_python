from random import randint
from buckshot_actor import BuckShot_Actor
from buckshot_shotgun import BuckShot_Shotgun



class BuckShot_Environment:
  def __init__(self, stage=1, round=0, turn=0) -> None:
    self.stage_count = stage
    self.round_count = round
    self.turn_count = turn

    self.Shotgun = BuckShot_Shotgun()
    self.Dealer = BuckShot_Actor()
    self.Player = BuckShot_Actor()

  # Getters
  def get_player(self) -> BuckShot_Actor:
    return self.Player

  def get_dealer(self) -> BuckShot_Actor:
    return self.Dealer

  def get_shotgun(self) -> BuckShot_Shotgun:
    return self.Shotgun
  
  
  def has_winner(self) -> bool:
    return self.get_player.is_dead or self.get_dealer.is_dead
  
  # @log_action
  def check_winner(self) -> int:
    if (self.get_dealer.is_dead): return 1
    elif (self.get_player.is_dead): return 0
    else: return -1 # Edge case. Shouldn't happen.


  # Setters
  # @log_action
  def set_actor_defaults(self, max_hp, threshold) -> None:
    self.get_dealer.set_max_hp(max_hp),       self.get_player.set_max_hp(max_hp)
    self.get_dealer.set_threshold(threshold), self.get_player.set_threshold(threshold) 
    self.get_dealer.to_max_hp(),              self.get_player.to_max_hp()
    self.get_dealer.clear_inventory(),        self.get_player.clear_inventory()
    self.get_shotgun.clear_shell_array()


  # Probably Unnecessary, but I don't
  # Know how Python works.
  def update_env(self) -> None:
    self.Player.set_env(self)
    self.Dealer.set_env(self)


  def stage_up(self) -> None:
    self.stage_count += 1

  def round_up(self) -> None:
    self.round_count += 1

  def turn_up(self) -> None:
    self.turn_count += 1



  # Game Logic Methods
  def turn(self, actor: BuckShot_Actor) -> None:
    actor.take_turn()
    self.Shotgun.dmg = 1


  # Looped by .stage(). New rounds until player wins or dies.
  # @log_action
  def round(self) -> None:
    self.round_up

    # New items for everyone, new shotgun array.
    self.Player.inventory.get_item_load(4)
    self.Dealer.inventory.get_item_load(4)
    self.Shotgun.gen_shell_array()

    # Alternate turns until one dies or the shotgun runs out
    while(self.Shotgun.shotty_empty() == False) and (not self.has_winner):
      self.turn(self.get_player)
      if(self.has_winner or self.Shotgun.shotty_empty): break
      self.turn(self.get_dealer)
    return


  # @log_action
  def stage(self, max_hp=2, threshold=0) -> None:
    # Increment Stage Counter
    self.stage_up

    # Set everything to defaults
    self.set_actor_defaults(self, max_hp, threshold)

    # Play rounds until there's a winner
    while(not self.has_winner):
      self.round()


  # Play 'length' games. Returns True if player won, and False if player lost.
  # TODO: Maybe a way to track turns/rounds/stages per run?
  
  # @log_action
  def game(self, length) -> bool:
    for L in range(length):
      if(L == length-1): thresh = 2
      else: thresh = 0
      
      self.stage(randint(2, 4), thresh)
      if(self.check_winner == 0): return False
    return True