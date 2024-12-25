import enchant #-- pip install pyenchant
import itertools as it

wordDictionary: enchant.Dict = enchant.Dict("en_US")

validWords: list = []
invalidWords: list = []

def add_to_list(addition: str, destination: list):
    """Adds the given addition to the destination list (if it's not already in there)"""
    if addition not in destination:
        destination.append(addition)

def find_all_permutations(word: str):
    """Finds all the permutations of a given word."""
    permutations: list = [permutation for permutation in it.permutations(word)]
    anagrams: list = []
    for group in permutations:
        combined = ""
        for letter in range(len(group)):
            combined += group[letter]
        anagrams.append(combined)
    return anagrams

def check_new_permutation(permutation: str):
    """Checks if the permutation of a word is a valid English language word."""
    return permutation, wordDictionary.check(permutation)

def organize_results(result: str):
    """Sorts a permutation into one of two lists based on validity."""
    permutation, validity = result
    match validity:
        case True:
            add_to_list(permutation, validWords)
        case False:
            add_to_list(permutation, invalidWords)
    invalidWords.sort()

def format_string(validAnagrams: list, invalidAnagrams: list):
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

def find_anagrams(word: str):
    """Gives all the anagrams of a given word in an easily-readable format. Isn't that nice?"""
    for newWord in find_all_permutations(word):
        organize_results(check_new_permutation(newWord))
    print(format_string(validWords, invalidWords))
