# Condicionais
# if, elif, else
'''
eu cheguei atrasado na aula, ainda posso entrar
Se essa não for sua terceira vez chegando atrasado então pode sim.
Caso contrário, ira tomar uma suspensão.
'''
vez_atrasado = 0
if vez_atrasado >=3:
  print('esta suspenso')
elif vez_atrasado == 1:
  print('pode entrar, porém se faltar mais 2 vzs, esta suspenso')
elif vez_atrasado ==2:
  print("pode entrar, porém se faltar mais 1 vez, esta suspenso")
else:
  print("pode entrar de boas")