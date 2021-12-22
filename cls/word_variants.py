﻿def word_variant_unhashed(word):
    #generates a list of all variations of a word and returns as list

    from string import punctuation
    import itertools

    word_var = word

    variant_list = []

    special_chars = ['@', '#', '$', '!']

    munging_combos = [
        ["d", "p"],
        ["p", "d"],

        ["q", "b"],
        ["b", "q"],

        ["w", "m"],
        ["m", "w"]
        ]
    
    if len(word) == 10:
        word_var = (word+word[0]).upper()
    
    elif len(word) >= 12:
        word_var = word[0:10].upper()

    

    return variant_list

def word_variant_hashed(word, salt, md5=True):
    import hashlib

    variant_list = word_variant_unhashed(word)
    hashed_variant_dict = {}

    for variant in variant_list:

        #gets both potential positions of salt
        encoded_variant_prepend = salt.encode()+variant.encode()
        encoded_variant_append = variant.encode()+salt.encode()

        #different hashing algorithm based upon detected algorithm in hashed password (within the function, it's based upon if md5 is true or not)
        if md5 == True:
            hashed_variant_prepend = hashlib.md5(encoded_variant_prepend)
            hashed_variant_append = hashlib.md5(encoded_variant_append)
        else:
            hashed_variant_prepend = hashlib.sha256(encoded_variant_prepend)
            hashed_variant_append = hashlib.sha256(encoded_variant_append)

        #pushes hex hash and the password to a dictionary in hash:password
        hashed_variant_dict[hashed_variant_prepend.hexdigest()] = variant
        hashed_variant_dict[hashed_variant_append.hexdigest()] = variant
    return hashed_variant_dict