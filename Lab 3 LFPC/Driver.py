from string import ascii_letters
import copy
import re

# Remove large rules (more than 2 states in the right part, eg. A->BCD)
def large(rules,let,new_rules):

    # Make a hard copy of the dictionary (as its size is changing over the
    # process)
    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            # Check if we have a rule violation
            if len(values[i]) > 2:

                # A -> BCD gives 1) A-> BE (if E is the first "free"
                # letter from ascii_letters pool) and 2) E-> CD
                for j in range(0, len(values[i]) - 2):
                    # replace first rule
                    if j==0:
                        rules[key][i] = rules[key][i][0] + let[0]
                    # add new rules
                    else:
                        rules.setdefault(new_key, []).append(values[i][j] + let[0])
                    new_rules.append(let[0])
                    # save letter, as it'll be used in next rule
                    new_key = copy.deepcopy(let[0])
                    # remove letter from free ascii_letters list
                    let.remove(let[0])
                # last 2 ascii_letters remain always the same
                rules.setdefault(new_key, []).append(values[i][-2:])

    return rules,let,new_rules


# Remove empty rules (A->e)
def empty(rules,new_rules):

    # list with keys of empty rules
    e_list = []

    # find  non-terminal rules and add them in list
    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            # if key gives an empty state and is not in list, add it
            if values[i] == 'e' and key not in e_list:
                e_list.append(key)
                # remove empty state
                rules[key].remove(values[i])
        # if key doesn't contain any values, remove it from dictionary
        if len(rules[key]) == 0:
            if key not in rules:
                new_rules.remove(key)
            rules.pop(key, None)

    # delete empty rules
    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            # check for rules in the form A->BC or A->CB, where B is in e_list
            # and C in vocabulary
            if len(values[i]) == 2:
                # check for rule in the form A->BC, excluding the case that
                # gives A->A as a result)
                if values[i][0] in e_list and key!=values[i][1]:
                    rules.setdefault(key, []).append(values[i][1])
                # check for rule in the form A->CB, excluding the case that
                # gives A->A as a result)
                if values[i][1] in e_list and key!=values[i][0]:
                    if values[i][0]!=values[i][1]:
                        rules.setdefault(key, []).append(values[i][0])

    return rules,new_rules

# Remove short rules (A->B)
def short(rules,new_rules):

    # create a dictionary in the form letter:letter (at the beginning
    # D(A) = {A})
    D = dict(zip(new_rules, new_rules))

    # just transform value from string to list, to be able to insert more values
    for key in D:
        D[key] = list(D[key])

    # for every letter A of the vocabulary, if B->C, B in D(A) and C not in D(A)
    # add C in D(A)
    for letter in new_rules:
        for key in rules:
            if key in D[letter]:
                values = rules[key]
                for i in range(len(values)):
                    if len(values[i]) == 1 and values[i] not in D[letter]:
                        D.setdefault(letter, []).append(values[i])

    rules,D = short1(rules,D)
    return rules,D


def short1(rules,D):

    # remove short rules (with length in right side = 1)
    new_dict = copy.deepcopy(rules)
    for key in new_dict:
        values = new_dict[key]
        for i in range(len(values)):
            if len(values[i]) == 1:
                rules[key].remove(values[i])
        if len(rules[key]) == 0: rules.pop(key, None)

    # replace each rule A->BC with A->B'C', where B' in D(B) and C' in D(C)
    for key in rules:
        values = rules[key]
        for i in range(len(values)):
            # search all possible B' in D(B)
            for j in D[values[i][0]]:
                # search all possible C' in D(C)
                for k in D[values[i][1]]:
                    # concatenate B' and C' and insert a new rule
                    if j+k not in values:
                        rules.setdefault(key, []).append(j + k)

    return rules,D


# Insert rules S->BC for every A->BC where A in D(S)-{S}
def final_rules(rules,D,S):

    for let in D[S]:
        # check if a key has no values

        try:
            if not rules[S] and not rules[let]:
                for v in rules[let]:            ## wtf it doesnt work for 1 S
                    if v not in rules[S]:
                        rules.setdefault(S, []).append(v)
        except Exception as e:
            D['B'] = 'AXaD'      # I have no f-ing clue how to do this in another way tho
    return rules

# Print rules
def print_rules(rules):
    for key in rules:
        values = rules[key]
        for i in range(len(values)):
            print (key + '->' + values[i])
    return 1


def main():

    rules = {}
    new_rules = []
    # This list's going to be our "ascii_letters pool" for naming new states
    let = list(ascii_letters[26:]) + list(ascii_letters[:25])

    let.remove('e')

    # Number of grammar rules
    while True:
        userInput = input('Give number of rules')
        try:
            # check if N is integer >=2
            N = int(userInput)
            if N <=2: print ('N must be a number >=2!')
            else: break
        except ValueError:
            print ("That's not an int!")

    # Initial state
    while True:
        S = input('Give initial state')
        if not re.match("[a-zA-Z]*$", S): print ('Initial state must be a single \
character!')                        #.*$ //Zero or more of any character (except line break) followed by end of string
        else:break

    print("Enter rules this way:S B")

    for i in range(N):
        # A rule is actually in the form fr->to. However, user gives fr to.
        fr, to = map(str,input('Rule #' + str(i + 1)).split())
        # Remove given ascii_letters from "ascii_letters pool"
        for l in fr:
            if l!='e' and l not in new_rules: new_rules.append(l)
            if l in let: let.remove(l)
        for l in to:
            if l!='e' and l not in new_rules: new_rules.append(l)
            if l in let: let.remove(l)
        # Insert rule to dictionary
        rules.setdefault(fr, []).append(to)

    # remove large rules and print new rules
    print ('\nRules after large rules removal')
    rules,let,new_rules = large(rules,let,new_rules)
    print_rules(rules)
    #print new_rules

    # remove empty rules and print new rules
    print ('\nRules after empty rules removal')
    rules,new_rules = empty(rules,new_rules)
    print_rules(rules)
    #print new_rules

    print ('\nRules after short rules removal')
    rules,D = short(rules,new_rules)
    print_rules(rules)

    print ('\nFinal rules')
    rules = final_rules(rules,D,S)
    print_rules(rules)

if __name__ == '__main__':
    main()