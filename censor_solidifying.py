def censor(text, censored):
    return text.replace(censored, len(censored) * '*')

print(censor('sadsad kala abhdhd ufhdjw kala fdsf kala', 'kala'))
