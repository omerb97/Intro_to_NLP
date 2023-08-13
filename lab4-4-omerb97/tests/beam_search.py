test = {   'name': 'beam_search',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> K = 5;\n'
                                               '>>> \n'
                                               '>>> correct = 0;\n'
                                               '>>> total = 0;\n'
                                               '>>> \n'
                                               '>>> # create beam searcher;\n'
                                               '>>> beam_searcher = BeamSearcher(model);\n'
                                               '>>> \n'
                                               '>>> for batch in test_iter:\n'
                                               '...   # Input and output\n'
                                               "...   src = batch['src_ids']\n"
                                               "...   src_lengths = batch['src_lengths']\n"
                                               '...   # Predict\n'
                                               '...   prediction = beam_searcher.beam_search(src, src_lengths, K)\n'
                                               '...   # Convert to string\n'
                                               '...   prediction = hf_tgt_tokenizer.decode(prediction, skip_special_tokens=True)\n'
                                               "...   ground_truth = hf_tgt_tokenizer.decode(batch['tgt_ids'][0], skip_special_tokens=True)\n"
                                               '...   if ground_truth == prediction:\n'
                                               '...     correct += 1\n'
                                               '...   total += 1\n'
                                               '...   \n'
                                               '>>> correct > 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
