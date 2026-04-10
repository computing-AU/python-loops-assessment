"""
autograder.py — Python Loops Assessment Auto-Grader
Run this file to check your answers: python autograder.py
"""

import subprocess
import sys
import os

QUESTIONS = [
    # (q_num, file, description, marks, section)
    (1,  "questions/q01.py", "Counting with a for Loop",       2,  "A"),
    (2,  "questions/q02.py", "Trace Table Practice",            2,  "A"),
    (3,  "questions/q03.py", "The while Loop",                  3,  "A"),
    (4,  "questions/q04.py", "Sum and Product with Loops",      3,  "A"),
    (5,  "questions/q05.py", "FizzBuzz Variant",                3,  "A"),
    (6,  "questions/q06.py", "Solid Rectangle",                 3,  "B"),
    (7,  "questions/q07.py", "Right-Angle Triangle",            3,  "B"),
    (8,  "questions/q08.py", "Inverted Triangle",               3,  "B"),
    (9,  "questions/q09.py", "Number Staircase Patterns",       4,  "B"),
    (10, "questions/q10.py", "Hollow Rectangle",                4,  "B"),
    (11, "questions/q11.py", "Centred Pyramid",                 4,  "B"),
    (12, "questions/q12.py", "Full Diamond (Hollow)",           4,  "B"),
    (13, "questions/q13.py", "Alphabet Patterns",               3,  "B"),
    (14, "questions/q14.py", "Pascal's Triangle",               6,  "B"),
    (15, "questions/q15.py", "Debug the Code",                  6,  "C"),
    (16, "questions/q16.py", "Understanding & Reflection",      6,  "C"),
    (17, "questions/q17.py", "Looping Through a List",          3,  "D"),
    (18, "questions/q18.py", "Finding Maximum and Minimum",     3,  "D"),
    (19, "questions/q19.py", "Looping Through a String",        3,  "D"),
    (20, "questions/q20.py", "Multiplication Grid",             4,  "D"),
    (21, "questions/q21.py", "break and continue",              3,  "D"),
    (22, "questions/q22.py", "Zigzag and Wave Patterns",        6,  "E"),
    (23, "questions/q23.py", "Checkerboard Pattern",            6,  "E"),
    (24, "questions/q24.py", "Prime Number Sieve",              8,  "E"),
    (25, "questions/q25.py", "Pattern Design Challenge",        4,  "E"),
]

CHECKS = {
    1:  lambda o: o == "\n".join(str(i) for i in range(1, 11)),
    2:  lambda o: o == "1\n3\n6\n10\n15",
    3:  lambda o: o == "1\n2\n4\n8\n16\n32\n64",
    4:  lambda o: "Sum: 31" in o and "Product: 9072" in o,
    5:  lambda o: (len(o.splitlines()) == 30 and
                   o.splitlines()[2] == "Fizz" and
                   o.splitlines()[4] == "Buzz" and
                   o.splitlines()[14] == "FizzBuzz"),
    6:  lambda o: (len(o.splitlines()) == 4 and
                   all(l == "******" for l in o.splitlines())),
    7:  lambda o: all(o.splitlines()[i] == "*" * (i+1) for i in range(5)),
    8:  lambda o: all(o.splitlines()[i] == "*" * (5-i) for i in range(5)),
    9:  lambda o: "2 2" in o and "3 3 3" in o,
    10: lambda o: (o.splitlines()[0] == "********" and
                   o.splitlines()[-1] == "********" and
                   all(l[1:-1] == " " * 6 for l in o.splitlines()[1:-1])),
    11: lambda o: ("*" * 9 in o and len(o.splitlines()) == 5),
    12: lambda o: len(o.splitlines()) == 9,
    13: lambda o: (o.splitlines()[0].strip() == "A" and
                   o.splitlines()[4].strip() == "A B C D E"),
    14: lambda o: ("10" in o and len([l for l in o.splitlines() if l.strip()]) == 6),
    15: lambda o: True,   # manually graded
    16: lambda o: True,   # manually graded
    17: lambda o: "Even count: 3" in o and "17" in o and "22" in o,
    18: lambda o: "Maximum: 94" in o and "Minimum: 3" in o and "Range: 91" in o,
    19: lambda o: "Vowel count: 3" in o,
    20: lambda o: "25" in o and len(o.splitlines()) == 5,
    21: lambda o: "21" in o and "Found" in o,
    22: lambda o: len([l for l in o.splitlines() if l.strip()]) >= 6,
    23: lambda o: "#" in o,
    24: lambda o: "47" in o and "25" in o and "1060" in o,
    25: lambda o: len([l for l in o.splitlines() if l.strip()]) >= 6,
}

def run_file(path, timeout=5):
    try:
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True, text=True, timeout=timeout
        )
        return result.stdout.strip(), result.returncode, None
    except subprocess.TimeoutExpired:
        return "", -1, "TIMEOUT (possible infinite loop)"
    except Exception as e:
        return "", -1, str(e)

def grade():
    print("\n" + "="*65)
    print("  🐍  PYTHON LOOPS ASSESSMENT — AUTO-GRADER")
    print("="*65)

    total_earned = 0
    total_possible = 0
    section_scores = {}

    for q_num, path, desc, marks, section in QUESTIONS:
        total_possible += marks
        if section not in section_scores:
            section_scores[section] = [0, 0]
        section_scores[section][1] += marks

        if not os.path.exists(path):
            status = "❌ FILE NOT FOUND"
            earned = 0
        else:
            output, code, err = run_file(path)
            if err:
                status = f"⚠️  ERROR — {err}"
                earned = 0
            elif code != 0:
                status = "❌ RUNTIME ERROR"
                earned = 0
            elif q_num in (15, 16):
                status = "📋 MANUAL GRADING REQUIRED"
                earned = 0
            else:
                try:
                    passed = CHECKS[q_num](output)
                    if passed:
                        earned = marks
                        status = f"✅ PASSED"
                    else:
                        earned = 0
                        status = "❌ WRONG OUTPUT"
                except Exception:
                    earned = 0
                    status = "⚠️  CHECK ERROR"

        total_earned += earned
        section_scores[section][0] += earned
        label = f"Q{q_num:02d} [{marks}m]"
        print(f"  {label:12} {desc:<35} {status}")

    print("\n" + "-"*65)
    print("  SECTION SCORES")
    print("-"*65)
    section_names = {
        "A": "Basic Loops",
        "B": "Nested & Patterns",
        "C": "Debug & Analysis  (manual)",
        "D": "Loops with Data",
        "E": "Advanced Patterns"
    }
    for sec in "ABCDE":
        earned, possible = section_scores.get(sec, [0, 0])
        bar = "█" * earned + "░" * (possible - earned)
        print(f"  Section {sec} — {section_names[sec]:<28} {earned:>3}/{possible}  {bar}")

    print("\n" + "="*65)
    pct = int(total_earned / total_possible * 100)
    print(f"  TOTAL SCORE:  {total_earned} / {total_possible}  ({pct}%)")
    if pct >= 90:   grade_letter = "A+"
    elif pct >= 80: grade_letter = "A"
    elif pct >= 70: grade_letter = "B"
    elif pct >= 60: grade_letter = "C"
    elif pct >= 50: grade_letter = "D"
    else:           grade_letter = "F"
    print(f"  GRADE:        {grade_letter}")
    print("="*65)
    print("  Note: Q15 and Q16 require manual grading by your instructor.")
    print("="*65 + "\n")

if __name__ == "__main__":
    grade()
