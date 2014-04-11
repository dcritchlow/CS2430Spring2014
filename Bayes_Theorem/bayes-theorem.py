#!/usr/bin/env python

# ===================================================================#
#    Functions
# ===================================================================#
def get_sum(sample_space, f_name='', e_name=''):
    """ Sum the total for the probability condition """
    sum = 0
    for k_1, v_1 in sample_space.items():
        if f_name == k_1:
            for k_2, v_2 in v_1.items():
                if e_name == k_2:
                    sum+=v_2
                elif e_name=='':
                    sum+=v_2
        if f_name=='':
            for k_2, v_2 in v_1.items():
                if e_name == '':
                    sum+=v_2
    return float(sum)

def p(sample_space, f_name):
    """ Calculate Probability of one condition """
    return get_sum(
        sample_space, f_name) / get_sum(sample_space, '', '')

def p_independent(sample_space, f_name, e_name):
    """ Calculate Probability of two independent variables """
    return get_sum(sample_space, f_name, e_name) / get_sum(
        sample_space, '', '')

def p_conditional(sample_space, f_name, e_name):
    """ Calculates Probability of two conditional variables """
    return p_independent(sample_space, f_name, e_name) / p(
        sample_space, f_name)

def bayes(sample_space, f, given_e):
    """
        Calculates Bayesian statistics of variable with a given known
        variable
    """
    sum = 0;
    for key, val in sample_space.items():
        sum+=p(sample_space, key) * p_conditional(
            sample_space, key, given_e)
    return p(sample_space, f) * p_conditional(
        sample_space, f, given_e) / sum

# ===================================================================#
#    Main
# ===================================================================#
if __name__ == "__main__":
    # Disease problem (example 2 in Ch 7 module)
    sample_space = {"Disease": {"Pos": .009, "Neg": .001}, "Healthy":\
        {"Pos": .1485, "Neg": .8415}}
    print 'Probability that they have the Disease and test positive:',\
        bayes(sample_space,'Disease', 'Pos')

    # Stock problem (example 3 in Ch 7 module)
    sample_space = {"Grows": {"Up": .56, "Down": .14},\
        "Slows": {"Up": .09, "Down": .21}}
    print 'Probability economy is growing when stock is Up:',\
        bayes(sample_space,'Grows', 'Up')

    # "French Guy" problem (example 4 in Ch 7 module)
    sample_space = {'UK':{'Boy':10, 'Girl':20},\
        'FR':{'Boy':10, 'Girl':10},'CA':{'Boy':10, 'Girl':30}}
    print 'Probability of being from France:', p(sample_space, 'FR')
    print 'Probability of being a French Boy:', p_independent(
        sample_space, 'FR', 'Boy')
    print 'Probability of being a Boy given a person is from France:', \
        p_conditional(sample_space, 'FR', 'Boy')
    print 'Probability of being from France given a person is a Boy:',\
        bayes(sample_space, 'FR', 'Boy')

    sample_space = {'Urn 1': {'Blue': 2,'Red': 8},\
        'Urn 2': {'Blue': 12, 'Red': 3}}
    print'Probability of being from Urn 1 given the token is blue:', \
        bayes(sample_space, 'Urn 1', 'Blue')
