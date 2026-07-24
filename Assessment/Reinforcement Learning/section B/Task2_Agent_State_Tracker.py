# Initial Agent State
agent_state = {
    "location": "Restaurant",
    "orders_delivered": 0,
    "total_reward": 0.0,
    "is_available": True
}


def update_state(state, new_location, reward_earned):

    state["location"] = new_location

    state["orders_delivered"] += 1

    state["total_reward"] += reward_earned

    print("\nCurrent Agent State")
    print("-" * 30)
    print(f"Location          : {state['location']}")
    print(f"Orders Delivered  : {state['orders_delivered']}")
    print(f"Total Reward      : {state['total_reward']}")
    print(f"Is Available      : {state['is_available']}")


# Simulate State Transitions
update_state(agent_state, "Customer A", 12.5)

update_state(agent_state, "Restaurant", 8.0)

update_state(agent_state, "Customer B", 15.0)

update_state(agent_state, "Charging Station", -2.0)