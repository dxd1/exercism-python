def sum_of_multiples(limit, multiples_of = [3, 5]):
    sum = 0
    for i in range(limit):
        for number in multiples_of:
            if number!=0 and number!=limit and i % number==0:
                sum+=i
                break
    return sum
