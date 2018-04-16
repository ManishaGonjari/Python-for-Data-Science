# coding: utf-8

# In[1]:
#importing required packages
import pandas as pd                      #Package to import dataset
#from itertools import combinations
import itertools as it
from collections import OrderedDict       #importing for ordered list
from operator import itemgetter


# In[2]:

#As pandas need equal column size adding column names
my_cols = ["A","B","C","D","E"]
training_data = pd.read_csv('http://kevincrook.com/utd/market_basket_training.txt',names=my_cols,header = None, encoding='utf-8')
training_data.drop('A', axis=1, inplace=True)   #Dropping first index column

# In[3]:

train_len = len(training_data.index)       #Training data length
frequency_dict = {}                     # This dict will hold key = each list combination in form of tuple and value= count

i = 1
while (i < train_len):                     #Traversing through each record in training_data
    train_list = []
    j= 0
    while (isinstance(training_data.iloc[i][j] , str) == True):     #If value is not 'nan' append it to list
        train_list.append(training_data.iloc[i][j])
        j += 1
        if(j > 3):
            break
    train_tuple = tuple(train_list)                             # As dict key can not be list converting it to list
    if train_tuple in frequency_dict:                           #If tuple already present in dictionary increament vale
        frequency_dict[train_tuple] +=1                         #Else add
    else:
        frequency_dict.update({train_tuple : 1})
    i += 1
    
print(frequency_dict)    
sorted_train = OrderedDict(sorted(frequency_dict.items(), key=itemgetter(1)))            #Sort keys based on value       
print(sorted_train)                       #Printing sorted data


print('done')


# In[6]:

train_keys = list(sorted_train.keys())          #Converting to list

for l in train_keys:                           #Looking through each key
    y  = list(l)
    print(y)

train_size = len(train_keys)                    #Taking size of training data           



# In[7]:

#Fetching test data

test_data = pd.read_csv('http://kevincrook.com/utd/market_basket_test.txt',names=my_cols,header = None)
test_data.drop('A', axis=1, inplace=True)         #Dropping index column
print('Done')


# In[19]:

def check_set(inp,inp_len):                       #Function to fetch the match list
    #x = train_size - 1
    i = train_size - 1            
    for x in reversed(train_keys):               #Traversing list in reverse order
        y = list(x)
        z = list(inp)
        if len(x) == inp_len + 1:               #Fetch the list only if it has +1 record
            if (set(z) < set(y)):               #Check if part of set 
                print("match")
                print(x)                        #Print what match found
                break                           #Break if match found
        i = i - 1                               #Returning this counter   

    print(i)
    return(i)                                   #Returning index
            
i = 0                                           #Initializing variables
k = 0

while (i < 100):                                #Looping through test data       
    inp_list = []                               #Initialiing list as empty
    j= 0
    while (isinstance(test_data.iloc[i][j] , str) == True):    #Read till its not nan
        inp_list.append(test_data.iloc[i][j])                  #Create input list
        j += 1
    print("inp list")                                          #Printing input list
    print(inp_list)
    
    if 'P04' in inp_list:                                      #Removing P04
        inp_list.remove('P04')
        
    if 'P08' in inp_list:                                      #Removing P08
        inp_list.remove('P08')
    
    inp_len = len(inp_list)                                    #Taking input length      
    k = 0
    k  = check_set(inp_list,inp_len)                          #Calling function to get match
    
    if (k > 0):                                          #K > 0 means we found match
        print("list is")
        finallist = train_keys[k]                       #Print the list                 
        print(finallist)         
    else:                                                
        i_list =[]                                      #If dont find then split
        split_list = list(it.combinations(inp_list, inp_len-1))   #split list
        for l in split_list:                               #traverse through each list after splitting
            k = 0
            k  = check_set(l,inp_len)                      #for each list call check set                 
            i_list.append(k)                               #append each record 
                   
        max_i = max(i_list)                                #Find max from list  
        print("after split")
        finallist = train_keys[max_i]                      #Find the list with max count
        
        
    final_out = [x for x in finallist if x not in inp_list]     #fetch out final list
    out = ','.join(final_out)
    z = i + 1                                                   #For pringting index in out file
    rnk = '00' + str(z) + ','
    y = str(z)                                                  #Formatting for output
    if (len(y) == 2):
        rnk = '0' + str(z) + ','        
    if (z == 100):                                              #If 100 dont do anythin
        rnk = str(z) + ','
    to_file = rnk + out                                        #Merging output 
    print(to_file)
    
    
    with open('market_basket_recommendations.txt', 'a') as out_file:   #Writing output to file
        print(to_file,file= out_file)



    i += 1                                                            #Increamenting count
    
print("Program Done")
