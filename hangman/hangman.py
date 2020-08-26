import random


def start_game():
    random.seed()
    word_list = ['python', 'java', 'kotlin', 'javascript']

    computer_choose = word_list[random.randint(0, 3)]
    secret_word = list('-' * len(computer_choose))
    repeating_letters = {}
    lives = 8

    while lives > 0:
        letter = input("{}\nInput a letter:".format("".join(secret_word)))
        if letter in set(computer_choose) and letter not in repeating_letters:
            repeating_letters.update({letter: computer_choose.index(letter)})
            secret_word[computer_choose.index(letter)] = letter
            index_of_next_letter = computer_choose.find(letter, int(computer_choose.index(letter)) + 1)
            while index_of_next_letter != -1:
                secret_word[index_of_next_letter] = letter
                if index_of_next_letter == len(computer_choose):
                    break
                else:
                    index_of_next_letter = computer_choose.find(letter, index_of_next_letter + 1)
        elif letter in set(secret_word) and letter != '-':
            print("You already typed this letter")
        elif letter not in computer_choose:
            if letter.isascii() and letter.islower() and len(letter) == 1:
                if letter in repeating_letters.keys():
                    print("You already typed this letter")
                else:
                    repeating_letters.update({letter: -1})
                    if lives == 1:
                        return print("No such letter in the word\nYou are hanged!")
                    else:
                        lives -= 1
                        print("No such letter in the word")
            elif len(letter) > 1:
                print("You should input a single letter")
            else:
                print("It is not an ASCII lowercase letter")


        if secret_word == list(computer_choose):
            return print("You guessed the word!\nYou survived!")

        print()

print('H A N G M A N')

while True:
    USER_CHOOSE = input('Type "play" to play the game, "exit" to quit:')
    if USER_CHOOSE == 'play':
        print()
        start_game()
    elif USER_CHOOSE == 'exit':
        exit()
    else:
        continue
