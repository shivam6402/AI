def greedy_activity_selector(start_times, finish_times):
    n = len(start_times)
    selected_activities = []

    # Sort activities based on their finish times
    activities = sorted(zip(start_times, finish_times), key=lambda x: x[1])

    selected_activities.append(activities[0])

    # Select activities greedily
    j = 0
    for i in range(1, n):
        if activities[i][0] >= activities[j][1]:
            selected_activities.append(activities[i])
            j = i

    return selected_activities


# Get user input for the number of activities
num_activities = int(input("Enter the number of activities: "))

# Get user input for the start times of the activities
start_times = list(map(int, input("Enter the start times of the activities (space-separated): ").split()))

# Get user input for the finish times of the activities
finish_times = list(map(int, input("Enter the finish times of the activities (space-separated): ").split()))

# Call the greedy_activity_selector function to find the maximum number of non-overlapping activities
selected_activities = greedy_activity_selector(start_times, finish_times)

# Print the selected activities
print("Selected Activities:")
for activity in selected_activities:
    start_time, finish_time = activity
    print(f"Start Time: {start_time}, Finish Time: {finish_time}")
