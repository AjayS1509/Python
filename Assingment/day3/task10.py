# Write a function translate() that will translate a text into "rövarspråket" (Swedish for
#  "robber's language"). That is, double every consonant and place an occurrence of "o" in
#  between. For example, translate("this is fun") should return the string "tothohisos isos
#  fofunon".

def add_o_in_between(val):
    return val+'o'+val

def main():
    #consonant are 21 and vowels are 5 
    #so we take vowels easy one and check these are vowels no apply changes on them

    vowels  = ['a','e','i','o','u']
    sentence = "this is fun"
    final_sentence = ''
    for ele in sentence:
        if(ele.isalpha()):
            if(ele.lower() in vowels):
                final_sentence += ele
            else:
                final_sentence += add_o_in_between(ele)
        else:
            final_sentence += ele

        
    print(final_sentence)

main()