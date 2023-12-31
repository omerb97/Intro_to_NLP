test = {   'name': 'attention',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # check for syntactic errors;\n'
                                               '>>> q  = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> k1 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k2 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> \n'
                                               '>>> batched_Q = q.view(1, 1, -1)                            # 1, 1, 5;\n'
                                               '>>> batched_K = torch.stack([k1, k2], 0).unsqueeze(0)       # 1, 2, 5;\n'
                                               '>>> batched_V = batched_K                                   # 1, 2, 5;\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> print (batched_A.size() == torch.Size([1, 1, 2]), \n'
                                               '...        batched_C.size() == torch.Size([1, 1, 5]))\n'
                                               'True True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # check for size;\n'
                                               '>>> q_len = 11;\n'
                                               '>>> k_len = 17;\n'
                                               '>>> bsz = 7;\n'
                                               '>>> D = 13;\n'
                                               '>>> \n'
                                               '>>> batched_Q = torch.randn(bsz, q_len, D).to(device);\n'
                                               '>>> batched_K = torch.randn(bsz, k_len, D).to(device);\n'
                                               '>>> batched_V = torch.randn(bsz, k_len, D).to(device);\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> print (batched_A.size() == torch.Size([bsz, q_len, k_len]), \n'
                                               '...        batched_C.size() == torch.Size([bsz, q_len, D]))\n'
                                               'True True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # check using [q1, q2] is the same as using q1/q2 separately;\n'
                                               '>>> q1 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> q2 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k1 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k2 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> \n'
                                               '>>> batched_Q = torch.stack([q1, q2], 0).unsqueeze(0);\n'
                                               '>>> batched_K = torch.stack([k1, k2], 0).unsqueeze(0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> # doing things separately;\n'
                                               '>>> batched_Q = q1.view(1, 1, -1);\n'
                                               '>>> batched_A1, batched_C1 = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> batched_Q = q2.view(1, 1, -1);\n'
                                               '>>> batched_A2, batched_C2 = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> print (torch.isclose(batched_A[:, 0], batched_A1).all().item(), \n'
                                               '...        torch.isclose(batched_A[:, 1], batched_A2).all().item(),\n'
                                               '...        torch.isclose(batched_C[:, 0], batched_C1).all().item(), \n'
                                               '...        torch.isclose(batched_C[:, 1], batched_C2).all().item()\n'
                                               '...       )\n'
                                               'True True True True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # check batch;\n'
                                               '>>> # first in batch:  q1 -> k1 k2;\n'
                                               '>>> # second in batch: q2 -> k3 k4;\n'
                                               '>>> q1 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> q2 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k1 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k2 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> k3 = torch.Tensor([6, 6, 6, 9, 0]).to(device);\n'
                                               '>>> k4 = torch.Tensor([7, 7, 7, 4, 5]).to(device);\n'
                                               '>>> \n'
                                               '>>> batched_Q = torch.stack([q1, q2], 0).unsqueeze(1);\n'
                                               '>>> batched_K = torch.cat([torch.stack([k1, k2], 0).unsqueeze(0),\n'
                                               '...                       torch.stack([k3, k4], 0).unsqueeze(0)],\n'
                                               '...                       dim=0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> # doing things separately;\n'
                                               '>>> batched_Q = q1.view(1, 1, -1);\n'
                                               '>>> batched_K = torch.stack([k1, k2], 0).unsqueeze(0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> batched_A1, batched_C1 = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> batched_Q = q2.view(1, 1, -1);\n'
                                               '>>> batched_K = torch.stack([k3, k4], 0).unsqueeze(0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> batched_A2, batched_C2 = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> print (torch.isclose(batched_A[0], batched_A1).all().item(), \n'
                                               '...        torch.isclose(batched_A[1], batched_A2).all().item(),\n'
                                               '...        torch.isclose(batched_C[0], batched_C1).all().item(), \n'
                                               '...        torch.isclose(batched_C[1], batched_C2).all().item()\n'
                                               '...       )\n'
                                               'True True True True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # check for mask;\n'
                                               '>>> q  = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> k1 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k2 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> mask = (torch.ones(1, 1, 2) == 1).to(device);\n'
                                               '>>> \n'
                                               '>>> batched_Q = q.view(1, 1, -1);\n'
                                               '>>> batched_K = torch.stack([k1, k2], 0).unsqueeze(0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V, mask=mask);\n'
                                               '>>> print (batched_A.size() == torch.Size([1, 1, 2]), \n'
                                               '...        batched_C.size() == torch.Size([1, 1, 5]))\n'
                                               'True True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # check for size with mask;\n'
                                               '>>> q_len = 11;\n'
                                               '>>> k_len = 17;\n'
                                               '>>> bsz = 7;\n'
                                               '>>> D = 13;\n'
                                               '>>> \n'
                                               '>>> _ = torch.manual_seed(1234);\n'
                                               '>>> \n'
                                               '>>> batched_Q = torch.randn(bsz, q_len, D).to(device);\n'
                                               '>>> batched_K = torch.randn(bsz, k_len, D).to(device);\n'
                                               '>>> batched_V = torch.randn(bsz, k_len, D).to(device);\n'
                                               '>>> mask = torch.randn(bsz, q_len, k_len).to(device) > 0;\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V, mask=mask);\n'
                                               '>>> print (batched_A.size() == torch.Size([bsz, q_len, k_len]), \n'
                                               '...        batched_C.size() == torch.Size([bsz, q_len, D]))\n'
                                               'True True\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # check for mask;\n'
                                               '>>> # no mask, q -> k1, k2;\n'
                                               '>>> q  = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> k1 = torch.Tensor([6, 7, 8, 9, 0]).to(device);\n'
                                               '>>> k2 = torch.Tensor([1, 2, 3, 4, 5]).to(device);\n'
                                               '>>> \n'
                                               '>>> batched_Q = q.view(1, 1, -1);\n'
                                               '>>> batched_K = torch.stack([k1, k2], 0).unsqueeze(0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> \n'
                                               '>>> batched_A, batched_C = attention(batched_Q, batched_K, batched_V);\n'
                                               '>>> \n'
                                               '>>> # q -> k1, k2, k3, with mask to disallow q -> k3;\n'
                                               '>>> k3 = torch.Tensor([91, 92, 93, 94, 95]).to(device);\n'
                                               '>>> batched_K = torch.stack([k1, k2, k3], 0).unsqueeze(0);\n'
                                               '>>> batched_V = batched_K;\n'
                                               '>>> \n'
                                               '>>> mask = (torch.LongTensor([1, 1, 0]).to(device) == 1).view(1, 1, -1);\n'
                                               '>>> batched_A_m, batched_C_m = attention(batched_Q, batched_K, batched_V, mask=mask);\n'
                                               '>>> \n'
                                               '>>> print (torch.isclose(batched_A, batched_A_m[:, :, :2]).all().item(), \n'
                                               '...        torch.isclose(batched_C, batched_C_m).all().item()\n'
                                               '...       )\n'
                                               'True True\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
