import json

file_path = r"D:\University Course Timetabling Optimization\Data"

def load_json(file_path):
    with open (file_path, "r", encoding='utf-8') as file:
        return json.load(file)

name = 'behnia'

if __name__ == "__main__":
    courses = load_json(r"D:\University Course Timetabling Optimization\Data\classes.json")
    professors = load_json(r"D:\University Course Timetabling Optimization\Data\courses.json")
    classes = load_json(r"D:\University Course Timetabling Optimization\Data\professors.json")
    
    print("Courses:", courses)
    print("Professors:", professors)
    print("Classes:", classes)


from src.timetable_model import Course, Professor, Classroom

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def load_courses(file_path):
    data = load_json(file_path)
    return [Course(**item) for item in data]

def load_professors(file_path):
    data = load_json(file_path)
    return [Professor(**item) for item in data]

def load_classrooms(file_path):
    data = load_json(file_path)
    return [Classroom(**item) for item in data]