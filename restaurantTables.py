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

# Level 1: Find all free tables at any time
def get_free_tables():
    free_tables = set()  
    header = restaurant_tables[0]  

    for row in restaurant_tables[1:]:  # Skipping header row
        for i in range(1, len(row)):  # Checking only table columns
            if row[i] == 'o':  
                free_tables.add(header[i])  # Store table label

    return list(free_tables)  # Return unique free tables



print("Free tables:", get_free_tables())  
