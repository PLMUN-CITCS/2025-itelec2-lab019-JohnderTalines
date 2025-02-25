def get_student_score():
    score = input("Please enter your score: ")

    try:
        score = float(score)
        return score
    except ValueError:
        print("Invalid input! Please enter a numerical score.")
        return get_student_score()  # Recurse to prompt the user again

def calculate_grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    score = get_student_score()
    grade = calculate_grade(score)
    	print(f"The grade for a score of {score} is: {grade}")
main()

