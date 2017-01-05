# You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Example:

# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".


def longest_consec(strarr, k):
    str = ''
    if len(strarr) == 0 or len(strarr) < k or k <= 0: return str
    else:
        for i in range(0, len(strarr) - k + 1):
            if len(''.join(strarr[i:(i+k)])) > len(str): str = ''.join(strarr[i:(i+k)])
        return str
