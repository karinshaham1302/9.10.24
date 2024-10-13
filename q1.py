import random

# start

list_rnd: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(list_rnd)

print('list_rnd all: ', all(list_rnd))

print('list_rnd any: ', any(list_rnd))

if not any(list_rnd):
    print('all False')
else:
    print('not all False')

if not all(list_rnd):
    print('at list one False')
else:
    print('zero False')

list_rnd2: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(list_rnd2)

if all([num != 0 for num in list_rnd2]):
    print('all different from zero')
else:
    print('NOT all different from zero')

if any([num != 0 for num in list_rnd2]):
    print('at least one num is not zero')
else:
    print('everything is zero')

if all([num == 0 for num in list_rnd2]):
    print('all nums are zero')
else:
    print('NO all num is zero')

if any([num == 0 for num in list_rnd2]):
    print('at least one num is zero')
else:
    print('nothing is zero')

# stop
