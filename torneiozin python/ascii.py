#"/usr/bin/python3"

ascii = [' ','!','\"','#','$','%','&','\'','*','+',',','-','.',
         '/','0','1','2','3','4','5','6','7','8','9',':',';',
         '<','=','>','?','@','A','B','C','D','E','F','G','H',
         'I','J','K','L','M','N','O','P','Q','R','S','T','U',
         'V','W','X','Y','Z','[','\\',']','^','_','`','a','b',
         'c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z','{','|',
         '}','~']

ascii_str = ''.join(ascii)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift_text(text, shift):
    shifted_table = ascii_str[shift:] + ascii_str[:shift]
    return text.translate(text.maketrans(ascii_str, shifted_table))

testCases = int(input())

for i in range(0, testCases):
    message = list(input())
    for i in range(0, len(message)):
        if message[i] in letters:
            message[i] = shift_text(message[i], 3)
    message = message[::-1]

    for i in range(int(len(message) / 2), len(message)):
        message[i] = shift_text(message[i], -1)
    print(''.join(message))

    
    