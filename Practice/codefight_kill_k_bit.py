def killKthBit(n, k):
	return n - int(n & (1<<(k-1))) if n & (1<< (k - 1)) else n 

print(killKthBit(37, 3))
print(killKthBit(37, 4))