def process_scores(students):
    """
    Calculates average score for each student.
    Returns a dictionary {name: average_score}
    """
    averages = {}

    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages


def classify_grades(averages):
    """
    Assigns letter grades based on average score.
    Returns a dictionary {name: (average, grade)}
    """
    # Grade thresholds (local variables only)
    grade_a = 90
    grade_b = 75
    grade_c = 60

    classified = {}

    for name, avg in averages.items():
        if avg >= grade_a:
            grade = "A"
        elif avg >= grade_b:
            grade = "B"
        elif avg >= grade_c:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


def generate_report(classified, passing_avg=70):
    """
    Prints formatted student report.
    Returns number of students who passed.
    """
    passed = 0
    failed = 0

    print("===== Student Grade Report =====")

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(f"{name:<9} | Avg: {avg:<6} | Grade: {grade} | Status: {status}")

    print("================================")
    print(f"Total Students : {len(classified)}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


# -------- Main Block --------
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 84, 86],
        "Bob": [60, 65, 63, 62],
        "Clara": [95, 97, 96, 97]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)