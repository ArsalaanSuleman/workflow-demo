import random
import time

# Initial data
name = "Workflow Demo"
work = "Automating Branch Push"
numbers = [1, 2, 3]


# Function to greet a user
def greet_user(name):
    return f"Hello, {name}! Welcome to the workflow demo."


# Function to calculate the sum of a list of numbers
def calculate_sum(numbers):
    return sum(numbers)


# Function to generate a message based on the sum
def generate_message(total):
    if total < 10:
        return "The total is small."
    elif 10 <= total <= 20:
        return "The total is moderate."
    else:
        return "The total is large."


# Function to double each number in a list
def double_numbers(numbers):
    return [number * 2 for number in numbers]


# New: Function to generate a random motivational quote
def get_motivational_quote():
    quotes = [
        "Keep pushing forward, no matter how tough it gets!",
        "Success is the sum of small efforts repeated daily.",
        "Believe in yourself, and the rest will fall into place.",
        "Every great developer you know started from scratch!",
        "Debugging is twice as hard as writing the code in the first place."
    ]
    return random.choice(quotes)


# New: Fun typing effect for display
def typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# New: Function to reverse the numbers in the list and display them
def reverse_numbers(numbers):
    return list(reversed(numbers))


# Main script execution
if __name__ == "__main__":
    # Greet the user with typing effect
    typing_effect(greet_user("Developer"))
    print(f"Name: {name}")
    print(f"Work: {work}")
    print(f"Numbers: {numbers}")

    # Calculate the sum of numbers
    total = calculate_sum(numbers)
    print(f"Total of numbers: {total}")
                        
    print(generate_message(total))

    # Double the numbers and display them
    doubled = double_numbers(numbers)
    print(f"Doubled numbers: {doubled}")

    # Display the numbers in reverse
    reversed_numbers = reverse_numbers(numbers)
    print(f"Reversed numbers: {reversed_numbers}")

    # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote())

    # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

     # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

     # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

     # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

        # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote())

    # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

     # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

     # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

     # Show a motivational quote
    print("\nMotivational Quote of the Day:")
    typing_effect(get_motivational_quote()) 

    # Function to generate a message based on the sum
def generate_message(total):
    if total < 10:
        return "The total is small."
    elif 10 <= total <= 20:
        return "The total is moderate."
    else:
        return "The total is large."
    
    # Function to generate a message based on the sum
def generate_message(total):
    if total < 10:
        return "The total is small."
    elif 10 <= total <= 20:
        return "The total is moderate."
    else:
        return "The total is large."