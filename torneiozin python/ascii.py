#"/usr/bin/python3"

ascii_str = "!\"#$%&'*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift_text(text, shift):
    shifted_table = ascii_str[shift:] + ascii_str[:shift]
    return text.translate(text.maketrans(ascii_str, shifted_table))

testCases = int(input())
result = ''

for i in range(0, testCases):
    message = list(input())
    for i in range(0, len(message)):
        if message[i] in letters:
            message[i] = shift_text(message[i], 3)
    message.reverse()

    for i in range(int(len(message) / 2), len(message)):
        message[i] = shift_text(message[i], -1)
    result += ''.join(message)

print(result)
    
    