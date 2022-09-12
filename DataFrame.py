import pandas as pd 
df = pd.DataFrame(data=[[4, 8, 5],
                        [2, 9, 4],
                        [6, 10, 2]], index = ['Sergio', 'Felipe', 'José'],columns = ['N1', 'N2', 'F'])

#Exemplo 
if (df['N1'].iloc[0] + df['N2'].iloc[0]) / 2 >= 7 and df['F'].iloc[0] <=5:
    print(f" Sergio voce foi aprovado")
else:
    print("Reprovado")

#media geral dos alunos 
media1 = (df['N1'].iloc[0] + df['N2'].iloc[0]) / 2
media2 = (df['N1'].iloc[1] + df['N2'].iloc[1]) / 2
media3 = (df['N1'].iloc[2] + df['N2'].iloc[2]) / 2
media = (media1 + media2 + media3) / 3
print(media)
#maior media
if media1 > media2 and media1 > media3:
    print("Sergio teve  a maior media")
elif media2 > media1 and media2 > media3:
    print("Felipe teve a maior media")
elif media3 > media1  and media3 > media2:
    print("Jose teve a maior media")
#maior numero de faltas
f1 = (df['F'].iloc[0] + df['F'].iloc[0])
f2 = (df['F'].iloc[1] + df['F'].iloc[1])
f3 = (df['F'].iloc[2] + df['F'].iloc[2])
if f1 > f2 and f1 > f3:
    print("Sergio Faltou mais")
elif f2 > f1 and f2 > f3:
    print("Felipe Faltou mais")
elif f3 > f1  and f3 > f2:
    print("Jose Faltou mais")