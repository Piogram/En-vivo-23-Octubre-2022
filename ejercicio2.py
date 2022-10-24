import math 
def distancia(x1,y1,x2,y2):
    # Opcion 1
    componente1 = (x2-x1)**2
    componente2 = (y2-y1)**2
    suma = componente1+componente2
    formula = math.sqrt(suma)
    # Opcion 2
    # formula = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    # Opcion 3
    # formula = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
    return formula
    
resultado = distancia(1, 1, 3, 4)
print("resultado",resultado)


   
    
    
    
    
    
    

    
    
