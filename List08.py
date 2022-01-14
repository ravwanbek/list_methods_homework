def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    not_apple=[]
    if fruits[0]!='apple':
        not_apple.insert(0,fruits[0])
    
    if fruits[1]!='apple':
        not_apple.insert(1,fruits[1])

    if fruits[2]!='apple':
        not_apple.insert(2,fruits[2])

    if fruits[3]!='apple':
        not_apple.insert(3,fruits[3])
    
    if fruits[4]!='apple':
        not_apple.insert(4,fruits[4])
    
    
    return not_apple
print(main(['apple','apple','orange','kiwi','apple']))