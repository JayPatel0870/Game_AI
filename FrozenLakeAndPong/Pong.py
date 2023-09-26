import gym
import numpy as np


def create_q_table(env):
    return np.zeros((100800, env.action_space.n))


def choose_action(q_table, state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(q_table[state, :])


def update_q_table(q_table, state, action, next_state, reward, learning_rate, discount_factor):
    q_table[state, action] = (1 - learning_rate) * q_table[state, action] + learning_rate * (
                reward + discount_factor * np.max(q_table[next_state, :]))


learning_rate = 0.1
discount_factor = 0.99
epsilon = 0.1
num_episodes = 1000

env = gym.make("ALE/Pong-v5", render_mode="human")
q_table = create_q_table(env)

for episode in range(num_episodes):
    state, info = env.reset(seed=42)
    terminated = False

    while not terminated:
        action = choose_action(q_table, state, epsilon)
        next_state, reward, terminated, truncated, info = env.step(action)


        update_q_table(q_table, state, action, next_state, reward, learning_rate, discount_factor)

        state = next_state

        if terminated or truncated:
            state, info = env.reset(seed=42)

env.close()
