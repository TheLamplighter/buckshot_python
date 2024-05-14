from buckshot_actor import BuckShot_Actor

class Player(BuckShot_Actor):
  
  # Might break something.
  def does_he_know(self, env) -> bool:
    return False
  
  def get_senses(self, env):
    pass
  
  # Most important method
  # @log_action
  def make_choice(self, env):
    pass