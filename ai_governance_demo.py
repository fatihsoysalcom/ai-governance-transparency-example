import json

class AIModel:
    def __init__(self, name, ethical_guidelines):
        self.name = name
        self.ethical_guidelines = ethical_guidelines
        self.decision_log = []

    def make_decision(self, input_data, context):
        """Simulates making a decision while logging for transparency."""
        decision = self._process(input_data, context)
        self.decision_log.append({
            "input": input_data,
            "context": context,
            "decision": decision,
            "guidelines_applied": self.ethical_guidelines
        })
        return decision

    def _process(self, input_data, context):
        """Placeholder for actual AI model logic."""
        # In a real scenario, this would involve complex ML model inference.
        # For this example, we'll simulate a simple decision based on input.
        if "high_risk" in input_data.lower() and "urgent" in context.lower():
            return "Approve with caution"
        elif "high_risk" in input_data.lower():
            return "Reject"
        else:
            return "Approve"

    def get_decision_log(self):
        """Provides access to the decision log for accountability."""
        return self.decision_log

    def check_compliance(self):
        """Checks if recent decisions align with ethical guidelines."""
        # This is a simplified compliance check.
        # In reality, this would involve more sophisticated analysis.
        compliant = True
        for log_entry in self.decision_log[-5:]:
            if "Reject" in log_entry["decision"] and "high_risk" not in log_entry["input"]:
                compliant = False
                print(f"Potential non-compliance: Decision '{log_entry['decision']}' for input '{log_entry['input']}' might violate guidelines.")
        return compliant

# --- Demonstration ---

# Define ethical guidelines for an AI model used in loan applications
loan_application_guidelines = [
    "No discrimination based on protected characteristics.",
    "Ensure fairness in approval rates.",
    "Provide clear reasons for rejection."
]

# Instantiate an AI model with its guidelines
loan_approver_ai = AIModel("LoanApprovalBot", loan_application_guidelines)

# Simulate some loan application decisions
print("--- Simulating Loan Decisions ---")
loan_approver_ai.make_decision("Applicant A: Salary 50k, Credit Score 700", "Standard application")
loan_approver_ai.make_decision("Applicant B: Salary 30k, Credit Score 500", "High risk application")
loan_approver_ai.make_decision("Applicant C: Salary 100k, Credit Score 750", "Urgent application")
loan_approver_ai.make_decision("Applicant D: Salary 40k, Credit Score 600", "Standard application")
loan_approver_ai.make_decision("Applicant E: Salary 60k, Credit Score 680", "High risk application")

print("\n--- Decision Log (Transparency) ---")
# Print the decision log to show how decisions were made
print(json.dumps(loan_approver_ai.get_decision_log(), indent=2))

print("\n--- Compliance Check (Accountability) ---")
# Check if the AI's recent decisions are compliant
is_compliant = loan_approver_ai.check_compliance()
if is_compliant:
    print("AI model appears to be operating within ethical guidelines.")
else:
    print("AI model may have deviations from ethical guidelines. Further investigation needed.")
