from django.db import models

# Create your models here.
class Empleado(models.Model):
    code = models.CharField(verbose_name='Codigo de empleado', max_length=8, unique=True)
    name = models.CharField(verbose_name="Nombre de empleado", max_length=90)
    password = models.CharField(verbose_name="Contraseña", max_length=6)

    def __str__(self):
        return "{0} {1}".format(self.code, self.name)

    class Meta:
        verbose_name= "Empleado"
        verbose_name_plural= "Empleados"

class Venta(models.Model):
    empleados = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Codigo de Venta', max_length=8)
    date = models.DateField(verbose_name='Fecha de venta')
    time = models.TimeField(verbose_name='Hora', max_length=200, unique=True)
    total = models.CharField(verbose_name='Total a pagar', max_length=150)
    id_employee = models.CharField(verbose_name='Id empleado', max_length=100, unique=True)

    def __str__(self):
        return "{0} {1}".format(self.code, self.date, self.time)

    class Meta:
        verbose_name="Venta"
        verbose_name_plural="Ventas"

class Categoria(models.Model):
    code = models.CharField(verbose_name='Codigo de Ctegoria', max_length=8, unique= True)
    name = models.CharField(verbose_name="Categoria", max_length=58)

    def __str__(self):
        return "{0} {1}".format(self.code, self.name)

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural= "Categorias"

class Telefono(models.Model):
    code = models.CharField(verbose_name='Codigo del Telefono', max_length=8, unique=True)
    phone = models.CharField(verbose_name="Numero telefonico", max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.code, self.phone)

    class Meta:
        verbose_name= "Telefono"
        verbose_name_plural= "Telefonos"

class Cliente(models.Model):
    code = models.CharField(verbose_name='Codigo del Cliente', max_length=8, unique=True)
    firstname = models.CharField( verbose_name='Nombre', max_length=80)
    lastname = models.CharField(verbose_name='Apellidos(s)', max_length=80)
    phone = models.CharField(verbose_name='Telefono', max_length=20)
    email = models.CharField( verbose_name='Email', max_length=100)
    direction = models.CharField( verbose_name='direccion', max_length=100)

    def __str__(self):
        return "{0} {1}".format(self.code, self.firstname)

class Meta:
            verbose_name= 'Cliente'
            verbose_name_plural= 'Clientes'

class Proveedor(models.Model):
    code = models.CharField(verbose_name='Codigo del proveedor', max_length=8, unique=True)
    firstname = models.CharField(verbose_name='Nombre', max_length=80)
    lastname = models.CharField(verbose_name='Apellidos(s)', max_length=80)
    phone = models.CharField(verbose_name='Telefono', max_length=20)
    email = models.CharField(verbose_name='Email', max_length=100)
    direction = models.CharField(verbose_name='direccion', max_length=100)

    def __str__(self):
        return "{0} {1} :: {2}".format(self.code, self.firstname, self.lastname)

    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural= 'Proveedores'

class Apartado(models.Model):
    empleados = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Codigo del apartado', max_length=8, unique=True)
    startdate = models.DateField(verbose_name='Fecha de inicio')
    finaldate = models.DateField(verbose_name='Fecha de liquidacion')
    advance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Abono')
    total = models.CharField(verbose_name='Total a pagar', max_length=150)

    def __str__(self):
        return "{0} {1} :: {2}".format(self.code, self.startdate, self.finaldate)

    class Meta:

            verbose_name= 'Apartado'
            verbose_name_plural= 'Apartados'

class Tiene(models.Model):
    apartados = models.ForeignKey(Apartado, on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Codigo del Telefono', max_length=8, unique=True)
    barcode = models.CharField(verbose_name="Codigo de barra", max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.code, self.phone)

    class Meta:
        verbose_name= "Codigo de barra"
        verbose_name_plural= "Codigo de barras"

class Producto(models.Model):
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedores = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Codigo del producto', max_length=8 , unique= True)
    name = models.CharField(verbose_name='Nombre del producto',max_length=200)
    price = models.DecimalField(decimal_places=2, verbose_name='Precio',max_digits=10)
    marca = models.CharField(verbose_name='Marca del producto',max_length=200)
    description = models.CharField(verbose_name='Descripcion del producto', max_length=150)
    saleExistence = models.PositiveIntegerField(verbose_name='Existencia en venta')
    cellarExistence = models.PositiveIntegerField(verbose_name='Existencia en bodega')

    def __str__(self):
        return "{0} - {1} - {2}".format(self.code, self.name, self.price)
    class Meta:

            verbose_name= 'Producto'
            verbose_name_plural= 'Productos'


class Aparece(models.Model):
    ventas = models.ForeignKey(Venta, on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Codigo de ID', max_length=8, unique=True)
    barcode = models.CharField(verbose_name="Codigo de barra", max_length=15)
    cantidadxpro = models.CharField(verbose_name="Cantida total", max_length=30)

    def __str__(self):
        return "{0} {1}".format(self.code, self.barcode)

    class Meta:
        verbose_name= "Aparece"
        verbose_name_plural= "Aparecen"