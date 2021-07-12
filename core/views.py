from django.shortcuts import redirect, render
from .models import Producto, Usuario, Venta, Cliente, Suscrito

def index(request):
    return render(request,'core/index.html')


def LoUsRe(request):
    return render(request,'core/LoUsRe.html')

def verificacionUser (request):
    if request.method == 'POST':
        username = request.POST['usernmaneCli']
        password = request.POST['passwordUser']

        selUsuario = Usuario.objects.get(nombreUser=username, passwordUser=password)

    return redirect('index.html')


def registroUser (request):
    if request.method == 'POST':
        numRut = request.POST['nroRutCli']
        dvRut = request.POST['dvRun']
        nombres = request.POST['nombreCli']
        apellidos = request.POST['apellidocli']
        nombreUser = request.POST['nombreUser']
        passwordUser = request.POST['passwordUser']

        Cliente.objects.create(idRutCli=numRut, dvRun=dvRut, nombreCli=nombres, apellidocli=apellidos)
 
        selCliente = Cliente.objects.get(idRutCli=numRut)
        Usuario.objects.create(nombreUser=nombreUser, passwordUser=passwordUser, idRutCli=selCliente)

    return redirect('index.html')


def donarSuscripcion (request):
    return render(request,'core/donarSuscripcion.html')

class userObtenido:
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad
                super().__init__()


def obtenerUser (request):
    nombreUser = userObtenido("Usuario", "16")
    contexto = {"nombreUser": nombreUser}
    return render(request, 'core/index.html', contexto)


def cerrarSesión (request):
    messages = print("Your form was saved") 
    return redirect('LoUsRe.html')