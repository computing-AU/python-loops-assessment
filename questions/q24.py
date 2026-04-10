"""
Q24 — Prime Number Sieve                                   [8 marks]
Section E: Advanced Patterns
================================================================
The Sieve of Eratosthenes is an ancient algorithm for finding
all prime numbers up to a given limit.

Algorithm:
  1. Create a list of True values, index 0 to n (all "assumed prime")
  2. Set index 0 and 1 to False (not prime)
  3. For each number p starting from 2:
     - If it's still marked True, it's prime
     - Mark all multiples of p (p*p, p*p+p, ...) as False
  4. All indices still True at the end are prime numbers

PART A (4 marks):
  Implement the Sieve of Eratosthenes to find all primes up to 50.
  Print them on one line, separated by spaces.

Expected Output:
  Primes up to 50:
  2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

PART B (2 marks):
  Count and print how many primes exist up to 100.

Expected Output:
  Prime count up to 100: 25

PART C (2 marks):
  Find and print the sum of all primes up to 100.

Expected Output:
  Sum of primes up to 100: 1060
"""

# PART A
print("Part A — Primes up to 50:")
# YOUR CODE HERE

print()

# PART B
print("Part B — Prime count up to 100:")
# YOUR CODE HERE

print()

# PART C
print("Part C — Sum of primes up to 100:")
# YOUR CODE HERE


