#este codigo es para identificar pares 
import sys 

x= int(sys.argv[1])
#declaramos la primera función 
def funcion(x): 
    st=[] #Declaramos la lista 
    for i in range(1, x+1): # hacemos un ciclo para desglozar el numero dado 
        st.append(i) #ingresamos los valores a la lista 
    return(st)
num=funcion(x)  #mandamos a llammar la funcion
print(num)
    
def primos(x): 
    cadena=[]
    for i in range(1, x+1): #contador para 
        p = 0
        for j in range(1, i+1):
            if i % j == 0:
                p += 1
        if p == 2:
            cadena.append(i)
    return(cadena)
Prim=primos(x) # mandamos a llammar la funcion

print("Primos:", Prim)
    
    #ingresamos el dato 
        
 