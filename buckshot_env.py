from buckshot_actor import BuckShot_Actor
from buckshot_shotgun import BuckShot_Shotgun
from buckshot_item import gen_alt_itemset

class Environment:
  def __init__(self, stage=1, round=0, turn=0) -> None:
    self.stage = stage
    self.round = round
    self.turn = turn

  Shotgun = BuckShot_Shotgun()
  Dealer = BuckShot_Actor()
  Player = BuckShot_Actor()

  def update_env(env) -> None:
    env.Player.set_env(env)
    env.Dealer.set_env(env)

  def stage_up(self):
    self.stage += 1



env = Environment()



def shellcount_by_round(env) -> int:
  pass

def shotty_empty(env) -> bool:
  return env.Shotgun.get_shell_count() <= 0


def turn(actor) -> None:
  actor.take_turn()
  actor.env.Shotgun.dmg = 1


def round(env) -> None:
  shellcount = shellcount_by_round(env)
  gen_alt_itemset(env.Player, 4)
  gen_alt_itemset(env.Dealer, 4)
  env.Shotgun.gen_shell_array(shellcount)

  while(shotty_empty(env) == False):
    turn(env.Player)

    if (shotty_empty(env)):
      break

    turn(env.Dealer)
  pass


def stage(env, max_hp=2, threshold=0) -> None:
  pass


# Running Logic starts HERE 

