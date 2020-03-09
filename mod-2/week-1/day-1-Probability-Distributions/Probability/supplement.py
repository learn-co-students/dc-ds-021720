
for letter in A:
    for number in B:
        element = (letter, number)
        product_of_AB.append(element)
product_of_AB

def fact(n):
    if n<0:
        print('Factorials are defined for non-negative numbers')
    # Note that n=0 is an exceptional case
    if n==0:
        return 1
    # for any non-zero n
    while n>0:
        # if n=1 then the result should be just 1
        if n ==1:
            return 1
        #otherwise the result is n times fact(n-1)
        else:
            return n*fact(n-1)

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

set(itertools.permutations([2 , 4, 7, 2]))