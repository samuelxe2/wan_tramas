# Proyecto de Captura y Análisis de Tramas WAN

Este proyecto tiene como objetivo capturar en tiempo real diferentes estructuras de información a nivel WAN, incluyendo tramas de Metro Ethernet, SDH/SONET y etiquetas MPLS. Los datos capturados se exportan a un archivo CSV para su análisis posterior.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
wan_tramas
├── src
│   ├── capture.py          # Captura de paquetes MPLS en tiempo real
│   ├── metro_ethernet.py   # Definición de la clase MetroEthernetFrame
│   ├── sdh_sonet.py        # Definición de la clase SDHFrame
│   ├── mpls.py             # Definición de la clase MPLSLabel
│   ├── export_csv.py       # Funciones para exportar datos a CSV
│   └── main.py             # Punto de entrada del programa (interfaz gráfica)
├── requirements.txt        # Dependencias del proyecto
├── iniciar_captura.bat     # Archivo para ejecutar la interfaz gráfica con doble clic
└── README.md               # Documentación del proyecto
```

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Ejecución

### Opción 1: Desde la terminal

Puedes ejecutar el programa desde la terminal con:

```
python src/main.py
```

### Opción 2: Doble clic

Haz doble clic en el archivo `iniciar_captura.bat` para abrir la interfaz gráfica directamente.

> **Nota:** Si el archivo `.bat` no funciona, asegúrate de tener Python agregado al PATH del sistema.

## Funcionalidades

- **Interfaz gráfica:** Permite seleccionar el protocolo, la interfaz de red, el tiempo de captura y el archivo CSV de salida.
- **Captura de Paquetes MPLS, Ethernet y SDH/SONET:** Utiliza la biblioteca PyShark para capturar paquetes en tiempo real.
- **Definición de Tramas:** Incluye clases para representar tramas de Metro Ethernet y SDH/SONET, así como etiquetas MPLS.
- **Exportación a CSV:** Los datos capturados se pueden exportar a un archivo CSV para su análisis posterior.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.