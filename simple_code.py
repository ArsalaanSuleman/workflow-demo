# simple_code.py
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

# Main script execution
if __name__ == "__main__":
    print(f"Name: {name}")
    print(f"Work: {work}")
    print(f"Numbers: {numbers}")

    # Call the greet_user function
    print(greet_user("Developer"))

    # Calculate the sum of numbers
    total = calculate_sum(numbers)
    print(f"Total of numbers: {total}")

    # Generate and display a message based on the total
    print(generate_message(total))
