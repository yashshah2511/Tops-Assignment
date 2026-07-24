# Possible Actions
actions = [
    "accept_order",
    "reject_order",
    "request_directions",
    "mark_delivered"
]

# Reward for Each Action
reward_table = {
    "accept_order": 2,
    "reject_order": -1,
    "request_directions": 0,
    "mark_delivered": 10
}

# One Episode
episode = [
    "accept_order",
    "request_directions",
    "mark_delivered",
    "accept_order",
    "reject_order",
    "mark_delivered"
]

total_reward = 0

print("Delivery RL Episode")
print("-" * 40)

for step, action in enumerate(episode, start=1):

    reward = reward_table[action]

    total_reward += reward

    print(f"Step {step}")
    print(f"Action            : {action}")
    print(f"Reward            : {reward}")
    print(f"Cumulative Reward : {total_reward}")
    print("-" * 40)

print(f"Final Episode Reward: {total_reward}")