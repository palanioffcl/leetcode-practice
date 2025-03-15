def compress_to_bytes(s):
    if not s:
        return b''

    compressed = bytearray()
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            # Handle overflow if count exceeds 255
            if count == 256:
                compressed.extend([255, ord(s[i - 1])])
                count = 1
        else:
            compressed.extend([count, ord(s[i - 1])])
            count = 1

    # Add the last group
    compressed.extend([count, ord(s[-1])])

    return bytes(compressed)




def decompress_from_bytes(compressed):
    if not compressed:
        return ""

    decompressed = []
    compressed = bytearray(compressed)

    for i in range(0, len(compressed), 2):
        count = compressed[i]
        char = chr(compressed[i + 1])
        decompressed.append(char * count)

    return ''.join(decompressed)


x = compress_to_bytes("AAABBBCCCCCC!!!DDDDDDDDDDD")
print(x, "COMPRESSED")
y = decompress_from_bytes(x)
print(y, "DECOMPRESSED")
