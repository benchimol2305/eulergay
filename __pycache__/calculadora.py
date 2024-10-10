def calcular(a,b,operacion):
    if(operacion=="+"):
      return a+b
    elif(operacion=="-"):
      return a-b
    elif(operacion=="/"):
        if(b!=0):
            return a/b
        else:
            return "error"
    elif(operacion=="*"):
     return a*b
    elif(operacion=="^"):
        return a**b
resultado=calcular(3,5,"^")
print(resultado)  
if __name__=="__main__":
    resultado=calcular(3,5,"^")
    print(resultado)    