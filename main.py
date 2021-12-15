############################# PASSWORD CRACKING ##################################
import cls

#get pw hash and salt
#go into dict and get first line
#check if 7 chars or more

#if not, ignore
#if 7 chars, add "1" to end then try with salt added to beginning and end
#if 8 chars or more, try as is with salt added to beginning and end

#if doesn't work, attempt with a variety of mangling rules

#if still doesn't work, move on to next line in dict and repeat

#if it finds a match, save to file
#if it gets to end of dict and finds no match, move on to next pw




############################# SSH BRUTE FORCE ####################################