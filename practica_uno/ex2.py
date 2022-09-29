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
print("numeros:",num)
    
def primos(x): 
    cad=[] #Declaramos la lista 
    for i in range(1, x+1): # hacemos un ciclo para desglozar el numero dado 
        p = 0 #contador
        for j in range(1, i+1): #Ciclo para recorrer todos los numeros desglozados
            if i % j == 0: #verificar numeros primos y sumar al contador
                p += 1 
        if p == 2: #Para los que son numeros primos  los ingresamos a la lista 
            cad.append(i)
    return(cad)
Prim=primos(x) # mandamos a llammar la funcion

print("Primos:", Prim)
    
    #ingresamos el dato 
        
 