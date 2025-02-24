def get_student_score():
    """
    Handles user input to obtain the student's score.
    Prompts the user to enter their score and returns it as a numerical type.
    """

    while True:
        try:
            score = float(input("Please enter your score: "))
            return score
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score):
    """
    Determines the letter grade based on the given score and grading scale.
    
    Parameters:
    score (numeric): The score to evaluate.

    Returns:
    str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
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
    """
    Main program flow to get the student's score and calculate the grade.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your grade is: {grade}")

if __name__ == "__main__":
    main()
