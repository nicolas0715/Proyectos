from twilio.rest import Client
from django.shortcuts import render
import datetime
import pymysql
from .models import Persona

# Create your views here.

fecha_actual_ctx = datetime.date.today() 

def index(request):
    cumple = []
    registros = Persona.objects.all()
    for registro in registros:
        if registro.fecha_nacimiento == fecha_actual_ctx:
            cumple.append([registro.nombre, registro.apellido, registro.fecha_nacimiento])
    if len(cumple) != 0:
        return render(request, 'index.html', {'ctx': fecha_actual_ctx, 'cumple': cumple[0], 'cantidad': len(cumple)})
    else:
        return render(request, 'index.html', {'ctx': fecha_actual_ctx, 'cumple': 'Nadie'})

def agregar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        if nombre and apellido and fecha_nacimiento:
            persona = Persona(nombre=nombre, apellido=apellido, fecha_nacimiento = fecha_nacimiento)
            persona.save()
        return render(request, 'agregar.html', {'ctx': fecha_actual_ctx, 'msj': 'Enviado Exitosamente!'})
    return render(request, 'agregar.html', {'ctx': fecha_actual_ctx})

def ver_mas(request):
    un_dia = datetime.timedelta(days=1)  
    fecha_ayer = fecha_actual_ctx - un_dia
    fecha_manana = fecha_actual_ctx + un_dia
    
    cumple_ayer = []
    cumple_hoy = []
    cumple_manana = []
    registros = Persona.objects.all()
    for registro in registros:
        if registro.fecha_nacimiento == fecha_ayer:
            cumple_ayer.append([registro.nombre, registro.apellido, registro.fecha_nacimiento])
        elif registro.fecha_nacimiento == fecha_actual_ctx:
            cumple_hoy.append([registro.nombre, registro.apellido, registro.fecha_nacimiento])
        elif registro.fecha_nacimiento == fecha_manana:
            cumple_manana.append([registro.nombre, registro.apellido, registro.fecha_nacimiento])
    return render(request, 'ver_mas.html', {'ctx': fecha_actual_ctx, 'fecha_ayer': fecha_ayer, 'fecha_manana': fecha_manana, 'cumple_ayer': cumple_ayer, 'cumple_hoy': cumple_hoy, 'cumple_manana': cumple_manana})

def buscar(request):
    if request.method == "POST":
        opcion = request.POST.get("opciones")
        valor = request.POST.get('valor')
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="cumpleanios"
        )
        sql = f"SELECT * FROM cumpleanios_persona WHERE {opcion} = '{valor}'"
        cursor = conn.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        resultado = []
        for registro in registros:
            resultado.append(registro) 
        print(opcion, valor)
        return render(request, 'buscar.html', {'ctx': fecha_actual_ctx, 'resultado': resultado})
    return render(request, 'buscar.html', {'ctx': fecha_actual_ctx})