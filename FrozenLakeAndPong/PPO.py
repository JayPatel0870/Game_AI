"""In the code I did not flattern any layer but I don't know how the code is flattening the linear Layer so the code gets stuck at the RuntimeError"""


import gym
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

lr = 0.001
num_steps = 2048
num_epochs = 10
gamma = 0.99
eps_clip = 0.1

env = gym.make('ALE/Pong-v5')
state_dim = 210
action_dim = env.action_space.n


class ActorCritic(nn.Module):

    def __init__(self, state_dim, action_dim):
        super(ActorCritic, self).__init__()

        self.actor = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )

        self.critic = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def act(self, state):
        # Convert state tuple to tensor
        state = state[0]
        state = torch.tensor(state, dtype=torch.float)

        action_probs = self.actor(state)
        dist = Categorical(action_probs)
        action = dist.sample()
        return action

    def evaluate(self, state, action):
        # Convert state tuple to tensor
        state = torch.tensor(state, dtype=torch.float)

        action_probs = self.actor(state)
        dist = Categorical(action_probs)
        action_logprobs = dist.log_prob(action)
        dist_entropy = dist.entropy()

        state_value = self.critic(state)

        return action_logprobs, state_value, dist_entropy


model = ActorCritic(state_dim, action_dim)
optimizer = optim.Adam(model.parameters(), lr=lr)


def ppo_update(ppo_epochs, mini_batch_size):
    states = []
    actions = []
    rewards = []
    old_logprobs = []

    for _ in range(num_steps):
        state = env.reset()
        done = False

        while not done:
            states.append(state)
            action = model.act(state)
            actions.append(action)
            old_logprobs.append(model.evaluate(state, action)[0])

            state, reward, done, _ = env.step(action)
            rewards.append(reward)

    states = torch.tensor(states, dtype=torch.float)
    actions = torch.tensor(actions)
    rewards = torch.tensor(rewards, dtype=torch.float)
    old_logprobs = torch.stack(old_logprobs).detach()

    for _ in range(ppo_epochs):
        for indx in torch.randperm(num_steps):
            state = states[indx]
            action = actions[indx]
            r = rewards[indx]

            logprobs, state_value, dist_entropy = model.evaluate(state, action)

            ratios = torch.exp(logprobs - old_logprobs[indx])
            surr1 = ratios * r
            surr2 = torch.clamp(ratios, 1 - eps_clip, 1 + eps_clip) * r

            loss = -torch.min(surr1, surr2) + 0.5 * state_value - 0.01 * dist_entropy

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


for i in range(num_epochs):
    ppo_update(4, 64)