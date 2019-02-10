def replaceCensoredWord(text, word):
  splittedText = text.split()
  for index, each in enumerate(splittedText):
    if each == word:
      splittedText[index] = len(word) * '*'
  return ' '.join(splittedText)

print(replaceCensoredWord('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))


def replaceCensoredWord(text, word):
  text = text.split()
  print(text)
  for index, x in enumerate(text):
    if x == word:
      text[index] = len(word) * ('*')
  return ' '.join(text)

print(replaceCensoredWord('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))
