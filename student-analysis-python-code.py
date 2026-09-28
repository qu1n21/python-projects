import pandas as pd

#Load the student dataset
df = pd.read_csv('dataset/student.csv')

#Preview the data
print(df.head())

#Check dataset size
df.shape()

#Check data types
df.dtypes

#Check for missing values
df.isnull().sum()

#Check mean, median, min and max marks
print("avg:", df.mark.mean(), "|| median:", df.mark.median(), "|| min:", df.mark.min(), "|| max:", df.mark.max())

#Show names of students that scored over 70 with their marks 
print(df.loc[(df.mark > 70), ['name', 'mark']])

#Check gender ratio of students
df.gender.value_counts()

#Creating a new column called "high_score" showing True or Flase if the student's grade is higher than 75
df.loc[df['mark'] >= 75, 'high_score'] = True
df.loc[df['mark'] < 75, 'high_score'] = False

#Renaming the name column to "student_name"
df.rename(columns={'name':'student_name'},inplace=True)

#Find the highest mark achieved in each class
print(df.groupby('class').mark.max())

#Finding the average mark in each class
table = pd.pivot_table(df, values=['mark'], index=['class'], columns=['gender'], aggfunc='mean')
table

#Create a new performance column with the following bands based on student marks:
#Excellent: 80-100
#Good: 70-79
#Satisfactory: 60-69
#Needs Improvement: < 60
df.loc[df['mark'] >= 80, 'performance'] = 'Excellent'
df.loc[(df['mark'] < 80) & (df['mark'] >=70), 'performance'] = 'Good'
df.loc[(df.mark <70) & (df.mark >= 60), 'performance'] = 'Satisfactory'
df.loc[df.mark < 60, 'performance'] = 'Needs Improvement'
#I used both df.mark and df[‘mark’] just as a test of each of them. I would of course keep it consistent in a work environment.

#Renaming and exporting specified columns to a new csv
df.rename(columns={'name':'full_name'}, inplace=True)
df.to_csv('studentMarks.csv', columns=['full_name', 'mark'], index=False)
df1= pd.read_csv('studentMarks.csv')

