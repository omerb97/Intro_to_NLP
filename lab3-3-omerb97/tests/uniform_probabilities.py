test = {   'name': 'uniform_probabilities',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(probabilistic_arithmetic_grammar) == nltk.grammar.PCFG\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> ## Verify that all of the probabilities per nonterminal are uniform.;\n'
                                               '>>> \n'
                                               '>>> def all_equal(lst):\n'
                                               '...     return lst[:-1] == lst[1:];\n'
                                               '>>> \n'
                                               '>>> print(all([all_equal([prod.prob() \n'
                                               '...                       for prod in probabilistic_arithmetic_grammar.productions()\n'
                                               '...                       if prod.lhs() == nltk.Nonterminal(nt)])\n'
                                               "...            for nt in ['S', 'OP', 'NUM', 'ADD', 'MULT']]))\n"
                                               'True\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
