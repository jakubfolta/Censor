def censor(text, censored):
    return text.replace(censored, len(censored) * '*')

print(censor('sadsad kala abhdhd ufhdjw kala fdsf kala', 'kala'))

def censor(text, censor_word):
    censor = len(censor_word) * '*'
    text = text.split()

    for index, x in enumerate(text):
        if x == censor_word:
            text[index] = censor
    return ' '.join(text)

print(censor('sadsad kala abhdhd ufhdjw kala fdsf kala', 'kala'))

def censor(text, censor_word):
    censor = len(censor_word) * '*'
    text = text.split()

    for x in text:
        text[text.index(x)] = censor if x == censor_word else text[text.index(x)] = x
        # if x == censor_word:
        #     text[text.index(x)] = censor
    return ' '.join(text)

print(censor('sadsad kala abhdhd ufhdjw kala fdsf kala', 'kala'))
