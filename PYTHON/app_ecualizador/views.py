from django.shortcuts import render
from scipy.io import wavfile
from .utilities import apply_ltspice_filter
import numpy as np
import os
from PyLTSpice.LTSpiceBatch import SimCommander

# Create your views here.
def Home(request):

    if request.method == "GET":
        return render(request, 'app_ecualizador/index.html', context = {"clase": "Electrónica Analógica I"})

    elif request.method == "POST":
        slider1 = int(request.POST.get('slider1'))
        slider2 = int(request.POST.get('slider2'))
        slider3 = int(request.POST.get('slider3'))
        slider4 = int(request.POST.get('slider4'))
        slider5 = int(request.POST.get('slider5'))
        slider6 = int(request.POST.get('slider6'))
        slider7 = int(request.POST.get('slider7'))
        slider8 = int(request.POST.get('slider8'))
        slider9 = int(request.POST.get('slider9'))
        slider10 = int(request.POST.get('slider10'))

        Gain = int(request.POST.get('gain'))
        Volumen = int(request.POST.get('volume'))

        Pista2 = request.FILES["pista2"]
        Pista1 = request.FILES["pista1"]

        samplerate, data = wavfile.read(Pista1.temporary_file_path())
        time = np.linspace(0, data.shape[0]/samplerate, data.shape[0])
        data = data[:,0]

        LTC = SimCommander("D:\\Archivos\\Documentos\\Universidad y colegio\\UVG\\2022\\Primer Semestre\\Electrónica analógica 1\\Proyectos\\Proyecto - Ecualizador 10 bandas\\LTSPICE\\Ecualizador de 10 bandas.asc")
        LTC.set_component_value('R34', slider1)
        LTC.set_component_value('R35', slider2)
        LTC.set_component_value('R36', slider3)
        LTC.set_component_value('R37', slider4)
        LTC.set_component_value('R38', slider5)
        LTC.set_component_value('R39', slider6)
        LTC.set_component_value('R40', slider7)
        LTC.set_component_value('R41', slider8)
        LTC.set_component_value('R42', slider9)
        LTC.set_component_value('R43', slider10)
        LTC.run()
        LTC.wait_completion()
        #dummy, output_data = apply_ltspice_filter("../LTSPICE/Ecualizador de 10 bandas.asc", time, data, params=configuration)


        return render(request, 'app_ecualizador/index.html', context = {"clase": "Electrónica Analógica I"})
