import random
import hashlib

class Decision:
    def __init__(self, options):
        self.options = options
        self.decision = self.make_decision()

    def make_decision(self):
        random_option = random.choice(self.options)
        decision_hash = hashlib.sha256(random_option.encode()).hexdigest()
        return random_option, decision_hash

# Define decision options
options = ["Option A", "Option B", "Option C", "Option D"]

# Make a decision
decision = Decision(options)

# Print the decision and its hash
print("Decision:", decision.decision[0])
print("Decision Hash:", decision.decision[1])
