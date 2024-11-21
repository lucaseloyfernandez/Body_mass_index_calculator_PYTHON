#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Una medida de la obesidad se determina mediante el índice de masa corporal (IMC), que se calcula dividiendo
# los kilogramos de peso por el cuadrado de la estatura en metros (IMC = peso (kg)/ [estatura (m)]2
# Según el Instituto Nacional del Corazón, los Pulmones y la Sangre de los Estados Unidos (NHLBI), el sobrepeso 
# se define como un IMC de más de 25. Se considera que una persona es obesa si su IMC es superior a 30. 
# Usted puede determinar su IMC con la calculadora que se encuentra a continuación. Con la cifra del IMC puede averiguar
# su composición corporal en la tabla que aparece debajo de la calculadora.


# In[7]:


nombre = input("Ingrese su nombre: ")

edad = int(input("Ingrese su edad: "))

sexo = input("Ingrese su sexo (M/F): ")

altura = float(input("Ingrese su altura (m): "))

peso = float(input("Ingrese su peso (kg): "))


# Calcular el IMC

imc = peso / altura**2
print("su IMC es: ", imc)

if imc < 20:
    print(nombre + " ESTAS BAJO DE PESO")

elif imc < 25:
    print( nombre +  " ESTAS DENTRO DE LOS VALORES NORMALES DE PESO")

elif imc > 25:
    print( nombre + " TIENES SOBRE PESO")

elif imc > 30:
    print( nombre + " TIENES OBESIDAD")
else :
    print(" ingrese valores dentro de los parametros")


# In[ ]:





# In[ ]:





# In[ ]:




