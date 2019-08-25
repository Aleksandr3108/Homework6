school = {}
while True:
     key1 = input("Please input class name \n")
     qty_k1 = int(input("Please input quantity of students \n"))
     school[key1] = qty_k1
     prog_exit = input("Do you want add any new class? Y / N \n").upper()
     if prog_exit == "N":
         break
print(school)