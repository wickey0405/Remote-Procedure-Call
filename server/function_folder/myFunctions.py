import math

def floor(params, param_types):
    if type(params) == float or (len(param_types) == 0 and param_types[0] == "float"):
        return math.floor(params), "int"
    return None, "error"

def nroot(params, param_types):
    if len(params) != 2: return None, "error"

    n = params[0]
    x = params[1]
    if type(n) == int and type(x) == int:
        return math.pow(x, 1/n), "float"
    return None, "error"
    
def reverse(params, param_types):
    if type(params) != str: return None, "error"

    ans = params[::-1]
    return ans, "string"

def validAnagram(params, param_types):
    if len(params) != 2: return None, "error"

    s1 = params[0]
    s2 = params[1]
    if type(s1) != str or type(s2) != str: return None, "error"

    s1.replace(' ', '')
    s2.replace(' ', '')
    for x in s1: s2 = s2.replace(x, '', 1)
    return len(s2) == 0, "boolean"

def sort(params, param_types):
    check = [x for x in params if type(x) != str]
    if len(check) != 0: return None, "error"
    
    ans = sorted(params)
    return ans, "List<string>"
