# Sample Table Data
restaurant_tables = [
    ['-', 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    [1,   'x',    'o',    'o',    'o',    'o',    'x'],
    [2,   'x',    'x',    'o',    'o',    'x',    'o'],
    [3,   'x',    'x',    'o',    'x',    'o',    'o'],
    [4,   'x',    'o',    'o',    'x',    'o',    'x'],
    [5,   'x',    'x',    'o',    'x',    'o',    'o'],
    [6,   'x',    'o',    'o',    'o',    'x',    'o']
]

#Hello Code2College! I used Visual Studio Code to run my code first then put that code into this assignment. GitHub was acting up and was glitching out, so I felt more comfortable there. If you guys would like my visual studio code or anything like that then let me know :). 

def get_free_tables():
    free_tables = []  
    top_row = restaurant_tables[0]  

    for row in restaurant_tables[1:]: 
        for x in range(1, len(row)):  
            if row[x] == 'o':  
                free_tables.append(top_row[x])  

    return list(free_tables)  


print("Free tables:", get_free_tables())  

#DOES NOT WORK BELOW but attempted it.

def find_table_for_party(party_size, timeslot):
    tables = restaurant_tables[0][1:] #Looked this up and it goes through every column of the graph.
    availability = restaurant_tables[timeslot][1:] #checks the timeslot in availability but not sure if this should work.
    
    for i in range(len(tables)): #goes through the entire table list
        table_capacity = int(tables[i]) #sets the capacity (to an integer) for the tables. 
        
    return "No table available"

#tables are not suitable yet
def find_tables(party_size, timeslot):
    tables = restaurant_tables[0][1:] 
    availability = restaurant_tables[timeslot][1:]
    
    suitable_tables = []
    for i in range(len(tables)):
        table_capacity = int(tables[i])
    
    return suitable_tables

#timeslot does not work with the adjacent tables
def find_combined_tables(party_size, timeslot):
    tables = restaurant_tables[0][1:]
    availability = restaurant_tables[timeslot][1:]
    
    suitable_combos = [] #list for the suitable combos. This should be 
    
    for i in range(len(tables) - 1):  # check pairs of adjacent tables
        table_capacity_1 = int(tables[i])  # first table 
        table_capacity_2 = int(tables[i+1])# second table that is right next to this table
        
        # checks if both tables are free
        if availability[i] == 'o' and availability[i+1] == 'o':
            suitable_combos.append
    
    return suitable_combos
    
    
