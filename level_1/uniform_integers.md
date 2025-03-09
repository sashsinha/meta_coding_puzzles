# Uniform Integers

## Problem Description
A positive integer is considered uniform if all of its digits are equal. For example, 222 is uniform, while 223 is not.

Given two positive integers **A** and **B**, determine the number of uniform integers between **A** and **B**, inclusive.

## Constraints
- 1 ≤ A ≤ B ≤ 10¹²

## Sample Test Cases

### Test Case 1
- **Input:** A = 75, B = 300  
- **Expected Output:** 5  
- **Explanation:** The uniform integers between 75 and 300 are: 77, 88, 99, 111, and 222.

### Test Case 2
- **Input:** A = 1, B = 9  
- **Expected Output:** 9  
- **Explanation:** All single-digit numbers are uniform.

### Test Case 3
- **Input:** A = 999999999999, B = 999999999999  
- **Expected Output:** 1  
- **Explanation:** The single number considered is uniform.
