def minOperations(s):
    s = list(s)
    # Write your code here
    if len(s) == 1:
        return 0
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
            if s[i] == '0':
                s[i] = '1'
            else:
                s[i] = '0'
    return min(count, len(s)-count)
