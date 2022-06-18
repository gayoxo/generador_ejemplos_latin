from msilib.schema import Verb
import pandas as pd
from environment import DATA_DIR
from models import Verb_data
from utils import get_all_verb_data, instanciate_verb

# ToDo: Cargar los literales como config
verb_database_path = f'{DATA_DIR}/verbos.xlsx'
sust_database_path = f'{DATA_DIR}/sustantivos.xlsx'
sheet = 'Hoja1'
len_verbos = 121

# Create dataframes
df_v = pd.read_excel(verb_database_path, sheet_name=sheet)
df_s = pd.read_excel(verb_database_path, sheet_name=sheet)


# Get the column values of the verb dataframe
all_data_verb = get_all_verb_data(df_v)

# List with all the verbs and their specific information
instance_verb = instanciate_verb(len_verbos,all_data_verb)

print(instance_verb[34])

