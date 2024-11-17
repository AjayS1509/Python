#  In English, present participle is formed by adding suffix-ing to infinite form: go->
#  going. A simple set of heuristic rules can be given as follows:
#  a)If the verb ends in e, drop the e and add ing
#  (if not exception be, see, flee, knee, etc.)
#  b) If the verb ends in ie, change ie to y and add ing
#  c)For words consisting of consonant-vowel-consonant, double the final
#  letter before adding ing
#  d) By default, just add ing
#  Your task in this exercise is to define a function make_ing_form() which given a verb in
# infinitive form returns its present participle form. Test your function with words such as
#  lie, see, move and hug. However, you must not expect such simple rules to work for all
#  cases.
def make_ing_form(verb):
    
    # Special exceptions are "be", "see", "flee", and "knee"
    exceptions = {"be", "see", "flee", "knee"}
    if verb in exceptions:
        return verb + "ing"
    elif(verb.endswith("e") or verb.endswith("ie")):
        # Rule b: If the verb ends in "ie", change "ie" to "y" and add "ing"
        if(verb.endswith("ie")):
            return verb[:-2] + "ying"
        # Rule a: If the verb ends in "e", drop "e" and add "ing"
        else:
            return verb[:-1] + "ing"
    
    
    # Rule c: If the verb has a consonant-vowel-consonant pattern, double the final letter
    elif len(verb) > 2 and (verb[-1] not in ["a","e","i","o","u"] and verb[-2] in ["a","e","i","o","u"] and verb[-3] not in ["a","e","i","o","u"]):
        return verb + verb[-1] + "ing"
    
    # Rule d: Default case, just add "ing"
    else:
        return verb + "ing"


print(make_ing_form("lie"))     # Output: lying

print(make_ing_form("see"))     # Output: seeing
print(make_ing_form("move"))    # Output: moving
print(make_ing_form("hug"))     # Output: hugging