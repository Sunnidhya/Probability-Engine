import math

class ProbabilitySpace:
    """
    A class to represent a finite probability space and enforce its axioms.
    """


    def __init__(self, sample_space, prob_distribution):
        """
        Initializes the probability space. 

        Args:
            sample_space (set): A set of all possible elementary outcomes
            prob_distribution (dict): A nmapping form each outcome to its probability
        """

        self.sample_space = sample_space
        self.prob_distribution = prob_distribution

        # --- Enforcing Axioms 1 & 2 ----
        # Axiom 1 (Non-negativity): Check if all probabilites are >=0
        
        if not all(p>=0 for p in self.prob_distribution.values()):
            raise ValueError("Axiom 1 Violatoin: All probabilites must be non-negative.")
        
        # Axiom 2 ( Normalization): Check if the sum of probabilites is 1
        total_prob = sum(self.prob_distribution.values())
        if not math.isclose(total_prob, 1.0):
            raise ValueError(f"Axiom 2 Violation: Sum of probabilites must be 1, but it is {total_prob}.")



    def P(self, event):
        """
        Calculates the probability of a given event.
        An event is a subset of the sample space.
        """

        # An event must be a subset of the sample space

        if not set(event).issubset(self.sample_space):
            raise ValueError("The event contains outcomes not in the sample space.")


        # Calculate probability by summing probabilities of outcomes in the event. 
        # This inherently uses the additivty axiom for elementary (disjoint) events
        return sum(self.prob_distribution[outcome] for outcome in event)


