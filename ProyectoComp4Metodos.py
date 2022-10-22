#El siguiente programa ejecuta 4 métodos de aproximación numérica
#para resolver una ecuación diferencial mediante un PVI.
# 1) Punto medio.......[yP(t)]
# 2) Euler mejorado....[yE(t)]
# 3) Runge Kuta 4......[yR(t)]

import matplotlib.pyplot as plt #Esta libreria es utilizada para las gráfias

e = 2.71828 #Constante de Euler utilizada para algunas funciones a evaluar

#Definieremos nuestra función a calcular de la forma f(t,y) y la siguiente para
#evaluar en la función obtenida analíticamente

#Funcion 1: w = -(y+1)*(y+3)
#Solución analítica 1: c = -(3+e**(2*t))/(1+e**(2*t))
#Intervalo [0,2] y valor inicial T=0 y vi=-2

#Funcion 2: w = 5*t**2 + 2*t - 5*y
#Solución analítica 2: c = e**(-5*t)*(1+3*e**(5*t)*t**2)/3
#Intervalo [0,1] y valor inicial T=0 y vi=1/3

def f(t,y):
    w = 5*t**2 + 2*t - 5*y
    return w

def g(t):
    c = e**(-5*t)*(1+3*e**(5*t)*t**2)/3
    return c

#Información indispensable para realizar las aproximaciones:
#intervalo de interés, número de iteraciones y ancho de paso
a = float(input("Invervalo a: "))
b = float(input("Invervalo b: "))
N = int(input("Num. de iteraciones: "))
h = (b-a)/N
print("El valor de h es: ",h)

#Variables utilizadas para las condiciones iniciales (tiempo y pisición)
#para cada método y el apoyo de n para el número de iteraciones, valores
#inicieles y variables para la desviación de cada método
T = 0; n = 0; vi = 1/3
DP = 0; DE = 0; DR = 0; DVR = 0
yM = vi; yP = vi; yE = vi; yR = vi; vR = vi
T1 = [T]; y1 = [vi]; y2 = [vi]; y3 = [vi]; y4 = [vi]; v5 = [vi]

#Creamos un archivo xls para guardar los datos en forma de tabla
with open("MejoradoGrafica2.xls","w") as MG:

    #Se crea el título de la tabla con el comando .write()
    MG.write(f"t\tPuntoMedio\tEulerMejorado\tRungeKuta4\tSol.Real\n{str(T)}\
        \t{str(yP)}\t{str(yE)}\t{str(yR)}\t{str(vR)}\t")

    #Se inicia el ciclo para realizar las iteraciones
    while N>0:
        
        N -= 1
        n += 1

        #Cada valor calculado se guardará en un arreglo utilizando la función
        #.append() para su graficación posterior
        
        #Cálculo del tiempo
        T += h
        T1.append(T) 

        #Cálculo del Punto Medio
        k1 = h*f(T,yP)
        yP = yP + h*f(T+h/2,yP+k1/2)
        y2.append(yP)
        
        #Cálculo de Euler Mejorado
        k1 = h*f(T,yE)
        k2 = h*f(T+h,yE+k1)
        yE = yE + (k1+k2)/2
        y3.append(yE)
        
        #Cálculo de RK4
        k1 = h*f(T,yR)
        k2 = h*f(T+h/2,yR+k1/2)
        k3 = h*f(T+h/2,yR+k2/2)
        k4 = h*f(T+h,yR+k3)
        yR = yR + (k1+2*k2+2*k3+k4)/6
        y4.append(yR)
        
        #Cálculo de valor real
        vR = g(T)
        v5.append(vR)
        
        #Cálculo de las desviaciones
        DP += (vR-yP)**2
        DE += (vR-yE)**2
        DR += (vR-yR)**2
        DVR += (vR-vR)**2

        #Se guardan los valores en tabla formato .xls
        MG.write(f"\n{str(T)}\t{str(yP)}\t{str(yE)}\
            \t{str(yR)}\t{str(vR)}")
    #Se guardan las desviaciones
    MG.write(f"\nDesviacion\t{str(DP**(1/2))}\
             \t{str(DE**(1/2))}\t{str(DR**(1/2))}\t{str(DVR**(1/2))}")

#Comando para la gráfia       
fig, graf=plt.subplots()
graf.plot(T1, y2, color="yellow")
graf.plot(T1, y3, color="red")
graf.plot(T1, y4, color="brown")
graf.plot(T1, v5, color="blue")
plt.xlabel("t")
plt.ylabel("y")   
plt.title(f"h={str(round(h,3))}")
plt.legend(["Punto medio","Euler mejorado","Runge-Kutta orden=4",\
            "Valor real"])
plt.show()

        
print("Número de iteraciones: ",n)
print("\n","El archivo se guardó como 'MejoradoGrafica2.xls' ")


