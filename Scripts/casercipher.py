import pyperclip
print ("Enter the message that to be encrypted")
message = input()

print ("Enter the key")
key = input()

mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTER.find(symbol)
        if mode == 'encrypt':
            num = num + key
            
        elif mode == 'decrypt':
             num = num - key
             
        if num >= len(LETTERS):
            num = num - len(LETTERS)
            
        elif num < 0:
             num = num + len(LETTERS)
             translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
        print(translated)
        pyperclip.copy(translated)
