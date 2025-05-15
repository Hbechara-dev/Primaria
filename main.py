import tkinter as tk
from tkinter import messagebox, font

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Cifrado y Descifrado")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Configuración de fuentes
        self.titulo_font = font.Font(family="Arial", size=16, weight="bold")
        self.subtitulo_font = font.Font(family="Arial", size=12)
        self.boton_font = font.Font(family="Arial", size=10, weight="bold")
        
        # Frame principal
        self.frame_principal = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        self.frame_principal.pack(expand=True, fill="both")
        
        # Título
        self.label_titulo = tk.Label(
            self.frame_principal, 
            text="Aplicación de Cifrado y Descifrado",
            font=self.titulo_font,
            bg="#f0f0f0",
            fg="#333333"
        )
        self.label_titulo.pack(pady=10)
        
        # Información del autor
        self.frame_autor = tk.Frame(self.frame_principal, bg="#ffffff", relief=tk.RIDGE, bd=2)
        self.frame_autor.pack(pady=20, fill="x")
        
        self.label_autor_titulo = tk.Label(
            self.frame_autor, 
            text="Información del Autor",
            font=self.subtitulo_font,
            bg="#ffffff",
            fg="#333333"
        )
        self.label_autor_titulo.pack(pady=10)
        
        # Aquí puedes colocar tu información personal
        self.label_nombre = tk.Label(
            self.frame_autor, 
            text="HERMES BECHARA CORDOBA",
            font=self.subtitulo_font,
            bg="#ffffff"
        )
        self.label_nombre.pack(pady=3)
        
        
        # Frame para botones
        self.frame_botones = tk.Frame(self.frame_principal, bg="#f0f0f0")
        self.frame_botones.pack(pady=20)
        
        # Botones para navegar a otras ventanas
        self.boton_cifrado = tk.Button(
            self.frame_botones,
            text="Cifrar Número",
            command=self.abrir_ventana_cifrado,
            bg="#007bff",
            fg="white",
            font=self.boton_font,
            padx=15,
            pady=8,
            relief=tk.RAISED,
            bd=2
        )
        self.boton_cifrado.pack(side=tk.LEFT, padx=10)
        
        self.boton_descifrado = tk.Button(
            self.frame_botones,
            text="Descifrar Número",
            command=self.abrir_ventana_descifrado,
            bg="#28a745",
            fg="white",
            font=self.boton_font,
            padx=15,
            pady=8,
            relief=tk.RAISED,
            bd=2
        )
        self.boton_descifrado.pack(side=tk.LEFT, padx=10)
    
    def abrir_ventana_cifrado(self):
        ventana_cifrado = tk.Toplevel(self.root)
        VentanaCifrado(ventana_cifrado, self.root)
    
    def abrir_ventana_descifrado(self):
        ventana_descifrado = tk.Toplevel(self.root)
        VentanaDescifrado(ventana_descifrado, self.root)


class VentanaCifrado:
    def __init__(self, ventana, ventana_principal):
        self.ventana = ventana
        self.ventana_principal = ventana_principal
        self.ventana.title("Cifrado de Números")
        self.ventana.geometry("500x400")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#f0f0f0")
        self.ventana.transient(ventana_principal)
        self.ventana.grab_set()
        
        # Configuración de fuentes
        self.titulo_font = font.Font(family="Arial", size=16, weight="bold")
        self.texto_font = font.Font(family="Arial", size=12)
        self.boton_font = font.Font(family="Arial", size=10, weight="bold")
        
        # Frame principal
        self.frame_principal = tk.Frame(self.ventana, bg="#f0f0f0", padx=20, pady=20)
        self.frame_principal.pack(expand=True, fill="both")
        
        # Título
        self.label_titulo = tk.Label(
            self.frame_principal, 
            text="Cifrado de Números",
            font=self.titulo_font,
            bg="#f0f0f0",
            fg="#333333"
        )
        self.label_titulo.pack(pady=10)
        
        # Frame para formulario
        self.frame_formulario = tk.Frame(self.frame_principal, bg="#ffffff", relief=tk.RIDGE, bd=2)
        self.frame_formulario.pack(pady=20, fill="x")
        
        # Instrucciones
        self.label_instrucciones = tk.Label(
            self.frame_formulario,
            text="Ingrese un número entero de 6 dígitos para cifrarlo",
            font=self.texto_font,
            bg="#ffffff"
        )
        self.label_instrucciones.pack(pady=10)
        
        # Entrada de datos
        self.entrada_numero = tk.Entry(
            self.frame_formulario,
            font=self.texto_font,
            width=20,
            justify="center",
            bd=2
        )
        self.entrada_numero.pack(pady=10)
        
        # Botón de cifrado
        self.boton_cifrar = tk.Button(
            self.frame_formulario,
            text="Cifrar",
            command=self.cifrar,
            bg="#007bff",
            fg="white",
            font=self.boton_font,
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=2
        )
        self.boton_cifrar.pack(pady=10)
        
        # Frame para resultados
        self.frame_resultado = tk.Frame(self.frame_principal, bg="#ffffff", relief=tk.RIDGE, bd=2)
        self.frame_resultado.pack(pady=20, fill="x")
        
        # Etiqueta para mostrar el resultado
        self.label_resultado_titulo = tk.Label(
            self.frame_resultado,
            text="Resultado del cifrado:",
            font=self.texto_font,
            bg="#ffffff"
        )
        self.label_resultado_titulo.pack(pady=5)
        
        self.label_resultado = tk.Label(
            self.frame_resultado,
            text="",
            font=font.Font(family="Arial", size=16, weight="bold"),
            bg="#ffffff",
            fg="#007bff"
        )
        self.label_resultado.pack(pady=10)
        
        # Botón de volver
        self.boton_volver = tk.Button(
            self.frame_principal,
            text="Volver al Menú Principal",
            command=self.volver,
            bg="#6c757d",
            fg="white",
            font=self.boton_font,
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=2
        )
        self.boton_volver.pack(pady=10)
    
    def cifrar(self):
        # Obtener el número ingresado
        try:
            numero = self.entrada_numero.get()
            
            # Validar que sea un número entero de 6 dígitos
            if not numero.isdigit() or len(numero) != 6:
                messagebox.showerror("Error", "Debe ingresar un número entero de 6 dígitos")
                return
            
            # Proceso de cifrado
            # 1. Cifrar cada dígito (sumando 7 y tomando el residuo de dividir entre 10)
            digitos = [int(d) for d in numero]
            cifrados = [(d + 7) % 10 for d in digitos]
            
            # 2. Intercambiar posiciones
            cifrados[0], cifrados[2] = cifrados[2], cifrados[0]  # Primer dígito con tercero
            cifrados[1], cifrados[3] = cifrados[3], cifrados[1]  # Segundo dígito con cuarto
            cifrados[4], cifrados[5] = cifrados[5], cifrados[4]  # Quinto dígito con sexto
            
            # Convertir los dígitos cifrados de nuevo a una cadena
            resultado = ''.join(map(str, cifrados))
            
            # Mostrar el resultado
            self.label_resultado.config(text=resultado)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def volver(self):
        self.ventana.destroy()


class VentanaDescifrado:
    def __init__(self, ventana, ventana_principal):
        self.ventana = ventana
        self.ventana_principal = ventana_principal
        self.ventana.title("Descifrado de Números")
        self.ventana.geometry("500x400")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#f0f0f0")
        self.ventana.transient(ventana_principal)
        self.ventana.grab_set()
        
        # Configuración de fuentes
        self.titulo_font = font.Font(family="Arial", size=16, weight="bold")
        self.texto_font = font.Font(family="Arial", size=12)
        self.boton_font = font.Font(family="Arial", size=10, weight="bold")
        
        # Frame principal
        self.frame_principal = tk.Frame(self.ventana, bg="#f0f0f0", padx=20, pady=20)
        self.frame_principal.pack(expand=True, fill="both")
        
        # Título
        self.label_titulo = tk.Label(
            self.frame_principal, 
            text="Descifrado de Números",
            font=self.titulo_font,
            bg="#f0f0f0",
            fg="#333333"
        )
        self.label_titulo.pack(pady=10)
        
        # Frame para formulario
        self.frame_formulario = tk.Frame(self.frame_principal, bg="#ffffff", relief=tk.RIDGE, bd=2)
        self.frame_formulario.pack(pady=20, fill="x")
        
        # Instrucciones
        self.label_instrucciones = tk.Label(
            self.frame_formulario,
            text="Ingrese un número cifrado de 6 dígitos para descifrarlo",
            font=self.texto_font,
            bg="#ffffff"
        )
        self.label_instrucciones.pack(pady=10)
        
        # Entrada de datos
        self.entrada_numero = tk.Entry(
            self.frame_formulario,
            font=self.texto_font,
            width=20,
            justify="center",
            bd=2
        )
        self.entrada_numero.pack(pady=10)
        
        # Botón de descifrado
        self.boton_descifrar = tk.Button(
            self.frame_formulario,
            text="Descifrar",
            command=self.descifrar,
            bg="#28a745",
            fg="white",
            font=self.boton_font,
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=2
        )
        self.boton_descifrar.pack(pady=10)
        
        # Frame para resultados
        self.frame_resultado = tk.Frame(self.frame_principal, bg="#ffffff", relief=tk.RIDGE, bd=2)
        self.frame_resultado.pack(pady=20, fill="x")
        
        # Etiqueta para mostrar el resultado
        self.label_resultado_titulo = tk.Label(
            self.frame_resultado,
            text="Resultado del descifrado:",
            font=self.texto_font,
            bg="#ffffff"
        )
        self.label_resultado_titulo.pack(pady=5)
        
        self.label_resultado = tk.Label(
            self.frame_resultado,
            text="",
            font=font.Font(family="Arial", size=16, weight="bold"),
            bg="#ffffff",
            fg="#28a745"
        )
        self.label_resultado.pack(pady=10)
        
        # Botón de volver
        self.boton_volver = tk.Button(
            self.frame_principal,
            text="Volver al Menú Principal",
            command=self.volver,
            bg="#6c757d",
            fg="white",
            font=self.boton_font,
            padx=15,
            pady=5,
            relief=tk.RAISED,
            bd=2
        )
        self.boton_volver.pack(pady=10)
    
    def descifrar(self):
        # Obtener el número ingresado
        try:
            numero = self.entrada_numero.get()
            
            # Validar que sea un número entero de 6 dígitos
            if not numero.isdigit() or len(numero) != 6:
                messagebox.showerror("Error", "Debe ingresar un número cifrado de 6 dígitos")
                return
            
            # Proceso de descifrado
            # 1. Convertir a lista de dígitos
            digitos = [int(d) for d in numero]
            
            # 2. Revertir los intercambios de posiciones
            digitos[0], digitos[2] = digitos[2], digitos[0]  # Primer dígito con tercero
            digitos[1], digitos[3] = digitos[3], digitos[1]  # Segundo dígito con cuarto
            digitos[4], digitos[5] = digitos[5], digitos[4]  # Quinto dígito con sexto
            
            # 3. Descifrar cada dígito
            descifrados = [(d + 3) % 10 for d in digitos]  # (d + 10 - 7) % 10 = (d + 3) % 10
            
            # 4. Convertir de nuevo a una cadena
            resultado = ''.join(map(str, descifrados))
            
            # Mostrar el resultado
            self.label_resultado.config(text=resultado)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def volver(self):
        self.ventana.destroy()


def main():
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
