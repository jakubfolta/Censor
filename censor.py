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
  for index in range(len(splittedText)):
    print(index)
    if index == word:
      print(index)
      splittedText[index] = censoredWord
  return ' '.join(splittedText)

print(censor('abece dede sksi dede', 'dede'))
    

