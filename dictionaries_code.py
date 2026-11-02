#dictionaries

my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"]= "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])

word = input("Please type in a word: ")
if word in my_dictionary:
    print("Translation: ",  my_dictionary[word])
else:
    print("Word not found in dictionary.")

results = {}
results["Mary"] = 2
results["Alice"] = 5
results["Tiana"]= 2

print(results)

lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5,4,5,4,5]
lists[100] = [5,2]
print(lists)

my_dictionary["suuri"] = "big"
my_dictionary["suuri"] = "large"
print(my_dictionary["suuri"])

word_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] 

def counts(my_list):
    words = {}
    for word in my_list:
        #if the word is not already in the dictionary, initialize the value to 0
        if word not in words:
            words[word] = 0
        #increment the value
        words[word] += 1
    return words

print(counts(word_list))
    