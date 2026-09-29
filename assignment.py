import random
def main():
    # Randomly choose an operation from this tuple for each question
    math_operations = ("add", "subtract", "multiply")

    # Your code begins here
    num_questions = random.randint(1, 5)
    correct = 0

    print("Welcome to the Random Math Quiz!")
    print(f"You will be asked {num_questions} questions")

    for i in range(num_questions):
        operation = random.choice(math_operations)

        if operation == "add":
            x = random.randint(1, 99)
            y = random.randint(1, 99)
            answer = x + y
            symbol = "+"

        elif operation == "subtract":
            x = random.randint(1, 99)
            y = random.randint(1, 99)
            answer = x - y
            symbol = "-"

        else:
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            answer = x * y
            symbol = "*"

        user_answer = int(input(f"\nWhat is {x} {symbol} {y}? "))

        if user_answer == answer:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The answer was {answer}")

    print(f"\nYou got {correct}/{num_questions} correct.")

    # Your code begins here


if __name__ == "__main__":
    main()
