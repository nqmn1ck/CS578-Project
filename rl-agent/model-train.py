from stable_baselines3 import DQN
from environ import PokerEnv

# Initialize environment
env = PokerEnv()

# Train using Deep Q-Learning
model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)

# Save model
model.save("poker_dqn")
