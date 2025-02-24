def get_student_score():
    """
    Handles user input to obtain the student's score.
    
    Returns:
        float: The numerical score entered by the user.
    """
    # Prompt the user to enter their score
    score_input = input("Please enter your score: ")

    try:
        # Convert the input to a float
        score = float(score_input)
        return score

    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numerical score.")
        return get_student_score()  # Recursive call to ask for input again

def calculate_grade(score):
    """
    Determines the letter grade based on the given score and grading scale.
    
    Parameters:
        score (float): The score to evaluate.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    # Determine the letter grade based on the score
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

# Main program flow
if __name__ == "__main__":
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your grade is: {grade}")