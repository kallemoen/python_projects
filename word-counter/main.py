# [ ] Open file and remove every special character
# [ ] Split words into a list
# [ ] Cycle through each word creating a dict for each word and counting every time a word is mentioned
# [ ] Cycle through values filtering out top 10 words


# Creates a list of lists from txt file
# traffic_file = open('article.txt', 'r') # Do I need to close this?
# traffic_file = traffic_file.read()

traffic_file = "The invention that could end obesity a michigan surgeon invented an apparatus, that he believes tricks the brain into thinking the stomach is full his full sense device could be a lifesaver for millions of obese americans and, raises questions about how hunger - our most basic human impulse — even works."

special_characters = ["-", ".", ",", "–", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "“", '”']

# remove casing

traffic_file = str.lower(traffic_file)

# remove special special_characters
listed_string = list(traffic_file)

for char in listed_string:
    if char in special_characters:
        listed_string.remove(char)
    else:
        pass

traffic_file = "".join(listed_string)

print(traffic_file)
# traffic_file = list(traffic_file.split(" "))
#
# word_occurance_dict = {}
#
# for word in traffic_file:
#     if word not in word_occurance_dict:
#         word_occurance_dict[word] = 1
#     if word in word_occurance_dict:
#         word_occurance_dict[word] += 1
#     else:
#         pass
#
# print(word_occurance_dict)
