from django.shortcuts import render
from scipy.io import wavfile
from .utilities import apply_ltspice_filter
import numpy as np
import os

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

        configuration = {
            "R1": slider1,
            "R2": slider2,
        }

        dummy, output_data = apply_ltspice_filter("../LTSPICE/Ecualizador de 10 bandas.asc", time, data, params=configuration)


        return render(request, 'app_ecualizador/index.html', context = {"clase": "Electrónica Analógica I"})
