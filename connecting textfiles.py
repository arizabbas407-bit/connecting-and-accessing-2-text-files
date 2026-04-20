with open("students.txt", "w") as f:
    f.write("1,Ariz\n2,Ali\n3,aaliya\n")

with open("marks.txt", "w") as f:
    f.write("1,85\n2,90\n3,78\n")

students = {}
marks = {}

with open("students.txt", "r") as f:
    for line in f:
        id, name = line.strip().split(",")
        students[id] = name
        
with open("marks.txt", "r") as f:
    for line in f:
        id, mark = line.strip().split(",")
        marks[id] = mark

for id in students:
    print(f"ID: {id} | Name: {students[id]} | Marks: {marks.get(id)}")
