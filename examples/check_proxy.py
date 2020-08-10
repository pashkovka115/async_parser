

j = CheckerProxy()
j.proxies_for_check = [
    '91.236.251.131:8164',
    '91.236.251.131:8255',
    '91.236.251.131:8106',
    '81.201.60.130:80',
    '91.236.251.131:8286',
    '79.137.44.85:3129',
]
print(j.save_and_return_proxies('test_proxies.txt'))

