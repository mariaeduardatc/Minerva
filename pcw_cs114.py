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


# letter b
'''
30+50*2+20*3
30 100 60 = 190 children

chance of getting chosen
1st rank (30+50+20)/190
2nd rank (50+20)/190
3rd rank 20/190

'''

def birth_rank_pmf(r):
    if r == 1:
        return 0.3*(30+50+20)/190 + 0.5*(50+20)/190+ 0.2*20/190
    
    elif r == 2:
        return 0.5*(50+20)/190 + 0.2*20/190
    
    elif r == 3:
        return 0.2*20/190

birth_rank_mean = sum([r * birth_rank_pmf(r) for r in range(1,4)])
birth_rank_variance = sum([r**2 * birth_rank_pmf(r) for r in range(1,4)]) - birth_rank_mean**2 

answer = birth_rank_pmf, birth_rank_mean, birth_rank_variance
