import math
from itertools import chain, combinations
from probability_space import ProbabilitySpace
from sigma_algebra import SigmaAlgebra

# --- Part 1: Define the sample space and the collection of events (sigma algebra) --- 

# Define the sample space for the die roll

outcomes = {1,2,3,4,5,6}

# Heler function to generate the pweor set (all possible events)

def power_set(iterable):
    s = list(iterable)
    return set(frozenset(subset) for i in range(len(s) + 1) for subset in combinations(s,i))


# Generate the power set of outcomes to serve as our sigma-algebra
# This collection contains every possible subset, from the empty set to the full sample sapce.

all_possible_events = power_set(outcomes)
print(f"Generated a collection of {len(all_possible_events)} possible events (the power set).")


# --- Part 2: Validate the Sigma-Algebra Axioms ---

try: 
    # Check if our collection of events is a valid sigma-algebra
    event_space = SigmaAlgebra(sample_space = outcomes, events = all_possible_events)

    # --- Part 3: validate the probability axioms ---

    print("--- Checking probability Axioms ---")
    probabilities = {outcome: 1.6 for outcome in outcomes}

    # Create an instance of ProbabilitySpace
    die_roll = ProbabilitySpace(sample_space=outcomes, prob_distribution=probabilities)
    print("Probabilites space for a fair die created successfully.")

    # Define some events
    event_even = {2,4,6}
    event_odd = {1,3,5}
    event_less_than3 = {1,2}

    # Calculate probabilites
    print(f"P(Even) = {die_roll.P(event_even):.2f}")
    print(f"P(Odd) = {die_roll.P(event_odd):.2f}")
    print(f"P(<3) = {die_roll.P(event_less_than3):.2f}")

    #explicitly check the additivity axiom for proabbility
    are_disjoint = not bool(event_even.intersection(event_odd))
    print(f"\nAre 'even' and 'odd' events dijoin? {are_disjoint}")

    if are_disjoint:
        p_union = die_roll.P(event_even.union(event_odd))
        p_sum = die_roll.P(event_even) + die_roll.P(event_odd)

        print(f"P(Even U Odd) = {p_union:.2f}")
        print(f"P(Even) + P(Odd) = {p_sum:.2f}")
        print(f"Is P(E U O) == P(E) + P(O)? {math.isclose(p_union, p_sum)}")


except ValueError as e:
    print(f"\n An error occured: {e}")

