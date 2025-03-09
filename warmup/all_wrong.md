# All Wrong


**Problem Description**

You are given a multiple-choice test with **N** questions, numbered from **1** to **N**. Each question has **two** answer options, labeled "A" and "B". You are provided with a string **C** of length **N**, where the **i**-th character in **C** represents the correct answer for question **i** (either "A" or "B").

Your objective is to get a score of **0** by answering every question incorrectly. That means you need to provide the wrong answer for each question.

### Task
Implement the function **getWrongAnswers(N, C)** which takes the following inputs:
- **N** (1 ≤ N ≤ 100): An integer representing the number of questions.
- **C**: A string of length **N** where each character is either "A" or "B", representing the correct answers.

The function should return a string of length **N**, where the **i**-th character is the incorrect answer for question **i** (either "A" or "B").

### Example

#### Sample Test Case #1
**Input:**
```python
N = 3
C = "ABA"
```

**Output:**
```python
"BAB"
```

**Explanation:**
The correct answers are A, B, and A. The incorrect answers should be B, A, and B.

#### Sample Test Case #2
**Input:**
```python
N = 5
C = "BBBBB"
```

**Output:**
```python
"AAAAA"
```

**Explanation:**
Since all correct answers are B, we should answer each question with A to ensure a score of 0.

### Constraints
- **1 ≤ N ≤ 100**
- Each character in **C** is either "A" or "B".

### Notes
- The solution should be efficient, handling the maximum constraint in a reasonable time.
- The function should always return a string of length **N**, ensuring each answer is incorrect.

