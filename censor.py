def censor(text, word):
  asterisksWord = len(word) * '*'
  return text.replace(word, asterisksWord)

print(censor('abece dede sksi dede', 'dede'))

