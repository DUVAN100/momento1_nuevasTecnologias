listWithDicctionary= [
    {"numberCheck":1},
    {"numberCheck":2
     },
    {"numberCheck":3},
    {"numberCheck":4},
    {"numberCheck":5},
    {"numberCheck":6},
    {"numberCheck":7},
    {"numberCheck":8},
    {"numberCheck":9},
    {"numberCheck":10},
]
for key in listWithDicctionary:
    key['balance'] = int( input('Type balance of the check: '))
    
sortedChecks = sorted(listWithDicctionary, key=lambda x: (x['balance']))
print(sortedChecks)
