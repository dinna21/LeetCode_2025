s = "zxyzxyz"
set_str = set(s)
# print(set_str)

max_len = 0
seen = set()
# print(seen)
start = 0
for end in range(len(s)):
    # print(end)
    while s[end] in seen:
        seen.remove(s[start])
        start+=1
    seen.add(s[end])
    max_len = max(max_len,end -start+1)
print(max_len)