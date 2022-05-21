set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.union(set2)
print(set3)

print(set1.intersection(set2))

print('set difference')
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.difference(set2)
print(set3)


print('symmmetric difference')

print(set1.symmetric_difference(set2))
print(set1 ^ set2)


print('Finding subset and supersets')

set1 = set([1,2,3,4])
set2 = set([2,3])
print(set2.issubset(set1))
print(set1.issuperset(set2))
