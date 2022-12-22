from django.shortcuts import render, redirect
from app.models import Persona, Intituto
from app.forms import FormPersona
from django.http import JsonResponse
from app.serializers import PersonasSerializer, IntitutoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404



# Create your views here.

def index(request):
    return render(request, 'index.html')

def listaPersonas(request):
    pro = Persona.objects.all()
    data = {'personas': pro}
    return render(request, 'listaPersona.html', data)

def agregarpersona(request):
    form = FormPersona()
    if request.method == 'POST':
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarpersona.html', data)

def eliminarPersona(request, id):
    pro = Persona.objects.get(id = id)
    pro.delete()
    return redirect('/listaPersonas')

def actualizaPersona(request, id):
    pro = Persona.objects.get(id = id)
    form = FormPersona(instance=pro)
    if request.method == 'POST':
        form = FormPersona(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarpersona.html', data)

def inscritos(request):
    ins = Persona.objects.all()
    data = {'inscritos': list(ins.values('id', 'nombre', 'telefono', 'fechaInscripcion', 'institucion', 'horaInscripcion', 'estado', 'observacion'))}
    
    return JsonResponse(data)

@api_view (['GET', 'POST'])
def intitutosLista(request):
    if request.method == 'GET':
        estu = Intituto.objects.all()
        serial = IntitutoSerializer(estu, many=True)
        return Response(serial.data)
        
    if request.method == 'POST':
        serial = IntitutoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def intitutosDetalle(request, pk):
    try:
        estu = Intituto.objects.get(idinstituto=pk)
    except Intituto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = IntitutoSerializer(estu)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = IntitutoSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class personasInscritas(APIView):
    def get(self, request):
        estu = Persona.objects.all()
        serial = PersonasSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = PersonasSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class personasDetalles(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(id=pk)
        except Persona.DoesNotExist:
            return Http404

    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = PersonasSerializer(estu)
        return Response(serial.data)
                
    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = PersonasSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)