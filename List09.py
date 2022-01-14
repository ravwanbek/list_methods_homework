def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """

    apple=[]
    apple_sum=fruits.count('apple')
    apple.insert(0,apple_sum)


    if fruits[0]=='apple':
        apple.insert(1,fruits.index('apple',0,1))
    
    if fruits[1]=='apple':
        apple.insert(2,fruits.index('apple',1,2))

    if fruits[2]=='apple':
        apple.insert(3,fruits.index('apple',2,3))

    if fruits[3]=='apple':
        apple.insert(4,fruits.index('apple',3,4))
    
    if fruits[4]=='apple':
        apple.insert(5,fruits.index('apple',4,5))

    return apple
print(main(['grape','apple','kiwi','apple','apple']))