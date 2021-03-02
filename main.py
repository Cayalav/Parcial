# Parcial 1 - Carlos Ayala

#Ejercicio 1
def num1(n):
  if n>=0 and n<2:
    print("0% Descuento")
  elif n>=2 and n<5:
    print("10% Descuento")
  elif n>=2 and n<5:  
    print("0% Descuento")
  else:
    print("0% Descuento")
  print("######################################################")  

#Ejercicio 2
def num2(key):
  if key=="010":
    print("20% Descuento")
  elif key=="020":
    print("40% Descuento")
  elif key=="030":
    print("55% Descuento")
  elif key=="040":
    print("75% Descuento")
  print("######################################################")  

#Ejercicio 3
def num3(costo,marca):
  desc=0
  if costo>=4000 :
    desc=0.2
  if marca=="NOSY":
    desc=desc+0.1
  iva = 0.3  
  perc = desc-iva  
  print(f"Pagará un total de: {costo+(costo*perc)}")
  print("######################################################")  

#Ejercicio 4
def num4(hect):
  if hect>5:
    pino= hect*0.8
    oya=hect*0.15
    cedro=hect*0.05
  else:
    pino= hect*0.45
    oya=hect*0.25
    cedro=hect*0.30
  print(f"Pino: {pino} hectareas")
  print(f"Oyamel: {oya} hectareas")
  print(f"Cedro: {cedro} hectareas")  
  print("######################################################")  

#Ejercicio 5
def num5(a,b,c):
  if a > b:
    if a > c:
      print(a)
    else: 
      print(c)
  else:
    if b > c:
      print(b)
    else:
      print (c)    

num1(23)
num2("030")
num3(2300, "NOSY")
num4(123)
num5(100, 3, 20)