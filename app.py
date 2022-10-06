print("Bienvenido al horoscopo Semanal")
def menu():

  print("##################")
  print("Ingresa tu opción")
  print("1","Aquarius")
  print("2","Aries")
  print("3","Cancer")
  print("4","Capricornus")
  print("5","Gemini")
  print("6","Leo")
  print("7","Libra")
  print("8","Pisces")
  print("9","Sagittarius")
  print("10","Escorpio")
  print("11","Taurus")
  print("12","Virgo")
  print("13","color favorito")
  print("0","salir")
def read_file(profesias):
   file = open("signs/"+ profesias,"r",encoding="UTF-8")
   for line in file:
      print(line)
user_input = ""

while user_input != "exit":
   menu()
   user_input = input()
   if user_input == "1":
      read_file("Aqurius.txt")
   elif user_input == "2":
      read_file("Aries.txt")
   elif user_input == "3":
      read_file("Cáncer.txt")
   elif user_input == "4":
      read_file("capricornus.txt")
   elif user_input == "5":
      read_file("Gemini.txt")
   elif user_input == "6":
      read_file("leo.txt")
   elif user_input == "7":
      read_file("Libra.txt")
   elif user_input == "8":
      read_file("Piscis.txt")
   elif user_input == "9":
      read_file("Sagittarius.txt")
   elif user_input == "10":
      read_file("Scorpio. txt")
   elif user_input == "11":
      read_file("Taurus.txt")
   elif user_input == "12":
      read_file("Virgo.txt")  
   elif user_input == "13":
      read_file("capricornus.txt")
   elif user_input == "exit":
       print("Hasta luego")
       exit()
   else:
      print("opción incorrecta")

