import os

# Path to the state-wise transaction data
path = "Pulse/data/aggregated/transaction/country/india/state/"

# List all states in the folder
Agg_state_list = os.listdir(path)

# Print the list of states (folders)
print("States found:", Agg_state_list)
