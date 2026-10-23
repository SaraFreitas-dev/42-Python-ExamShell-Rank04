<p align="center">
  <img src="assets/banner_practice.png" alt="ExamShell Banner" width="800">
</p>

<br>


<p align="center">
  <a href="https://github.com/stars/SaraFreitas-dev/lists/practiceshell"><img src="https://raw.githubusercontent.com/SaraFreitas-dev/42_School_Badges/main/assets/practiceshell.svg" width="250" alt="PracticeShell"/></a>
  <br>
  <sub>👉 <a href="https://github.com/SaraFreitas-dev/42_School_Badges">Get your 42 badges here</a></sub>
</p>

<h2 align="center">Rank 04 (Python) PracticeShell - Exercises & Solutions</h2>

<br>


> [!WARNING]
> At the request of the 42 Network, this repository no longer contains the real Rank 04 exam subjects or solutions. The PracticeShell now uses **original  exercises**. They are great for training, but they are **not** the actual exam questions.


---

# 💡 About
 
This repository is a **growing bank of exercises** for the topics learned during Milestone 4 of the Python Common Core.
 
The goal is to help you:
 
- **Train** the topics you learned during the milestone
- **Review** your doubts and find your weak points
- **Prepare** for the exam by practicing under time and test pressure.

New exercises will be added over time. Each one focuses on a concept learned during this milestone.
 
---

<br>
<p align="center">
  <img src="assets/terminal_menu.png" alt="PracticeShell Preview" width="400">
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-main-feature-practiceshell-simulator">Features</a> •
  <a href="#️-performance-tests">Performance</a> •
  <a href="#-exam-mode">Exam Mode</a> •
  <a href="#-practice-mode">Practice Mode</a> •
  <a href="#-solutions">Solutions</a>
</p>

---

A Python-based **PracticeShell simulator** inspired by the new 42 School Common Core Rank 04 learning material, combined with a collection of organized solutions grouped by difficulty level.

---

# 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/SaraFreitas-dev/42-Python-ExamShell-Rank04
cd 42-Python-ExamShell-Rank04
```

Run the PracticeShell:

```bash
python3 practiceshell.py
```

You will be presented with the main menu:

```text
[1] Start Exam
[2] Practice Mode
[3] List all exercises
[q] Quit
```

No dependencies, no setup: just Python 3.

---

## 📝 Workspace

When the PracticeShell starts, it automatically creates an `exam_workspace` directory.

All exercise files should be created inside this folder. The grader will only validate solutions placed in the generated workspace.

Example:

```text
exam_workspace/
└── py_move_zeros_end.py
```

Simply create the requested file, implement your solution, and submit it through the PracticeShell interface for automatic evaluation.

---

# ⭐ Main Feature: PracticeShell Simulator

The PracticeShell is the core of this repository.

It lets you practice each milestone topic hands-on, with hidden tests and automatic feedback, instead of just reading solutions.

<p align="center">
  <img src="assets/terminal_example.png" alt="PracticeShell Preview" width="400">
</p>

| Grading | Exam experience | Interface |
|---|---|---|
| Automatic grading | Random exercise assignment | Colored terminal UI |
| Hidden test cases | Progressive level system | Score tracking |
| Performance tests with timeout | Exam & practice modes | Time tracking |
| Forbidden function rules | Rank progression logic | Pure Python |

The workflow:

1. Receive a subject
2. Create the requested Python file
3. Implement the solution
4. Submit for grading
5. Fix failing tests
6. Progress to the next level

<p align="center">
  <img src="assets/ko_grade.png" alt="PracticeShell KO example" width="400">
</p>

---

# ⏱️ Performance Tests

Many exercises require solutions that are not only correct, but also efficient.

Some exercises include large hidden inputs. If your solution takes too long, the test is marked as `[TIMEOUT]`, even if the result would eventually be correct:

```text
✘ KO  count_pairs_sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15...
        expected: 5000
        got     : '[TIMEOUT]'
```

> 💡 If you get a timeout, review the complexity of your approach rather than the correctness of the output.

---

# 🎯 Exam Mode

Select:

```text
[1] Start Exam
```

The simulator will:

- Assign exercises automatically
- Increase difficulty after each successful exercise
- Track your score
- Simulate a 3-hour exam session

## 🏆 Passing the Exam

The simulator uses a progressive difficulty system.
To successfully complete the exam you must validate:

```text
4 / 4 exercises
```

---

# 🛠 Practice Mode

Select:

```text
[2] Practice Mode
```

Practice Mode allows you to:

- Choose any exercise
- Focus on a specific level
- Submit unlimited times
- Train without time pressure

---

# 📚 Solutions

Solutions are organized by level and include the completed exercises.

```text
solutions/
├── level_1
├── level_2
├── level_3
└── level_4
```

This makes it easy to study specific difficulty ranges or review previously solved exercises.

> ⚠️ Try each exercise in the PracticeShell first. Reading solutions before attempting them will not show you where your weak points are.

---

# 📖 Topics Covered

- Lists and nested lists
- Two-pointer techniques
- Sorted sequences and intervals
- Algorithmic efficiency and time complexity
- Implementing algorithms without forbidden built-ins (`sorted()`, `.sort()`, `heapq`)
- Edge case handling
- Algorithmic thinking

---

## ⚠️ Disclaimer

This project is an independent educational tool. 
It is not affiliated with or endorsed by 42 School, and it does not contain any official 42 exam content.

---

## 💡 Suggestions

Found a bug, a missing test case or have an idea? Feel free to [open an issue](https://github.com/SaraFreitas-dev/42-Python-ExamShell-Rank04/issues).

---

## ⭐ Support

<h3 align="center">If this repository helped you prepare for the exam, consider giving it a star ⭐</h3>

<p align="center">Good luck and happy coding 🚀</p>