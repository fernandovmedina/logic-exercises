# 🐍 Python Exercises

A personal collection of Python solutions to competitive programming and coding interview problems, organized by platform. Problems span algorithmic challenges from LeetCode, Beecrowd, Codeforces, ICPC, and a curated set of AWS interview-style questions.

## Structure

```
python/
├── aws/          # Common interview problems (Amazon / cloud-style)
├── beecrowd/     # Beecrowd online judge problems
├── codeforces/   # Codeforces competitive programming problems
├── icpc/         # ICPC-style problems
└── leetcode/     # LeetCode problems
```

## Requirements

- Python 3.10+ (uses structural pattern matching `match/case` in some solutions)

## Running a solution

```bash
python leetcode/two_sum.py
python aws/islands.py
```

Some Beecrowd and Codeforces problems read from stdin:

```bash
echo "400" | python beecrowd/age_in_days.py
echo "wjmzbmr" | python codeforces/236A.py
```

## Topics Covered

- Arrays & Hash Maps
- Strings & Parsing
- Sliding Window
- Two Pointers
- Recursion & Backtracking
- Depth-First Search (DFS)
- Stacks
- Sorting & Greedy
- Math & Number Theory
- Geometry
- Competitive Programming (Codeforces, ICPC, Beecrowd)