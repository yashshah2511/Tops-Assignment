# Agent State
agent_state = {
    "location": "Restaurant",
    "reward": 0,
    "step_count": 0
}

# Reward Table
reward_table = {
    "accept_order": 2,
    "navigate": 1,
    "deliver_order": 10,
    "wait": -2
}

# Episode
actions = [
    "accept_order",
    "navigate",
    "deliver_order",
    "wait",
    "deliver_order"
]

print("Food Delivery RL Episode")
print("-" * 40)

for action in actions:

    reward = reward_table[action]

    agent_state["reward"] += reward
    agent_state["step_count"] += 1

    if action == "navigate":
        agent_state["location"] = "Customer Location"

    elif action == "wait":
        agent_state["location"] = "Waiting Area"

    print(f"Action : {action}")
    print(f"Reward : {reward}")
    print(f"Running Reward : {agent_state['reward']}")
    print(f"Location : {agent_state['location']}")
    print("-" * 40)

print("Episode Summary")
print(f"Total Reward : {agent_state['reward']}")
print(f"Total Steps : {agent_state['step_count']}")