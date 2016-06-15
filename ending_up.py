pyg = 'ay'

original = raw_input('Enter a word:')

#ensures text entered as original has greater than 0 characters and is a word (uses letters) instead of a digit
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

#converts original word to its lowercase form
word = original.lower()

#takes first letter of word and stores it
first = word[0]

#stores lower case word, adds first letter and then pyg. Word should print as "wordway"
new_word = word + first + pyg

# prints new word for debugging purposes
print new_word

#prints everything after position 0 in length of word
new_word=new_word[1:len(new_word)]

#prints new work for debugging purposes
print new_word