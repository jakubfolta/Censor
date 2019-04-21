def censor(text, censored):
    return text.replace(censored, len(censored) * '*')

print(censor('sadsad kala abhdhd ufhdjw kala fdsf kala', 'kala'))

def censor(text, censor_word):
    censor = len(censor_word) * '*'
    text = text.split()

    for index, x in enumerate(text):
        if x == censor_word:
            text[index] = censor
            print(text)
        #text[x] = censor if x == censor_word else text[x] = x
print(censor('sadsad kala abhdhd ufhdjw kala fdsf kala', 'kala'))
