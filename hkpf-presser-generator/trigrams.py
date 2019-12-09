from nltk import trigrams
from collections import defaultdict
import random
import re


punctuation = ['.', ',', '!', '?', ':', ';']
sentence_terminators = ['.', '!', '?']

# there's an empty sentence at the end, but whatever
# inputs definitely need to be cleaned better, lots of random whitespace in there still
def clean_text(raw_text):
    clean_text = re.sub('\n ', '\n', raw_text)
    clean_text = re.sub(r'(\n\s*)+\n', '\n\n', clean_text)

    words = re.split('\s', clean_text)
    sentence_index = 0
    result = [[]]

    for word in words:
        if (word.endswith(tuple(punctuation))):
            result[sentence_index].append(word[:-1])
            result[sentence_index].append(word[-1])

            if word.endswith(tuple(sentence_terminators)):
                sentence_index += 1
                result.append([])
        else:
            result[sentence_index].append(word)

    return result


# a "sentence" is an array of words, terminated by a full stop.
def create_model(sentences):
    # Create empty model
    model = defaultdict(lambda: defaultdict(lambda: 0))

    # Count frequency of co-occurrence
    for sentence in sentences:
        for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
            model[(w1, w2)][w3] += 1 # increments frequency of w3 when preceded by w1 and w2

    # Transform the counts to probabilities
    for w1_w2 in model:
        total_count = float(sum(model[w1_w2].values()))
        for w3 in model[w1_w2]:
            model[w1_w2][w3] /= total_count

    return model


# returns probabilities that sentences start with certain words
def create_sentence_starters(sentences):
    starting_words = defaultdict(lambda: 0)

    for sentence in input:
        if len(sentence) >= 2:
            starting_words[(sentence[0], sentence[1])] += 1

    # Transform the counts to probabilities
    total_count = len(starting_words)
    for key in starting_words.keys():
        starting_words[key] = float(starting_words[key] / total_count)

    return starting_words


def get_random_starting_words(sentence_starters):
    r = random.random()
    accumulator = .0

    for words in sentence_starters.keys():
        accumulator += sentence_starters[words]
        if accumulator >= r:
            return [words[0], words[1]]



# text is an array of words to start the sentence with
def generate_sentence(model, text, word_limit):

    sentence_finished = False
    word_count = 0

    while (not sentence_finished) and (word_count < word_limit):
        # select a random probability threshold
        r = random.random()
        accumulator = .0

        for word in model[tuple(text[-2:])].keys():
            accumulator += model[tuple(text[-2:])][word]
            # select words that are above the probability threshold
            if accumulator >= r:
                text.append(word)
                word_count += 1
                break

        if text[-2:] == [None, None]:
            sentence_finished = True



    return ' '.join([t for t in text if t])





input = None

with open("raw", "r", encoding="utf-8") as f:
    raw_text = f.read()
    input = clean_text(raw_text)

model = create_model(input)
sentence_starters = create_sentence_starters(input)
starting_words = get_random_starting_words(sentence_starters)
sentence = generate_sentence(model, starting_words, 100000)
print(sentence)




