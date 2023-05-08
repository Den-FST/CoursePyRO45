### Regular expressions ###
"""
Regular expressions are patterns that describe strings of symbols. 
For example, we can create an expression that will match any e-mail address, any date, phone number, or credit card number, etc.

In Python, we need a re module to work with regular expressions. 
This module will help us to search for strings matching a pattern in text, or to check if a given text exactly matches a given pattern.

SPECIAL SIGNS: (https://regex101.com/  -- akaka93kskasja7474jnfsdkjbfd734747)
    a. dot: . - any character except a newline. The .la pattern matches the strings: "Ola", "ala" and "Ela",
    b. question mark: ? - means zero or one occurrence of the preceding character. The pattern Olk?a matches "Ola" and "Olka",
    c. plus: + - means one or more occurrences. The a+le pattern matches the strings: "ale", "aaale", "aaaaale", etc.,
    d. asterisk: * - means any number of occurrences of the character (including zero). The pattern a*la matches the strings "la", "ala", "aaaaala", etc.,
    e. square brackets match any of the characters they contain. The [OA]la pattern matches "Ola" and "Ala". We can also specify a range of characters by using a hyphen. 
       The [a-z]al pattern will match a word beginning with any lowercase letter followed by "al", e.g. "mal", "pal" or "eal",
    f. parentheses allow you to group characters in an expression so that you can apply various modifiers collectively,
    g. the braces indicate the number of repeats. The pattern a(la){1,3} will be matched by all strings starting with "a" followed by one to three times the "la" cluster, i.e. "ala", "alala" and "alalala",
    h. caret: ^ - is a negation of characters given in square brackets. It means that the [^ OA]la pattern is matched by "Ela" and "Bla", but not "Ola" and "Ala",
    i. vertical bar: | means an alternative, e.g. the Ala has a (dog|cat), both the string "Ala has a cat" and "Ala has a dog" will match,
    j. The caret ^ at the beginning of a pattern signifies a match to the beginning of a line (i.e. we want the strings to match the pattern from the beginning), pattern ^ [a-z] * will not match eg. "Basia has a hedgehog", because the string does not start with a lowercase letter,
    k. Similarly, the dollar sign $ matches the end of the line
    l. if we want to use a special character as an ordinary one, we must precede it with a backslash. For example, for the "john.kowalski" string, an example pattern that this matches would be [a-z]\.[A-z],
    m. \d stands for a digit and is an alias for [0-9],
    n. \s matches any white space,
    o. \w stands for a word and is an alias for [A-Za-z0-9_].


FUNCTIONS:
    1. search - It returns a Match object that contains information about which string was matched and where it is, or a None object if no matching string was found
    2. match - This function takes exactly the same parameters as search. The difference is that match tells you whether the beginning of the text matches the expression, not just a part of it
    3. fullmatch - This function is used to search for “all” occurrences that match a given pattern.
    4. findall - The function returns all matches against a pattern from text.
    5. findfiter - This function works like findall, but returns an iterator that allows you to access successive items as you step over them.
    6. split - The split function from the re module works similarly to the split function from the os module, except that here we can specify a regular expression against which we split the string.
    7. sub - The function converts all strings described by the regular expression into a given string.
    8. subn - The function works like sub, but additionally it returns information on how many substitutions have been made
"""

def main():

    #####################################################
    ### search ### checks if pattern is inside text ###
    print(f"\n\n{'-'*50}\nSEARCH:")



    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### match ### checks if text starts with pattern ###
    print(f"\n\n{'-'*50}\nMATCH:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### full match ### checks if text == pattern ###
    print(f"\n\n{'-'*50}\nFULL MATCH:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### findall ### find all pattern occurances and creates a list ###
    print(f"\n\n{'-'*50}\nFIND ALL:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### finditer ### works like findall but returns iterator instead of list ###
    print(f"\n\n{'-'*50}\nFIND ITER:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### split ### split text by pattern and creates a list ###
    print(f"\n\n{'-'*50}\nSPLIT:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### sub ### converts the pattern given with a string given ###
    print(f"\n\n{'-'*50}\nSUB:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### subn ### like sub but also gives how many substitutions were made ###
    print(f"\n\n{'-'*50}\nSUBN:")

    

    print(f"{'-'*50}\n\n")
    #####################################################


    #####################################################
    ### group-ing ###
    print(f"\n\n{'-'*50}\nGROUP-ing:")

    

    print(f"{'-'*50}\n\n")
    #####################################################

if __name__ == "__main__":
    main()