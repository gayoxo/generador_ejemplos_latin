import pandas as pd
import re
from bs4 import BeautifulSoup
import requests
import random
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel


# FastAPI Settings
app = FastAPI()
CORS_ORIGINS = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




path_file_v = 'data/verbos_modded.xlsx'
path_file_s = 'data/sustantivos.xlsx'
hoja = 'Hoja1'


df_v = pd.read_excel(path_file_v, sheet_name=hoja)
df_s = pd.read_excel(path_file_s, sheet_name=hoja)

# Organizamos la información de la tabla de verbos en listas
ve = df_v[['VERBOS']].to_string(header=False, index=False)
verbos = []
b = ve.split('\n')
for word in b:
    word = word.split()
    if len(word)>1:
        verbos.append(word[0][:-1])
    else:
        verbos.append(word[0])
# ------------------------------------------------------------------------------------------
ca1 = df_v[['CASO A1']].to_string(header=False, index=False)
caso1 = []
b = ca1.split('\n')
for word in b:
    caso1.append(word.lstrip())
# ------------------------------------------------------------------------------------------
arg1 = df_v[['RASGO A1']].to_string(header=False, index=False)
argumento1 = []
b = arg1.split('\n')
for word in b:
    argumento1.append(word.lstrip())
# ------------------------------------------------------------------------------------------
ca2 = df_v[['CASO A2']].to_string(header=False, index=False)
caso2 = []
b = ca2.split('\n')
for word in b:
    caso2.append(word.lstrip())
# ------------------------------------------------------------------------------------------
arg2 = df_v[['RASGO A2']].to_string(header=False, index=False)
argumento2 = []
b = arg2.split('\n')
for word in b:
    argumento2.append(word.lstrip())
# ------------------------------------------------------------------------------------------
ca3 = df_v[['CASO A3']].to_string(header=False, index=False)
caso3 = []
b = ca3.split('\n')
for word in b:
    caso3.append(word.lstrip())
# ------------------------------------------------------------------------------------------
arg3 = df_v[['RASGO A3']].to_string(header=False, index=False)
argumento3 = []
b = arg3.split('\n')
for word in b:
    argumento3.append(word.lstrip())
# ------------------------------------------------------------------------------------------
va = df_v[['VALENCIAS']].to_string(header=False, index=False)
valencias = []
b = va.split('\n')
for word in b:
    valencias.append(word.lstrip())


# Por cada verbo se crea una lista con sus características y se almacena en una lista general
datos_verbales_list = []
for i, v in enumerate(verbos):
    for ind_ca1, ca1 in enumerate(caso1):
        if i == ind_ca1:
            super_caso1 = ca1
    for ind_ca2, ca2 in enumerate(caso2):
        if i == ind_ca2:
            super_caso2 = ca2
    for ind_ca3, ca3 in enumerate(caso3):
        if i == ind_ca3:
            super_caso3 = ca3
    for ind_ar1, arg_ar1 in enumerate(argumento1):
        if i == ind_ar1:
            super_argumento1 = arg_ar1
    for ind_ar2, arg_ar2 in enumerate(argumento2):
        if i == ind_ar2:
            super_argumento2 = arg_ar2
    for ind_ar3, arg_ar3 in enumerate(argumento3):
        if i == ind_ar3:
            super_argumento3 = arg_ar3
    for ind_val, val in enumerate(valencias):
        if i == ind_val:
            super_valencias = val 
    

    datos_verbales_list.append(
        [v, super_caso1, super_argumento1, super_caso2, super_argumento2, super_caso3, super_argumento3, super_valencias])



# Creamos los dataframes según la caracterización léxica
df_A_and_H = df_s.loc[df_s['Caracterización Léxica'] == '+animado +humano']
df_A_not_H = df_s.loc[df_s['Caracterización Léxica'] == '+animado -humano']
df_D = df_s.loc[df_s['Caracterización Léxica'] == '-animado +definido']
df_not_D = df_s.loc[df_s['Caracterización Léxica'] == '-animado -definido']
df_l = df_s.loc[df_s['Caracterización Léxica'] == 'lugar']

# Ahora los dataframes de los papeles temáticos
df_user = df_s.loc[df_s['User'] == 'y']
df_poseedor = df_s.loc[df_s['Poseedor'] == 'y']
df_mover = df_s.loc[df_s['Mover'] == 'y']
df_content = df_s.loc[df_s['Content'] == 'y']
df_implement = df_s.loc[df_s['Implement'] == 'y']
df_posesion = df_s.loc[df_s['Posesion'] == 'y']
df_judgment = df_s.loc[df_s['Judgment'] == 'y']
df_situacion = df_s.loc[df_s['Situación'] == 'y']
df_emocion = df_s.loc[df_s['Emoción'] == 'y']
df_performance = df_s.loc[df_s['Performance'] == 'y']

# Creamos las listas de los sustantivos con cierto papel temático
a = df_A_and_H[['Descripción']].to_string(header=False, index=False)
A_and_H = []
A_and_H_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    A_and_H.append(word[0][:-1])
    A_and_H_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_A_not_H[['Descripción']].to_string(header=False, index=False)
A_not_H = []
A_not_H_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    A_not_H.append(word[0][:-1])
    A_not_H_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_D[['Descripción']].to_string(header=False, index=False)
d = []
d_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    d.append(word[0][:-1])
    d_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_l[['Descripción']].to_string(header=False, index=False)
lu = []
lu_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    lu.append(word[0][:-1])
    lu_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_user[['Descripción']].to_string(header=False, index=False)
user = []
user_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    user.append(word[0][:-1])
    user_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_poseedor[['Descripción']].to_string(header=False, index=False)
poseedor = []
poseedor_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    poseedor.append(word[0][:-1])
    poseedor_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_mover[['Descripción']].to_string(header=False, index=False)
mover = []
mover_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    mover.append(word[0][:-1])
    mover_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_content[['Descripción']].to_string(header=False, index=False)
content = []
content_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    content.append(word[0][:-1])
    content_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_implement[['Descripción']].to_string(header=False, index=False)
implement = []
implement_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    implement.append(word[0][:-1])
    implement_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_posesion[['Descripción']].to_string(header=False, index=False)
posesion = []
posesion_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    posesion.append(word[0][:-1])
    posesion_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_judgment[['Descripción']].to_string(header=False, index=False)
judgment = []
judgment_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    judgment.append(word[0][:-1])
    judgment_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_situacion[['Descripción']].to_string(header=False, index=False)
situacion = []
situacion_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    situacion.append(word[0][:-1])
    situacion_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_emocion[['Descripción']].to_string(header=False, index=False)
emocion = []
emocion_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    emocion.append(word[0][:-1])
    emocion_esp.append(word[2])
# ------------------------------------------------------------------------------------------
a = df_performance[['Descripción']].to_string(header=False, index=False)
performance = []
performance_esp = []
b = a.split('\n')
for word in b:
    word = word.split()
    performance.append(word[0][:-1])
    performance_esp.append(word[2])


# Creamos el resto de listas con los papeles temáticos
entidad = A_and_H + A_not_H + d
paciente_e = A_and_H + A_not_H
paciente_c = d
numeral = ['40kg', '35kg', '30kg']
h_content = content + user
h_implement = implement + user
h_lugar = user + lu
implemen_content = implement + content
mover_creation = mover + implement
h_situation = mover + situacion
paciente = paciente_e + paciente_c    



#Almacenamos estas listas en tres listas más grandes
super_lista_papeles_tematicos = [user, entidad, paciente_e, paciente_c, poseedor, A_and_H, lu, mover, h_content,
                                 h_implement, implement]
mega_lista_papeles_tematicos = [user, lu, entidad, paciente_e, paciente_c, numeral, content, implement, h_content,
                                posesion, judgment, implemen_content, poseedor, h_lugar, mover_creation, situacion,
                                emocion, h_situation, performance, paciente]
hiper_lista_papeles_tematicos = [user, entidad, h_content, lu, content, h_lugar, implemen_content, user, situacion,
                                 h_situation]



# Función para analizar el papel que tiene el primer argumento y elegir un sustantivo en base a eso:
def eleccion_verbal_arg1(arg_v1, lista_papeles):
   
    arg_v1 = str(arg_v1)
    
    if arg_v1 == 'Judger' or arg_v1 == 'Cognizer' or arg_v1 == 'Emoter' or arg_v1 == 'User' or arg_v1 == 'Creator' or arg_v1 == 'Causante' or arg_v1 == 'Wanter' or arg_v1 == 'Performer':
        mini_lista = lista_papeles[0]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Entidad':
        mini_lista = lista_papeles[1]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Paciente-E' or arg_v1 == 'Target':
        mini_lista = lista_papeles[2]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Paciente-C':
        mini_lista = lista_papeles[3]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Poseedor' or arg_v1 == 'Consumer' or arg_v1 == 'Observer' or arg_v1 == 'Perciever':
        mini_lista = lista_papeles[4]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == '+animado +humano':
        mini_lista = lista_papeles[0]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Lugar':
        mini_lista = lista_papeles[6]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Mover':
        mini_lista = lista_papeles[7]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]
        

    elif arg_v1 == 'H-Judgment':
        mini_lista = lista_papeles[8]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'H-Implement':
        mini_lista = lista_papeles[9]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v1 == 'Implement':
        mini_lista = lista_papeles[10]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]
        

    return salida

# Argumento 2
def eleccion_verbal_arg2(arg_v2, lista_papeles, li_verbos):
    
    arg_v2 = str(arg_v2)

    if arg_v2 == '+animado +humano' or arg_v2 == 'Experiencer':
        mini_lista = lista_papeles[0]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Entidad':
        mini_lista = lista_papeles[2]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Lugar':
        mini_lista = lista_papeles[1]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Paciente-E' or arg_v2 == 'Target':
        mini_lista = lista_papeles[3]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Paciente-C':
        mini_lista = lista_papeles[4]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Numeral':
        mini_lista = lista_papeles[5]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Content':
        mini_lista = lista_papeles[6]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]
        

    elif arg_v2 == 'Implement' or arg_v2 == 'Stimulus' or arg_v2 == 'Creation':
        mini_lista = lista_papeles[7]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'H-Judgmen' or arg_v2 == 'H-Sensatio':
        mini_lista = lista_papeles[8]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Posesión':
        mini_lista = lista_papeles[9]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Judgment':
        mini_lista = lista_papeles[10]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Implemen-Conten':
        mini_lista = lista_papeles[11]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v2 == 'Poseedor' or arg_v2 == 'Consumer' or arg_v2 == 'Observer' or arg_v2 == 'Perciever' or arg_v2 == 'Mover':
        mini_lista = lista_papeles[12]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'H-Luga':
        mini_lista = lista_papeles[13]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'Move-Creatio':
        mini_lista = lista_papeles[14]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'Deseo' or arg_v2 == 'Situación':
        mini_lista = lista_papeles[15]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'Emoción' or arg_v2 == 'Sensation':
        mini_lista = lista_papeles[16]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'H-Situatio':
        mini_lista = lista_papeles[17]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'Performance':
        mini_lista = lista_papeles[18]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v2 == 'Paciente':
        mini_lista = lista_papeles[19]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]

        
    elif arg_v2 == 'Verbo':
        salida = random.choice(li_verbos)[0]


    return salida

# Argumento3
def eleccion_verbal_arg3(arg_v3, lista_papeles, li_verbos):
    
    arg_v3 = str(arg_v3)

    if arg_v3 == '+animado +humano' or arg_v3 == 'Poseedor':
        mini_lista = lista_papeles[0]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]
        

    elif arg_v3 == 'Entidad':
        mini_lista = lista_papeles[1]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v3 == 'H-Conten':
        mini_lista = lista_papeles[2]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v3 == 'Lugar':
        mini_lista = lista_papeles[3]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v3 == 'Content':
        mini_lista = lista_papeles[4]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v3 == 'H-Luga':
        mini_lista = lista_papeles[5]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v3 == 'Implemen-Conten':
        mini_lista = lista_papeles[6]
        i_verb = random.choice(range(len(mini_lista)))
        salida = mini_lista[i_verb]


    elif arg_v3 == 'Judger' or arg_v3 == 'Cognizer' or arg_v3 == 'Emoter' or arg_v3 == 'User' or arg_v3 == 'Creator' or arg_v3 == 'Causante' or arg_v3 == 'Wanter' or arg_v3 == 'Performer':
        mini_lista = lista_papeles[7]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v3 == 'Deseo' or arg_v3 == 'Situación':
        mini_lista = lista_papeles[8]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]


    elif arg_v3 == 'H-Situatio':
        mini_lista = lista_papeles[9]
        inde = random.choice(range(len(mini_lista)))
        salida = mini_lista[inde]

        
    elif arg_v3 == 'Verbo':
        salida = random.choice(li_verbos)[0]


    return salida

class query(BaseModel):
    query: str


@app.post("/gen")
def main(q:query) -> str:
    # Por último pedimos al usuario que introduzca un verbo
    selec = q.query

    if selec not in verbos:
        return 'ERROR IN DATA'
    # Seleccion de reglas verbales

    monoval = False
    bival = False
    trival = False

    for verbo in datos_verbales_list:
        if selec == verbo[0]:
            if verbo[7] == 'MONOVALENTE':
                monoval = True
                
            elif verbo[7]== 'BIVALENTE':
                bival = True 

            elif verbo[7]== 'TRIVALENTE':
                trival = True

            else:
                print('Critical Error')
                quit()
            break

    if monoval:
        argumento1 = eleccion_verbal_arg1(verbo[2], super_lista_papeles_tematicos)
        
    elif bival:
        argumento1 = eleccion_verbal_arg1(verbo[2], super_lista_papeles_tematicos)
        argumento2 = eleccion_verbal_arg2(verbo[4], mega_lista_papeles_tematicos, datos_verbales_list)
        
    elif trival:
        argumento1 = eleccion_verbal_arg1(verbo[2], super_lista_papeles_tematicos)
        argumento2 = eleccion_verbal_arg2(verbo[4], mega_lista_papeles_tematicos, datos_verbales_list)
        argumento3 = eleccion_verbal_arg3(verbo[6], hiper_lista_papeles_tematicos, datos_verbales_list)


    # Declinación (a partir del https://www.online-latin-dictionary.com/latin-dictionary-flexion.php?parola=)
    coda = selec[-1]
    if coda == str(2) or coda == str(3):
        url = f'https://www.online-latin-dictionary.com/latin-dictionary-flexion.php?parola={selec[:-1]}'
    else:
        url = f'https://www.online-latin-dictionary.com/latin-dictionary-flexion.php?parola={selec}'

    # Declinación verbal
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    a = soup.find('div', class_='col span_1_of_2')
    for x in a:
        for i, y in enumerate(x):
            if i == 7:
                for index, w in enumerate(y):
                    if index == 1:
                        verbo_conjugado = re.sub(r'<.+?>', '', str(w)).strip()
                        
                        break
    # Declinación Argumento 2
    if not monoval:
        url = f'https://www.online-latin-dictionary.com/latin-dictionary-flexion.php?parola={argumento2}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        a = soup.find('div', class_='col span_1_of_2')
        for x in a:
            if x.name == 'table':
                for row in x:
                    row = re.sub(r'<.+?>', '', str(row))
                    if 'Gen.' in row:
                        genitivo2 = row[4:]
                    if 'Dat.' in row:
                        dativo2 = row[4:]
                    if 'Acc.' in row:
                        acusativo2 = row[4:]
                    if 'Abl.' in row:
                        ablativo2 = row[4:]

    # Declinación Argumento 3
    if trival:
        url = f'https://www.online-latin-dictionary.com/latin-dictionary-flexion.php?parola={argumento3}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        a = soup.find('div', class_='col span_1_of_2')
        for x in a:
            if x.name == 'table':
                for row in x:
                    row = re.sub(r'<.+?>', '', str(row))
                    if 'Gen.' in row:
                        genitivo3 = row[4:]
                    if 'Dat.' in row:
                        dativo3 = row[4:]
                    if 'Acc.' in row:
                        acusativo3 = row[4:]
                    if 'Abl.' in row:
                        ablativo3 = row[4:]
    # Selección de caso
    if verbo[1] == 'Nominativo':
        output1 = argumento1

    if verbo[3] == 'Nominativo':
        output2 = argumento2
    elif verbo[3] == 'Genitivo':
        output2 = genitivo2
    elif verbo[3] == 'Ablativo':
        output2 = ablativo2
    elif verbo[3] == 'Dativo':
        output2 = dativo2
    elif verbo[3] == 'Acusativo':
        output2 = acusativo2
    else:
        output2 = ''

    if verbo[5] == 'Nominativo':
        output3 = argumento3
    elif verbo[5] == 'Genitivo':
        output3 = genitivo3
    elif verbo[5] == 'Ablativo':
        output3 = ablativo3
    elif verbo[5] == 'Dativo':
        output3 = dativo3
    elif verbo[5] == 'Acusativo':
        output3 = acusativo3
    else:
        output3 = ''


    # Ordenación SOV
    if output2 == '':
        return f'{output1} {verbo_conjugado}'
    elif output3 == '':
        return f'{output1} {output2} {verbo_conjugado}'
    else:
        return f'{output1} {output2} {output3} {verbo_conjugado}'
