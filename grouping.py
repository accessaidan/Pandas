import pandas as pd

# Creating a sample DataFrame with student information
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Charlie'],
        'Subject': ['Math', 'Math', 'Math', 'Math', 'English', 'English', 'English'],
        'Score': [80, 90, 75, 85, 85, 88, 92],
        'Attendance': [90, 95, 80, 92, 88, 93, 78]}

df = pd.DataFrame(data)

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")


######tasks#####

def task_1(df):
        grouped_scores = df.groupby('Subject')['Score'].mean()
        print(grouped_scores)

def task_2(df):
        grouped_scores = df.groupby('Subject')['Score'].mean()
        grouped_sorted = grouped_scores.sort_values(ascending = False)
        print(grouped_sorted.iloc[0])

def task_3(df):
        grouped_students = df.groupby('Name')['Score'].mean()
        grouped_sorted = grouped_students.sort_values(ascending = False)
        print(grouped_sorted)



task_3(df)
