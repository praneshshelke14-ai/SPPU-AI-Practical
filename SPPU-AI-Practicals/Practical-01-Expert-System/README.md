# Practical 01 Expert System
## Expert System Using Rule-Based System (RBS) in AI

## Aim
Build a simple expert system using rules to provide simple decision-making advice.

## Problem statement
Develop an expert system using a Rule-Based System. The notebook frames this as a simple decision-making expert system; the included demonstration domain is computer troubleshooting.

## Objectives
- Understand the concept of an expert system and rule-based system.
- Represent knowledge as facts and IF-THEN rules.
- Apply rules to known facts to infer a recommendation.

## Theory
1. An expert system is an AI program that uses stored domain knowledge to provide advice or decisions in a limited subject area.
2. A rule-based system represents knowledge using IF-THEN rules. The IF part is the condition and the THEN part is the conclusion or action.
3. A fact is information supplied by the user or already known to the system. An inference engine checks rules against facts and fires matching rules.
4. A knowledge base stores rules and facts; an inference engine applies them. Forward chaining starts from facts and derives conclusions. Backward chaining starts from a goal and checks whether supporting facts are true.

## Algorithm / Procedure
1. Start the program.
2. Ask the user a small set of yes/no questions and store the answers as facts.
3. Compare the known facts with conditions in the rule base.
4. When all conditions of a rule match, display its conclusion.
5. If no rule matches, request more information or display a fallback message.
6. Stop.

## Complexity / Practical nature
For R rules with up to C conditions per rule, the simple sequential rule check is O(R x C) time. Space is O(F + R), where F is the number of stored facts.

## Expected output / record
Example: answer n to “Does the computer power on?” The system reports that the computer does not power on and recommends checking the socket, cable, adapter and battery.

## Python program
Source file: [`practical_01_rule_based_expert_system.py`](practical_01_rule_based_expert_system.py)

### Run
```bash
python practical_01_rule_based_expert_system.py
```

The program uses only Python's standard library; no external package installation is needed.

<!-- BEGIN FULL PYTHON SOURCE -->
## Complete Python code (copy-ready)

The same program is also saved as [`practical_01_rule_based_expert_system.py`](practical_01_rule_based_expert_system.py) so it can be run directly.

```python
"""Practical 1: Rule-Based Expert System (RBS) for simple computer troubleshooting.

This is a small educational rule-based system. It is not a professional diagnostic tool.
"""

RULES = [
    ({"power_on": False},
     "The computer does not power on. Check the wall socket, power cable, adapter and battery."),
    ({"power_on": True, "display_visible": False},
     "The computer powers on but shows no display. Check brightness, display cable and external monitor."),
    ({"power_on": True, "display_visible": True, "internet_working": False},
     "The display works but internet does not. Check Wi-Fi/Ethernet, router and network settings."),
    ({"power_on": True, "display_visible": True, "internet_working": True},
     "The basic checks are normal. The system appears to be working."),
]


def ask_yes_no(question):
    """Read a yes/no answer and return True for yes, False for no."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def infer(facts):
    """Apply the first rule whose conditions match the known facts."""
    for conditions, conclusion in RULES:
        if all(facts.get(key) == value for key, value in conditions.items()):
            return conclusion
    return "Not enough information. Please collect more facts."


def main():
    print("RULE-BASED EXPERT SYSTEM - COMPUTER TROUBLESHOOTING")
    facts = {"power_on": ask_yes_no("Does the computer power on?")}

    if facts["power_on"]:
        facts["display_visible"] = ask_yes_no("Is anything visible on the display?")
        if facts["display_visible"]:
            facts["internet_working"] = ask_yes_no("Is the internet connection working?")

    print("\nKnown facts:", facts)
    print("Expert-system advice:", infer(facts))


if __name__ == "__main__":
    main()
```

<!-- END FULL PYTHON SOURCE -->

## Oral / viva questions with answers
**Q1. What is an expert system?**
Answer: An AI program that uses stored expert knowledge and rules to solve problems in a specific domain.

**Q2. What is a rule-based system?**
Answer: A system that represents knowledge as IF-THEN rules.

**Q3. What is a knowledge base?**
Answer: The collection of facts and rules used by the expert system.

**Q4. What is an inference engine?**
Answer: The component that matches facts with rules and derives conclusions.

**Q5. What is a fact?**
Answer: A known piece of information, usually supplied by the user or stored in the system.

**Q6. What is forward chaining?**
Answer: A data-driven method that starts with facts and applies rules to derive new facts or conclusions.

**Q7. What is backward chaining?**
Answer: A goal-driven method that starts with a possible conclusion and checks whether its conditions can be proved.

**Q8. Why is this example not a general AI system?**
Answer: It uses a limited set of manually written rules for one narrow troubleshooting domain.

**Q9. What happens if no rule matches?**
Answer: The system returns a fallback message saying that there is not enough information.

**Q10. Give one advantage and one limitation of an RBS.**
Answer: It is easy to explain and audit; however, it only handles cases covered by its rules.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.
