
def get_employee_data():

    name = input("Enter employee name: ").strip()
    try:
        quality = int(input("Performance in Quality of Work (1-10): "))
        teamwork = int(input("Performance in Teamwork (1-10): "))
        punctuality = int(input("Performance in Punctuality (1-10): "))
    except ValueError:
        print("Please enter a number between 1 and 10.")
        return None

    if any(score < 1 or score > 10 for score in (quality, teamwork, punctuality)):
        print("Scores should be between 1 and 10 only.")
        return None

    return {
        'name': name,
        'scores': (quality, teamwork, punctuality)
    }



def calculate_average(scores: tuple) -> float:

    return sum(scores) / len(scores)


def evaluate_grade(avg_score: float) -> str:

    if avg_score >= 9:
        return "Outstanding"
    elif avg_score >= 7:
        return "Exceeds Expectations"
    elif avg_score >= 5:
        return "Meets Expectations"
    else:
        return "Needs Improvement"


def main():
    employees = []

    print("\n Employee Performance Management System \n")

    while True:
        record = get_employee_data()
        if record:
            avg = calculate_average(record['scores'])
            grade = evaluate_grade(avg)
            record['average'] = avg
            record['grade'] = grade
            employees.append(record)


        more = input("\nAdd another employee? (y/n): ").lower()
        if more != 'y':
            break


    print("\n Employees  Summary Report ")
    for employee in employees:
        print(f"{employee['name']} - Avg: {employee['average']:.2f} - Grade: {employee['grade']}")


    if employees:
        avg_all = sum(emp['average'] for emp in employees) / len(employees)
        best = max(employees, key=lambda x: x['average'])
        print(f"\nCompany Avg Score: {avg_all:.2f}")
        print(f"Top Performer: {best['name']} with Avg: {best['average']:.2f}")



if __name__ == "__main__":
    main()
