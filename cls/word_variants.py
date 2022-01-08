class WordVarGen:
    
    def __init__(self):
        pass

    def word_variant_unhashed(self, word, date_list):
        #generates a list of all variations of a word and returns as list

        word_var = word
        word_var_list = []

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
            word_var += word[0]
            word_var = word_var.capitalize()
    
        elif len(word) >= 12:
            word_var = word[0:10]
            word_var = word_var.capitalize()

        else:
            word_var = word_var.capitalize()

        for combo in munging_combos:
            if combo[0] not in word_var:
                combo[0] = combo[0].upper()
                combo[1] = combo[1].upper()

            munged_var = word_var.replace(combo[0], combo[1])
            word_var_list += [munged_var+x for x in special_chars]
    
        variant_list = [variant+individual_date for variant in word_var_list for individual_date in date_list]

        del word_var_list
        return variant_list
        #return word_var_list



    def word_variant_hashed(self, variant_list, salt, md5=True):
        import hashlib

        if md5:
            hashed_variant_dicta = {hashlib.md5(salt.encode()+variant.encode()).hexdigest():variant for variant in variant_list}
            hashed_variant_dictb = {hashlib.md5(variant.encode()+salt.encode()).hexdigest():variant for variant in variant_list}

        else:
            hashed_variant_dicta = {hashlib.sha256(salt.encode()+variant.encode()).hexdigest():variant for variant in variant_list}
            hashed_variant_dictb = {hashlib.sha256(variant.encode()+salt.encode()).hexdigest():variant for variant in variant_list}

        del variant_list
        return hashed_variant_dicta | hashed_variant_dictb