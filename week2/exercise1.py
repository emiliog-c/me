"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# This line defines what is contained in the variable of some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# This will print all the variables in some_words
for word in some_words:
    print(word)
# This will do the same as the above
for x in some_words:
    print(x)
# Print the statement after somewords from how it is set out
print(some_words)
# Will check if the amount of words in some_words are above 3, and if so, will print the statement
if len(some_words) > 3:
    print('some_words contains more than 3 words')
# Prints the specifications of the computer that is running this python program
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
