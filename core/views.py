from django.shortcuts import redirect, render
from .models import Producto, Venta, Cliente
# Create your views here.

# Create your views here.
def index(request):
    return render(request,'core/index.html')

# Login de usuarios previamente registrados
def LoUsRe(request):
    return render(request,'core/LoUsRe.html')

# Validación: Existe el usuario en la BD
def verificacionUser (request):
    if request.method == 'POST':
        username = request.POST['usernmaneCli']
        password = request.POST['passwordUser']

        selUsuario = Usuario.objects.get(nombreUser=username, passwordUser=password)

    return redirect('index.html')

# Registro de nuevos Usuarios
def registroUser (request):
    if request.method == 'POST':
        numRut = request.POST['nroRutCli']
        dvRut = request.POST['dvRun']
        nombres = request.POST['nombreCli']
        apellidos = request.POST['apellidocli']
        nombreUser = request.POST['nombreUser']
        passwordUser = request.POST['passwordUser']

        # 1. Agregando datos a la taba Cliente
        Cliente.objects.create(idRutCli=numRut, dvRun=dvRut, nombreCli=nombres, apellidocli=apellidos)

        # 2.- Agregando datos a la tabla Usuario
        selCliente = Cliente.objects.get(idRutCli=numRut)
        Usuario.objects.create(nombreUser=nombreUser, passwordUser=passwordUser, idRutCli=selCliente)

    return redirect('index.html')