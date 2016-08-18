# reverse a string
# fisher adelakin

def reverse_string(string):
    # we slice the string to return it in reversed form
    # this is essentially the most pythonic way to do this
    # negative values using slice creates a copy of the string but in reverse order
    return string[::-1]
