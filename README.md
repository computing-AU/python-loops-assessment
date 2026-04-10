# 🐍 Python Loops & Patterns — Assessment

Welcome to the **Python Loops & Patterns Assessment**. This repository contains 25 programming questions across 5 sections, testing your understanding of loops, nested patterns, debugging, data traversal, and advanced pattern generation.

---

## 📋 Assessment Overview

| Section | Topics | Questions | Marks |
|---------|--------|-----------|-------|
| A | Basic Loops | Q1–Q5 | 13 |
| B | Nested & Patterns | Q6–Q14 | 34 |
| C | Debug & Analysis | Q15–Q16 | 12 |
| D | Loops with Data | Q17–Q21 | 16 |
| E | Advanced Patterns | Q22–Q25 | 24 |
| | **TOTAL** | **25** | **100** |

---

## 🚀 Getting Started

### 1. Accept the Assignment
Click the GitHub Classroom invite link shared by your instructor. This will create your own private copy of this repository.

### 2. Clone Your Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 3. Answer the Questions
- All question files are inside the `questions/` folder
- Each file is named `qXX.py` (e.g., `q01.py`, `q14.py`)
- Read the instructions inside each file carefully
- Write your solution in the space marked `# YOUR CODE HERE`

### 4. Test Your Solutions
Run the autograder locally:
```bash
python autograder.py
```
Or run a single test:
```bash
python -m pytest tests/test_q01.py -v
```

### 5. Submit
```bash
git add .
git commit -m "Submit answers"
git push
```

---

## 📁 Repository Structure

```
loops-assessment/
│
├── README.md                  ← You are here
├── MARKSHEET.md               ← Mark sheet (filled by instructor)
├── autograder.py              ← Run this to check your answers
│
├── questions/
│   ├── q01.py  ← Q1:  Counting with a for Loop         [2 marks]
│   ├── q02.py  ← Q2:  Trace Table Practice             [2 marks]
│   ├── q03.py  ← Q3:  The while Loop                   [3 marks]
│   ├── q04.py  ← Q4:  Sum and Product with Loops       [3 marks]
│   ├── q05.py  ← Q5:  FizzBuzz Variant                 [3 marks]
│   ├── q06.py  ← Q6:  Solid Rectangle                  [3 marks]
│   ├── q07.py  ← Q7:  Right-Angle Triangle             [3 marks]
│   ├── q08.py  ← Q8:  Inverted Triangle                [3 marks]
│   ├── q09.py  ← Q9:  Number Staircase Patterns        [4 marks]
│   ├── q10.py  ← Q10: Hollow Rectangle                 [4 marks]
│   ├── q11.py  ← Q11: Centred Pyramid                  [4 marks]
│   ├── q12.py  ← Q12: Full Diamond (Hollow)            [4 marks]
│   ├── q13.py  ← Q13: Alphabet Patterns                [3 marks]
│   ├── q14.py  ← Q14: Pascal's Triangle                [6 marks]
│   ├── q15.py  ← Q15: Debug the Code                   [6 marks]
│   ├── q16.py  ← Q16: Understanding & Reflection       [6 marks]
│   ├── q17.py  ← Q17: Looping Through a List           [3 marks]
│   ├── q18.py  ← Q18: Finding Maximum and Minimum      [3 marks]
│   ├── q19.py  ← Q19: Looping Through a String         [3 marks]
│   ├── q20.py  ← Q20: Multiplication Grid              [4 marks]
│   ├── q21.py  ← Q21: break and continue               [3 marks]
│   ├── q22.py  ← Q22: Zigzag and Wave Patterns         [6 marks]
│   ├── q23.py  ← Q23: Checkerboard Pattern             [6 marks]
│   ├── q24.py  ← Q24: Prime Number Sieve               [8 marks]
│   └── q25.py  ← Q25: Pattern Design Challenge         [4 marks]
│
└── tests/
    ├── test_q01.py ... test_q25.py   ← Automated tests
```

---

## 📌 Rules

- ✅ You may use any Python built-in functions unless stated otherwise
- ❌ Do not import external libraries unless the question allows it
- ❌ Do not copy answers from classmates or the internet
- ✅ Comments and clean code are encouraged
- ⏰ Submit before the deadline shown in GitHub Classroom

---

## 🧑‍🏫 Instructor Notes

- Autograder checks output format strictly — spacing and newlines matter
- Partial marks are awarded manually for Q15 and Q16
- To view all student submissions: use GitHub Classroom dashboard

---

Good luck! 🚀
