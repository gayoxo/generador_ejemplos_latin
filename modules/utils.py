from pandas import DataFrame
from typing import List
from pydantic import BaseModel
from models import Verb_data



def _verb_categorizer(dataframe:DataFrame, cat:str) -> List:
    data = dataframe[cat].to_list()
    category = []
    for verb in data:
        category.append(verb.split(',')[0])
    return category

def _categorizer(dataframe:DataFrame, cat:str) -> List:
    data = dataframe[cat].to_list()
    return data


def get_all_verb_data(dataframe:DataFrame)-> List:
    li = list(dataframe)
    li.remove('TIPO')
    li.remove('SUBTIPO')
    li.remove('SUBSUBTIPO')
    data = []
    for column in li:
        if column == 'VERBOS':
            data.append({column:_verb_categorizer(dataframe,column)})
        else:
            data.append({column:_categorizer(dataframe,column)})
    return data


def instanciate_verb(number:int, list_verb:List) -> List:
    data = []
    for i in range(number):
        data.append(Verb_data(
            verbo= list_verb[0]['VERBOS'][i],
            caso1= list_verb[2]['CASO A1'][i],
            argumento1= list_verb[3]['RASGO A1'][i],
            caso2= list_verb[4]['CASO A2'][i],
            argumento2= list_verb[5]['RASGO A2'][i],
            caso3= list_verb[6]['CASO A3'][i],
            argumento3= list_verb[7]['RASGO A3'][i],
            valencias= list_verb[1]['VALENCIAS'][i]
        ))
    return data



def constructor(column_names:List) -> List[BaseModel]:
    data = []
    for column in column_names:
        data.append(0)

    return data



"""def verb_data()
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
        [v, super_caso1, super_argumento1, super_caso2, super_argumento2, super_caso3, super_argumento3, super_valencias])"""