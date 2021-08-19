from django.shortcuts import render
from datetime import datetime
import pytz 

# Create your views here.
from bs4 import BeautifulSoup
import requests


url = 'https://weather.com/es-DO/tiempo/hoy/l/DRXX0009:1:DR?Goto=Redirected'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#clima
#<div data-testid="wxPhrase" class="CurrentConditions--phraseValue--17s79">Muy nublado</div>


timeZ_Ny = pytz.timezone('America/Santo_Domingo') 
now = datetime.now(timeZ_Ny)



print (now.hour)

dia = True


if now.hour <= 7  or now.hour >= 20:
    dia = False
    print ("noche")
else:
    dia = True
    print ("dia")




clima_temperatura = soup.find_all('div', class_='CurrentConditions--primary--2SVPh')
equipo = list()
for i in clima_temperatura:
    equipo.append(i.text)

clima_temperatura = equipo[0]
clima = clima_temperatura[3:]


print(clima)


print(clima_temperatura)


# def climamyNublado (request):

#     return render(request,'climamyNublado.html',{'climaRD':clima_temperatura})

#funcion que muestra un clima dependiendo del clima en santo domingo y tambien dependiendo de la hora del dia


def indexclima (request):
    if dia == True:
        if clima == "Soleado":
            return render(request,'climasoleado.html',{'climaRD':clima_temperatura})
        elif clima == "Muy nublado":
            return render(request,'climamyNublado.html',{'climaRD':clima_temperatura})
        elif clima == "nublado" or clima == "Parcialmente nublado":
            return render(request,'climanublado.html',{'climaRD':clima_temperatura})
        elif clima == "Chubascos" or clima == "Chubasco" or clima == "Lluvia débil" or clima == "Chubascos en el área":
            return render(request,'climaChubascos.html',{'climaRD':clima_temperatura})
        elif clima == "Tormentas eléctricas" or clima == "Tormentas eléctricas dispersas" or clima == "Tormentas eléctricas dispersas / Viento" or clima == "Tormentas eléctricas aisladas":
            return render(request,'climaTormentas.html',{'climaRD':clima_temperatura})
    elif dia == False:
        if clima == "Despejado" or clima == "Mayormente despejado" or clima == "Soleado":
            return render(request,'despejadonocheclima.html',{'climaRD':clima_temperatura})
        elif clima == "Muy nublado":
            return render(request,'climamuynubladonoche.html',{'climaRD':clima_temperatura})
        elif clima == "nublado" or clima == "Parcialmente nublado":
            return render(request,'climanubladonoche.html',{'climaRD':clima_temperatura})
        elif clima == "Chubascos" or clima == "Chubasco" or clima == "Lluvia débil" or clima == "Chubascos en el área":
            return render(request,'climaChubascos.html',{'climaRD':clima_temperatura})
        elif clima == "Tormentas eléctricas" or clima == "Tormentas eléctricas dispersas" or clima == "Tormentas eléctricas dispersas / Viento" or clima == "Tormentas eléctricas aisladas":
            return render(request,'climaTormentas.html',{'climaRD':clima_temperatura})
