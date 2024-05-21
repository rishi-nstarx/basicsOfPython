# def reverse_words_and_characters(input_string):
#     # Split the string into words
#     words = input_string.split()

#     # Reverse the words and characters of each word
#     reversed_words = [word[::-1] for word in words[::-1]]

#     # Join the reversed words to form the final string
#     reversed_string = ' '.join(reversed_words)

#     return reversed_string

# # Test the function
# input_string = "Hello world! This is a test."
# reversed_string = reverse_words_and_characters(input_string)
# print("Reversed string:", reversed_string)
word ="\"Hello world! This is a test.\""
rev=""
for i in word[::-1]:
    rev=rev+i
print(rev)