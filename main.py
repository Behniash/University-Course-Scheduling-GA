from src.utils import load_courses, load_professors, load_classrooms

if __name__ == "__main__":
    courses = load_courses(r"D:\University Course Timetabling Optimization\Data\courses.json")
    professors = load_professors(r"D:\University Course Timetabling Optimization\Data\professors.json")
    classrooms = load_classrooms(r"D:\University Course Timetabling Optimization\Data\classes.json")

    print(" Courses:")
    for c in courses:
        print("-", c)

    print("\n Professors:")
    for p in professors:
        print("-", p)

    print("\n Classrooms:")
    for cl in classrooms:
        print("-", cl)




from src.utils import load_courses, load_professors, load_classrooms
from src.genetic_algorithm import generate_initial_population

if __name__ == "__main__":
    # لود داده‌ها
    courses = load_courses(r"D:\University Course Timetabling Optimization\Data\courses.json")
    professors = load_professors(r"D:\University Course Timetabling Optimization\Data\professors.json")
    classrooms = load_classrooms(r"D:\University Course Timetabling Optimization\Data\classes.json")

    # تولید جمعیت اولیه
    population = generate_initial_population(5, courses, professors, classrooms)

    # چاپ نمونه
    print(" Initial Population:")
    for i, chromosome in enumerate(population, 1):
        print(f"\nChromosome {i}:")
        for gene in chromosome:
            print(gene)


from src.utils import load_courses, load_professors, load_classrooms
from src.genetic_algorithm import generate_initial_population, evaluate_population

if __name__ == "__main__":
    courses = load_courses(r"D:\University Course Timetabling Optimization\Data\courses.json")
    professors = load_professors(r"D:\University Course Timetabling Optimization\Data\professors.json")
    classrooms = load_classrooms(r"D:\University Course Timetabling Optimization\Data\classes.json")

    population = generate_initial_population(5, courses, professors, classrooms)
    fitness_scores = evaluate_population(population)

    for i, (chromosome, score) in enumerate(zip(population, fitness_scores), 1):
        print(f"\n Chromosome {i} (Fitness: {score}):")
        for gene in chromosome:
            print(gene)


from src.utils import load_courses, load_professors, load_classrooms
from src.genetic_algorithm import genetic_algorithm

if __name__ == "__main__":
    courses = load_courses(r"D:\University Course Timetabling Optimization\Data\courses.json")
    professors = load_professors(r"D:\University Course Timetabling Optimization\Data\professors.json")
    classrooms = load_classrooms(r"D:\University Course Timetabling Optimization\Data\classes.json")

    # اجرای الگوریتم ژنتیک
    best_timetable, best_fitness = genetic_algorithm(
        courses, professors, classrooms,
        population_size=10, generations=20, mutation_rate=0.2
    )

    print("\n Best Timetable Found (Fitness:", best_fitness, ")")
    for gene in best_timetable:
        print(gene)
        



from src.utils import load_courses, load_professors, load_classrooms
from src.genetic_algorithm import genetic_algorithm
from src.visualization import plot_timetable

if __name__ == "__main__":
    courses = load_courses(r"D:\University Course Timetabling Optimization\Data\courses.json")
    professors = load_professors(r"D:\University Course Timetabling Optimization\Data\professors.json")
    classrooms = load_classrooms(r"D:\University Course Timetabling Optimization\Data\classes.json")

    # اجرای الگوریتم ژنتیک
    best_timetable, best_fitness = genetic_algorithm(
        courses, professors, classrooms,
        population_size=10, generations=20, mutation_rate=0.2
    )

    print("\n🎉 Best Timetable Found (Fitness:", best_fitness, ")")
    for gene in best_timetable:
        print(gene)

    # رسم نمودار
    plot_timetable(best_timetable, title=f"Best Timetable (Fitness: {best_fitness})")