def word_variant_unhashed(word):
    #generates a list of all variations of a word and returns as list

    from string import punctuation
    import itertools

    word_var = word

    variant_list = []

    special_chars = [char for char in punctuation]

    if len(word) >= 10:
        variant_list.append(word)
        variant_list.append(word.capitalize())
        variant_list.append(word.upper())

        variant_list.append("1"+word)
        variant_list.append(word+"1")

        #appends munges and variations on the munges
        for i in range(4):

            #goes through every combination of rules possible
            for i in range(0, len(munging_combos)+1):
                for subset in itertools.combinations(munging_combos, i):
                    for munging_rule in subset:
                        if word_var.replace(munging_rule[0], munging_rule[1]) != word_var:
                            variant_list.append(word_var.replace(munging_rule[0], munging_rule[1]))
                        else:
                            variant_list.append(word_var.replace(munging_rule[0].upper(), munging_rule[1]))


            if i == 0:
                #capitalizes first char for second run
                word_var = word.capitalize()
            
            elif i == 1:
                #capitalizes last letter for third run
                word_var = word[::-1].capitalize()
                word_var = word_var[::-1]
                variant_list.append(word_var)

            elif i == 2:
                #capitalizes all letters for last run
                word_var = word.upper()

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