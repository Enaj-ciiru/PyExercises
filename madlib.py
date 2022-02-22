# creating madlib using variables
copycolor = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are", copycolor)
print(pluralNoun + " are blue")
print("I love", celebrity)

# another way of creating madlib using for while

data = "a ADJECTIVE NOUN VERB ADVERB to the NOUN to VERB some NOUN"
for part_of_speech in ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]:
    while data.find(part_of_speech) > -1:
        data = data.replace(part_of_speech, input("enter a %s: " % (part_of_speech.lower())), 1)

print(data)