import matplotlib.pyplot as plt
import random

def plot_timetable(timetable, title="University Timetable"):
    """
    رسم نمودار زمان‌بندی
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    y_labels = []
    colors = {}

    for idx, gene in enumerate(timetable):
        course = gene["course"]
        time_slot = gene["time"]
        classroom = gene["classroom"]

        # تفکیک ساعت شروع و پایان
        day, hours = time_slot.split()
        start, end = map(int, hours.split('-'))

        # اختصاص رنگ به هر درس
        if course not in colors:
            colors[course] = (random.random(), random.random(), random.random())

        # محور y: کلاس‌ها
        y = idx
        y_labels.append(f"{course} ({classroom})")

        ax.barh(y, end - start, left=start, color=colors[course])

        # نوشتن روز
        ax.text(start, y, day, va='center', ha='right', fontsize=9, color="white")

    ax.set_yticks(range(len(y_labels)))
    ax.set_yticklabels(y_labels)
    ax.set_xlabel("Hour of Day")
    ax.set_title(title)

    plt.show()