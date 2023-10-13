def calc_paralel(resistanses_P):
   total_R_P = 0
   for i in resistanses_P:
      total_R_P += 1/i
   total_R_P = 1/total_R_P
   return total_R_P

def calc_serial(resistanses_S):
   total_R_S = 0
   for i in resistanses_S:
      total_R_S += i
   return total_R_S


R=[]
R = input('Ange resistorer: ')
R = R.split()
for i in range(0,len(R)):
   R[i] = float(R[i])

print(f'Serieresistan: {calc_serial(R)}')
print(f'Parallellresistans: {calc_paralel(R)}')