
def extract_words_starting_with_s(list_of_words):
    """
    Extract a list of words beginning with the letter s from a list of words
    provided by the user.

    Args:
        list_of_words: A list of words from which to extract

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

def generate_times_table(number: int) -> list[int]:
    """
    Generate the 1 to 12 times table for the number input to the function,
    returning it as a list.

    Args:
        number: The number for which to generate the times table.

    Returns:
        A list containing the values of the 1 to 12 times table for the number

    """
    times_table = []
    
    for i in range(1, 13):
        times_table.append(i*number)

    return times_table

three_times_table = generate_times_table(3)
print (three_times_table)

