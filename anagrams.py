"""
Does a word have an anagram that is another word in the English language? Perhaps! This module can help discover that information.\n
Using the "find_anagrams" function you, too, can test any given word (though longer ones might take a while) and, if you so choose,\n
save it to a .txt file because the list might be longer than the terminal is happy with.
"""

import enchant #-- pip install pyenchant
import itertools as it

wordDictionary: enchant.Dict = enchant.Dict("en_US")

validWords: list[str] = []
invalidWords: list[str] = []

def add_to_list(addition: str, destination: list[str]):
    """Adds the given addition to the destination list (if it's not already in there)"""
    if addition not in destination:
        destination.append(addition)

def find_all_permutations(word: str):
    """Finds all the permutations of a given word."""
    permutations: list[str] = [permutation for permutation in it.permutations(word)]
    anagrams: list[str] = []
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

def format_string(validAnagrams: list[str], invalidAnagrams: list[str]):
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

def find_anagrams(word: str, save: bool = False):
    """Gives all the anagrams of a given word in an easily-readable format. Isn't that nice?"""
    for newWord in find_all_permutations(word):
        organize_results(check_new_permutation(newWord))
    finalAnagramList = format_string(validWords, invalidWords)
    print(finalAnagramList)
    if save == True:
        with open("anagrams.txt", "w") as anagramText:
            anagramText.write(finalAnagramList)
