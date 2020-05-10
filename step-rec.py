# Sabendo que podemos subir uma escada de um em um degrau
# ou de dois em dois;
# Quantas maneiras diferentes podemos subir
# uma escada de N degraus ?
# =)
# 
#

def step(x):
	if x == 2:
		return 2

	if x <= 1:
		return 1

	return step(x-1) + step(x-2)


print(step(5))