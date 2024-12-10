import enchant #-- pip install pyenchant
import itertools as it

wordDictionary = enchant.Dict("en_US")

validWords = []
invalidWords = []

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
            if permutation not in validWords:
                validWords.append(permutation)
        case False:
            if permutation not in invalidWords:
                invalidWords.append(permutation)

def format_string(validAnagrams, invalidAnagrams):
    """Formats all the anagrams into a nice, readable format."""
    validString = ", ".join(validAnagrams)
    invalidString = ", ".join(invalidAnagrams)
    formattedString = f"""
        Your valid English language anagrams are:
        {validString}
        
        Your invalid anagrams are:
        {invalidString}
        """
    return formattedString

def find_anagrams(word):
    """Gives all the anagrams of a given word in an easily-readable format. Isn't that nice?"""
    for newWord in find_all_permutations(word):
        organize_results(check_new_permutation(newWord))
    print(format_string(validWords, invalidWords))

if __name__ == "__main__":
    find_anagrams("test")
