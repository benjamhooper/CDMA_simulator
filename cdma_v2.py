#CDMA.py Version 2.0
#Code Division Multople Access Protocol Simulator

def encode(s,bit):
	Z=[]
	for m in range(8):
		Z.append(bit*s[m])
	return Z

def decode(s,Z):
	tot=0
	for m in range(8):
		tot = tot + (code_s1[m]*Z[m])
	di = int(tot/8)
	return di

def Z_sum(s1,s2):
	print('********Z Star********')
	Z=[]
	for m in range(8):
		Z.append(s1[m]+s2[m])
		#print('s1_{:1d} = {:2d}'.format(m,s1[m]))
		#print('s2_{:1d} = {:2d}'.format(m,s2[m]))
		print(' Z_{:1d} = {:2d}'.format(m,Z[m]))
	return Z

code_s1 = [1,1,1,-1,1,-1,-1,-1]
code_s2 = [1,-1,1,1,1,-1,1,1]

print("Encode di using cdma code...")
Z_1 = encode(code_s1,-1)
Z_2 = encode(code_s2,1)
Z_star = Z_sum(Z_1,Z_2)
print("Decode using cdma code...")
di = decode(code_s1,Z_star)
print('Decoded di = {:1d} from sender 1'.format(di))
di = decode(code_s2,Z_star)
print('Decode di = {:1d} from sender 2'.format(di))
