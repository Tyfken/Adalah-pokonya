# QUIZ_TITLE: Customizable title for the quiz
# This is displayed at the start of the quiz
QUIZ_TITLE = "Welcome to My Quiz!"

# QUIZ_DESCRIPTION: A description of the quiz to motivate the user
# This text is shown before the quiz begins to explain what the quiz is about
QUIZ_DESCRIPTION = "Test your general knowledge with this simple yes/no quiz. Do your best!"

# COUNTDOWN_TIMER: Customizable countdown time in seconds before the quiz starts
# Set to 0 to skip the countdown, or set any positive number for a countdown
# Example: 5 means there will be a 5-second countdown before the quiz begins
COUNTDOWN_TIMER = 5

# QUESTIONS: This is a list that stores all quiz questions as tuples
# Each tuple contains two elements:
#   - First element (string): The question text to be asked
#   - Second element (boolean): The correct answer (True for "yes", False for "no")
# This structure makes it easy to add or remove questions by editing this list
QUESTIONS = [
    # Question 1: "Is the sky blue?" - The correct answer is True (yes)
    ("Is the sky blue?", True),   
    # Question 2: "Do fish live on land?" - The correct answer is False (no)
    ("Do fish live on land?", False),
]


# Import the time module to add countdown functionality
import time


# Function: countdown
# Purpose: Displays a customizable countdown timer on the screen
# Parameters:
#   - seconds (int): The number of seconds to count down from
# This function displays each second and creates anticipation before the quiz begins
def countdown(seconds: int):
    # Check if countdown is enabled (seconds > 0)
    if seconds <= 0:
        # If countdown is disabled, return immediately without counting down
        return
    
    # Print a message to alert the user that countdown is starting
    print(f"\nStarting in {seconds} seconds...\n")
    # Loop from the specified number of seconds down to 1
    for i in range(seconds, 0, -1):
        # Display the current countdown number
        print(f"{i}...", end=" ", flush=True)
        # Wait for 1 second before showing the next number
        time.sleep(1)
    
    # After countdown finishes, print "Go!" to signal the start of the quiz
    print("Go!\n")


# Function: ask_yes_no
# Purpose: Prompts the user for a yes/no answer and validates their input
# Parameters:
#   - prompt (str): The question text to display to the user
# Return value: bool
#   - Returns True if user answers "yes" or "y"
#   - Returns False if user answers "no" or "n"
# Special features:
#   - Uses a while loop to keep asking until a valid answer is provided
#   - Converts input to lowercase to handle both uppercase and lowercase answers
#   - Strips whitespace from the input to handle accidental spaces
def ask_yes_no(prompt: str) -> bool:
    # Loop indefinitely until a valid answer is received
    while True:
        # Display the prompt and get user input, then clean it up (remove spaces and convert to lowercase)
        ans = input(f"{prompt} (yes/no): ").strip().lower()
        # Check if user entered "yes" or "y" (abbreviated form of yes)
        if ans in ("yes", "y"):
            # Return True to indicate user answered "yes"
            return True
        # Check if user entered "no" or "n" (abbreviated form of no)
        if ans in ("no", "n"):
            # Return False to indicate user answered "no"
            return False
        # If the input is not a valid answer, show error message and loop again
        print("Please answer 'yes' or 'no'.")



# Function: run_quiz
# Purpose: Main quiz runner that displays questions, gets user answers, and calculates the final score
# This function orchestrates the entire quiz experience, including title, description, and countdown
def run_quiz():
    # Display the quiz title to the user
    print(f"\n{'='*50}")
    print(f"{QUIZ_TITLE.center(50)}")
    print(f"{'='*50}\n")
    
    # Display the quiz description to help the user understand what they're about to do
    print(f"Description: {QUIZ_DESCRIPTION}\n")
    
    # Start the countdown timer (customizable via COUNTDOWN_TIMER variable)
    # If COUNTDOWN_TIMER is 0, countdown will be skipped
    countdown(COUNTDOWN_TIMER)
    
    # First, check if there are any questions in the QUESTIONS list
    if not QUESTIONS:
        # If the QUESTIONS list is empty, inform the user
        print("No questions found. Edit the QUESTIONS list in this file to add quizzes.")
        # Exit the function early since there's nothing to quiz
        return

    # Initialize the score counter to 0 (user starts with no correct answers)
    score = 0
    # Get the total number of questions by checking the length of the QUESTIONS list
    total = len(QUESTIONS)

    # Loop through each question in the QUESTIONS list
    # enumerate() provides both the index (idx) and the item (a tuple of question and answer)
    # start=1 makes the numbering start from 1 instead of 0 (more user-friendly)
    for idx, item in enumerate(QUESTIONS, start=1):
        # Try to unpack the question and answer from the item tuple
        try:
            # Extract the question text and the correct answer from the tuple
            question_text, yes_is_correct = item
        # If something goes wrong with unpacking (invalid format), catch the error
        except Exception:
            # Notify the user that this question will be skipped
            print(f"Skipping invalid question entry at position {idx}: {item}")
            # Continue to the next question in the loop
            continue

        # Create a question prefix with the question number, but only if there are multiple questions
        # Example: "Q1. " for first question if there are 2+ questions
        # If only 1 question, no prefix is added
        prefix = f"Q{idx}. " if total > 1 else ""
        # Display the question with its prefix to the user
        print(f"{prefix}{question_text}")
        # Call ask_yes_no() to get the user's answer (True for yes, False for no)
        user_says_yes = ask_yes_no("Your answer")

        # Compare the user's answer with the correct answer
        if user_says_yes == bool(yes_is_correct):
            # If the answer is correct, display success message
            print("Correct!\n")
            # Increment the score by 1 since the user got this question right
            score += 1
        else:
            # If the answer is incorrect, display failure message
            print("Incorrect.\n")

    # After all questions have been asked, display the final score
    # Shows format like "Final score: 2/3" (got 2 out of 3 correct)
    print(f"Final score: {score}/{total}")
    print(f"{'='*50}\n")



# This is the main entry point of the script
# "__name__ == '__main__'" is a Python convention that checks if this file is being run directly
# (as opposed to being imported as a module in another file)
# If the file is run directly, the code inside this block will execute
if __name__ == "__main__":
    # Call the run_quiz() function to start the quiz
    run_quiz()

