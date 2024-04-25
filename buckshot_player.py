from buckshot_actor import BuckShot_Actor

class Player(BuckShot_Actor):
  
  # Might break something.
  def does_he_know(self, env) -> bool:
    return False
  
  # Most important method
  def make_choice(self, env):
    pass