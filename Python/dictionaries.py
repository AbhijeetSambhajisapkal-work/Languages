hogwarts = {
    "Hermoine" : "Gyn",
    "Ron" : "Gyn",
    "Harry" : "Gyn",
    "Draco" : "sln"
 }

students = [
{"name":"harry","role":"main","hair color":"brunette"},
{"name":"Ron","role":"sup","hair color":"brunette"},
{"name":"Harmione","role":"sup","hair color":"brunette"},
{"name":"Draco","role":"villian","hair color":"blonde"}
]


for key,value in enumerate(hogwarts):
    print(f"{key} : {value}") 

for st in hogwarts:
    print(f"{st}:{hogwarts[st]}");

for i in students:
    print(f"{i["name"]} : {i["role"]} : {i["hair color"]}")