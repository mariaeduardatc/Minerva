'''
Explanation:

- Population 100 families
- 30 families (1)
- 50 families (1, 2)
- 20 families (1, 2, 3)

Family hs the same probability to be chosen (1/100)
A child has the same probability to be chosen (1/30, 1/50, 1/20)



'''

# rank
def birth_rank_pmf(r):

    # family probabilities
    p1 = 30/100
    p2 = 50/100
    p3 = 20/100 
    
    # 1st rank
    if r == 1: 
        return p1 + 1/2*p2 + (1/3)*p3
    # 2nd rank
    elif r == 2:
        return 1/2*p2 + (1/3)*p3
    # 3rd rank
    else:
        return (1/3)*p3


# expected value 
birth_rank_mean = birth_rank_pmf(1) + 2*birth_rank_pmf(2) + 3*birth_rank_pmf(3)

# E(x^2)
ex_2 = birth_rank_pmf(1) + 4*birth_rank_pmf(2) + 9*birth_rank_pmf(3)

birth_rank_variance = ex_2 - birth_rank_mean**2

answer = birth_rank_pmf, birth_rank_mean, birth_rank_variance