from buckshot_item import item_id_size


class Logger():
    def __init__(self) -> None:
      self.item_id_size = item_id_size()
      pass
    
    def log_action(self, func, cur_actor, extra):
      
      def wrap(*args, **kwargs):

        #See what function is being run
        func_type = func.__name__
        actor = "" # TODO: Figure out how to cleanly get actor
        tgt = ""

        #Handle Appropriately
        #TODO: Proper order!
        if func_type == None:
          print()
          print("A new stage starts.")
          result = func(*args, **kwargs)
          #Case - env.stage
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          if(result): print(actor + " was handcuffed! - [Turn Skipped]")

          #Case - actor.get_cuffed_status
          pass

        elif func_type == None:
          print("The shotgun has been reloaded")
          print("New items given out")
          result = func(*args, **kwargs)
          #Case - env.round
          pass

        elif func_type == None:
          print("[Game started]")
          result = func(*args, **kwargs)
          #Case - env.game
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          if result == 1:
            print("The Dealer is Dead.")
          elif result == 0:
            print("The Player is Dead. - [Game Over*]")
          elif result == -1:
            print("Error: Invalid Winner")
          #Case - env.check_winner
          pass

        elif func_type == None:
          print("The pieces are in play.")
          result = func(*args, **kwargs)
          #Case - env.set_actor_defaults
          pass


        elif func_type == None:
          result = func(*args, **kwargs)

          if(result > -1) and (result < item_id_size):
            # Item Logic
            pass
          elif(result < item_id_size):
            # Gun Logic
            pass
          else:
            # Bad Logic
            pass

          #Case - actor.make_choice
          pass

        elif func_type == None:
          print(actor + " shoots " + tgt)
          result = func(*args, **kwargs)
          #Case - actor.shoot_shotgun
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - actor.take_damage
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - actor.heal_damage
          pass


        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - shotgun.eject_shell
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - shotgun.gen_shell_array
          pass


        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - item.use
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - item.check_usable
          pass


        elif func_type == None:
          print(actor + " gains [" + tgt + "]")
          result = func(*args, **kwargs)
          #Case - inventory.place_item
          pass

        return result

      return wrap
    pass