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
    


    def log_action(self, function, cur_actor, cur_event, extra):
      
      def wrap(*args, **kwargs):

        #See what function is being run
        func_type = function.__name__
        actor = "" # TODO: Figure out how to cleanly get actor

        #Handle Appropriately
        #TODO: Proper order!
        if func_type == None:
          #Case 1 - actor.take_turn (turn start)
          pass

        elif func_type == None:
          #Case - env.stage
          pass

        elif func_type == None:
          #Case - env.round
          pass

        elif func_type == None:
          #Case - env.game
          pass

        elif func_type == None:
          #Case - env.check_winner
          pass

        elif func_type == None:
          #Case - env.set_actor_defaults
          pass


        elif func_type == None:
          #Case - actor.make_choice
          pass

        elif func_type == None:
          #Case - actor.shoot_shotgun
          pass

        elif func_type == None:
          #Case - actor.take_damage
          pass

        elif func_type == None:
          #Case - actor.heal_damage
          pass


        elif func_type == None:
          #Case - shotgun.eject_shell
          pass


        elif func_type == None:
          #Case - item.use
          pass

        elif func_type == None:
          #Case - item.check_usable
          pass


        elif func_type == None:
          #Case - inventory.place_item
          pass





        result = function(*args, **kwargs)
        return result

      return wrap
    pass