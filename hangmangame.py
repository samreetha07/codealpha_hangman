import random

# Step 1: Word list
words = ["apple", "train", "robot", "pizza", "magic"]
word_to_guess = random.choice(words)

# Step 2: Initialize game variables
guessed_letters = []
tries = 6
display_word = ["_" for _ in word_to_guess]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", tries, "incorrect guesses. Let's begin!\n")

# Step 3: Main game loop
while tries > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try again!\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"❌ Wrong guess. You have {tries} tries left.\n")

# Step 4: Game result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("💀 Game Over! The word was:", word_to_guess)
