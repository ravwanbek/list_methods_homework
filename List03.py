def main(fruits1, fruits2):
    """
    You will be given a list of several fruits called fruits1 and fruits2. Return the result by adding the second to the first list.
    Args:
        fruits1(list): parameter
        fruits2(list): parameter
    Returns:
        list: return answer
    """
    f=fruits1+fruits2
    return f
print(main(['apple','kiwi'],['orange']))