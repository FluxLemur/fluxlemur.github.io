import random

# S: Sentence, NP: Noun Phrase, VP: Verb Phrase
# V_intrans: Intransitive Verb, V_trans: Transitive Verb
# Det: Determiner, N: Noun, PN: Proper Noun

# try changing and adding your own rules!
g = '''
    S = NP VP
    VP = V_intrans | V_trans NP
    NP = Det N | PN
    PN = Sasha | Nikolai | Olga
    N = Adj N | dog | goat | tree
    Adj = slim | green
    Det = the | a | every
    V_intrans = runs | barks | grows
    V_trans = feeds | walks | bites
'''

language = {}
for rule in g.split('\n'):
    if '=' in rule:
        left, right = [i.strip() for i in rule.split('=')]
        language[left] = language.get(left, []) + [i.split() for i in right.split('|')]

def generate(language, rule):
    if rule not in language:
        return rule
    else:
        generated = ''
        rand_rule = language[rule]
        rand_rule = rand_rule[int(random.random() * len(rand_rule))]
        for component in rand_rule:
            generated += ' ' + generate(language, component)
        return generated.strip()

print generate(language, 'S')
