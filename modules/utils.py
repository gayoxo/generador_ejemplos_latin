from pandas.core.frame import DataFrame as DF
from typing import List

def csv_to_list(column:str, df:DF)->List:
    
    clase = df[[column]].to_string(header=False, index=False).split('\n')
    lista = [word.lstrip() for word in clase]

    return lista

def verbcsv_to_list(df:DF)->List:

    ve = df[['VERBOS']].to_string(header=False, index=False)
    verbos = []
    b = ve.split('\n')
    for word in b:
        word = word.split()
        if len(word)>1:
            verbos.append(word[0][:-1])
        else:
            verbos.append(word[0])
    return verbos