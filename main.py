import random

def main():
    number = random.randint(1, 100)
    attempts = 0

    try:
        while True:
            user_input = input("Enter your guess (1-100) or 'q' to quit: ").strip()
            if user_input.lower() == 'q':
                print(f"Goodbye! The number was {number}.")
                break

            try:
                guess = int(user_input)
            except ValueError:
                print("Please enter a valid integer between 1 and 100.")
                continue

            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1
            if guess < number:
                print("Too Low! Try again.")
            elif guess > number:
                print("Too High! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
                break
    except KeyboardInterrupt:
        print(f"\nGoodbye! The number was {number}.")

if __name__ == "__main__":
    main()