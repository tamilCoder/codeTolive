def manachers_algorithm( S ):

    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    S1 = '#'.join('^{}$'.format(S))

    # used tracking the expand length around all indices
    LPS = [0] * len(S1)

    # used for tracking the center of largest palindrome thus far
    # and its right boundary
    center = right = 0

    for i in range(1, len(S1) - 1):

        # Checking if new palindrome
        # around i lies within a bigger palindrome
        # If so, copy expand length of its mirror or right - i
        mirror = 2 * center - i
        if i < right:
            LPS[i] = min(right - i, LPS[mirror])

        # Expanding around new center
        # Update expand length at i as needed
        while S1[i + LPS[i] + 1] == S1[i - (LPS[i] + 1)]:
            LPS[i] += 1

        # If we breached previous right boundary
        # Make i the new center of the longest palin
        # and update right boundary
        if i + LPS[i] > right:
            right = i + LPS[i]
            center = i

    max_len, centerIndex = max((j, i) for i, j in enumerate(LPS))
    return S[(centerIndex  - max_len)//2: (centerIndex  + max_len)//2]
print(manachers_algorithm('abababababababab'))
