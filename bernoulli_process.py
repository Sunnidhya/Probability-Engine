import random 
import math

class BernoulliProcess:
    """
    A class to simulate a Bernoulli process and calculate related statistics, 
    including KL divergence
    """

    def __init__(self, p):
        if not(0<= p <= 1):
            raise ValueError("Probability 'p' must be between 0 and 1.")
        self.p = p
        self.last_run = []


    def run(self,n):
        self.last_run = [1 if random.random() < self.p else 0 for _ in range(n)]
        return self.last_run
    
    def get_partial_sum(self):
        """
        Returns the total numebr of successes ( the partial sum 'k').
        """

        return sum(self.last_run)

    def kl_divergence(self):
        """
        Calculates the KL divergence betweent he true distribution (p) and the observed distribution from the last run (k/n)
        """

        n = len(self.last_run)
        if n == 0:
            return None

        k = self.get_partial_sum()
        q = k / n # This is our observed probability

        # ---- Handle Edge cases ---
        # If observed q is 0 or 1, the KL divergence is theoritically infinite
        # unless p is also 0 or 1, respectively

        if q == 0 or q == 1:
            # We cant compute log(0), so handle this gracefully
            if q == self.p:
                return 0.0
            return float('inf') # return infinty for maximally different distributions

        p = self.p
        # the KL divergence formula

        return p*math.log(p/q) + (1-p)*math.log((1-p)/(1-q))
