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
