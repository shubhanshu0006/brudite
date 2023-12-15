def find_most_frequent_word(sentence):
    # Split the sentence into words
    words = sentence.lower().split()

    # Create an empty dictionary to store word frequencies
    word_frequency = {}

    # Count the frequency of each word
    for word in words:
        # Remove punctuation if necessary
        word = word.strip('.,!?()[]{}":;')

        # Update the dictionary with the word frequency
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Find the word with the maximum frequency
    most_frequent_word = max(word_frequency, key=word_frequency.get)

    return most_frequent_word

# Example usage
input_sentence = "This is an example sentence. This sentence has some words, and some words are repeated."
result = find_most_frequent_word(input_sentence)

print(f"The most frequent word is: {result}")
