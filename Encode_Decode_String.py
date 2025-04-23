strs = ["we","say",":","yes"]
def encode(strs):
    encode_str = []
    for states in strs:
        encode_str.append(f"{len(states)}/{states}")
    return ''.join(encode_str)


def decode(strs):
    decode = []
    # for s in strs:
    i = 0
    while i < len(strs):
        slash = strs.index('/',i)
        length = int(strs[i:slash])
        decode.append(strs[slash+1:slash+1+length])
        i = slash+1+length
    return decode


strs = ["we","say",":","yes"]
encoded_str = encode(strs)
print(encoded_str)  # Output: "2/we3/say1/:3/yes"
decoded_strs = decode(encoded_str)
print(decoded_strs) 