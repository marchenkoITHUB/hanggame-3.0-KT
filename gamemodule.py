# Данный проект включает в себя файлы:
# phase1.txt - phase5.txt для отображения текущего состояния висельницы
# words.txt словарь для хранения слов в формате "слово": "подсказка"

import random

kStart = "start"
kVic = "victory"
kHint = "hint"
kInput = "input"
kNext = "next"
kCorrect = "correct"
kWrong = "wrong"
kDefeat = "defeat"
kYes = "yes"
kCongrat = "congrat"
kGiveUp = "giveUp"

msgs = {
    kStart: "Загаданное слово: {}",
    kVic: "Победа! Вы угадали слово: {}",
    kHint: "Подсказка: {}",
    kCongrat: "Слова закончились! Поздравляем!",
    kGiveUp: "Выход из игры...",
    kInput: "Буква или слово: ",
    kNext: "Еще слово? (+): ",
    kYes: "+",
    kCorrect: "Есть такая буква!",
    kWrong: "Промах!",
    kDefeat: "Поражение! Это было слово: {}"
}

gameWords = {}
allWords = []

def loadWordsFromFile() -> None:

    f = open('words.txt', 'r', encoding='utf-8')

    line = f.readline()
    while line:

        if line.find(':') != -1:
            parts = line.split(':')

            word = parts[0].replace("'", "").replace('"', "").strip()
            desc = parts[1].replace("'", "").replace('"', "").strip()

            gameWords[word] = desc
            allWords.append(word)

        line = f.readline()
    f.close()

def getAnswer(prompt: str) -> str:
    return input(prompt)

def showMessage(text: str) -> None:
    print(text)

def hasWords() -> bool:
    return len(allWords) > 0

def getNextWord() -> str:
    return allWords.pop(random.randint(0, len(allWords) - 1))

def getWordDescription(word: str) -> str:
    return gameWords[word]

def getDisplayWord(word: str, letters: str) -> str:
    result = []
    i = 0
    while i < len(word):
        char = word[i]
        if letters.find(char) != -1:
            result.append(char)
        else:
            result.append("*")
        i += 1
    return " ".join(result)

def isWordGuessed(word: str, letters: str) -> bool:
    return getDisplayWord(word, letters).find("*") == -1

def isGameOver(mistakes: int) -> bool:
    return mistakes == 5

def drawPhase(mistakes: int) -> None:

    if mistakes == 0:
        return

    filename = f'phase{mistakes}.txt'
    f = open(filename, 'r', encoding='utf-8')
    showMessage(f.read())
    f.close()

def processGuess(word: str, letters: str, mistakes: int) -> tuple[str, int]:
    guess = getAnswer(msgs[kInput])

    if guess == word:
        return letters + word, mistakes
    elif len(guess) == 1 and word.find(guess) != -1:
        showMessage(msgs[kCorrect])
        return letters + guess, mistakes
    else:
        showMessage(msgs[kWrong])
        return letters, mistakes + 1

def checkContinue() -> bool:
  return getAnswer(msgs[kNext]) == msgs[kYes]

def initEmptyString() -> str:
  return str()

def initZero() -> int:
  return 0
