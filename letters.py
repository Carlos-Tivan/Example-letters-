

# By: Carlos Tivan

letters = {'a', 'e', 'i', 'o', 'u'}

count = {}.fromkeys(letters, 0)

word = input("Enter a word: ").lower()

total = 0

for words in word:
    if words in letters:
        count[words] += 1
        total += 1

for letter in count:
    print(f"The letter {letter} is appear : {count[letter]}")

print(f"The total of vocals is: {total}")
