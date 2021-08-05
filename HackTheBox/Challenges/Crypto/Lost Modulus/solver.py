import sys
try:
	import gmpy2
except ImportError:
	print("Install gmpy2 first to run this program")
	sys.exit()

import gmpy2

flag = open('flag.txt', 'r').read()

cipher=int(flag, 16)


with gmpy2.local_context(gmpy2.context(), precision=800) as ctx:
 ctx.precision += 800
 root = gmpy2.cbrt(cipher)

try:
	print(hex(int(root))[2:].decode())
except AttributeError:
	print(bytes.fromhex(str('%x' % + int(root))).decode('utf-8'))
