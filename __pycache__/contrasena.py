def comprobarcontraseña(password):
    largo= False
    mayus= False
    minus= False
    numero= False
    simbolo= False
    if len(password) >=8:
        largo= True
    for i in range(len(password)):
        if password[i].isupper():
         mayus=True
        if password[i].islower():
          minus=True   
        if password[i] in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/":
            simbolo=True
        if password[i].isnumeric():
            numero=True
    if largo and mayus and minus and numero and simbolo:
       return "la contraseña es muy segura"
    elif (mayus or minus) and numero and largo and simbolo:
       return "la contraseña es segura"
    elif(mayus or minus)and numero:
       return "la contraseña es poco segura"
    elif(mayus) and minus:
       return "la contraseña es insegura"
    else:
       return "la contraseña es muy insegura"
password= input("ingrese su contraseña: ")
verificacion=comprobarcontraseña(password)
print(f"la contraseña es: ",verificacion)