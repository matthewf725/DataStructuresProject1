# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n < 42:
        return False
    
        #Base case
    if n == 42:
        return True

    #If n is even, then you may give back n//2 bears.
    if n % 2 == 0 and bears((n - n//2)):
        return True
    #2. If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
    if n % 3 == 0 or n % 4 == 0:
        secondLast = str(n)[-2]
        last = str(n)[-1]
        bearCount = int(last) * int(secondLast)
        if bearCount > 0 and bears(n - bearCount):
            return True
    #3. If n is divisible by 5, then you may give back 42 bears.
    if n % 5 == 0 and bears(n - 42):
        return True
    
    return False

#33333333333333333333333333333333
