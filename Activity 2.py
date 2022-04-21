import random

lvl = 90
power = 110
attack = 205
defense = 188

target = 1
weather = 1
badge = 1
crit = 1
rndm = round(random.uniform(0.85,1.0),2)
stab = 1.5
type = 0.5
burn = 1
modifier = target*weather*badge*crit*rndm*stab*type*burn*1

damage = ((2*lvl)/5)+2
damage = (damage*power)*(attack/defense)
damage = ((damage/50)+2)*modifier

print(round(damage))
print("random number = "+str(rndm))

