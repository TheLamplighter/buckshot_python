class Logger():
    def __init__(self) -> None:
      pass
    
    actor_event_list = [
      #Actor Events
      "[Actor] uses [Item]", "[Actor] gains [Item]", "[Actor] fires at [Actor]", 
      "[Actor] gains health", "[Actor] loses health", "[Actor] dies", 
      "[Actor] is handcuffed", "[Actor] wins the stage", "[Actor] ends their turn"
      ]

    stage_event_list = [
      #Stage Events
      "[Stage 'Number'] starts", "Health is set to [Number]",
    ]
       
    shotgun_event_list = [
      #Shotgun Events
      "[Shotgun] runs out of ammo", "[Shotgun] is reloaded", "[Shotgun] ejects a round", 
      "[Shotgun] gains damage", "[Shotgun] goes back to normal", "[Shotgun]",
      ]
    

    
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
          result = function(*args, **kwargs)
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
          #Case - env.check_winner
          pass

        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - env.set_actor_defaults
          pass


        elif func_type == None:
          result = func(*args, **kwargs)
          #Case - actor.make_choice
          pass

        elif func_type == None:
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
          print(actor + " gains the item " + tgt)
          #Case - inventory.place_item
          pass

        return result

      return wrap
    pass