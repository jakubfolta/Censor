def censor(text, word):
  asterisksWord = len(word) * '*'
  print(asterisksWord)
  return text.replace(word, asterisksWord)

print(censor('abece dede sksi dede', 'dede'))


def censor(text, word):
  splittedText = text.split()
  asterisksWord = len(word) * '*'
  for index, position in enumerate(splittedText):
    if position == word:
      splittedText[index] = asterisksWord
  return ' '.join(splittedText)

print(censor('abece dede sksi dede', 'dede'))


def censor(text, word):
  censoredWord = len(word) * '*'
  splittedText = text.split()
  print(splittedText)
  for index in range(len(splittedText)):
    if splittedText[index] == word:
      splittedText[index] = censoredWord
  return ' '.join(splittedText)

print(censor('abece dede sksi dede', 'dede'))


def replaceCensoredWord(text, word):
  return text.replace(word, len(word) * '*')

print(replaceCensoredWord('abece dede sksi fdsfr fdfds dede das dede dede', 'dede'))
    

def splitText(text):
  return text.split()

def joinSplittedText(text):
  return ' '.join(text)

def exchangeCensoredWord(text, word):
  splittedText = splitText(text)
  for index, x in enumerate(splittedText):
    if x == word:
      splittedText[index] = len(word) * '*'
  return joinSplittedText(splittedText)


print(exchangeCensoredWord('abece dede sksi fdsfr fdfds dede das dede dede', 'dede'))

