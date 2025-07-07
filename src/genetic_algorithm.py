import random

[
  {"course": "AI101", "time": "sunday 10-8", "classroom": "C101", "professor": "P1"},
  {"course": "DB201", "time": "Tuesday 16-14", "classroom": "C102", "professor": "P1"},
  {"course": "OS301", "time": "monday 10-8", "classroom": "C101", "professor": "P2"}
]


def generate_chromosome(courses, professors, classrooms):
    """یک زمان‌بندی تصادفی تولید می‌کند"""
    chromosome = []

    for course in courses:
        # انتخاب تصادفی زمان از زمان‌های مجاز درس
        time_slot = random.choice(course.allowed_times)

        # پیدا کردن استاد
        professor = next((p for p in professors if p.code == course.professor_code), None)

        # بررسی اینکه استاد در آن زمان آزاد است
        if time_slot not in professor.available_times:
            # اگر زمان آزاد نبود یکی از زمان‌های آزاد استاد را انتخاب کن
            time_slot = random.choice(professor.available_times)

        # انتخاب تصادفی کلاس
        classroom = random.choice(classrooms)

        gene = {
            "course": course.code,
            "time": time_slot,
            "classroom": classroom.code,
            "professor": professor.code
        }
        chromosome.append(gene)

    return chromosome


def generate_initial_population(pop_size, courses, professors, classrooms):
    """یک جمعیت اولیه تولید می‌کند"""
    population = []
    for _ in range(pop_size):
        chromosome = generate_chromosome(courses, professors, classrooms)
        population.append(chromosome)
    return population


def calculate_fitness(chromosome):
    """
    نمره کیفیت یک کروموزوم (زمان‌بندی)
    """
    score = 100  # شروع از نمره کامل

    time_professor_map = {}
    time_classroom_map = {}

    for gene in chromosome:
        time_slot = gene["time"]
        professor = gene["professor"]
        classroom = gene["classroom"]

        #  بررسی تداخل استاد
        if (time_slot, professor) in time_professor_map:
            score -= 10  # پنالتی
        else:
            time_professor_map[(time_slot, professor)] = True

        #  بررسی تداخل کلاس
        if (time_slot, classroom) in time_classroom_map:
            score -= 10  # پنالتی
        else:
            time_classroom_map[(time_slot, classroom)] = True

        #  اگر همه چیز درست بود، امتیاز کم نمی‌کنیم

    return max(score, 0)  # نمره منفی نده


def evaluate_population(population):
    """
    نمره‌دهی به تمام جمعیت
    """
    fitness_scores = []
    for chromosome in population:
        fitness = calculate_fitness(chromosome)
        fitness_scores.append(fitness)
    return fitness_scores



def select_parents(population, fitness_scores):
    """
    انتخاب دو والد از جمعیت با روش چرخ رولت
    """
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]

    parents = random.choices(population, weights=probabilities, k=2)
    return parents[0], parents[1]

def crossover(parent1, parent2):
    """
    Single-point crossover
    """
    point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

def mutate(chromosome, courses, professors, classrooms, mutation_rate=0.1):
    """
    تغییر تصادفی در ژن‌ها
    """
    for gene in chromosome:
        if random.random() < mutation_rate:
            # تغییر زمان درس
            new_time = random.choice(courses_by_code(gene["course"], courses).allowed_times)
            gene["time"] = new_time

        if random.random() < mutation_rate:
            # تغییر کلاس درس
            new_classroom = random.choice(classrooms).code
            gene["classroom"] = new_classroom

    return chromosome


def courses_by_code(code, courses):
    """
    پیدا کردن شیء Course با کد درس
    """
    return next((c for c in courses if c.code == code), None)

def genetic_algorithm(
    courses, professors, classrooms,
    population_size=10, generations=50, mutation_rate=0.1 ):

    # تولید جمعیت اولیه
    population = generate_initial_population(population_size, courses, professors, classrooms)

    for generation in range(generations):
        print(f"\n Generation {generation + 1}")

        # ارزیابی جمعیت
        fitness_scores = evaluate_population(population)
        best_fitness = max(fitness_scores)
        print(f"⭐ Best Fitness: {best_fitness}")

        # تولید نسل جدید
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)

            child1 = mutate(child1, courses, professors, classrooms, mutation_rate)
            child2 = mutate(child2, courses, professors, classrooms, mutation_rate)

            new_population.extend([child1, child2])

        population = new_population

    # بهترین کروموزوم
    final_fitness_scores = evaluate_population(population)
    best_index = final_fitness_scores.index(max(final_fitness_scores))
    best_timetable = population[best_index]

    return best_timetable, max(final_fitness_scores)