# DashParking

## Descripción

DashParking es un sistema de gestión de parqueaderos diseñado para optimizar el control y administración de espacios de estacionamiento. El proyecto busca centralizar procesos que normalmente se realizan de forma manual, permitiendo llevar un registro organizado de conductores, vehículos, cupos disponibles, tarifas, ingresos y pagos.

La solución facilita la supervisión de la ocupación del parqueadero, el cálculo automático de cobros según el tiempo de permanencia y la gestión de pagos mediante códigos QR. De esta manera, se mejora el control operativo, se reduce la posibilidad de errores en los registros y se agiliza la atención a los usuarios del servicio.

El sistema fue desarrollado aplicando los principios de Programación Orientada a Objetos y utilizando FastAPI para la construcción de una API REST que permite interactuar con cada uno de los módulos del parqueadero.

---

## Objetivos del Proyecto

* Aplicar los principios fundamentales de la Programación Orientada a Objetos.
* Desarrollar una API REST utilizando FastAPI.
* Gestionar la información de conductores y vehículos.
* Administrar los cupos disponibles dentro del parqueadero.
* Controlar los registros de ingreso y salida de vehículos.
* Calcular automáticamente los valores correspondientes al servicio de estacionamiento.
* Gestionar pagos mediante generación de códigos QR.
* Implementar una estructura modular y escalable para la organización del sistema.

---

## Principios de POO Aplicados

### Encapsulación

Los atributos de las entidades fueron definidos como privados mediante el uso de doble guion bajo (`__atributo`) y se accede a ellos mediante propiedades (`@property`).

### Herencia

La clase `Conductor` hereda de la clase abstracta `Usuario`.

### Abstracción

La clase `Usuario` fue implementada como una clase abstracta utilizando el módulo `abc` de Python.

### Polimorfismo

Las clases derivadas implementan el método abstracto `mostrarInformacion()`, permitiendo comportamientos específicos según el tipo de objeto.

---

## Funcionalidades

### Conductores

* Crear conductores.
* Consultar conductores.
* Buscar conductores por ID.
* Eliminar conductores.

### Vehículos

* Registrar vehículos.
* Consultar vehículos registrados.
* Eliminar vehículos.

### Cupos

* Registrar espacios de estacionamiento.
* Consultar disponibilidad de cupos.

### Tarifas

* Registrar tarifas según el tipo de vehículo.
* Consultar tarifas registradas.

### Registros de Ingreso

* Registrar entradas y salidas de vehículos.
* Calcular automáticamente el valor del servicio según el tiempo de permanencia.

### Pagos

* Registrar pagos.
* Generar códigos QR asociados a cada pago realizado.

---

## Interfaz Web

El sistema cuenta con una interfaz web desarrollada en HTML que complementa la API y facilita la interacción con los usuarios.

### Inicio

Página principal de presentación de la plataforma y acceso a las diferentes funcionalidades.

### Login

Formulario de autenticación para el acceso de usuarios al sistema.

### Registro

Formulario para la creación de nuevas cuentas de usuario.

### Dashboard

Panel principal desde el cual se visualiza la información general y se gestionan las funcionalidades del parqueadero.

---

## Instalación

### Clonar repositorio

```bash
git clone <repositorio>
cd PROYECTO
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar servidor

```bash
uvicorn main:app --reload
```

---

## Documentación de la API

Una vez iniciado el servidor, FastAPI genera automáticamente una documentación interactiva accesible desde:

```text
http://127.0.0.1:8000/docs
```

Esta interfaz permite probar todos los endpoints disponibles, enviar solicitudes y visualizar las respuestas generadas por el sistema.