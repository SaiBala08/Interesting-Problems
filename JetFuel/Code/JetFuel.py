
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
import json


Output = {}

Output["Students"] = []

student_data = pd.read_csv("Example1/students.csv")
student_data = np.array(student_data[["id","name"]]).reshape(-1,2)

marks_data = pd.read_csv("Example1/marks.csv")
marks_data = np.array(marks_data[["test_id","student_id","mark"]]).reshape(-1,3)

tests_data = pd.read_csv("Example1/tests.csv")
tests_data = np.array(tests_data[["id","course_id","weight"]]).reshape(-1,3)

courses_data = pd.read_csv("Example1/courses.csv")
courses_data = np.array(courses_data[["id","name","teacher"]]).reshape(-1,3)

for i in student_data:
    dic = {}
    dic["id"],dic["name"] = i
    dic["totalAverage"] = 0
    dic["courses"] = []
    Output["Students"].append(dic)


for i in marks_data:
    test_id, student, mark = i
    d, course_id, weight = tests_data[test_id-1] 
    d, name, teacher = courses_data[course_id-1] 
    
    course = {}
    course["id"],course["name"],course["teacher"],course["courseAverage"] = d, name, teacher, 0
    
    
    if course not in Output["Students"][student-1]["courses"]:
        Output["Students"][student-1]["courses"].append(course)


for i in marks_data:
    test_id, student, mark = i
    d, course_id, weight = tests_data[test_id-1] 
    d, name, teacher = courses_data[course_id-1] 
    
    for l in range(len(Output["Students"][student-1]["courses"])):
        if d == Output["Students"][student-1]["courses"][l]["id"]:
            Output["Students"][student-1]["courses"][l]["courseAverage"] += mark*weight/100
            
for i in Output["Students"]:
    s = 0
    for j in i["courses"]:
        s += j["courseAverage"]
    i["totalAverage"] = s/len(i["courses"])
    


with open('Output.json', 'w') as outfile:
    json.dump(Output, outfile, indent = 4)

