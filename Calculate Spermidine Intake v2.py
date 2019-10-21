import csv
import pandas as pd

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

# write results
class WriteResults(object):
    def __init__(self,sumby,filename):
        SumData = table.groupby(['SEQN'])[sumby].sum()
        SumData.to_csv(filename,mode = 'a',index = True,header = True)

# def search engine
class SearchFoodID(object):
    
    def __init__(self,table):
        self.table = table
        self.dictories = []
        
    def SearchEngine(self,x):
        y = str(x)
        Result = self.dictories.dict.get(y)
        if Result != None :
            int_result = int(Result)
        else:
            int_result = 0
        return int_result

    def SearchFunc(self,From,To,dictory):
        self.dictories = dictory
        self.table[To] = self.table[From].apply(self.SearchEngine)

# read Food_ID to tabel
table = pd.read_csv('2010FoodIntakeData.csv')

# load dictories
FoodIDtoFCID = ReadTable('FoodIdToFCID.txt')
FCIDtoSPDID = ReadTable('FCIDtoSPDID.txt')
Spermidine = ReadTable('Spermidine.txt')
Spermine = ReadTable('Spermine.txt')
Putrescine = ReadTable('Putrescine.txt')

# do Search
SearchID = SearchFoodID(table)
SearchID.SearchFunc('DR1IFDCD','FCID_Code',FoodIDtoFCID)
SearchID.SearchFunc('FCID_Code','SPD_ID',FCIDtoSPDID)
SearchID.SearchFunc('SPD_ID','Spermidine',Spermidine)
SearchID.SearchFunc('SPD_ID','Spermine',Spermine)
SearchID.SearchFunc('SPD_ID','Putrescine',Putrescine)

table = SearchID.table
# calculate SPD intake
table['SpermidineTotal'] = table['Spermidine']*table['DR1IGRMS']
table['SpermineTotal'] = table['Spermine']*table['DR1IGRMS']
table['PutrescineTotal'] = table['Putrescine']*table['DR1IGRMS']

# write to csv table
table.to_csv('SPD_Result.csv',mode = 'a',index = False)
WriteResults('SpermidineTotal','SpermidineTotal.csv')
WriteResults('SpermineTotal','SpermineTotal.csv')
WriteResults('PutrescineTotal','PutrescineTotal.csv')
