def replaceCensoredWord(text, censoredWord):
    asterisksWord = len(censoredWord) * '*'
    return text.replace(censoredWord, asterisksWord)

print(replaceCensoredWord('abece dede sksi dede', 'dede'))
