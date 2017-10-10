import binascii


def xorNums(first, second):
    return first ^ second


originalBuffer = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
testBuffer = binascii.unhexlify('686974207468652062756c6c277320657965')


targetBuffer = binascii.unhexlify('746865206b696420646f6e277420706c6179')

#resultBuffer = xorNums(originalBuffer, testBuffer)

print("original", originalBuffer)
print ("test", testBuffer)
print("target", targetBuffer)
#print("result", resultBuffer)

#if resultBuffer == targetBuffer:
 #   print("XORing successful!")

