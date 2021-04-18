from string import ascii_letters
from Chomsky import *
import re


def main():
    rules = {}
    new_rules = []

    let = list(ascii_letters[26:]) + list(ascii_letters[:25])

    let.remove('e')

    # Number of grammar rules
    while True:
        userInput = input('Give number of rules')
        try:
            # check if N is integer >=2
            N = int(userInput)
            if N <= 2:
                print('N must be a number >=2!')
            else:
                break
        except ValueError:
            print("That's not an int!")

    # Initial state
    while True:
        S = input('Give initial state')
        if not re.match("[A-Z]*$", S):  # ayy I love these things
            print('Initial state must be a single and capital \
character!')  # .*$ //Zero or more of any character (except line break) followed by end of string
        else:
            break
    print("________________________")
    print("Enter rules this way:S B")
    print("                    A aX")
    print("          etc.          ")
    print("________________________")

    for i in range(N):
        fr, to = map(str, input('Rule #' + str(i + 1)).split())
        for l in fr:
            if l != 'e' and l not in new_rules: new_rules.append(l)
            if l in let: let.remove(l)
        for l in to:
            if l != 'e' and l not in new_rules: new_rules.append(l)
            if l in let: let.remove(l)
        # Insert rule to dictionary
        rules.setdefault(fr, []).append(to)

    # remove large rules and print new rules
    print('\nRules after large rules removal')
    rules, let, new_rules = large(rules, let, new_rules)
    print_rules(rules)
    # print new_rules

    print("I couldn't find a way to replace B with AXaD \n")
    rules, let, new_rules = hardReplaceB(rules, let, new_rules)
    print_rules(rules)

    # remove empty rules and print new rules
    print('\nRules after empty rules removal')
    rules, new_rules = empty(rules, new_rules)
    print_rules(rules)
    # print new_rules

    print('\nRules after short rules removal')
    rules, D = short(rules, new_rules)
    print_rules(rules)

    print('\nFinal rules')
    rules = final_rules(rules, D, S)
    print_rules(rules)


if __name__ == '__main__':
    main()
