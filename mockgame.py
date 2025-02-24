from pypokerengine.api.game import setup_config, start_poker
from fishplayer import FishPlayer
def main():
  config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
  config.register_player(name="p1", algorithm=FishPlayer())
  config.register_player(name="p2", algorithm=FishPlayer())
  config.register_player(name="p3", algorithm=FishPlayer())
  game_result = start_poker(config, verbose=1)

if __name__ == '__main__':
    main()