
"""
Title: Gradebook Analyzer
Author: <Your Name>
Date: 2025-11-23
Description: CLI tool for entering/loading student marks, analyzing statistics,
assigning grades, and displaying results.
"""

import csv
import statistics


def print_welcome():
    print("\n===== Gradebook Analyzer =====")
    print("1. Manual data entry")
    print("2. Import from CSV file")
    print("3. Exit")


def manual_entry():
    marks = {}
    print("\nEnter student data (type 'done' to finish):")
    while True:
        name = input("Student name: ")
        if name.lower() == "done":
            break
        try:
            score = float(input(f"Marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("Invalid marks. Try again.")
    return marks


def csv_entry():
    marks = {}
    file_path = input("Enter CSV file path: ")
    try:
        with open(file_path, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    name, score = row[0], row[1]
                    try:
                        marks[name] = float(score)
                    except ValueError:
                        pass
    except FileNotFoundError:
        print("File not found.")
    return marks


def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0


def calculate_median(marks_dict):
    return statistics.median(marks_dict.values()) if marks_dict else 0


def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else 0


def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else 0


def assign_grades(marks_dict):
    grades = {}
    for student, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[student] = grade
    return grades


def grade_distribution(grades):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades.values():
        if g in dist:
            dist[g] += 1
    return dist


def pass_fail_lists(marks_dict):
    passed = [s for s, m in marks_dict.items() if m >= 40]
    failed = [s for s, m in marks_dict.items() if m < 40]
    return passed, failed


def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("--------------------------------------------")
    for name, mark in marks.items():
        print(f"{name}\t\t{mark}\t{grades[name]}")


def run_analysis(marks):
    if not marks:
        print("No data available.")
        return

    avg = calculate_average(marks)
    med = calculate_median(marks)
    max_s = find_max_score(marks)
    min_s = find_min_score(marks)

    print(f"\nAverage Marks: {avg}")
    print(f"Median Marks: {med}")
    print(f"Highest Score: {max_s}")
    print(f"Lowest Score: {min_s}")

    grades = assign_grades(marks)
    dist = grade_distribution(grades)
    print("\nGrade Distribution:")
    for g, c in dist.items():
        print(f"{g}: {c}")

    passed, failed = pass_fail_lists(marks)
    print(f"\nPassed ({len(passed)}): {passed}")
    print(f"Failed ({len(failed)}): {failed}")

    print_table(marks, grades)


def main():
    while True:
        print_welcome()
        choice = input("Enter choice: ")

        if choice == "1":
            marks = manual_entry()
            run_analysis(marks)
        elif choice == "2":
            marks = csv_entry()
            run_analysis(marks)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()
