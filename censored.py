def censoredWord(text, word):
  censored = len(word) * '*'
  return text.replace(word, censored)

print(censoredWord('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))


def censor(text, word):
  splittedText = text.split()
  for index, each in enumerate(splittedText):
    if each == word:
      splittedText[index] = len(word) * '*'
  return ' '.join(splittedText)

print(censor('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))

def replaceCensoredWord(text, word):
  sameText = text.split()
  for index, x in enumerate(sameText):
    print(index)
    if x == word:
      sameText[index] = '*'
  return ' '.join(sameText)
    
  
print(replaceCensoredWord('abh dkkfir kala kvko keje kala fnjeribv kala', 'kala'))
  
























def replaceCensoredWord(text, word):
  censored = len(word) * '*'
  return text.replace(word, censored)

print(replaceCensoredWord('abh dkkfir kvko keje kaka fnjeribv kaka', 'kaka'))






  
