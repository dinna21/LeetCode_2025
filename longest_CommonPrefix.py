def longestCommonFreifx(strs):
    if not strs:
        return ""
    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            # print(prefix)
            if not prefix:
                return "hi"
    return prefix

print(longestCommonFreifx(["flower", "flow", "flight"]))
print(longestCommonFreifx(["car", "hhhcar", "car"]))