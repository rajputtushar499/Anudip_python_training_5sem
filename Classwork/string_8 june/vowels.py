#write a program to find out input a sentence and display the frequency of vowels which are present in given sentence ignoring the case of the characters
sentence = input("Enter a sentence: ")
vowel_count = 0
for char in sentence:
    if char in "aeiou":
        vowel_count += 1
print("Frequency of vowels in the sentence:", vowel_count)
