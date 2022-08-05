from matplotlib import pyplot as plt
from sklearn import tree
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import webbrowser
from pandas import DataFrame

datos = []
with open ('CDMXYEDO.csv','r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        datos.append([float(linea[1]), float(linea[2])])

y = []
z = []

for elem in sorted(datos):
    y.append(elem[0])
    z.append(elem[1])
print(y)
print(z)

x=np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]).reshape((-1,1))



model=LinearRegression()
model.fit(x,y)
R_sq= model.score(x,y)
y_pred_CDMX = model.predict(x)
print(y_pred_CDMX)

model2=LinearRegression()
model2.fit(x,z)
R_sq2= model2.score(x,z)
y_pred_EDO = model2.predict(x)
print(y_pred_EDO)

datosStr="["
for i in range(len(x)):
    if(i==len(x)-1):
        datosStr=datosStr+str(y_pred_CDMX[i])+"]"
    elif(i<len(x)):
        datosStr=datosStr+str(y_pred_CDMX[i])+','
datosStr2="["
for i in range(len(x)):
    if(i==len(x)-1):
        datosStr2=datosStr2+str(y_pred_EDO[i])+"]"
    elif(i<len(x)):
        datosStr2=datosStr2+str(y_pred_EDO[i])+','
print (datosStr2)

datos2 = []
with open ('HealthySexencusta.csv','r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        datos2.append([str(linea[1]), str(linea[2])])

PrimeraRelacion = []
Estudios = []

for elem in sorted(datos2):
    PrimeraRelacion.append(elem[0])
    Estudios.append(elem[1])
print(PrimeraRelacion)
print(Estudios)

datos3 = []
with open ('HealthySexencusta.csv','r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        datos3.append([str(linea[0]), str(linea[3])])

Edad = []
DeDonde = []

for elem in sorted(datos3):
    Edad.append(elem[0])
    DeDonde.append(elem[1])
print(Edad)
print(DeDonde)

datos4 = []
with open ('HealthySexencusta.csv','r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        datos4.append([str(linea[4]), str(linea[5])])

DeDondeApren = []
pITS = []

for elem in sorted(datos4):
    DeDondeApren.append(elem[0])
    pITS.append(elem[1])
print(DeDondeApren)
print(pITS)

datos5 = []
with open ('HealthySexencusta.csv','r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        datos5.append([str(linea[6]), str(linea[7])])

Opinion = []
Metodo = []

for elem in sorted(datos5):
    Opinion.append(elem[0])
    Metodo.append(elem[1])
print(Opinion)
print(Metodo)

respuestas=[]
barras=[]
ceros = 0
unos = 0

features = [["15","1","2","0","5","1"],["18","1","2","0","5","1"],["22","2","2","1","5","2"],["21","1","2","0","5","1"],["15","1","5","0","5","1"],["18","2","6","0","5","1"]]
labels=["0","1","1","1","1","0"]
classifier = tree.DecisionTreeClassifier()
classifier.fit(features,labels)
for i in range(len(Opinion)):
    res = classifier.predict([[Edad[i],DeDonde[i],DeDondeApren[i],pITS[i],Opinion[i],Metodo[i]]])
    respuestas.append(res)


datosStrTree="["
for i in range(len(respuestas)):
    if(i==len(respuestas)-1):
        datosStrTree=datosStrTree+str(respuestas[i])+"]"
    elif(i<len(respuestas)):
        datosStrTree=datosStrTree+str(respuestas[i])+','
print("cadena")
datosStrTreeFinal=datosStrTree.replace("[", "")
datosStrTreeFinal=datosStrTreeFinal.replace("]", "")
ceros = datosStrTreeFinal.count("0")
unos = datosStrTreeFinal.count("1")
print(ceros)
print(unos)

cerosReales=0
unosReales=0

for i in range(len(PrimeraRelacion)):
    if(PrimeraRelacion[i]=="1"):
        unosReales=unosReales+1
    else:
        cerosReales=cerosReales+1


features = [["15","1","2","0","5","1"],["18","1","2","0","5","1"],["22","2","2","1","5","2"],["21","1","2","0","5","1"],["15","1","5","0","5","1"],["18","5","2","0","5","1"]]
labels=["0","2","3","5","2","5"]
classifier = tree.DecisionTreeClassifier()
classifier.fit(features,labels)
for i in range(len(Opinion)):
    res = classifier.predict([[Edad[i],DeDonde[i],DeDondeApren[i],pITS[i],Opinion[i],Metodo[i]]])
    respuestas.append(res)

datosStrTree="["
for i in range(len(respuestas)):
    if(i==len(respuestas)-1):
        datosStrTree=datosStrTree+str(respuestas[i])+"]"
    elif(i<len(respuestas)):
        datosStrTree=datosStrTree+str(respuestas[i])+','
print("cadena")
datosStrTreeFinal=datosStrTree.replace("[", "")
datosStrTreeFinal=datosStrTreeFinal.replace("]", "")
Aceros=0
Aunos=0
Ados=0
Atres=0
Acinco=0
Aceros = datosStrTreeFinal.count("0")/2
Aunos = datosStrTreeFinal.count("1")/2
Ados = datosStrTreeFinal.count("2")/2
Atres = datosStrTreeFinal.count("3")/2
Acinco = datosStrTreeFinal.count("5")/2
print(Aceros,Aunos,Ados,Atres,Acinco)
print(datosStrTreeFinal)

RAceros=0
RAunos=0
RAdos=0
RAtres=0
RAcinco=0

for i in range(len(Estudios)):
    if(Estudios[i]=="0"):
        RAceros=RAceros+1
    elif(Estudios[i]=="1"):
        RAunos=RAunos+1
    elif(Estudios[i]=="2"):
        RAdos=RAdos+1
    elif(Estudios[i]=="3"):
        RAtres=RAtres+1
    else:
        RAcinco=RAcinco+1
RAunos=RAdos/2
RAdos=RAdos/2
print(RAceros,RAunos,RAdos,RAtres,RAcinco)


Data={ 'x' : Edad,
          'y' : pITS
      }
df=DataFrame(Data,columns=['x','y'])
print(df)
plt.scatter(df['x'],df['y'])
plt.show()



kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
centrosX = []
centrosY = []
for i in range(3):
    centrosX.append(centroids[i][0])
    centrosY.append(centroids[i][1])
print(centrosX)
print(centrosY)

valoresCluster="{"
for i in range(len(centrosX)):
    if(i!=len(centrosX)-1):
        valoresCluster=valoresCluster+"x:"+str(centrosX[i])+", y:"+str(centrosY[i])
        valoresCluster=valoresCluster+"},{"
    else:
        valoresCluster=valoresCluster+"x:"+str(centrosX[i])+", y:"+str(centrosY[i])
        valoresCluster=valoresCluster+"}"
print(valoresCluster)

valoresTodosLosP="{"

for i in range(len(Edad)):
    if(i!=len(Edad)-1):
        valoresTodosLosP=valoresTodosLosP+"x:"+str(Edad[i])+", y:"+str(pITS[i])
        valoresTodosLosP=valoresTodosLosP+"},{"
    else:
        valoresTodosLosP=valoresTodosLosP+"x:"+str(Edad[i])+", y:"+str(pITS[i])
        valoresTodosLosP=valoresTodosLosP+"}"
print(valoresTodosLosP)


Data={ 'x' : DeDonde,
          'y' : DeDondeApren
      }
df=DataFrame(Data,columns=['x','y'])
print(df)
plt.scatter(df['x'],df['y'])
plt.show()

kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
centrosX2 = []
centrosY2 = []
for i in range(3):
    centrosX2.append(centroids[i][0])
    centrosY2.append(centroids[i][1])
print(centrosX2)
print(centrosY2)

valoresCluster2="{"
for i in range(3):
    print(i)
    if(i!=2):
        valoresCluster2=valoresCluster2+"x:"+str(centrosX2[i])+", y:"+str(centrosY2[i])
        valoresCluster2=valoresCluster2+"},{"
    else:
        valoresCluster2=valoresCluster2+"x:"+str(centrosX2[i])+", y:"+str(centrosY2[i])
        valoresCluster2=valoresCluster2+"}"
print(valoresCluster2)

valoresTodosLosP2="{"

for i in range(len(DeDonde)):
    if(i!=len(DeDonde)-1):
        valoresTodosLosP2=valoresTodosLosP2+"x:"+str(DeDonde[i])+", y:"+str(DeDondeApren[i])
        valoresTodosLosP2=valoresTodosLosP2+"},{"
    else:
        valoresTodosLosP2=valoresTodosLosP2+"x:"+str(DeDonde[i])+", y:"+str(DeDondeApren[i])
        valoresTodosLosP2=valoresTodosLosP2+"}"
print(valoresTodosLosP2)


f = open('algoritmos.html', 'w')
mensaje = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE-edge">	
	<title>Modulo de python</title>
	<script	src="./js/Chart.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Dancing+Script|Raleway:500,600&display=swap" rel="stylesheet">

	<!-- Materialize con el css-->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
	<link rel="stylesheet" type="text/css" href="./css/estilo.css">
</head>
<body>
        
        <div style="width:100%;">
                <a class="btn btn-primary btn-lg" href="#" role="button" id="boton">Mostrar G. 1 &raquo;</a>
            		<canvas id="MiGrafica" width="400" height="300"></canvas>
                
                <a class="btn btn-primary btn-lg" href="#" role="button" id="boton2">Mostrar G. 2 &raquo;</a>
                    <canvas id="MiGrafica2" width="400" height="300"></canvas>
                
                <a class="btn btn-primary btn-lg" href="#" role="button" id="boton3">Mostrar G. 3 &raquo;</a>
                    <canvas id="MiGrafica3" width="400" height="300"></canvas>
                
                <a class="btn btn-primary btn-lg" href="#" role="button" id="boton4">Mostrar G. 4 &raquo;</a>
                    <canvas id="MiGrafica4" width="400" height="300"></canvas>
                
                <a class="btn btn-primary btn-lg" href="#" role="button" id="boton5">Mostrar G. 5 &raquo;</a>
                    <canvas id="MiGrafica5" width="400" height="300"></canvas>
                
                <a class="btn btn-primary btn-lg" href="#" role="button" id="boton6">Mostrar G. 6 &raquo;</a>
                    <canvas id="MiGrafica6" width="400" height="300"></canvas>
        </div>
        
        
</body>
<script>


let miCanvas=document.getElementById("MiGrafica").getContext("2d");
	var chart = new Chart(miCanvas,{
		type:"line",
		data:{
			labels:"""+"[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]"+""",
			datasets:[{
				label:"Prediccion de Contagios de VIH en CDMX:",
				backgroundColor:"rgb(0,0,0)",
				borderColor:"rgb(12,12,12)",
                fill:false,
				data:"""+datosStr+"""
			},
            {
                label:"Contagios Reales de VIH en CDMX:",
				backgroundColor:"rgb(216, 240, 231)",
				borderColor:"rgb(216, 240, 231)",
                fill:false,
				data:"""+"[170,724,757,911,920,954,1157,1394,1435,1522,1860,1884]"+"""
                }]
		}
	})
    let miCanvas2=document.getElementById("MiGrafica2").getContext("2d");
	var chart = new Chart(miCanvas2,{
		type:"line",
		data:{
			labels:"""+"[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]"+""",
			datasets:[{
				label:"Prediccion de Contagios de VIH en EDOMEX:",
				backgroundColor:"rgb(0,0,0)",
				borderColor:"rgb(12,12,12)",
                fill:false,
				data:"""+datosStr2+"""
			},
            {
                label:"Contagios Reales de VIH en EDOMEX:",
				backgroundColor:"rgb(216, 240, 231)",
				borderColor:"rgb(216, 240, 231)",
                fill:false,
				data:"""+"[2020,2002,1931,1606,1481,1481,1442,1217,1179,1058,1014,419]"+"""
                }]
		}
	})
    let miCanvas3=document.getElementById("MiGrafica3").getContext("2d");
	var chart = new Chart(miCanvas3,{
		type:"bar",
		data:{
			labels:"""+"['Si','No']"+""",
			datasets:[{
				label:"Prediccion de Personas que Ya han tenido su primer relacion sexual:",
				backgroundColor:"rgb(0,0,0)",
				borderColor:"rgb(12,12,12)",
                fill:false,
				data:["""+str(unos)+""","""+str(ceros)+"""]
			},
            {
                label:"Datos Reales de Personas que Ya han tenido su primer relacion sexual:",
				backgroundColor:"rgb(216, 240, 231)",
				borderColor:"rgb(216, 240, 231)",
                fill:false,
				data:["""+str(unosReales)+""","""+str(cerosReales)+"""]
                }]
		}
	})
    let miCanvas4=document.getElementById("MiGrafica4").getContext("2d");
	var chart = new Chart(miCanvas4,{
		type:"bar",
		data:{
			labels:"""+"['0','1','2','3','5']"+""",
			datasets:[{
				label:"Prediccion de los anos que las personas han tenido educacion sexual:",
				backgroundColor:"rgb(0,0,0)",
				borderColor:"rgb(12,12,12)",
                fill:false,
				data:["""+str(Aceros)+""","""+str(Aunos)+""","""+str(Ados)+""","""+str(Atres)+""","""+str(Acinco)+"""]
			},
            {
                label:"Datos Reales de los anos que las personas han tenido educacion sexual:",
				backgroundColor:"rgb(216, 240, 231)",
				borderColor:"rgb(216, 240, 231)",
                fill:false,
				data:["""+str(RAceros)+""","""+str(RAunos)+""","""+str(RAdos)+""","""+str(RAtres)+""","""+str(RAcinco)+"""]
                }]
		}
	})
    let miCanvas5=document.getElementById("MiGrafica5").getContext("2d");
	var chart = new Chart(miCanvas5,{
		type:"scatter",
		data:{
			datasets:[{
				label:"Clustering en relacion Edades y Pruebas de ITS:",
				pointBackgroundColor:['red','red','red'],
				data:[
                        """+valoresCluster+","+valoresTodosLosP+"""
                    ]
            }]
		}
	})
    let miCanvas6=document.getElementById("MiGrafica6").getContext("2d");
	var chart = new Chart(miCanvas6,{
		type:"scatter",
		data:{
			datasets:[{
				label:"Clustering en relacion Deseo/Aprendi:",
				pointBackgroundColor:['red','red','red'],
				data:[
                        """+valoresCluster2+","+valoresTodosLosP2+"""
                    ]
            }]
		}
	})



document.getElementById("MiGrafica").style.visibility='hidden';
document.getElementById("MiGrafica2").style.visibility='hidden';
document.getElementById("MiGrafica3").style.visibility='hidden';
document.getElementById("MiGrafica4").style.visibility='hidden';
document.getElementById("MiGrafica5").style.visibility='hidden';
document.getElementById("MiGrafica6").style.visibility='hidden';


var boton = document.getElementById("boton");
boton.onclick = function(e) {
    e.preventDefault();
    document.getElementById("MiGrafica").style.visibility='visible';
    document.getElementById("MiGrafica2").style.visibility='hidden';
    document.getElementById("MiGrafica3").style.visibility='hidden';
    document.getElementById("MiGrafica4").style.visibility='hidden';
    document.getElementById("MiGrafica5").style.visibility='hidden';
    document.getElementById("MiGrafica6").style.visibility='hidden';
    
}
var boton2 = document.getElementById("boton2");
boton2.onclick = function(e) {
    e.preventDefault();
    document.getElementById("MiGrafica").style.visibility='hidden';
    document.getElementById("MiGrafica2").style.visibility='visible';
    document.getElementById("MiGrafica3").style.visibility='hidden';
    document.getElementById("MiGrafica4").style.visibility='hidden';
    document.getElementById("MiGrafica5").style.visibility='hidden';
    document.getElementById("MiGrafica6").style.visibility='hidden';
    
}
    
var boton3 = document.getElementById("boton3");
boton3.onclick = function(e) {
    e.preventDefault();
    document.getElementById("MiGrafica").style.visibility='hidden';
    document.getElementById("MiGrafica2").style.visibility='hidden';
    document.getElementById("MiGrafica3").style.visibility='visible';
    document.getElementById("MiGrafica4").style.visibility='hidden';
    document.getElementById("MiGrafica5").style.visibility='hidden';
    document.getElementById("MiGrafica6").style.visibility='hidden';
    
}
var boton4 = document.getElementById("boton4");
boton4.onclick = function(e) {
    e.preventDefault();
    document.getElementById("MiGrafica").style.visibility='hidden';
    document.getElementById("MiGrafica2").style.visibility='hidden';
    document.getElementById("MiGrafica3").style.visibility='hidden';
    document.getElementById("MiGrafica4").style.visibility='visible';
    document.getElementById("MiGrafica5").style.visibility='hidden';
    document.getElementById("MiGrafica6").style.visibility='hidden';
    
}

var boton5 = document.getElementById("boton5");
boton5.onclick = function(e) {
    e.preventDefault();
    document.getElementById("MiGrafica").style.visibility='hidden';
    document.getElementById("MiGrafica2").style.visibility='hidden';
    document.getElementById("MiGrafica3").style.visibility='hidden';
    document.getElementById("MiGrafica4").style.visibility='hidden';
    document.getElementById("MiGrafica5").style.visibility='visible';
    document.getElementById("MiGrafica6").style.visibility='hidden';
    
}
var boton6 = document.getElementById("boton6");
boton6.onclick = function(e) {
    e.preventDefault();
    document.getElementById("MiGrafica").style.visibility='hidden';
    document.getElementById("MiGrafica2").style.visibility='hidden';
    document.getElementById("MiGrafica3").style.visibility='hidden';
    document.getElementById("MiGrafica4").style.visibility='hidden';
    document.getElementById("MiGrafica5").style.visibility='hidden';
    document.getElementById("MiGrafica6").style.visibility='visible';
    
}
</script>
</html>
"""
f.write(mensaje)
f.close()
webbrowser.open_new_tab('algoritmos.html')