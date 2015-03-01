def is_pal(word):
    return word == word[::-1]

words = 'I want a robot racecar'.split()

for (w,p) in zip(words, map(is_pal, words)):
    print repr(w) + ':', p
