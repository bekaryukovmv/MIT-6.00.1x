# Игра "Виселица", выполненная в рамках курса 6.00.1х, русифицированная и доработанная мной.

# Мною были написаны следующие функции:
# 1. isWordGuessed()
# 2. getGuessedWord()
# 3. getAvailableLetters()
# 4. hangman()
# А также добавлена функция, поэтапно рисующая виселицу, в случае ошибки игрока: hang()


# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "game.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = True
    for char in secretWord:
        if char in lettersGuessed:
            continue
        else:
            flag = False
            break
    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    newWord = ''
    for char in secretWord:
        if char in lettersGuessed:
            newWord += char
        else:
            newWord += '_ '
    return newWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alp = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    for i in lettersGuessed:
        if i in alp:
            alp.remove(i)
    return ''.join(alp)


def hang(count):
  '''
  This function partial printed a hanged man when you miss.
  INPUT: count(int)
  OUTPUT part of strings in the list or all list when you loose.
  '''
  stages = [["Добро пожаловать на казнь!"], "_____     ", "|         ", "|    |    ", "|    0    ", "|   /|\   ", "|   / \   ", "|         "]
  if count == 1:
    return stages[0]
  return stages[1 : count]

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    count = 0
    print('Добро пожаловать на игру - Виселица!')
    print('Я загадал слово, состоящее из', len(secretWord), 'букв')
    while isWordGuessed(secretWord, lettersGuessed) == False and count < 8:
      print('-----------')
      print('У Вас осталось', 8 - count, 'попыток')
      print('Неназванные буквы:', getAvailableLetters(lettersGuessed))
      letter = input('Пожалуйста, назовите букву из списка: ').lower()
      if letter in lettersGuessed:
        print('Упс! Эту букву уже называли:', getGuessedWord(secretWord, lettersGuessed))
        print(*hang(count), sep="\n")
      elif letter in secretWord:
        lettersGuessed.append(letter)
        getAvailableLetters(lettersGuessed)
        print('Верно!', getGuessedWord(secretWord, lettersGuessed))
        print(*hang(count), sep="\n")
      else:
        count += 1
        lettersGuessed.append(letter)
        getAvailableLetters(lettersGuessed)
        print('Ой! Такой буквы нет в моём слове:', getGuessedWord(secretWord, lettersGuessed))
        print(*hang(count), sep="\n")
    if isWordGuessed(secretWord, lettersGuessed):
      print('-----------')
      print('Поздравляю! Вы выиграли!')
    else:
      print('-----------')
      print('Сожалею, но Вы проиграли!')
      print('Я загадывал слово:', secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)