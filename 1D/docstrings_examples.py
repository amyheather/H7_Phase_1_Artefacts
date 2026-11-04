
def extract_words_starting_with_s(list_of_words):
    """
    Extract a list of words beginning with the letter s from a list of words
    provided by the user.

    Args:
        list_of_words: A list of words from which to extract.

    Returns:
        A list containing only those words that begin with the letter s from
            the provided list of words.

    """
    list_of_s_words = [
        word for word in list_of_words if word[0].lower() == "s"
    ]

    return list_of_s_words

list_of_words = ["Dan", "Sammi", "sausages"]

s_words = extract_words_starting_with_s(list_of_words)
print (s_words)

