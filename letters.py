

# By: Carlos Tivan

# Create a set of the vowels
letters = {'a', 'e', 'i', 'o', 'u'}

# Create a dictionary to store the count of each vowel
count = {}.fromkeys(letters, 0)

# Promt the user to enter a word and convert it to lowercase
word = input("Enter a word: ").lower()
# Initialize a varaible to store the total number of vowels
total = 0
# Iterate over the word to store the total number of vowels
for words in word:
    if words in letters:
        count[words] += 1
        total += 1
# Iterate over the dictionary and print the count for each vowel
for letter in count:
    print(f"The letter {letter} is appear : {count[letter]}")

# Print the total number of vowels
print(f"The total of vocals is: {total}")
