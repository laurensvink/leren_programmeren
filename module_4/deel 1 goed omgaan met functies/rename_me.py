def even_number(number:int) -> bool: # hij check of het gegeven nummer even is en return True or False
    return number % 2 == 0

def reverse_words(sentence: str) -> str:
    words = sentence.split()       # Split the sentence into a list of words
    reversed_words = words[::-1]  # Reverse the list of words
    reversed_sentence = ' '.join(reversed_words)  # Join them back into a string
    return reversed_sentence
    
def count_unique_characters(text: str) -> int:
    unique_chars = set(text)  # Convert to a set to get only unique characters
    return len(unique_chars)  # Return the number of unique characters

def average_word_length(sentence: str) -> float:
    words = sentence.split()  # Split the sentence into words
    
    total_length = 0
    for word in words:
        total_length += len(word)  # Add up the length of each word

    average = total_length / len(words)  # Divide by the number of words
    return average

def times_table(number: int, up_to: int = 10) -> None:
    for i in range(1, up_to + 1):
        result = i * number
        print(f'{i} x {number} = {result}')