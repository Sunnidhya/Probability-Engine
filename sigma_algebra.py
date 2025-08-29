class SigmaAlgebra: 
    """
    A class to represent and validate a sigma-algebra ( a collection of events).
    """

    def __init__(self, sample_space, events):
        """
        Initialize and validates the sigma-algebra.

        Args:
            sample_space (frozenst): The set of all possible outcomes.
            events (st of forzensets(: the proposed collection of even4ts.
        """

        self.sample_space = frozenset(sample_space)
        self.events = {frozenset(e) for e in events} # Ensure all events are frozensets

        # --- Validate the three axioms --- 
        self._check_axiom_1()
        self._check_axiom_2()

        print("Success: The provided collection of events forms a valid sigma-algebra.")


    def _check_axiom_1(self):
        """Axiom 1: The sample sapce must be an event."""
        if self.sample_space not in self.events:
            raise ValueError(f"Axiom 1 Violation: The sample space {self.sample_space} is not in the events collection.")
        print("Axiom 1 check passed/")


    def _check_axiom_2(self):
        """Axiom 2 : Must be closed uner complementation."""

        for event in self.events:
            complement = self.sample_space.difference(event)
            if complement not in self.events:
                raise ValueError(f"Axiom 2 Violation: The complement of {event}, which is {complement}, is not in the events collection.")

        print("Axiom 2 check passed.")
    

    def _check_axiom_3(self):
        """Axiom 3: Must be closed under countable (int his case, finite) unions."""
        # Note: For a finite sample sape, we only need to check for finite unions. 
        # This is a practical simplication
        import itertools
        for i in range(1, len(self.events) + 1):
            print(i)
            for combo in itertools.combinations(self.events, i):
                union_of_combo = frozenset().union(*combo)
                if union_of_combo not in self.events:
                    raise ValueError(f"Axiom 3 Violation: The union of {combo}, which is {union_of_combo}, is not in the events collection.")

        print("Axiom 3 check passed.")

    def __str__(self):
        return f"Sample Space (S): {set(self.sample_space)}\nEvents (F): {{ set(e) for e in self.events }}"
