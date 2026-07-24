def calculate_reward(delivery_time, is_on_time, customer_rating):

    reward = 0

    if is_on_time:
        reward += 10
    else:
        reward -= 5

    reward += customer_rating

    print(f"Delivery Time : {delivery_time} minutes")
    print(f"On Time       : {is_on_time}")
    print(f"Customer Rating : {customer_rating}")
    print(f"Final Reward : {reward}")
    print("-" * 40)
    
    
# Test Case 1
calculate_reward(25, True, 5)

# Test Case 2
calculate_reward(40, False, 2)

# Test Case 3
calculate_reward(30, True, 3)