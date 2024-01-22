# Write a program to find how many times substring “Emma” appears in the given string.

# pseudo code

# Make a variable to contain a sentence
# Change the sentence if you want to test it more
given_sentence = ("Emma is a great person. She cooks for us in the morning that's why I always " 
                "look forward to meeting Emma in the morning. Emma is my very loving and caring mother.")

# Use count function to count the number of times "Emma" appeared in the sentence
emma_counter = given_sentence.count("Emma")

# print how many times
print(f'The word "Emma" appeared', emma_counter,'times in the sentence')