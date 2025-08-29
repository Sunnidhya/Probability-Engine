"""
A module for calculating the expectaiton of discrete random variables. 

Provides funcitons to compute expectation using the standard definition and th4e laternativ tail-sum
forumula for  non-negative variables. It also includes a check for the existence of the expectation
"""

import math
def check_existence(prob_dist):
    """
    Checks if the expectation exists by verifying E[|X|] is finite.

    For a discrete random variable X, the epxectation E[|X|] exists if and only if the sum of 
    |X|*P(X = x) overa ll x converges to a finite value. 

    Args:
        prob_dist(dict): A Dictionary mapping outcomes to probabilites.

    Returns:
        bool: True if the sum is finite, False otherwise.


    Note: For any finite distribution provided as a dict, this will always be True. 
    This check is conceptually important for infinite distributions.
    """

    absolute_sum = sum(abs(outcome) * prob for outcome, prob in prob_dist.items())

    return math.isfinite(absolute_sum)

def calculate_expectation(prob_dist):
    """
    Calculates the expectation of a discrete random variable using the standard formula. 
    E[X] = Σ [x * P(X=x)]

    Args:
    prob_dist (dict): A dictionay mapping outcomes to their porbabilites.

    Returns:
        ValueError: If the expectation does not exist (the sum is not finite)
    """

    if not check_existence(prob_dist):
        raise ValueError("Expectation does not exist: E[|X|] is not finite.")

    return sum(outcome*prob for outcome, prob in prob_dist.items())


def calculate_tail_sum_expectation(prob_dist):
    """
    Calculates the epxectation of NON-NEGATIVE INTEGER random variable using
    the complementary CDF (tail sum) formula.

    E[X] = Σ [P(X > k)] for k from 0 to ∞

    this formula is only valid for randopm variables whose outcomes are 
    non-negatie integers {0,1,2...}

    Args:
        prob_dist (dict): A dictionary mapping outcomes to probabilites

    Raises:
        ValueError: If any outcome is negative or not an integer.
    """

    for outcome in prob_dist.keys():
        if outcome < 0 or not isinstance(outcome, int):
            raise ValueError("Tail sum formula only applies to non-negative integer random variables")

    expected_value = 0.0

    max_outcome = max(prob_dist.keys()) if prob_dist else 0
    
    for k in range(max_outcome + 1):
        prob_x_gt_k  = sum(prob for outcome, prob in prob_dist.items() if outcome > k)
        expected_value += prob_x_gt_k

    return expected_value
