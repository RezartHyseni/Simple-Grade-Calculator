# Function to get a valid grade from the user
def get_grade(number):
    while True:
        try:
            grade = float(input(f"Enter grade {number} (0-10): "))
            if 0 <= grade <= 10:
                return grade
            else:
                print("Grade must be between 0 and 10.")
        except ValueError:
            print("Please enter a valid number.")

# Function to calculate the average
def calculate_average(g1, g2, g3):
    return (g1 + g2 + g3) / 3

# Function to evaluate the average
def evaluate_average(avg):
    if avg >= 8.5:
        return "Excellent"
    elif avg >= 7:
        return "Good"
    elif avg >= 5:
        return "Pass"
    else:
        return "Fail"

# Main function to run the program
def grade_calculator():
    print("Grade Average Calculator")
    grade1 = get_grade(1)
    grade2 = get_grade(2)
    grade3 = get_grade(3)
    
    average = calculate_average(grade1, grade2, grade3)
    evaluation = evaluate_average(average)
    
    print(f"\n - Your average is: {average:.2f}")
    print(f" - Evaluation: {evaluation}")

# Start the program
grade_calculator()