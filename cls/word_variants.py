def word_variant_hashes(word, salt, algorithm=""):
    #generates a list of all variations of a word and the salt to compare against

    #if algorithm entered, then hash before adding any of these to list using specified algorithm, and use the hash as key in a dictionary with the unhashed ver as value. otherwise just store in array
    #add salt to beginning of word, add to list
    #add salt to end of word, add to list
    #capitalise first letter, add to list with salt added at start and end
    #capitalise last letter, add to list with salt added at start and end
    #add 1 to beginning of word, add to list with salt added at start and end
    #add 1 to end of word, add to list with salt added at start and end
    #replace a's with @, add to list with salt added at start and end
    #replace i's with !, add to list with salt added at start and end
    #replace o's with 0, add to list with salt added at start and end
    #replace e's with 3, add to list with salt added at start and end


    pass