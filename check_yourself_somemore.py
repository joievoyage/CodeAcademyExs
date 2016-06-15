print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

if len(original) > 0 and original.isalpha(): ### drop a key notes here, not so understand.
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg ## You can use + to concatenate (put together) two strings, like this:
    print original
    #Run this block.
    #Maybe print something?

else:
    print "This is empty."
    #That string must be original.