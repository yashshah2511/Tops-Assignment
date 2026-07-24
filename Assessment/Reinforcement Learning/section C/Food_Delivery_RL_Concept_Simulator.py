"""
=====================================================
Food Delivery RL Concept Simulator
=====================================================

Objective:
Simulate the Reinforcement Learning (RL) loop for a
food delivery dispatch system.

Features:
1. Start New Delivery Episode
2. View Agent Stats
3. Exit

Technology:
- Python 3

=====================================================
"""

# ==========================================
# Agent State
# ==========================================

agent_state = {
    "location": "Restaurant",
    "orders_delivered": 0,
    "total_reward": 0
}

# ==========================================
# Overall Statistics
# ==========================================

total_episodes = 0

overall_reward = 0

# ==========================================
# Reward Table
# ==========================================

reward_table = {
    "accept_order": 2,
    "navigate_to_customer": 1,
    "deliver_order": 10,
    "wait": -2
}


def show_menu():

    print("\n" + "=" * 50)
    print(" Food Delivery RL Concept Simulator")
    print("=" * 50)

    print("1. Start New Delivery Episode")
    print("2. View Agent Stats")
    print("3. Exit")


# ==========================================
# View Agent Statistics
# ==========================================

def view_agent_stats():

    print("\n" + "=" * 50)
    print(" Agent Statistics")
    print("=" * 50)

    print(f"Current Location     : {agent_state['location']}")
    print(f"Orders Delivered     : {agent_state['orders_delivered']}")
    print(f"Total Reward         : {agent_state['total_reward']}")

    print(f"Total Episodes       : {total_episodes}")
    print(f"Overall Reward       : {overall_reward}")

    if total_episodes > 0:
        average_reward = overall_reward / total_episodes
    else:
        average_reward = 0

    print(f"Average Reward       : {average_reward:.2f}")
    

# ==========================================
# Start New Delivery Episode
# ==========================================

def start_delivery_episode():
    global total_episodes
    global overall_reward

    print("\n" + "=" * 50)
    print(" Starting New Delivery Episode")
    print("=" * 50)

    actions = [
        "accept_order",
        "navigate_to_customer",
        "deliver_order",
        "wait",
        "deliver_order"
    ]

    episode_reward = 0
    episode_log = []

    print("\nEpisode Actions")
    print("-" * 50)

    for step, action in enumerate(actions, start=1):

        reward = reward_table[action]

        episode_reward += reward
        
        episode_log.append({
    "step": step,
    "action": action,
    "reward": reward
})

        # Update Agent State
        if action == "accept_order":

            agent_state["location"] = "Restaurant"

        elif action == "navigate_to_customer":

            agent_state["location"] = "Customer Location"

        elif action == "deliver_order":

            agent_state["orders_delivered"] += 1

        elif action == "wait":

            agent_state["location"] = "Waiting Area"

        # Update Total Reward
        agent_state["total_reward"] += reward

        print(f"\nStep {step}")
        print("-" * 50)
        print(f"Action              : {action}")
        print(f"Reward              : {reward}")
        print(f"Episode Reward      : {episode_reward}")

        print("\nUpdated Agent State")
        print(f"Location            : {agent_state['location']}")
        print(f"Orders Delivered    : {agent_state['orders_delivered']}")
        print(f"Total Reward        : {agent_state['total_reward']}")
        print("-" * 50)

    print("\n" + "=" * 50)
    print("Episode Summary")
    print("=" * 50)

    for log in episode_log:

        print(
            f"Step {log['step']} | "
            f"Action: {log['action']} | "
            f"Reward: {log['reward']}"
        )

    print("-" * 50)
    print(f"Total Episode Reward : {episode_reward}")
    # ==========================================
# Update Overall Statistics
# ==========================================

    total_episodes += 1

    overall_reward += episode_reward

while True:

    show_menu()

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":

        start_delivery_episode()

    elif choice == "2":

        view_agent_stats()

    elif choice == "3":

        print("\nThank you for using the Food Delivery RL Concept Simulator.")
        print("Goodbye!")

        break

    else:

        print("\nInvalid choice! Please enter a number between 1 and 3.")