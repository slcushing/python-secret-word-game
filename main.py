import random

words = ["bubble", "bear", "socks", "leaves", "trail", "beers"]

word = random.choice(words) #random.choice to choose random word from list
wrong = [] #place to store wrong guesses

guessed = []
for i in range(len(word)): # range() returns IMMUTABLE sequence of #s between the given start integer to the stop integer - HERE using range(stop) meaning stoping at the word length
    guessed.append("_")
print(*[i for i in guessed]) # the * is for unpacking in the print function call

turns=7

while(turns):

    letter_guess = input("Guess a letter:")
    if(letter_guess in wrong):
        print("You already tried that")
        turns += 1

    if letter_guess in word:
        for i in range(len(word)):
            if word[i] == letter_guess:
                guessed[i] = word[i] 
    else:
        print("Nope")
        wrong.append(letter_guess)
        turns -= 1
    
    guess_word = [i for i in guessed]
    guess_word = "".join(guess_word)

    if word == guess_word:
        print("You guessed the word correctly!")
        break
    print(*([i for i in guessed])) # the * is for unpacking in function call
    print("You have", + turns, "guesses left")
    if turns == 0:
        if word != guessed:
            print("you lost,the word was", word)
            break

