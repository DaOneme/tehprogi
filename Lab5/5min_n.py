import _5A6 as A
import _5B1 as B
import matplotlib.pyplot as plt

n = 1000

while True:
    res_a = A.main(n)
    res_b = B.main(n)
    if res_a > res_b:
        print(n)
        break
    n += 100
    
while True:
    res_a = A.main(n)
    res_b = B.main(n)
    if res_a < res_b:
        print(n)
        break
    
    n+= 1
    
    
    