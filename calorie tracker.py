# ============================================================
# Name: Kirtika Khowal
# Date: 7th November 2025
# Project: Building a Calorie Tracking Console App
# ============================================================

import datetime

print("==========================================")
print("Welcome to Daily Calorie Tracker")
print("==========================================")
print("This tool helps you log meals and calories,")
print("compare with your daily calorie limit, and")
print("optionally save the session as a report.\n")

meal_names = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal = input(f"\nEnter meal #{i+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calories.append(cal)

total_cal = sum(calories)
avg_cal = total_cal / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

if total_cal > daily_limit:
    status_msg = "Warning: You have exceeded your daily calorie limit!"
else:
    status_msg = "Great job! You're within your daily calorie goal."

print("\n\n========== Calorie Summary ==========")
print(f"{'Meal Name':<15}{'Calories'}")
print("----------------------------------")

for meal, cal in zip(meal_names, calories):
    print(f"{meal:<15}{cal:.2f}")

print("----------------------------------")
print(f"{'Total:':<15}{total_cal:.2f}")
print(f"{'Average:':<15}{avg_cal:.2f}")
print("----------------------------------")
print(status_msg)
print("==================================\n")

save = input("Do you want to save this session? (yes/no): ").strip().lower()

if save == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w") as file:
        file.write("===== Daily Calorie Tracker Log =====\n")
        file.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        file.write(f"{'Meal Name':<15}{'Calories'}\n")
        file.write("----------------------------------\n")
        for meal, cal in zip(meal_names, calories):
            file.write(f"{meal:<15}{cal:.2f}\n")
        file.write("----------------------------------\n")
        file.write(f"{'Total:':<15}{total_cal:.2f}\n")
        file.write(f"{'Average:':<15}{avg_cal:.2f}\n")
        file.write("----------------------------------\n")
        file.write(status_msg + "\n")
        file.write("==================================\n")

    print(f"\n📄 Session saved successfully as '{filename}'")
else:
    print("\nSession not saved. Goodbye!")


 