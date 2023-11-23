from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nom_proveedor = models.CharField(max_length=20)
    apell_proveedor = models.CharField(max_length=20)
    cuil_proveedor = models.BigIntegerField()
    tel_proveedor = models.BigIntegerField()
    dom_proveedor = models.CharField(max_length=50, default='sin domicilio')
    correo_proveedor = models.EmailField()

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    nom_componente = models.CharField(max_length=20)
    descripcion_componente = models.CharField(max_length=100)
    stock_componente = models.IntegerField()

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    nom_componente_nuevos = models.CharField(max_length=20)
    descripcion_componente_nuevos = models.CharField(max_length=100)
    cantidad_componente_nuevos = models.IntegerField()
    fecha_compra = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class ComponentesXCompras(models.Model):
    id_componentexcompra = models.AutoField(primary_key=True)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nom_tecnico = models.CharField(max_length=20)
    apell_tecnico = models.CharField(max_length=20)
    cuil_tecnico = models.BigIntegerField()
    tel_tecnico = models.BigIntegerField()
    dom_tecnico = models.CharField(max_length=50, default='sin domicilio')
    alias_tecnico = models.CharField(max_length=50)
    contra_tecnico = models.CharField(max_length=50)

class EstadoTecnico(models.Model):
    id_estado_tecnico = models.AutoField(primary_key=True)
    nom_estado_tecnico = models.CharField(max_length=20)

class TecnicosXEstados(models.Model):
    id_tecnicoxestado = models.AutoField(primary_key=True)
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    id_estado_tecnico = models.ForeignKey(EstadoTecnico, on_delete=models.CASCADE)
    fecha_estado_disponible = models.DateField()

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nom_usuario = models.CharField(max_length=20)
    apell_usuario = models.CharField(max_length=20)
    cuil_usuario = models.BigIntegerField()
    dom_usuario = models.CharField(max_length=50, default='sin domicilio')
    tel_usuario = models.BigIntegerField()
    alias_usuario = models.CharField(max_length=20)
    contra_usuario = models.CharField(max_length=20)


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    descripcion_solicitud = models.CharField(max_length=100)
    fecha_solicitud = models.DateField()

class EstadoSolicitud(models.Model):
    id_estado_solicitud = models.AutoField(primary_key=True)
    nom_estado_solicitud = models.CharField(max_length=20)

class UsuariosXSolicitudes(models.Model):
    id_usuarioxsolicitud = models.AutoField(primary_key=True)
    id_estado_solicitud = models.ForeignKey(EstadoSolicitud, on_delete=models.CASCADE)
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_estado_solicitud = models.DateField()

class Incidente(models.Model):
    id_incidente = models.AutoField(primary_key=True)
    descripcion_incidente = models.CharField(max_length=100)
    id_usuarioxsolicitud = models.ForeignKey(UsuariosXSolicitudes, on_delete=models.CASCADE)
    id_tecnicoxestado = models.ForeignKey(TecnicosXEstados, on_delete=models.CASCADE)

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nom_equipo = models.CharField(max_length=30)
    descripcion_equipo = models.CharField(max_length=100)
    fecha_antiguedad = models.DateField()

class EstadoEquipo(models.Model):
    id_estado_equipo = models.AutoField(primary_key=True)
    nom_estado_equipo = models.CharField(max_length=20)

class EquiposXUsuarios(models.Model):
    id_equipoxusuario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_estado_equipo = models.ForeignKey(EstadoEquipo, on_delete=models.CASCADE)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_estado_equipo = models.DateField()

class EquiposXComponentes(models.Model):
    id_equipoxcomponente = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    descripcion_cambio = models.CharField(max_length=100)
    fecha_cambio = models.DateField()

class IncidentesXEquipos(models.Model):
    id_incidentexequipo = models.AutoField(primary_key=True)
    descripcion_reparacion = models.CharField(max_length=50)
    fecha_reparacion = models.DateField()
    id_incidente = models.ForeignKey(Incidente, on_delete=models.CASCADE)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)


