# variable
var1 = 10

# list
anything = [10, 10, 3, 2]

# dict
dict1 = {'apple': 'green', 'grape':'red', 'other grape':'green', 'apple':'red'}

# loops through lists
for index, element in enumerate(anything):
    # My favorite method for inserting variables into strings
    print "Element {0}: {1}".format(index, element)
    # another method for inserting into strings.
    print "Element %i: %i" % (index, element)

#through dicts
for key, val in dict1.iteritems():
    if val == 'green':
        print key + ' is ' + val

#ex function 1
def key_in_value(input_to_function):
    """
    INPUT: dict
    OUTPUT: list
    Return the keys from the dictionary where the key is a member in the
    associated value.
    example:
    INPUT: {"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]}
    OUTPUT: ["a", "c"]
    Hint: Use iteritems
    (Can be done on one line with a list comprehension)
    """
    answer = []

    for key, val in input_to_function.iteritems():
        # print 'key: {0}'.format(key)
        # print 'val: {0}'.format(val)
        # print key in val
        if key in val:
            answer.append(key)

    return answer

storage = key_in_value({"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]})
