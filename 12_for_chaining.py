rules = {
    "A and B": "C",
    "C and D": "E",
    "E": "F"
}
facts = {"A", "B", "D"}
print("Initial Facts:", facts)
def conditions_met(condition, known_facts):
    parts = condition.split(" and ")
    return all(part in known_facts for part in parts)
inferred = True
while inferred:
    inferred = False
    for condition, conclusion in rules.items():
        if conditions_met(condition, facts) and conclusion not in facts:
            facts.add(conclusion)
            print(f"Rule fired: IF {condition} THEN {conclusion}")
            inferred = True

print("\nFinal Facts:", facts)

