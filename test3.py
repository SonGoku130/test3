1. # dictionary      →  store at least 5 student name-score pairs
2. #for loop        →  to calculate the class average
3. #ax() min()     →  to find the top and bottom scorer
4. #.get()          →  to look up a student by name
5. #input()         →  to let the user search for a student

#Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, 
#finds the top and bottom scorer, and lets the user look up any student's grade.

grds = {"Alice" :  {40} ,
        "Jane" : {70} ,
        "Patrick" : { 75 },
        "Lesba" : { 30 },
        "Janel" : { 65 }}

for k, v in grds.items():
    search = input("Enter a students name : ")
    if grds.get(search):
        print("Name : ", k)
        print("Grades : ", v)
    else:
        print("Student not found!")

    classAvg =  int(grds.get(v)) / 5
    print("class Average is : ", classAvg)

    print("Class highest : ", anext(grds.values))
    print("class lowest : ", min(grds.values))