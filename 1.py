import numpy as np
P = 'wuxiaofeng'
print(P)
P = list(map(ord,P))
K = 3
P = np.array(P)
P = P - ord('a')
C = (P + K) % 26
C = C + ord('A')
C = list(map(chr,C))
print(''.join(C))

D = list(map(ord,C))
D = np.array(D)
D = D - ord('A')
D = (D - K) % 26
D = D + ord('a')
D = list(map(chr,D))
print(''.join(D))
