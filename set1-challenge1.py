import base64
import binascii

def hexToBase64(hexstr):
    numRep = binascii.unhexlify(hexstr)
    return base64.b64encode(numRep).decode('ascii')


hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
converted = hexToBase64(hexString)
baseString = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


print ('input string:', hexString)
print ('base 64 string:', baseString)
print ('converted string:', baseString)
if converted == baseString:
    print('conversion is correct!')




