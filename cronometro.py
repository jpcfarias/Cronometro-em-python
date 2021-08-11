from time import sleep
import datetime

segundos = int(input('digite o numero (em segundos): '))

if(segundos < 0):
  print("numero invalido")
  exit()
else:
  pass

print('*' * 18)  
print('Cronometro')  
print('*' * 18)  
 
minutos ,segundos = divmod(segundos, 60)

while(segundos >= 0):  
  print('{0}:{1}'.format(minutos,segundos))  
  
  if segundos == 0:
    if minutos > 0:
      minutos = minutos - 1
      segundos = segundos + 60
    else:
      pass
  else:
    pass
  segundos = segundos - 1
  sleep(1)