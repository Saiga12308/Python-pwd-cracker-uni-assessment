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
            word_var = (word+word[0])
            word_var = word_var.capitalize()
    
        elif len(word) >= 12:
            word_var = word[0:10]
            word_var = word_var.capitalize()

        else:
            word_var = word_var.capitalize()

        for combo in munging_combos:
            for symbol in special_chars:
                if combo[0] not in word_var:
                    combo[0] = combo[0].upper()

                munged_var = word_var.replace(combo[0], combo[1])

                word_var_list.append(symbol + munged_var)
                word_var_list.append(munged_var + symbol)
    
        for individual_date in date_list:
            for variant in word_var_list:
                variant_list.append(variant+individual_date)

        del word_var_list
        return variant_list



    def word_variant_hashed(self, word, salt, dates, md5=True):
        import hashlib

        variant_list = self.word_variant_unhashed(word, dates)
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

        del variant_list
        return hashed_variant_dict