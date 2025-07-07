
class Course:
    def __init__(self, code, name, units, allowed_times, professor):
        self.code = code                  # کد درس (AI101)
        self.name = name                  # نام درس (هوش مصنوعی)
        self.units = units                # تعداد واحد
        self.allowed_times = allowed_times  # زمان‌های مجاز
        self.professor_code = professor  # کد استاد مرتبط

    def __str__(self):
        return f"{self.code} - {self.name} ({self.units} unit)"


class Professor:
    def __init__(self, code, name, available_times, courses):
        self.code = code                  # کد استاد (P1)
        self.name = name                  # نام استاد
        self.available_times = available_times  # زمان‌های دردسترس
        self.courses = courses            # لیست کد دروس

    def __str__(self):
        return f"{self.name} ({self.code})"


class Classroom:
    def __init__(self, code, capacity):
        self.code = code                  # کد کلاس (C101)
        self.capacity = capacity          # ظرفیت کلاس

    def __str__(self):
        return f"{self.code} (capacity: {self.capacity})"