
from Correlations import HFCorrelations

case = HFCorrelations()
print(case.hammerschmidt(1, 50) , "\n")
print('-'*500)

print(case.bahadori_and_vuthaluru(1, 50, 0.8))

aa = case.bahadori_and_vuthaluru(1, 50, 0.8)
x, y = [], []
for i in range(len(aa)):
    x.append(aa[i][0])
    y.append(aa[i][1])
print(x)
print(y)
print('-'*500)

print(case.towler_and_mokhatab(1, 50, 0.8))
print('-'*500)

print(case.berge(1, 50, 0.8))
print('-'*500)

print(case.holder_et_al(1, 50))
print('-'*500)

print(case.motiee(1, 50, 0.8))
print('-'*500)

print(case.aut(1, 50, 0.8))
print('-'*500)

print(case.kobayashi_et_al(1, 50, 0.8))
print('-'*500)
print("The End")

