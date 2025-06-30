#!/usr/bin/env python3
"""
FAFO Calculator
==========================
Figure out how much you’re gonna Find Out
based on how much you decided to Fuck Around.

Formula:
    FindOut(FA) = e^(K(t, d, i) * FA)

K(t, d, i) = 0.125 * t + 0.5 * d + 0.25 * i

Author: You :)
"""

import math

def calculate_k(t, d, i):
    """
    Compute scaling factor K.
    """
    return 0.125 * t + 0.5 * d + 0.25 * i

def calculate_findout(fa, k):
    """
    Compute the final FindOut value.
    """
    return math.exp(k * fa)

def main():
    print("\nFAFO (Fuck Around and Find Out) Calculator\n")

    # Time input with scale
    print("Time scale (how long you were fucking around):")
    print("1 = 1-8 hours")
    print("2 = 8-24 hours")
    print("3 = Several days")
    print("4 = Weeks")
    print("5 = Months")
    t = int(input("Enter Time (1-5): "))

    # Distance input with scale
    print("\nDistance scale (how many were affected):")
    print("1 = Just you (the individual)")
    print("2 = Your team")
    print("3 = Your platoon")
    print("4 = The Battery")
    print("5 = The battalion or more")
    d = int(input("Enter Distance (1-5): "))

    # Intensity input with scale
    print("\nIntensity scale (how hard you went):")
    print("1 = Mild testing of boundaries")
    print("2 = Somewhat bold")
    print("3 = Pretty bold")
    print("4 = Very aggressive")
    print("5 = Full send (IDGAF mode)")
    i = int(input("Enter Intensity (1-5): "))

    # FA input with examples
    print("\nFA (How big was the overall action?)")
    print("Examples of what defines FA:")
    print("- The size of the decision (small prank vs massive stunt)")
    print("- The resources or energy you committed")
    print("- How many areas you messed with")
    print("- The overall scale of your action")
    fa = float(input("Enter Fuck Around level (numeric, e.g., 1.0 to 5.0): "))

    # Compute K
    k = calculate_k(t, d, i)

    # Compute FindOut
    findout = calculate_findout(fa, k)

    # Show results
    print("\nAlright, here’s what you got yourself into:")
    print(f"K(t, d, i) = {k:.3f}")
    print(f"FindOut(FA) = e^({k:.3f} * {fa}) = {findout:.3f}")

    # Interpret the FindOut value
    print("\nAssessment of Consequences:")

    if findout < 3:
        print("Result: Minor screw-up. Expect some push-ups and an eye roll.")
    elif findout < 10:
        print("Result: You’ll probably get extra duty and a counseling statement.")
    elif findout < 50:
        print("Result: Negative counseling. Maybe a written reprimand.")
    elif findout < 200:
        print("Result: You’re headed for an Article 15. Start sweating.")
    elif findout < 1000:
        print("Result: Field Grade Article 15 incoming. Hope you like paperwork.")
    else:
        print("Result: UCMJ action likely. You have officially found out.")

if __name__ == "__main__":
    main()
