import pandas as pd

data = {
    "emp_id": [1, 2, 3, 4, 5, 6],
    "name":   ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"],
    "dept":   ["Eng", "HR", "Eng", "Fin", "HR", "Eng"],
    "salary": [90000, 60000, 95000, 70000, 65000, 85000]
}

my_dataframe = pd.DataFrame(data)

'''
# Q1. find total salary per department
# sql: select dept, sum(salary) from table group by dept
# equivalent python
## steps to write
### my_dataframe["salary"] ->                       bas salary wala column de dega
### my_dataframe.groupby("dept")["salary"] ->       ab groupby daldo
### my_dataframe.groupby("dept")["salary"].sum()->  ab sum() daldo
'''

# print(my_dataframe.groupby("dept")["salary"].sum())

'''
Q2. Give me a complete salary summary for each department —
how many people are in it,
what is the total salary being paid out,
and what is the average salary?"
'''

# people_in_each_dept = my_dataframe.groupby("dept")["emp_id"].count()
# print(f'people-in-each-dept:\n{people_in_each_dept}')
#
# salary_in_each_dept = my_dataframe.groupby("dept")["salary"].sum()
# print(f'salary_in_each_dept:\n{salary_in_each_dept}')
#
# average_salary_in_each_dept = my_dataframe.groupby("dept")["salary"].mean()
# print(f'average_salary_in_each_dept:\n{average_salary_in_each_dept}')

























