#!/usr/bin/python

import struct
import intelhex
import sys


def crc16(data):
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        crc ^= b << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1
        crc &= 0xffff

    return crc


if len(sys.argv) != 2:
    print('Please specify VBF file')
    quit(-1)

inname = sys.argv[1]

with open(inname, 'rb') as f:
    data = f.read()


# search for header end
patterns = [ b';\r\n}', b';\r\n\r\n}' ]
for p in patterns:
    header_len = data.find(p)
    if header_len > 0:
        header_len += len(p)
        break

print('Header length: 0x%04X' % header_len)

if header_len < 100:
    print('Header too short! Unknown format')
    quit(-1)


out_hex = intelhex.IntelHex()

offset = header_len
while offset < len(data):

    [block_addr, block_len] = struct.unpack('>2L', data[offset: offset + 8])
    offset += 8

    block_data = bytearray(data[offset: offset + block_len])
    offset += block_len

    crc = struct.unpack('>H', data[offset: offset + 2])[0]
    offset += 2

    crc_res = 'ok' if crc16(block_data) == crc else 'error'
    print("Block adr: 0x%X length: 0x%X crc %s" % (block_addr, block_len, crc_res))

    out_hex.frombytes(block_data, block_addr)


out_hex.tofile(inname + '.hex', 'hex')
out_hex.tofile(inname + '.bin', 'bin')
