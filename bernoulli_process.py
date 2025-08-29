import random

class BernoulliProcess:
    """
    A class to simulate a Bernoulli processa nd calculate related statistics
    """
    def __init__(self, p):
        """
        Initializes the bernoulli process with a given probability of success. 

        Args:
        p(float): The probability of success (msut be 0 and 1).
        """

        if not (0<=p <=1):
            raise ValueError("probability of 'p' must be between 0 and 1.")

        self.p = p
        self.last_run = []


    def run(self, n):
        """
        Runs the process for a specified number of trails.

        Args:
        n ( int ): the numbr of trials to run.

        Returns:
            List: A list of outcomes (1 for success,0 for failure)

        """

        self.last_run = [1 if random.random() < self.p else 0 for _ in range(n)]
        return self.last_run
    
    def num_successes(self):
        """
        Calculates the total numbe rof successes in the last run. 
        This relates to the Binaomal distrubution. 

        Returns:
            int: The ount of successes (1sz).
        """

        return sum(self.last_run)

    def trials_for_first_success(self):
        """
        Finds the trial number of the fisrt success int eh last run. 
        This rleates to the Geometric distributoin.

        Returns:
            int or None: the trial number (1-index of the first sucess, or None of no usccesses occured.
        """

        try:
            # Find the index of the first '1' and add 1 for 1-based indexing.
            return self.last_run.index(1) + 1
        except ValueError:
            return None
