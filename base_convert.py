# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    if num < 0:
        raise ValueError
    if b < 2 or b > 16:
        raise ValueError
    #Get numbers
    """
    quotient = int(num / b)

    remainder = num % b
    """

    quotient, remainder = divmod(num, b)
    #Convert to symbols for bases greater than 10
    if b > 10:
        if remainder == 10:
            remainder = "A"
        if remainder == 11:
            remainder = "B"
        if remainder == 12:
            remainder = "C"
        if remainder == 13:
            remainder = "D"
        if remainder == 14:
            remainder = "E"
        if remainder == 15:
            remainder = "F"
    if quotient != 0:
        return str(convert(quotient, b)) + str(remainder)
    return str(remainder)
