WORDS_FILE = "words.txt"

side_length: int = 3
side_count: int = 4
sides = [[0] * side_length for _ in range(side_count)]

if False:
    for i, side in enumerate(sides):
        for j, letter in enumerate(side):
            sides[i][j] = input(f"Letter for side {i + 1}, letter {j + 1}: ").lower()

sides = [['l', 'e', 's'], ['u', 'm', 'i'], ['b', 'j', 'r'], ['c', 'o', 't']]
alphabet = "".join(char for side in sides for char in side)

words0 = []

with open(WORDS_FILE) as file:
    for line in file:
        if not line[0] == "#":
            words0.append(line.rstrip().lower())

print("Initial word list length:", len(words0))

# Filter 1: all words must be at least 3 letters long
words1 = []

for word in words0:
    if len(word) >= 3:
        words1.append(word)

print("Filter #1:", len(words1))

# Filter 2: cull all words that have impossible 2-letter sequences
words2 = []

for word in words1:
    eligible: bool = True
    for i in range(len(word) - 1):
        if not eligible:
            break
        sequence = word[i:i + 2]
        for side in sides:
            if sequence[0] in side and sequence[1] in side:
                eligible = False
                break
    if eligible:
        words2.append(word)

print("Filter #2:", len(words2))

# Filter 3: All words have to be comprised solely of letters present in the puzzle
words3 = []

for word in words2:
    eligible = True
    for letter in word:
        if letter not in alphabet:
            eligible = False
            break
    if eligible:
        words3.append(word)

print("Filter #3:", len(words3))

buckets = [[] for _ in range(12)]

max_unique_char_count = 0
max_bucket = []
for word in words3:
    count = len(set(word))
    buckets[count - 1].append(word)
    if count == max_unique_char_count:
        max_bucket.append(word)
    elif count > max_unique_char_count:
        max_unique_char_count = count
        max_bucket.clear()
        max_bucket.append(word)

buckets.reverse()

print("Found", len(max_bucket), "maximally unique word(s)")

i = 1
for bucket in buckets[0:6]: # Resolves fast if you only want the first answer
    # print(bucket)
    for starter in bucket: # definitely not O(N), more like O(7ish) if you just want the first occurrence
        for word in words3: # O(N = 2000ish)
            i += 1
            if len(set("".join(starter).join(word))) == len(alphabet):
                if starter[-1] == word[0]:
                    print(i, starter, word)
                elif starter[0] == word[-1]:
                    print(i, word, starter)

print("Ran", i, "final brute-force checks")