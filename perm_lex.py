def perm_gen_lex(str_in):
    if type(str_in) != str:
        raise TypeError
    if len(str_in) == 1:
        return [str_in]
    if len(str_in) == 0:
        return []
    list = []

    for charindex in range(len(str_in)):
        simpler_string = str_in[:charindex] + str_in[charindex+1:]
        permutations = perm_gen_lex(simpler_string)
        for permutation in permutations:
            permutation = str_in[charindex] + permutation
            list.append(permutation)
    
    return list

"""
For each character in the input string:
 Form a simpler string by removing the character from the input string
 Generate all permutations of the simpler string recursively (i.e. call the
perm_gen_lex function with the simpler string)
 Add the removed character to the front of each permutation of the simpler string, and
add the resulting permutation to the list"""



"""
DOCSTRING: 
string -> List of strings
Returns list of permutations for input string
e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
"""