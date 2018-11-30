import numpy as np

pw = 1.023 # g cm-3
pa = 0.997 # g cm-3
fH = 0.7
V = 6.06 # L
A = 450 # cm2
BT = 0.000416 # mol kg-1
KB = 2.53e-9 # mol kg-1
Kw = 6.06e-14 # (mol kg-1)2
K1 = 1.42e-6 # mol kg-1
K2 = 1.08e-9 #mol kg-1

pH = 8.000
AT = 2200 #umol kg-1
AT *= 1e-6 #mol kg-1

Hp = 10 ** (- pH) / fH
AC = AT - KB / (KB + Hp) * BT - Kw / Hp + Hp
print(AC)

CO2 = AC * Hp ** 2 / (K1 * (Hp + 2 * K2))
HCO3 = AC * Hp / (Hp + 2 * K2)
CO3 = AC * K2 / (Hp + 2 * K2)

CT = CO2 + HCO3 + CO3

print(CT)
