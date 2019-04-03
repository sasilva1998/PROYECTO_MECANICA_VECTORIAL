
import beammech as bm
import numpy as np
import matplotlib.pyplot as plt

#funciones para poder definir los maximos y minimos en las graficas
def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

def annot_min(x,y, ax=None):
    xmin = x[np.argmin(y)]
    ymin = y.min()
    text= "x={:.3f}, y={:.3f}".format(xmin, ymin)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="bottom")
    ax.annotate(text, xy=(xmin, ymin), xytext=(0.50,0.20), **kw)

while True:
	#se inicializa el menu por la terminal
	beamop=input("\nElija la opción de viga predeterminada a calcular\n1. Viga simplemente apoyada\n2. Viga con voladizo\n3. Viga en voladizo\n")
	if beamop=='1':
		#dependiendo de la opcion escogida, se lanza una de las funciones que maneja los menus y envia la solucion de lo requerido almacenada en results
		results=bm.simplebeam()
		#se muestran los datos y resultados obtenidos
		print("\nLa fuerza equivalente es: "+str(results.get("R")[0].shear(int(float(results.get("length"))*1000))[0]+results.get("R")[1].shear(int(float(results.get("length"))*1000))[int(float(results.get("length"))*1000)]))
		print("\nLas reacciones en los puntos de soporte son:\nPrimer soporte: "+str(results.get("R")[0].shear(int(float(results.get("length"))*1000))[0])+"\nSegundo soporte: "+str(results.get("R")[1].shear(int(float(results.get("length"))*1000))[int(float(results.get("length"))*1000)]))
		#se prepara para comenzar a graficar y se arman las distintas lineas y listas
		x=np.linspace(0,float(results.get("length"))/1000,int(results.get("length"))+1)
		y=np.zeros(int(results.get("length")+1))
		plt.figure("Grafica 1")
		plt.title("Grafica de momento flector")
		plt.plot(x, results.get("M"))
		#se define el punto maximo y minimo
		annot_max(x,results.get("M"))
		annot_min(x,results.get("M"))
		#se define los margenes de los ejes
		plt.xlabel('Posicion (m)')
		plt.ylabel('Momento flector (kN/m)')
		plt.plot(x,y)

		#lo mismo se hace para la parte de corte flector
		plt.figure("Grafica 2")
		plt.title('Grafica de corte')
		plt.plot(x, results.get("D"))
		annot_max(x,results.get("D"))
		annot_min(x,results.get("D"))
		plt.xlabel('Posicion (m)')
		plt.ylabel('Esfuerzo cortante (kN)')
		plt.plot(x,y)
		plt.show()
	#lo mismo se realiza para las distintas opciones usando otras funciones ya establecidas.
	elif beamop=='2':
		results=bm.overhangbeam()
		suppa=results[1]
		suppb=results[2]
		results=results[0]
		print("\nLa fuerza equivalente es: "+str(results.get("R")[0].shear(int(float(results.get("length"))*1000))[int(float(suppa)*1000)]+results.get("R")[1].shear(int(float(results.get("length"))*1000))[int(float(suppb)*1000)]))
		print("\nLas reacciones en los puntos de soporte son:\nPrimer soporte: "+str(results.get("R")[0].shear(int(float(results.get("length"))*1000))[int(float(suppa)*1000)])+"\nSegundo soporte: "+str(results.get("R")[1].shear(int(float(results.get("length"))*1000))[int(float(suppb)*1000)]))
		x=np.linspace(0,float(results.get("length"))/1000,int(results.get("length"))+1)
		y=np.zeros(int(results.get("length")+1))
		plt.figure("Grafica 1")
		plt.title("Grafica de momento flector")
		plt.plot(x, results.get("M"))
		annot_max(x,results.get("M"))
		annot_min(x,results.get("M"))
		plt.xlabel('Posicion (m)')
		plt.ylabel('Momento flector (kN/m)')
		plt.plot(x,y)

		plt.figure("Grafica 2")
		plt.title('Grafica de corte')
		plt.plot(x, results.get("D"))
		annot_max(x,results.get("D"))
		annot_min(x,results.get("D"))
		plt.xlabel('Posicion (m)')
		plt.ylabel('Esfuerzo cortante (kN)')
		plt.plot(x,y)
		plt.show()

	elif beamop=='3':
		
		results= cantilevbeam()
		print("\nEl momento donde se encuentra empotrado es igual a: "+str(results.get("R")))
		x=np.linspace(0,float(results.get("length"))/1000,int(results.get("length"))+1)
		y=np.zeros(int(results.get("length")+1))
		plt.figure("Grafica 1")
		plt.title("Grafica de momento flector")
		plt.plot(x, results.get("M"))
		annot_max(x,results.get("M"))
		annot_min(x,results.get("M"))
		plt.xlabel('Posicion (m)')
		plt.ylabel('Momento flector (kN/m)')
		plt.plot(x,y)

		plt.figure("Grafica 2")
		plt.title('Grafica de corte')
		plt.plot(x, results.get("D"))
		annot_max(x,results.get("D"))
		annot_min(x,results.get("D"))
		plt.xlabel('Posicion (m)')
		plt.ylabel('Esfuerzo cortante (kN)')
		plt.plot(x,y)
		plt.show()