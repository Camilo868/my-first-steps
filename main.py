Students=[]
subjects = ["Math", "Biology", "Socials"]
print("\n1 Welcome to my program about register the sutednts")
diferent_student=int(input("\n1 How many students do you want to registeer: "))
for student in range (diferent_student):
    grades={}
    name=input(f"What is the name of the student? {student+1}. ")
    
    for idx in range(len(subjects)):
        grade = float(input(f"Enter the grade for {subjects[idx]}: "))
        grades[subjects[idx]] = grade 

    Students.append({
        "name":name,
        "grades":grades
    })

for idx, mostrar in enumerate(Students):
    print(f"{idx+1}. The student {mostrar["name"]} {mostrar["grades"]}")
