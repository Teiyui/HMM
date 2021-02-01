import math

# Transaction Probabilities
p_ss = 0.8
p_sr = 0.2
p_rr = 0.6
p_rs = 0.4

# Initial Probabilities
p_s = 2/3
p_r = 1/3

# Emission Probabilities (bad and happy)
p_hs = 0.8
p_bs = 0.2
p_hr = 0.4
p_br = 0.6

moods = ['B', 'H', 'H', 'B', 'B', 'H']
probabilities = []
weather = []

if moods[0] == 'H':
    p_sI = p_s * p_hs
    p_rI = p_r * p_hr
    probabilities.append((p_sI, p_rI))
else:
    p_sI = p_s * p_bs
    p_rI = p_r * p_br
    probabilities.append((p_sI, p_rI))

for i in range(1, len(moods)):
    if moods[i] == 'H':
        p_ssP = probabilities[i-1][0] * p_ss * p_hs
        p_rsP = probabilities[i-1][1] * p_rs * p_hr
        p_sP = max(p_ssP, p_rsP)
        p_srP = probabilities[i-1][0] * p_sr * p_hs
        p_rrP = probabilities[i-1][1] * p_rr * p_hr
        p_rP = max(p_srP, p_rrP)
        probabilities.append((p_sP, p_rP))
    else:
        p_ssP = probabilities[i - 1][0] * p_ss * p_bs
        p_rsP = probabilities[i - 1][1] * p_rs * p_br
        p_sP = max(p_ssP, p_rsP)
        p_srP = probabilities[i - 1][0] * p_sr * p_bs
        p_rrP = probabilities[i - 1][1] * p_rr * p_br
        p_rP = max(p_srP, p_rrP)
        probabilities.append((p_sP, p_rP))

for j in range(len(probabilities)):
    pro = probabilities[j]
    if pro[0] > pro[1]:
        weather.append('S')
    else:
        weather.append('R')

print(weather)