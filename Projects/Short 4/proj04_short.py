# finds how many items the two objects share at the start of the list
def compare_front(obj1, obj2):

    # asserts that both objects are the same data type
    assert type(obj1) == type(obj2)

    # goes through each item in the lists, if it finds a match, adds one to the
    # counter, otherwise it stops looking
    out = 0
    for i in range(len(obj1)):
        if i < len(obj1) and i < len(obj2) and obj1[i] == obj2[i]:
            out+=1
        else: 
            break
    return out

# similar fuction to compare_front but checks from the back rather than front
def compare_back(obj1, obj2):
    # just runs compare_front with the reversed lists
    return compare_front(obj1[::-1], obj2[::-1])


# function used to find the primary stress in a list of phonemes
def primary_stress(phonemes):

    # asserts that the input is a list, that it is not empty, and that all
    # of its elements are non empty strings
    assert type(phonemes) == list
    assert len(phonemes) > 0
    assert all(True if type(i) == str and len(i) > 0 else False for i in phonemes)

    # finds the index of the primary stress
    index = [i for i, val in enumerate(phonemes) if val[-1] == '1']

    # outputs the index if one was found, otherwise return None
    if len(index) > 0: 
        return index[0]
    else:
        return None
