
def nonbonus_additive_persistence(number):
    number = [int(i) for i in str(number)]
    count = 0
    while len(number) > 1:
        number = [int(i) for i in str(sum(number))]
        count +=1
    return count


def decompose(number):
    number_repr = []
    digits = len(str(number))
    for i in reversed(range(digits)):
        number_repr.append(number // 10**i)
        number = number -  (10**i)* number_repr[-1]
    return number_repr


def bonus_additive_persistence(number):
    count  = 0
    while number >= 10:
        number = sum(decompose(number))
        count += 1
    return count





print(nonbonus_additive_persistence(13))
print(nonbonus_additive_persistence(1234))
print(nonbonus_additive_persistence(9876))
print(nonbonus_additive_persistence(199))

print(bonus_additive_persistence(13))
print(bonus_additive_persistence(1234))
print(bonus_additive_persistence(9876))
print(bonus_additive_persistence(199))