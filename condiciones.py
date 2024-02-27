"""""
def NroMayor():
    pass

def Edad():
    pass    

def mensajeNota():
    pass   


if __name__== "__main__":
    NroMayor()  

#dos nro diferentes, imprimir el mayor
    
numero1=0
numero2=0

print("escriva el numero 1")
numero1=int(input()) 

print("escriva el numero 2")
numero2=int(input()) 

if numero1>=numero2:
    print (f"el numero mayor es {numero1}")
else:
     print (f"el numero mayor es {numero2}")

"""""
def mensajeNota():
    pass  
if __name__== "__main__":
     mensajeNota()  

  

print("".center(30,"*"))
print("estudiante-->")
primeranota1=int(input("nota 1-->"))
nota2=float(input("nota 2-->"))
nota3=float(input("nota 3-->"))


suma=(primeranota1+nota2+nota3)/3


if suma >2:
    print(f"gano la materia en{suma}")
else :
    print("la perdio por bago")






def TernarioEdad():
    edad=int(input("edad ->"))
    mensaje ="bienbenido..." if edad>=18 else "prohibido el ingreso"
    print(mensaje)




    if __name__== "__main__":
     TernarioEdad()
     #menasajeNota() 
     #Nrmayor()



def Nrsemana():

    print("Dia semana ".center(30,"*"))
    dia=int(input("Numero de 1 a 7"))

    if dia==1:
        print("lunes")
    elif dia==2:
        print("martes")  
    elif dia==3:
        print("miercoles")  
    elif dia==4:
        print("jueves")  
    elif dia==5:
        print("viernes")  
    elif dia==6:
        print("sabado")  
    elif dia==7:
        print("domingo")  
    else :
        print("no es un numero del 1 al 7")




def Definitiva():
    print("observacion academica".center(30,"*"))   
    Definitiva = float(input("nro entre 0-5 ->"))
    if Definitiva >= 0 and Definitiva<=5:
        if Definitiva <=2.999:
            mensaje="perdio por vago"
        elif Definitiva >=3.000 and Definitiva <=3.99 :
          mensaje="voy regular"
        elif Definitiva >=4.000  :
         mensaje="voy bien"
    else:
        print("la nota no es del 0 al 5")
            

print(mensaje)