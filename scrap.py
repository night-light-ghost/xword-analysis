# this to serve as where code is to be gathered


class Counter(dict):
    def __missing__(self, key):
        return 0

frequencies = Counter()

for word in words:
    for c in word:
        if frequencies[c]==0:
            frequencies[c] += 1
        else:
            frequencies[c] = frequencies[c] + 1

print("frequencies: ")
print(frequencies)

weightedWords = {}

for word in words:
    weight = 0
    use = 0
    for c in word:
        weight += frequencies[c]
    use = weight / len(word)
    weightedWords[use] = word

usefulWords = sorted(weightedWords.items(), reverse=True)
print("weightedWords: ")
print(usefulWords)


