import enchant #-- pip install pyenchant
import itertools as it

wordDictionary = enchant.Dict("en_US")

validWords = [] #-- there might be a better place to store these. I dunno
invalidWords = []

def add_to_list(addition, destination):
    """Adds the given addition to the destination list (if it's not already in there)"""
    if addition not in destination:
        destination.append(addition)

def find_all_permutations(word):
    """Finds all the permutations of a given word."""
    permutations = [permutation for permutation in it.permutations(word)]
    anagrams = []
    for group in permutations:
        combined = ""
        for letter in range(len(group)):
            combined += group[letter]
        anagrams.append(combined)
    return anagrams

def check_new_permutation(permutation):
    """Checks if the permutation of a word is a valid English language word."""
    return permutation, wordDictionary.check(permutation)

def organize_results(result):
    """Sorts a permutation into one of two lists based on validity."""
    permutation, validity = result
    match validity:
        case True:
            add_to_list(permutation, validWords) #-- if I could put the "valid" and "invalid" lists here I think that could work
        case False:
            add_to_list(permutation, invalidWords) #-- but how? How would I get them out in the later function?

def format_string(validAnagrams, invalidAnagrams):
    """Formats all the anagrams into a nice, readable format."""
    validString = ", ".join(validAnagrams)
    invalidString = ", ".join(invalidAnagrams)
    formattedString = f"""
        There are {len(validAnagrams)} valid English language anagrams:
        {validString}
        
        There are {len(invalidAnagrams)} that are not valid English language words:
        {invalidString}
        """
    return formattedString

def find_anagrams(word):
    """Gives all the anagrams of a given word in an easily-readable format. Isn't that nice?"""
    for newWord in find_all_permutations(word):
        organize_results(check_new_permutation(newWord))
    print(format_string(validWords, invalidWords))
