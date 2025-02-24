def get_student_score():
    Handles user input to obtain the student's score.
    
    Returns:
        float: The numerical score entered by the user.

    while True:
        try:
            score = float(input("Please enter the student's score: "))
            if score < 0:
                print("Score cannot be negative. Please enter a valid score.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score):

    Determines the letter grade based on the given score and grading scale.
    
    Parameters:
        score (float): The numerical score.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').

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

    Main program flow to obtain the student's score and calculate the grade.

    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The calculated grade is: {grade}")

if __name__ == "__main__":
    main()