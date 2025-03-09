import numpy as np
from pypokerengine.players import BasePokerPlayer
from stable_baselines3 import DQN

class RLPlayer(BasePokerPlayer):
    def __init__(self, model):
        self.model = model

    def declare_action(self, valid_actions, hole_card, round_state):
        obs = np.random.rand(10)  # Get the current game state
        action, _states = self.model.predict(obs)
        
        if action == 0:
            return "fold", 0
        elif action == 1:
            return "call", valid_actions[1]["amount"]
        else:
            return "raise", valid_actions[2]["amount"]["max"]

# Load trained model
trained_model = DQN.load("poker_dqn")
rl_player = RLPlayer(trained_model)
