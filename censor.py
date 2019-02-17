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

def exchangeCensoredWord(text, word):
  for x in splitText(text):
    if x 
