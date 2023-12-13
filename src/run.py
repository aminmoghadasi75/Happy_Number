def happy_num(x : int)->str :
    """
    Determines if a number is a Happy Number.

    A Happy Number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.

    :param x: The number to check for happiness.
    :type x: int
    :return: A message indicating whether the number is a Happy Number or not.
    :rtype: str
    """
    num = x
    set_num = set()
    while num != 1 and num not in set_num :
        set_num.add(num)
        n = sum([int(i)**2  for i in str(num)])
        num = n
    if num == 1 :
        print (f"{x} --> Happy Number :)")
        return True
    else :
        print (f"{x} -->  is Not a Happy Number :( ")
        return False

if __name__ == '__main__' :
    assert happy_num(7) is True
    assert happy_num(13) is True
    assert happy_num(45) is False
    assert happy_num(99) is False
