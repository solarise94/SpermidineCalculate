import csv
import pandas as pd

# read Food_ID to tabel
table = pd.read_csv('2010FoodIntakeData.csv')

# write things into dictories
class ReadTable(object):
    def __init__(self,filename):
        file = open(filename,'r')
        self.dict = {}
        for line in file.readlines():
            line = line.strip()
            key = line.split()[0]
            value = line.split()[1]
            self.dict[key] = value
        file.close()

class WriteResults(object):
    def __init__(self,sumby,filename):
        SumData = table.groupby(['SEQN'])[sumby].sum()
        SumData.to_csv(filename,mode = 'a',index = True,header = True)

# load dictories
FoodIDtoFCID = ReadTable('FoodIdToFCID.txt')
FCIDtoSPDID = ReadTable('FCIDtoSPDID.txt')
Spermidine = ReadTable('Spermidine.txt')
Spermine = ReadTable('Spermine.txt')
Putrescine = ReadTable('Putrescine.txt')

# def the finding functions
def SearchFCIDtoSPDID(x):
    y = str(x)
    Result = FCIDtoSPDID.dict.get(y)
    if Result != None :
        int_result = int(Result)
    else:
        int_result = 0
    return int_result

def SearchFoodIDtoFCID(x):
    y = str(x)
    Result = FoodIDtoFCID.dict.get(y)
    if Result != None :
        int_result = int(Result)
    else:
        int_result = 0
    return int_result

def SearchSpermidine(x):
    y = str(x)
    Result = Spermidine.dict.get(y)
    if Result != None :
        int_result = int(Result)
    else:
        int_result = int("0")
    return int_result

def SearchSpermine(x):
    y = str(x)
    Result = Spermine.dict.get(y)
    if Result != None :
        int_result = int(Result)
    else:
        int_result = int("0")
    return int_result

def SearchPutrescine(x):
    y = str(x)
    Result = Putrescine.dict.get(y)
    if Result != None :
        int_result = int(Result)
    else:
        int_result = int("0")
    return int_result

# run Searching engine
table['FCID_Code'] = table['DR1IFDCD'].apply(SearchFoodIDtoFCID)
table['SPD_ID'] = table['FCID_Code'].apply(SearchFCIDtoSPDID)
table['Spermidine'] = table['SPD_ID'].apply(SearchSpermidine)
table['Spermine'] = table['SPD_ID'].apply(SearchSpermine)
table['Putrescine'] = table['SPD_ID'].apply(SearchPutrescine)

# def the calculater for SPD
table['SpermidineTotal'] = table['Spermidine']*table['DR1IGRMS']
table['SpermineTotal'] = table['Spermine']*table['DR1IGRMS']
table['PutrescineTotal'] = table['Putrescine']*table['DR1IGRMS']

# write to csv table
table.to_csv('SPD_Result.csv',mode = 'a',index = False)
WriteResults('SpermidineTotal','SpermidineTotal.csv')
WriteResults('SpermineTotal','SpermineTotal.csv')
WriteResults('PutrescineTotal','PutrescineTotal.csv')
