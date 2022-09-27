#este codigo es para identifacr pares 
#declarama la primera función 
import sys 

x= int(sys.argv[1])
def funcion(x): 
    st=[]
    for i in range(1, x+1):
        st.append(i)
    return(st)
st=funcion(x)
print(st)
    

    #ingresamos el dato 
        
 