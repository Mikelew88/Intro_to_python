from collections import Counter, defaultdict

def most_common_letters(sentence):
    """
    INPUT: string
    OUTPUT: list of strings
    Given a sentence, give the most common letter for each word.
    You should lowercase the letters. If there's a tie, include any of them.
    example:
    INPUT: "Welcome to Zipfian Academy!"
    OUTPUT: 'e t i a'
    Hint: use Counter and the string join method
    (It is possible to do this in one line, but you might lose some
    readability)
    """
    output = ''
    for word in sentence.lower().split():
        char_counter = Counter(word)
        print word
        print 'counter: '
        print char_counter
        print 'most common: '
        print  char_counter.most_common(1)[0][0]
        print '\n'


        output += char_counter.most_common(1)[0][0]
        output += ' '

    return output
    # Here is the one-liner version
    # ' '.join(Counter(word).most_common(1)[0][0] for word in sentence.lower().split())


def merge_dictionaries(d1, d2):
    """
    INPUT: dict (string => int), dict (string => int)
    OUTPUT: dict (string => int)
    example:
    INPUT: {"a": 2, "b": 5}, {"a": 7, "c":10}
    OUTPUT: {"a": 9, "b": 5, "c": 10}
    Create a new dictionary that contains all the key, value pairs from d1 and
    d2. If a key is in both dictionaries, sum the values.
    """
    output = defaultdict(int)
    for key, val in d1.iteritems():
        output[key] += val
    for key, val in d2.iteritems():
        output[key] += val

    return output

if __name__ == '__main__':
    print most_common_letters("Welcome to Zipfian Academy!")
    # print merge_dictionaries({"a": 2, "b": 5}, {"a": 7, "c":10})
