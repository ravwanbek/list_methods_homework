def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    sum_of_one_and_zero=[]
    one=list1.count(1)
    zero=list1.count(0)
    sum_of_one_and_zero.append(one)
    sum_of_one_and_zero.append(zero)

    return sum_of_one_and_zero
print(main([0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1]))