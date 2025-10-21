
#def subtraction (x,y):
#    return x - y
#    subtraction(10,9);

#def substration_absolute(x,y):
#    if x > y:
#        return x - y
#    return y-x
#substration_absolute(900,9)

#def calculo_triangulo (b , a):
#    if b >= 0 and a >= 0:
#        return (b * a) / 2
#    if b < 0 and a < 0:
#        return b * a / 2
#    return b * a / 2 * -1

#calculo_triangulo (-5,5)   
#calculo_triangulo (-10,5) 
#print(calculo_triangulo (10,5))
#print(substration_absolute(900,9))


def concreto (agua, cimento, areia, pedra):
    total = agua + cimento + areia + pedra
    if total == 0 or total < 0:
        return {
        "erro": "valor inválido"
    }
    return {
    "agua": round((agua / total),2)*100,
    "cimento": round((cimento / total),2)*100,
    "areia": round((areia / total),2)*100,
    "pedra": round((pedra / total),2)*100
                   }

print(concreto (10,10,10,20))