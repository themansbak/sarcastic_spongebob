import random

def addSarcasm(string):
    """ Returns sarcastically formatted string
    Paramaters: 
    # string: string to be reversed

    Returns:
    # string: New sarcatsically formatted string
    """

    sarcasticString = []
    for i, char in enumerate(string):
        if random.random() >= 0.5:
            sarcasticString.append(str(char).upper())
        else:
            sarcasticString.append(str(char).lower())
    
    return ''.join(sarcasticString)

if __name__ == "__main__":
    word = 'why hello there!'
    sarcasticString = addSarcasm(word)
    print(sarcasticString)