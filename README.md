# Programming Task 03 – Loops, Patterns & Basic Automation

**Task:** Task 03
**Topics Covered:** Loops, Patterns, Automation, Authentication, String Manipulation

---

## What is This Task About?

This task is all about practising loops and logical thinking in Python.
Every program here solves a real-world style problem using simple loops,
conditions, and string operations. The goal is to understand how repeating
steps can automate tasks that would otherwise take forever to do manually.

---

## Folder Structure

```
Programming_Task_03_Akhil_Vargis_S/
│
├── multiplication_table.py
├── number_analysis.py
├── patterns.py
├── password_attempt.py
├── username_generator.py
├── number_guessing.py        ← Bonus
│
└── README.md
```

---

## Part A – Multiplication Table Generator

**File:** `multiplication_table.py`

### What it does
You type a number, and the program prints its full multiplication table
from 1 to 10. Simple and clean.

### How it works — in plain words

1. We ask the user to enter a number.
2. We use a `for` loop that counts from 1 to 10.
3. In each step of the loop, we multiply the user's number by the loop
   counter and print the result.
4. That's it — 10 lines of output, one per multiplication step.

### The key idea
A `for` loop with `range(1, 11)` visits the numbers 1, 2, 3 … all the
way to 10, one at a time. We do our calculation inside that loop so it
runs automatically for every number.

### Sample Output
```
Enter a number: 7

Multiplication Table of 7:
--------------------
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

## Part B – Number Analysis Tool

**File:** `number_analysis.py`

### What it does
You enter a number N. The program goes through every number from 1 to N
and tells you the total sum, how many of those numbers are even, and how
many are odd.

### How it works — in plain words

1. We ask the user for a number N.
2. We create three buckets to keep track: `total`, `even_count`, `odd_count`.
   All start at zero.
3. We loop from 1 to N. For each number:
   - We add it to `total` to keep a running sum.
   - We check if it divides evenly by 2. If yes, it is even. If no, it is odd.
   - We add 1 to the right counter.
4. After the loop finishes, we print all three results.

### The key idea
The `%` symbol (called modulus) gives the remainder after dividing.
So `7 % 2` gives `1` (not even), and `8 % 2` gives `0` (even).
That one check is how we sort every number into even or odd.

### Sample Output
```
Enter a number N: 10

Sum = 55
Even Numbers = 5
Odd Numbers = 5
```

---

## Part C – Pattern Printing Challenge

**File:** `patterns.py`

### What it does
Prints three visual patterns made of stars and numbers using loops.

### How it works — in plain words

**Pattern 1 – Growing Stars**
We loop from 1 to 5. In row 1 we print one star, in row 2 we print two
stars, and so on. The trick is `"*" * row` which repeats the star
character as many times as the row number.

**Pattern 2 – Shrinking Stars**
Same idea but we count backwards from 5 down to 1 using `range(5, 0, -1)`.
So the first row has 5 stars and each row after that has one fewer.

**Pattern 3 – Number Triangle**
This one uses two loops nested inside each other.
The outer loop controls which row we are on (1 to 5).
The inner loop prints numbers from 1 up to the current row number,
all on the same line. After the inner loop finishes, we move to the
next line.

### The key idea
`end=""` inside the print statement stops Python from jumping to a new
line. We use this to print numbers side by side on the same row.
After all numbers in a row are printed, we call `print()` with nothing
in it — that gives us the line break.

### Sample Output
```
Pattern 1 - Growing Stars:
*
**
***
****
*****

Pattern 2 - Shrinking Stars:
*****
****
***
**
*

Pattern 3 - Number Triangle:
1
12
123
1234
12345
```

---

## Part D – Password Attempt Simulator

**File:** `password_attempt.py`

### What it does
The program has a password stored inside it. The user gets 3 chances to
type the correct password. If they get it right, access is granted.
If they fail all 3 times, the account gets locked.

### How it works — in plain words

1. We store the correct password inside the program as a variable.
2. We run a loop 3 times (once per attempt).
3. Each time, we ask the user to type a password.
4. We compare what they typed to the real password using `==`.
   - If it matches → print "Access Granted" and stop the loop with `break`.
   - If it does not match → tell them how many tries are left.
5. Python has a special trick: a `for` loop can have an `else` block.
   That `else` block only runs if the loop finished without hitting a
   `break`. We use this to print "Account Locked" automatically after
   3 failed attempts.

### The key idea
This simulates how real login systems protect accounts. After too many
wrong tries, they lock you out to stop someone from guessing the password
by trying thousands of combinations. That technique is called
brute-force protection.

### Sample Output
```
=== Login System ===
Attempt 1 of 3 - Enter password: hello
 Wrong password! You have 2 attempt(s) remaining.

Attempt 2 of 3 - Enter password: abc
 Wrong password! You have 1 attempt(s) remaining.

Attempt 3 of 3 - Enter password: wrong

 Account Locked. Too many failed attempts.
```

---

## Part E – Username Generator

**File:** `username_generator.py`

### What it does
You enter your first name, last name, and birth year. The program creates
5 different username suggestions by mixing and matching parts of your
name and year in clever ways.

### How it works — in plain words

1. We ask the user for their first name, last name, and birth year.
2. We convert everything to lowercase so the usernames look neat
   (using `.lower()`).
3. We pull out two useful pieces:
   - The **short year**: last 2 digits of birth year (e.g. `2004` → `04`)
     using `birth_year[-2:]`.
   - The **first initial**: just the first letter of the first name
     using `first_name[0]`.
4. We then combine these pieces in 5 different ways to build unique
   username suggestions.

### The 5 username formats

| # | Format | Example |
|---|--------|---------|
| 1 | firstname + lastname + full year | `sohampatel2004` |
| 2 | first initial + dot + lastname + short year | `s.patel04` |
| 3 | lastname + underscore + firstname | `patel_soham` |
| 4 | firstname + short year + underscore + lastname | `soham04_patel` |
| 5 | first initial + lastname + underscore + full year | `spatel_2004` |

### The key idea
String slicing lets us cut out specific parts of a word.
`word[0]` gives the first character. `word[-2:]` gives the last two
characters. By combining these small pieces in different orders, we
can generate many unique variations from just three inputs.

### Sample Output
```
=== Username Generator ===

Enter your First Name: Soham
Enter your Last Name: Patel
Enter your Birth Year: 2004

Here are your username suggestions:

1.  sohampatel2004
2.  s.patel04
3.  patel_soham
4.  soham04_patel
5.  spatel_2004
```

---

## Bonus – Number Guessing Game

**File:** `number_guessing.py`

### What it does
The computer secretly picks a random number between 1 and 50. You keep
guessing until you find it. After each guess it tells you if the answer
is higher or lower. At the end it shows how many attempts you took.

### How it works — in plain words

1. We use Python's `random` module to generate a secret number between
   1 and 50 that the user cannot see.
2. We start an attempt counter at zero.
3. We use a `while True` loop — this keeps running forever until we
   tell it to stop.
4. Each time through the loop:
   - We ask the user to guess.
   - We add 1 to the attempt counter.
   - We compare the guess to the secret number.
     - Too low → hint to go higher.
     - Too high → hint to go lower.
     - Exactly right → print the congratulations message and use
       `break` to exit the loop and end the game.

### The key idea
`while True` creates a loop that never stops on its own. The only way
out is the `break` statement, which we trigger the moment the user
guesses correctly. This pattern is very common in real programs — menus,
games, and servers all use it to keep running until something specific
happens.

### Sample Output
```
=== Number Guessing Game ===
I have picked a secret number between 1 and 50.
Keep guessing until you find it!

Your guess: 25
Too low! Try a higher number.

Your guess: 38
 Too high! Try a lower number.

Your guess: 31
 Too low! Try a higher number.

Your guess: 35
 Correct! The secret number was 35.
You got it in 4 attempt(s). Well done!
```

---

## Concepts Used — Quick Reference

| Concept | What it means | Used in |
|--------|--------------|---------|
| `for` loop | Repeats steps a fixed number of times | A, B, C, D |
| `while` loop | Keeps repeating until a condition is met | Bonus |
| `range()` | Generates a sequence of numbers to loop over | A, B, C |
| `break` | Exits a loop immediately | D, Bonus |
| `for-else` | Runs extra code only if loop was never broken | D |
| `%` modulus | Finds the remainder — used to check even/odd | B |
| Nested loops | A loop inside another loop | C |
| `==` comparison | Checks if two values are exactly equal | D |
| String slicing `[-2:]` | Cuts out the last 2 characters of a string | E |
| String indexing `[0]` | Gets the first character of a string | E |
| `.lower()` | Converts text to all lowercase | E |
| `random.randint()` | Picks a random whole number in a range | Bonus |

---

## How to Run the Programs

Make sure Python is installed on your computer, then open a terminal
in the folder where the files are saved and run:

```bash
python multiplication_table.py
python number_analysis.py
python patterns.py
python password_attempt.py
python username_generator.py
python number_guessing.py
```

---

## What I Learned From This Task

- Loops save enormous amounts of time — instead of writing the same
  line 10 times, one loop does it automatically.
- The `%` operator is a small but powerful tool for checking divisibility.
- Nested loops let us build grids and patterns row by row and column
  by column.
- A `while True` loop combined with `break` is the standard way to
  keep a program running until the user does something specific.
- Even simple programs like a username generator use real techniques
  (string slicing, indexing, formatting) that appear in professional
  code every day.
