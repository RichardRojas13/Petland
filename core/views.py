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

def suscripcionUsuario (request):
    if request.method == 'POST':
        montoDonacion = request.POST['montoDonacion']
        nombreUser = request.POST['nombreUser']

        selUsuario = Usuario.objects.get(nombreUser=nombreUser)

        Suscrito.objects.create(nombreUser=selUsuario)

    return redirect('index.html')

def desSuscripcion (request):
    if request.method == 'POST':
        nombreUser = request.POST['nombreUser']

        selUsuario = Suscrito.objects.get(nombreUser=nombreUser)

        
        Suscrito.objects.filter(nombreUser=selUsuario).delete()

    return redirect('index.html')


def listadoCompras (request):
    return render(request,'core/listadoCompras.html')


def obtenerDatosCompraProducto (request):
    if request.method == 'POST':
        idProducto = request.POST['idProducto']

        selProducto = Producto.objects.get(idProducto=idProducto)
        
        datosObtenidos = {
            'selProducto' : selProducto
        }

    return render(request, 'core/listadoCompras.html', datosObtenidos)


def mantenedorClientes (request):
    clientes = Cliente.objects.order_by("idRutCli", "nombreCli")
    clientesObtenidos = {
        'clientes': clientes
    }

    return render(request, 'core/mantenedorClientes.html', clientesObtenidos)

def formAddClientes (request):
    return render(request, 'core/formAddClientes.html')

def addClientes (request):
    if request.method == 'POST':
        nroRutCli = request.POST['idRutCli']
        dvRun = request.POST['dvRun']
        nombreCli = request.POST['nombreCli']
        apellidocli = request.POST['apellidocli']


        Cliente.objects.create(idRutCli=nroRutCli,dvRun=dvRun,nombreCli=nombreCli,apellidocli=apellidocli)

    return redirect('mantenedorClientes.html')

def formUpdClientes (request):
    return render(request, 'core/formUpdClientes.html')

def updClientes (request):
    if request.method == 'POST':
        nroRutCli = request.POST['idRutCli']
        nombreCli = request.POST['nombreCli']
        apellidocli = request.POST['apellidocli']
        
        selCliente = Cliente.objects.get(idRutCli=nroRutCli)

        Cliente.objects.filter(idRutCli=nroRutCli).update(nombreCli=nombreCli, apellidocli=apellidocli)

    return redirect('mantenedorClientes.html')    