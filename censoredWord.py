def replaceCensoredWord(text, word):
  splittedText = text.split()
  for index, each in enumerate(splittedText):
    if each == word:
      splittedText[index] = len(word) * '*'
  return ' '.join(splittedText)

print(replaceCensoredWord('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))


def replaceCensoredWord(text, word):
  copyText = list(text)
  print(copyText)
  for x in text:
    if x == word:
      x = len(word) * ('*')
  return text

print(replaceCensoredWord('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))
