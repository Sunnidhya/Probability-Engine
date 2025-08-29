from bernoulli_process import BernoulliProcess


# -- Simulation Setup ---

# probability of succes (Heads)
p_heads = 0.6

# Numbe rof coin flips
num_trials = 20

# Create an instance of the process

coin_toss_process = BernoulliProcess(p = p_heads)

# --- Run the Simulation --- 
print(f"Simulating a biased coin toss ({num_trials} times) with P(Heads) = {p_heads}...\n")
outcomes = coin_toss_process.run(n = num_trials)

# --- calculate and display statistics --- 
total_heads = coin_toss_process.num_successes()
first_head_trial = coin_toss_process.trials_for_first_success()

print(f"\n--- Results ---")
print(f"Total number of Heads (Successes) : {total_heads} out of {num_trials}")

if first_head_trial is not None:
    print(f"The first Head occurred on trial number: {first_head_trial}")
else:
    print("No Heads occurred in this run.")
