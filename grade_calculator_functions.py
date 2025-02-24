def get_student_score():
    """
    Handles user input to obtain the student's score.
    Prompts the user to enter their score and returns it as a numerical type.
    """
    while True:
        try:
            score = float(input("Please enter your score: "))  # Read input and convert to float
            return score  # Return the numerical score
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Handle non-numeric input

def calculate_grade(score):
    """
    Determines the letter grade based on the given score and grading scale.
    
    Parameters:
    score (numeric): The score to evaluate.

    Returns:
    str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'  # Grade A for scores 90 and above
    elif score >= 80:
        return 'B'  # Grade B for scores 80 to 89
    elif score >= 70:
        return 'C'  # Grade C for scores 70 to 79
    elif score >= 60:
        return 'D'  # Grade D for scores 60 to 69
    else:
        return 'F'  # Grade F for scores below 60

def main():
    """
    Main program flow to get the student's score and calculate the grade.
    """
    score = get_student_score()  # Call function to get the student's score
    grade = calculate_grade(score)  # Call function to calculate the grade
    print(f"Your grade is: {grade}")  # Display the calculated grade

if __name__ == "__main__":
    main()  # Execute the main function
