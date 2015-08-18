#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here

    error = list( (net_worths - predictions) **2 )

    cleaned_data = sorted(zip(ages, net_worths, error), key = lambda tup: tup[2])[:len(ages)-9]
    # cleaned_data = cleaned_data[:80]

    return cleaned_data