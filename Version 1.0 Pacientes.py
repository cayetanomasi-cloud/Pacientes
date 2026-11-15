import json

def buscar_paciente(archivo_json_pacientes, CUIT):
    """
    Objetivo: Buscar un paciente por su CUIT.
    Parámetros: archivo_json_pacientes y CUIT.
    Retorno: Bandera encontrado y diccionario del paciente.
    """
    try:
        with open(archivo_json_pacientes, 'r', encoding='utf-8') as archivo:
            Pacientes = json.load(archivo)
        
        encontrado = False
        paciente_encontrado = {}
        
        for paciente in Pacientes:
            if str(CUIT) == str(paciente.get('CUIT')):
                encontrado = True
                paciente_encontrado = paciente
                break
                
        return encontrado, paciente_encontrado
    
    except FileNotFoundError:
        print("El archivo no existe.")
        return False, {}
    except Exception as e:
        print("Error:", e)
        return False, {}


def cargar_paciente(CUIT, archivo_json_pacientes):
    """
    Objetivo: Cargar un nuevo paciente en Archivo JSON.
    Parámetros: CUIT y archivo_json_pacientes.
    """
    try:
        try:
            with open(archivo_json_pacientes, 'r', encoding='utf-8') as archivo:
                Pacientes = json.load(archivo)
        except FileNotFoundError:
            Pacientes = []
            
        paciente = {}
        paciente['CUIT'] = CUIT
        paciente['Apellido'] = input("Ingresar apellido: ").strip().capitalize()
        paciente['Nombre'] = input("Ingresar nombre del paciente: ").strip().capitalize()
        paciente['Edad'] = int(input("Ingresar edad: "))
        
        Pacientes.append(paciente)
        
        with open(archivo_json_pacientes, 'w', encoding='utf-8') as archivo:
            json.dump(Pacientes, archivo, indent=4, ensure_ascii=False)
            
        print("Paciente cargado correctamente.")
    except Exception as e:
        print("Error:", e)


def mostrar_pacientes(archivo_json_pacientes):
    try:
        with open(archivo_json_pacientes, 'r', encoding='utf-8') as archivo:
            Pacientes = json.load(archivo)
        return True, Pacientes
    except FileNotFoundError:
        print("El archivo no existe.")
        return False, []
    except Exception as e:
        print("Error:", e)
        return False, []


def crear_archivo_json(archivo_json_pacientes):
    try:
        print("Cargar Primer Paciente:")
        pacientes = []
        paciente = {}
        paciente['CUIT'] = input("Ingresar CUIT: ").strip()
        paciente['Apellido'] = input("Ingresar apellido: ").strip().capitalize()
        paciente['Nombre'] = input("Ingresar nombre del paciente: ").strip().capitalize()
        paciente['Edad'] = int(input("Ingresar edad: "))
        
        pacientes.append(paciente)
        
        with open(archivo_json_pacientes, 'w', encoding='utf-8') as archivo:
            json.dump(pacientes, archivo, indent=4, ensure_ascii=False)
            
        print("Paciente cargado correctamente.")
    except Exception as e:
        print("Error:", e)


def main():
    archivo_json_pacientes = "Pacientes.json"  
    
    opcion = 0
    while opcion != -1:
        print("\n--- PACIENTES ---")
        print("Opcion 1: Buscar paciente")
        print("Opcion 2: Mostrar pacientes")
        print("Opcion -1: SALIR DEL PROGRAMA")
        
        try:
            opcion = int(input("Ingresar opcion PACIENTES: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            CUIT = input("Ingresar CUIT del paciente: ").strip()
            encontrado, paciente = buscar_paciente(archivo_json_pacientes, CUIT)
            
            if encontrado:
                print("Paciente encontrado:")
                print(paciente)
                
                sub_opcion = 0
                while sub_opcion != -1:
                    print("\n--- OPCIONES ---")
                    print("Opcion 1: Dar turno")
                    print("Opcion 2: Actualizar paciente")
                    print("Opcion -1: Regresar")
                    try:
                        sub_opcion = int(input("Ingresar opción: "))
                    except ValueError:
                        continue
                        
                    if sub_opcion == 1:
                        print("Próximamente se completará...")
                    elif sub_opcion == 2:
                        print("Próximamente se completará...")
                    elif sub_opcion == -1:
                        break
                    else:
                        print("Opción incorrecta")
            else:
                print("Paciente no existe en el archivo JSON.")
                try:
                    respuesta = int(input("¿Desea cargarlo? (1 = Si / 2 = No): "))
                    if respuesta == 1:
                        cargar_paciente(CUIT, archivo_json_pacientes)
                    else:
                        print("No se cargó el paciente.")
                except ValueError:
                    print("Opción inválida.")

        elif opcion == 2:
            existe, Pacientes = mostrar_pacientes(archivo_json_pacientes)
            if existe and len(Pacientes) > 0:
                print("\nLISTADO DE PACIENTES:")
                for p in Pacientes:
                    print(p)
            else:
                print("Archivo JSON no existe o está vacío...")
                try:
                    respuesta = int(input("¿Desea crearlo cargando un paciente? (1 = Si / 2 = No): "))
                    if respuesta == 1:
                        crear_archivo_json(archivo_json_pacientes)
                    else:
                        print("No se creó el archivo.")
                except ValueError:
                    print("Opción inválida.")

        elif opcion == -1:
            print("Saliendo del programa...")
        else:
            print("Opción incorrecta.")

main()