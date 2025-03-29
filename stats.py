def get_num_words(text):
    return len(text.split())

def get_character_occurrence(text):
    words_list = [x.lower() for x in text.split()]
    char_dict = {}
    for word in words_list:
        for letter in word:
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1    

    return sort_character_occurrence(char_dict)

def sort_character_occurrence(char_dict):
    # dict.items() --> returns a view object containing all key-value pairs like [('a', 3), ('b', 5)]...
    # sorted() returns a new sorted list from the elements of any iterable
        # iterable: list of key,value pairs in this case
        # key: function that tells sorted() how to compare elements
        # reverse~: sorts in descending order
    # key=lambda item: item[1]
        # the parameter item representes each (key, value) pair
        # item[1] accesses the value part of the tuple
            # so this tells the sorted() function to compare elements based on the value, not the key
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict

