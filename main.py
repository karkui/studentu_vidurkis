num_students = int(input("Irasykite studentu kieki: "))


students = []
atsakymas = []
rezultatas = []

i = 0
while i < num_students:
   name = input("Irasykite studento varda: ")




   matematika = int(input("Irasykite matematikos bala: "))
   if matematika < 0 or matematika > 100:
       print("Reiksme turi buti tarp 0 ir 100")
       break

   informatika = int(input("Irasykite informatikos bala: "))
   if informatika < 0 or informatika > 100:
       print("Reiksme turi buti tarp 0 ir 100")
       break

   fizika = int(input("Irasykite fizikos bala: "))
   if fizika < 0 or fizika > 100:
       print("Reiksme turi buti tarp 0 ir 100")
       break

   atsakymas = (matematika + informatika + fizika)/3
   rezultatas.append(atsakymas)
   students.append(name)
   i+=1



i = 0
while i < num_students:

    final_student = students[i]
    final_result = rezultatas[i]
    final_result = round(final_result, 2)
    print(f"Studentas, kurio vardas yra: {final_student} jo vidurkis yra: {final_result}")
    i+=1


