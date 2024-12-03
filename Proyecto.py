class Tarea:
    def __init__(self, titulo, prioridad):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):  
        estado = chr(0x2714) if self.completada else chr(0x274C)
        return f"[{estado}] {self.titulo} - Prioridad: {self.prioridad}"

class GestorDeTareas:
    PRIORIDAD_VALORES = {'baja': 1, 'media': 2, 'alta': 3}

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, prioridad):
        if prioridad in self.PRIORIDAD_VALORES:
            self.tareas.append(Tarea(titulo, prioridad))
        else:
            print("Prioridad no válida.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas disponibles.")
            return []
        tareas_ordenadas = sorted(self.tareas, key=lambda tarea: self.PRIORIDAD_VALORES[tarea.prioridad], reverse=True)
        print("Lista de Tareas:")
        for i, tarea in enumerate(tareas_ordenadas):
            print(f"{i}. {tarea}")
        return tareas_ordenadas

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)

    def guardar_tareas_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as file:
            for tarea in self.tareas:
                file.write(str(tarea) + '\n')

def main():
    gestor = GestorDeTareas()
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Eliminar tarea")
        print("5. Guardar tareas en archivo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            titulo = input("Título de la tarea: ")
            prioridad = input("Prioridad (baja, media, alta): ").lower()
            gestor.agregar_tarea(titulo, prioridad)
            print("Tarea agregada.")
        elif opcion == '2':
            tareas_ordenadas = gestor.mostrar_tareas()
            try:
                indice = int(input("Selecciona el índice de la tarea a marcar como completada: "))
                if 0 <= indice < len(tareas_ordenadas):
                    tareas_ordenadas[indice].marcar_completada()
                    print("Tarea marcada como completada.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == '3':
            gestor.mostrar_tareas()
        elif opcion == '4':
            tareas_ordenadas = gestor.mostrar_tareas()
            try:
                indice = int(input("Selecciona el índice de la tarea a eliminar: "))
                if 0 <= indice < len(tareas_ordenadas):
                    gestor.eliminar_tarea(tareas_ordenadas[indice])
                    print("Tarea eliminada.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == '5':
            nombre_archivo = input("Nombre del archivo para guardar tareas: ")
            gestor.guardar_tareas_en_archivo(nombre_archivo)
            print("Tareas guardadas en el archivo.")
        elif opcion == '6':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()