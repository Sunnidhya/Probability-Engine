from bernoulli_process import BernoulliProcess

true_p = 0.6
process = BernoulliProcess(p = true_p)

# A list of tiral numbers, increasing exponentially

trial_counts = [10,100,1000,10000]

print(f"---- Demonstrating Asymptotic Tightness with True p = {true_p} ---\n")
print(f"{'Trials (n)':>12}  {'Successes (k)':>14} | {'Observed p (k/n)':>18} | {'KL Diveregence':>15}")
print("-"*70)

for n in trial_counts:
    process.run(n)

    k = process.get_partial_sum()
    observed_p = k/n
    divergence = process.kl_divergence()

    print(f"{n:>12,} | {k:>14,} | {observed_p:>18.6f} | {divergence:>15.10f}")


