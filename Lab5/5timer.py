import _5A6 as A
import _5B1 as B
import matplotlib.pyplot as plt

n = [10,100,500,1000]
res_a = A.main(10,100,500,1000)
res_b = B.main(10,100,500,1000)


plt.figure(figsize=(10, 6))
plt.plot(n, res_a, label='A', marker='o')
plt.plot(n, res_b, label='B', marker='s')
plt.xlabel('n')
plt.ylabel('Значение')
plt.title('Графики результатов A и B')
plt.legend()
plt.grid(True)
plt.show()