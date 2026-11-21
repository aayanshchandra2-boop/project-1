secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()
while count < max_attempts and guess != secret:
    guess = int(input("Enter your guess: "))
    count += 1
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret} in {count} attempts.")
if guess != secret:
      print(f"Game over! The secret number was {secret}.")