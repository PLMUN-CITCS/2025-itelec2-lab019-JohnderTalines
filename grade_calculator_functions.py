def get_student_score():
    """
    Prompts the user to enter their score and returns it as a numerical type.
    """
    while True:
        try:
            score = input("Please enter your score: ")
            # Convert input to float, which can handle both integer and decimal scores
            score = float(score)
            if score < 0 or score > 100:
                print("Score must be between 0 and 100. Please try again.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a numerical score.")

def calculate_grade(score):
    """
    Determines the letter grade based on the given score.
    
    Parameters:
    score (numeric): The score to evaluate.
    
    Returns:
    string: The corresponding letter grade.
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

# Run the main program
if __name__ == "__main__":
    main()