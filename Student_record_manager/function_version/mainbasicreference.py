data = [
    {"name": "Anu", "marks": [80, 87, 98]},
    {"name": "Ann", "marks": [85, 86, 97]},
    {"name": "Meera", "marks":[92,89,95]}
]
print("details of students:",data)
print("first student details:",data[0])
print("second student details:",data[1])
print("first student name:",data[0]["name"])
print("second student name:",data[1]["name"])
print("marks of second subject of student Ann:",data[1]["marks"][1])

# display student
def view_student():
    
    for student in data:
        print ("Name:",student["name"],"," ,"Marks :", student["marks"])
view_student()

"""
print("marks of first student:",data[0]["marks"])  
print("marks of second student:",data[1]["marks"]) 

topper_name=""
highest_average=0
for student in data:
    total=0
    
    for mark in student["marks"]:
        total=total+mark
    average=total/len(student["marks"])
    if average>highest_average:
        highest_average=average
        topper_name=student["name"]


       
    print("Name:", student["name"], "\nMarks:", student["marks"], "\nTotal marks:", total, "\nAverage:", average, sep="")
    print("____________________________")
print("Highest Average",highest_average,"\nTopper", topper_name)





#serach student in the data

search_name=input("Enter the name to search\n")
found=False
for student in data:
    if student["name"]==search_name:
        found=True
        print("Name:", student["name"], "\nMarks:", student["marks"], sep="")
        break
        #search_name=student["name"]
        
if not found:
    print("Student not found.")


#Update student marks

search_name_mark=input("Enter the name of student to update\n")
search_subject_mark1=int(input("Enter the mark of subject1\n"))
search_subject_mark2=int(input("Enter the mark of subject2\n"))
search_subject_mark3=int(input("Enter the mark of subject3\n"))

updated_marks=[search_subject_mark1,search_subject_mark2,search_subject_mark3]
found=False
for student in data:
    if student["name"]==search_name_mark:
        found=True
        student["marks"]=updated_marks
        print("Name:", student["name"], "\nMarks:", student["marks"], sep="")
        
        break
        
        
if not found:
    print("Student not found.")
print("updated data",data)    


# delete student record

delete_student="Meer"
found=False
for student in data:
    if student["name"]==delete_student:
        found=True
        data.remove(student)
        print("student details is removed successfully")
        break

if not found:
    print("Student not found.")
print("updated data",data) 

"""
