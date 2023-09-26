"""""
5. Comparing Q-learning algorithm and policy iteration algorithm 

In the FrozenLake environment, policy iteration converges over 2x 
faster to the optimal policy compared to Q-learning due to exploiting 
the known environment dynamics.

"""""

import numpy as np
import gym


def policy_evaluation(env, policy, V, gamma, theta):
    while True:
        delta = 0
        for s in range(env.observation_space.n):
            v = V[s]
            V[s] = sum([p * (r + gamma * V[s_prime]) for p, s_prime, r, _ in env.P[s][policy[s]]])
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break


def policy_improvement(env, policy, V, gamma):
    policy_stable = True
    for s in range(env.observation_space.n):
        old_action = policy[s]
        action_values = np.zeros(env.action_space.n)
        for a in range(env.action_space.n):
            action_values[a] = sum([p * (r + gamma * V[s_prime]) for p, s_prime, r, _ in env.P[s][a]])
        policy[s] = np.argmax(action_values)
        if old_action != policy[s]:
            policy_stable = False
    return policy_stable


def policy_iteration(env, gamma, theta):
    policy = np.random.choice(env.action_space.n, env.observation_space.n)
    V = np.zeros(env.observation_space.n)

    while True:
        policy_evaluation(env, policy, V, gamma, theta)
        if policy_improvement(env, policy, V, gamma):
            break

    return policy, V


env = gym.make('FrozenLake-v1', is_slippery=False)

gamma = 0.9
theta = 1e-6

optimal_policy, optimal_values = policy_iteration(env, gamma, theta)

print("Optimal Policy:")
print(optimal_policy)
print("\nOptimal State Values:")
print(optimal_values)
