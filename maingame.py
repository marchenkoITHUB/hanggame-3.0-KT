from gamemodule import *

loadWordsFromFile()

while hasWords():
    word = getNextWord()
    desc = getWordDescription(word)
    letters = initEmptyString()
    mistakes = initZero()

    showMessage(msgs[kStart].format(getDisplayWord(word, letters)))

    while not isWordGuessed(word, letters) and not isGameOver(mistakes):
        showMessage(msgs[kHint].format(desc))
        letters, mistakes = processGuess(word, letters, mistakes)
        drawPhase(mistakes)
        showMessage(getDisplayWord(word, letters))

    if isWordGuessed(word, letters):
        showMessage(msgs[kVic].format(word))
    else:
        showMessage(msgs[kDefeat].format(word))


    if not hasWords():
      showMessage(msgs[kCongrat])
      break

    if not checkContinue():
      showMessage(msgs[kGiveUp])
      break