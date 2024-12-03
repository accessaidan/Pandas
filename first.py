import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])  # Adding custom row indices

# Displaying the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

############################### using loc and iloc #######################
### task 1 ###
def task_1(data):
    row_2 = df.iloc[1,:]
    print(row_2)

### task 2 ###
def task_2(data):
    row_3_collum_2 = df.iloc[2,1]
    print(row_3_collum_2)

### task 3 ###
def task_3(data):
    row_c = df.loc['c']
    print(row_c)

## task 4 ###
def task_4(data):
    multi = df.loc[['b','d'],['Name','City']]
    print(multi)



task_4(data)