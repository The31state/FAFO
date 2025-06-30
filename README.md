# FAFO Calculator

Welcome to the **Fuck Around and Find Out Calculator**.

This handy little tool calculates exactly how much you're gonna Find Out depending on how much you decided to go full send, as well as how long, how far, and how hard you kept at it. Think of it like risk assessment...but with more honesty and less PowerPoint.

---

## The Formula

```
FindOut(FA) = e^(K(t, d, i) * FA)
```

Where:

- **FA** = How much you fucked around (the overall size of your decision)
- **K(t, d, i)** = How much your Time, Distance, and Intensity cranked up the consequences:

```
K(t, d, i) = 0.125 * t + 0.5 * d + 0.25 * i
```

---

## The Scales

**Time (t): How long you were messing around**
- 1 = 1–8 hours
- 2 = 8–24 hours
- 3 = Several days
- 4 = Weeks
- 5 = Months

**Distance (d): How many people got pulled into this**
- 1 = Just you (good job, Private)
- 2 = Your team
- 3 = The whole platoon
- 4 = The Battery
- 5 = The battalion and beyond (nice work, everybody knows now)

**Intensity (i): How hard you went**
- 1 = Mild curiosity, "just seeing what happens"
- 2 = Somewhat bold
- 3 = Pretty bold
- 4 = Very aggressive
- 5 = Full send, IDGAF mode

**FA (the Big One):**
Examples of what defines FA:
- Was it a small prank or a massive stunt?
- Did you burn a little time or half the budget?
- How many areas did you impact?
- How big was the overall action?

---

## How to Use

1. Make sure you have Python 3 installed.
2. Download or clone this repo.
3. Open a terminal and run:

   ```
   python fafo_calculator.py
   ```

4. Answer the questions about your operation.
5. Receive your official assessment of how thoroughly you will Find Out.

---

## Example

```
Time scale (how long you were fucking around):
1 = 1-8 hours
...
Enter Time (1-5): 3

Distance scale (how many were affected):
1 = Just you
...
Enter Distance (1-5): 4

Intensity scale (how hard you went):
1 = Mild testing
...
Enter Intensity (1-5): 5

FA (How big was the overall action?)
Enter Fuck Around level: 3

Alright, here’s what you got yourself into:
K(t, d, i) = 3.000
FindOut(FA) = e^(3.000 * 3.0) = 8103.084

Assessment of Consequences:
Result: UCMJ action likely. You have officially found out.
```

---

## Disclaimer

This project is for entertainment (and a little perspective). If you actually do find out, that's on you and probably your chain of command.

---

## License

Do whatever you want with this. Just don’t blame me when you’re standing at parade rest explaining yourself.
