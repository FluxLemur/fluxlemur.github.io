import random

# try changing and adding your own rules
g = '''
    S -> NP VP
    VP -> V_INTRANS | V_TRANS NP
    NP -> DET N | PN
    PN -> Sasha | Nikolai | Olga
    N -> ADJ N | dog | goat | tree
    ADJ -> slim | green
    DET -> the | a | every
    V_INTRANS -> runs | barks | grows
    V_TRANS -> feeds | walks | bites
'''

language = {}
for rule in g.split('\n'):
    if '->' in rule:
        left, right = [i.strip() for i in rule.split('->')]
        language[left] = language.get(left, [])
        language[left] += [i.split() for i in right.split('|')]

def generate(language, rule):
    if rule not in language:
        return rule
    else:
        generated = ''
        rand_rule = language[rule]
        rand_rule = random.choice(rand_rule)
        for component in rand_rule:
            generated += ' ' + generate(language, component)
        return generated.strip()

START = 'S'
print generate(language, START)
