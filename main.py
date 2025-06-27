import argparse 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from metro_ethernet import MetroEthernetFrame, capture_ethernet_frames
from sdh_sonet import SDHFrame, capture_sdh_frames
from mpls import MPLSLabel, capture_mpls_labels
from export_csv import export_to_csv

def ejecutar_captura():
    protocolo = protocolo_var.get()
    interfaz = interfaz_var.get()
    timeout = int(timeout_var.get())
    archivo_csv = archivo_csv_var.get()

    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, "===== Simulación de Tramas WAN =====\n")
    eth = MetroEthernetFrame("AA:BB:CC:DD:EE:01", "11:22:33:44:55:66", "0x0800", "Datos Ethernet")
    resultado_text.insert(tk.END, f"[Trama Ethernet]: {eth.show_frame()}\n")
    sdh = SDHFrame("HeaderSDH", "Pointer001", "PayloadSDH", "CRC16")
    resultado_text.insert(tk.END, f"[Trama SDH/SONET]: {sdh.show_frame()}\n")
    mpls = MPLSLabel(label=104857, exp=0, s=1, ttl=64)
    resultado_text.insert(tk.END, f"[Etiqueta MPLS]: {mpls.show_label()}\n")

    resultado_text.insert(tk.END, f"\n===== Captura de paquetes {protocolo.upper()} (PyShark) =====\n")
    if protocolo == 'ethernet':
        captured = capture_ethernet_frames(interface=interfaz, timeout=timeout)
        rows = [frame.show_frame() for frame in captured]
    elif protocolo == 'sdh':
        captured = capture_sdh_frames(interface=interfaz, timeout=timeout)
        rows = [frame.show_frame() for frame in captured]
    else:
        captured = capture_mpls_labels(interface=interfaz, timeout=timeout)
        rows = [label.show_label() for label in captured]

    resultado_text.insert(tk.END, f"\n===== Exportando resultados a CSV =====\n")
    export_to_csv(rows, filename=archivo_csv)
    resultado_text.insert(tk.END, f"Exportado a {archivo_csv}\n")
    messagebox.showinfo("Finalizado", f"Captura y exportación completadas.\nArchivo: {archivo_csv}")

def seleccionar_csv():
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if archivo:
        archivo_csv_var.set(archivo)

root = tk.Tk()
root.title("Captura de Tramas WAN")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Protocolo:").grid(row=0, column=0, sticky="e")
protocolo_var = tk.StringVar(value="mpls")
ttk.Combobox(frame, textvariable=protocolo_var, values=["ethernet", "sdh", "mpls"], state="readonly").grid(row=0, column=1)

ttk.Label(frame, text="Interfaz:").grid(row=1, column=0, sticky="e")
interfaz_var = tk.StringVar(value="eth0")
ttk.Entry(frame, textvariable=interfaz_var).grid(row=1, column=1)

ttk.Label(frame, text="Tiempo (s):").grid(row=2, column=0, sticky="e")
timeout_var = tk.StringVar(value="10")
ttk.Entry(frame, textvariable=timeout_var).grid(row=2, column=1)

ttk.Label(frame, text="Archivo CSV:").grid(row=3, column=0, sticky="e")
archivo_csv_var = tk.StringVar(value="captura.csv")
ttk.Entry(frame, textvariable=archivo_csv_var).grid(row=3, column=1)
ttk.Button(frame, text="Seleccionar...", command=seleccionar_csv).grid(row=3, column=2)

ttk.Button(frame, text="Iniciar Captura", command=ejecutar_captura).grid(row=4, column=0, columnspan=3, pady=10)

resultado_text = tk.Text(root, height=15, width=80)
resultado_text.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()