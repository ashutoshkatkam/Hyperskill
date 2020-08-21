import random
print("H A N G M A N")
while 1 != 0 :
     game = input('Type "play" to play the game, "exit" to quit:')
     if game == "play" or game == "quit":
         break
if game == "play":
    print()
    words = ('python', 'java', 'kotlin', 'javascript')
    word = random.choice(words)
    guessword = '-'*len(word)
    counter = 0
    lettersused = []
    while counter < 8:
        print(guessword)
        letter = input("Input a letter: ")
        if letter in lettersused :
            print("You already typed this letter")
        if letter.islower() == False:
            print("It is not an ASCII lowercase letter")
        if len(letter) > 1 or len(letter) == 0:
            print("You should input a single letter")
        for i in range(0,len(word)):
            if letter == word[i]:
                guessword = guessword[:i] + letter + guessword[i+1:]
        if guessword == word:
            print("You guessed the word!")
            print("You survived!")
            break
        pos = word.find(letter)
        if pos < 0 and letter.islower() == True and len(letter) == 1 and letter not in lettersused:
            print("No such letter in the word")
            counter = counter + 1
        if counter == 8 and guessword != word :
            print("You are hanged!")
            break
        lettersused.append(letter)
        print()
