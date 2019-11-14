phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Alice'])
phonebook_dict.update(Kareem = "938-489-1234")
phonebook_dict.pop("Alice", False)
print(phonebook_dict)
for key, value in phonebook_dict.items():
    print(key + "'s number is " + value)

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit["name"])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][0]['interests'][1])

def letter_histogram(sentence): #takes a string, and returns a dictionary with letters for keys and tallies for values
    histogram = {}
    for letter in sentence:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram.update({letter : 1})
    return histogram

print(letter_histogram("banana"))


# word_histogram mk1
# def word_histogram(sentence):
#     histogram = {}
#     word = ""
#     start=0
#     end=0
#     sentence = (" " + sentence + " ").lower()
    
#     for i in range(len(sentence)):
#         if  sentence[i] == " ":
#             start = i+1
#             end = sentence.find(' ', i+1)
#             word = sentence[start:end]
#             if word in histogram:
#                 histogram[word] += 1
#             else:
#                 histogram.update({word : 1})
#     histogram.pop('', False)
#     return histogram

#word_histogram mk2
def word_histogram(sentence):
    histogram = {}
    for word in sentence.lower().split(" "):
        if word in histogram:
            histogram[word] += 1
        else:
            histogram.update({word : 1})
    histogram.pop('', False)
    return histogram

print(word_histogram("To  be or not to be"))

def top_three(histogram):
    one = (0, '')
    two = (0, '')
    three = (0, '')
    for key, value in histogram.items():
        if value > one[0]:
            two = one
            one = (value, key)
        elif value > two[0]:
            three = two
            two = (value, key)
        elif value > three[0]:
            three = (value, key)
    print("The top three words are: ")
    print(f"{one[1]} : {one[0]}")
    print(f"{two[1]} : {two[0]}")
    print(f"{three[1]} : {three[0]}")

top_three(word_histogram("To  be or not to be do be do be"))