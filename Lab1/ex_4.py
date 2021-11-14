
def encoding_algorim(seq):
    result = []
    count = 0
    for i in range(0, len(seq)):
        if seq[i] == '0':
            count = count + 1
        else: #No es 0
            if (count != 0):
                result.append('0')
                result.append(count)
                count = 0
                if seq[i] != '0':
                    result.append(seq[i])
            else:
                result.append(seq[i])

    return result


# Function to convert
def listToString(s):
    str1 = ""
    for i in range(0,len(s)):
        str1 += str(s[i])
    return str1

if __name__ == "__main__":
    seq = '00011000110001'
    print('Original', seq)
    list1 = encoding_algorim(seq)
    compressed_seq = listToString(list1)
    print('Compress ', compressed_seq)