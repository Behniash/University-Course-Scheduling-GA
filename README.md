#  University Course Scheduling with Genetic Algorithm

A Python implementation of a Genetic Algorithm (GA) to solve the university course scheduling problem. This system automatically assigns courses to timeslots and classrooms while satisfying constraints like professor availability and avoiding conflicts.

---

##  Features
 Automatically generates optimized course schedules  
 Handles constraints (e.g., no professor/classroom conflicts)  
 Configurable population size, mutation rates, and generations  
 Clean and modular Python code  
 Includes visualization of scheduling results  

---

##  Project Structure
university-course-scheduling-GA/
├── src/                     # Source code
│   ├── genetic_algorithm.py
│   ├── utils.py
│   ├── timetable_model.py
│   ├── visualization.py
├── data/                    # Input datasets
│   ├── courses.json
│   ├── professors.json
│   ├── classes.json
├── notebooks/               # Jupyter notebooks for testing & visualization
│   ├── main.ipynb
├── main.py                   # Generated schedules and plots
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies

---
## Algorithm Overview

The Genetic Algorithm (GA) workflow:
 1. Initialization: Generate random populations of schedules.
 2. Fitness Evaluation: Assign scores based on constraint satisfaction and optimization goals.
 3. Selection: Select the fittest schedules for reproduction.
 4. Crossover & Mutation: Combine and slightly alter schedules to produce new generations.
 5. Termination: Repeat until an optimal or acceptable schedule is found.

---

##  Requirements
- Python >= 3.8
- numpy
- pandas
- matplotlib
- tqdm
- 
Install dependencies:
```bash
pip install -r requirements.txt

