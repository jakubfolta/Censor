def replaceCensoredWord(text, word):
  splittedText = text.split()
  for index, each in enumerate(splittedText):
    if each == word:
      splittedText[index] = len(word) * '*'
  return ' '.join(splittedText)

print(censor('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))

