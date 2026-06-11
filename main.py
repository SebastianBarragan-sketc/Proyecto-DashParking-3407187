from datetime import datetime

import qrcode

from fastapi import FastAPI, HTTPException

from modelos.conductor import Conductor
from modelos.vehiculo import Vehiculo
from modelos.cupo import Cupo
from modelos.tarifa import Tarifa
from modelos.pago import Pago
from modelos.registro_ingreso import RegistroIngreso

from schemas.conductor_schema import ConductorCreate
from schemas.vehiculo_schema import VehiculoCreate
from schemas.cupo_schema import CupoCreate
from schemas.tarifa_schema import TarifaCreate
from schemas.pago_schema import PagoCreate
from schemas.registro_schema import RegistroCreate

from storage.memoria import (
    conductores,
    vehiculos,
    cupos,
    tarifas,
    registros,
    pagos
)

app = FastAPI()

@app.get("/conductores")
def listar_conductores():
    return [
        conductor.mostrarInformacion()
        for conductor in conductores
    ]


@app.get("/conductores/{id_conductor}")
def obtener_conductor(id_conductor: int):
    for conductor in conductores:
        if conductor.idUsuario == id_conductor:
            return conductor.mostrarInformacion()
    raise HTTPException(404, "Conductor no encontrado")


@app.post("/conductores")
def crear_conductor(datos: ConductorCreate):
    conductor = Conductor(
        len(conductores) + 1,
        datos.nombre,
        datos.correo,
        datos.numeroLicencia
    )
    conductores.append(conductor)
    return conductor.mostrarInformacion()


@app.delete("/conductores/{id_conductor}")
def eliminar_conductor(id_conductor: int):
    for conductor in conductores:
        if conductor.idUsuario == id_conductor:
            conductores.remove(conductor)
            return {"mensaje": "Conductor eliminado"}
    raise HTTPException(404, "Conductor no encontrado")


@app.get("/vehiculos")
def listar_vehiculos():
    return [
        {
            "placa": v.placa,
            "tipoVehiculo": v.tipoVehiculo,
            "modelo": v.modelo,
            "idConductor": v.idConductor
        }
        for v in vehiculos
    ]


@app.post("/vehiculos")
def crear_vehiculo(datos: VehiculoCreate):
    existe = False
    for conductor in conductores:
        if conductor.idUsuario == datos.idConductor:
            existe = True
    if not existe:
        raise HTTPException(404, "Conductor no encontrado")
    vehiculo = Vehiculo(
        datos.placa,
        datos.tipoVehiculo,
        datos.modelo,
        datos.idConductor
    )
    vehiculos.append(vehiculo)
    return {"mensaje": "Vehiculo creado"}


@app.delete("/vehiculos/{placa}")
def eliminar_vehiculo(placa: str):
    for vehiculo in vehiculos:
        if vehiculo.placa == placa:
            vehiculos.remove(vehiculo)
            return {"mensaje": "Vehiculo eliminado"}
    raise HTTPException(404, "Vehiculo no encontrado")


@app.get("/cupos")
def listar_cupos():
    return [
        {
            "idEspacio": c.idEspacio,
            "piso": c.piso,
            "estado": c.estado
        }
        for c in cupos
    ]


@app.post("/cupos")
def crear_cupo(datos: CupoCreate):
    cupo = Cupo(
        len(cupos) + 1,
        datos.piso,
        datos.estado
    )
    cupos.append(cupo)
    return {"mensaje": "Cupo creado"}


@app.get("/tarifas")
def listar_tarifas():
    return [
        {
            "idTarifa": t.idTarifa,
            "tipoVehiculo": t.tipoVehiculo,
            "valorMinuto": t.valorMinuto
        }
        for t in tarifas
    ]


@app.post("/tarifas")
def crear_tarifa(datos: TarifaCreate):
    tarifa = Tarifa(
        len(tarifas) + 1,
        datos.tipoVehiculo,
        datos.valorMinuto
    )
    tarifas.append(tarifa)
    return {"mensaje": "Tarifa creada"}


@app.get("/registros")
def listar_registros():
    return registros


@app.post("/registros")
def crear_registro(datos: RegistroCreate):
    tarifa = None
    for t in tarifas:
        if t.idTarifa == datos.idTarifa:
            tarifa = t
    if tarifa is None:
        raise HTTPException(404, "Tarifa no encontrada")
    try:
        entrada = datetime.combine(datos.fecha, datos.horaEntrada)
        salida = datetime.combine(datos.fecha, datos.horaSalida)
        minutos = (salida - entrada).total_seconds() / 60
        valor = minutos * tarifa.valorMinuto
    except Exception:
        valor = 0
    registro = RegistroIngreso(
        len(registros) + 1,
        datos.fecha,
        datos.horaEntrada,
        datos.horaSalida,
        valor,
        datos.placaVehiculo,
        datos.idEspacio,
        datos.idTarifa
    )
    registros.append(registro)
    return {"mensaje": "Registro creado", "valorCalculado": valor}


@app.get("/pagos")
def listar_pagos():
    return pagos


@app.post("/pagos")
def crear_pago(datos: PagoCreate):
    id_pago = len(pagos) + 1
    contenido_qr = f"""
Pago #{id_pago}
Monto: {datos.monto}
Metodo: {datos.metodoPago}
Estado: {datos.estadoPago}
"""
    imagen = qrcode.make(contenido_qr)
    ruta = f"qr_pago_{id_pago}.png"
    imagen.save(ruta)
    pago = Pago(
        id_pago,
        datos.monto,
        datos.metodoPago,
        datos.estadoPago,
        ruta
    )
    pagos.append(pago)
    return {"mensaje": "Pago creado", "qr": ruta}
