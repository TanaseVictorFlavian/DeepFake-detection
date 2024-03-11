def name_creator(counter : int , num_samples : int =100000 ):
    """
    Function to create a name for the output file for a dataset

    :param counter: the number of the current sample
    :param num_samples: the total number of samples
    
    """

    front_zeros = len(str(num_samples)) - 1
    p = 10
    while (p <= num_samples):
        if counter < p:
            return '0'*front_zeros + str(counter)
        p *= 10
        front_zeros -= 1

    return '0' * front_zeros + str(counter)

