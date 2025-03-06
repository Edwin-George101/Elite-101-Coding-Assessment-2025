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


def get_free_tables():
    free_tables = set()  
    header = restaurant_tables[0]  

    for row in restaurant_tables[1:]: 
        for i in range(1, len(row)):  
            if row[i] == 'o':  
                free_tables.add(header[i])  

    return list(free_tables)  


print("Free tables:", get_free_tables())  

#DOES NOT WORK

def find_table_for_party(party_size, timeslot):
    tables = restaurant_tables[0][1:]
    availability = restaurant_tables[timeslot][1:]
    
    for i in range(len(tables)):
        table_capacity = int(tables[i])
        
    return "No table available"

#tables are not suitable yet
def find_tables_for_party(party_size, timeslot):
    tables = restaurant_tables[0][1:]
    availability = restaurant_tables[timeslot][1:]
    
    suitable_tables = []
    for i in range(len(tables)):
        table_capacity = int(tables[i])
    
    return suitable_tables

#timeslot does not work with the adjacent tables
def find_combined_tables_for_party(party_size, timeslot):
    tables = restaurant_tables[0][1:]
    availability = restaurant_tables[timeslot][1:]
    
    suitable_combinations = []
    
    for i in range(len(tables) - 1):  # check pairs of adjacent tables
        table_capacity_1 = int(tables[i])  # first table capacity
        table_capacity_2 = int(tables[i+1])# Second table capacity
        
        # check if both tables are free and can accommodate the party
        if availability[i] == 'o' and availability[i+1] == 'o'
            suitable_combinations.append
    
    return suitable_combinations if suitable_combinations else "No suitable combinations found."