def name_creator(counter, num_samples=100000):
    """
    Function to create a name for the output file for a dataset
    """

    front_zeros = len(str(num_samples)) - 1
    p = 10
    while (p <= num_samples):
        if counter < p:
            return '0'*front_zeros + str(counter)
        p *= 10
        front_zeros -= 1

    return '0' * front_zeros + str(counter)

