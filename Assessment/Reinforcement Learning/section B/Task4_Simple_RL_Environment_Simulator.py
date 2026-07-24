class DeliveryEnvironment:

    def __init__(self):

        self.current_state = {
            "location": "Restaurant",
            "pending_orders": 3
        }

        self.total_reward = 0

        self.step_count = 0

    def step(self, action):

        self.step_count += 1

        if action == "deliver_order":

            if self.current_state["pending_orders"] > 0:

                self.current_state["pending_orders"] -= 1

                reward = 10

            else:

                reward = 0

        elif action == "wait":

            reward = -2

        elif action == "navigate_to_zone":

            self.current_state["location"] = "High Demand Zone"

            reward = 2

        else:

            reward = 0

        self.total_reward += reward

        print(f"\nStep {self.step_count}")
        print("-" * 35)
        print(f"Action         : {action}")
        print(f"Reward         : {reward}")
        print(f"Current State  : {self.current_state}")
        print(f"Total Reward   : {self.total_reward}")

        return reward


environment = DeliveryEnvironment()

actions = [
    "navigate_to_zone",
    "deliver_order",
    "deliver_order",
    "wait",
    "deliver_order"
]

for action in actions:

    environment.step(action)

print("\nEpisode Completed")
print("=" * 35)
print(f"Final Total Reward : {environment.total_reward}")
print(f"Total Steps        : {environment.step_count}")

