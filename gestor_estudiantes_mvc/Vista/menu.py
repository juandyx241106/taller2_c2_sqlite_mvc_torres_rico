from Controlador.gestor import GestorEstudiantes

def menu():
    gestor = GestorEstudiantes()

    while True:
        print("\n=== GESTOR DE ESTUDIANTES ===")
        print("1. Agregar estudiante")
        print("2. Listar estudiantes (por ID)")
        print("3. Actualizar nota")
        print("4. Eliminar estudiante por correo")
        print("5. Listar por nota descendente")
        print("6. Buscar por nombre")
        print("7. Salir")


        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = input("Nombre: ")
            c = input("Correo: ")
            nota = input("Nota: ")
            print(gestor.agregar_estudiante(n, c, nota))

        elif opcion == "2":
            estudiantes = gestor.listar_estudiantes()
            if isinstance(estudiantes, str):
                print(estudiantes)
            else:
                print("\nID | Nombre | Correo | Nota")
                print("-" * 40)
                for est in estudiantes:
                    print(f"{est[0]} | {est[1]} | {est[2]} | {est[3]}")

        elif opcion == "3":
            c = input("Correo del estudiante: ")
            nota = input("Nueva nota: ")
            print(gestor.actualizar_nota(c, nota))

        elif opcion == "4":
            c = input("Correo del estudiante a eliminar: ")
            print(gestor.eliminar_estudiante(c))

        elif opcion == "5":
            estudiantes = gestor.listar_por_nota_desc()
            if isinstance(estudiantes, str):
                print(estudiantes)
            else:
                print("\n--- ESTUDIANTES ORDENADOS POR NOTA ---")
                for e in estudiantes:
                    print(f"ID: {e[0]} | Nombre: {e[1]} | Correo: {e[2]} | Nota: {e[3]}")

        elif opcion == "6":
            patron = input("Ingrese parte del nombre a buscar: ")
            estudiantes = gestor.buscar_por_nombre(patron)
            if isinstance(estudiantes, str):
                print(estudiantes)
            else:
                print("\n--- RESULTADOS DE BÚSQUEDA ---")
                for e in estudiantes:
                    print(f"ID: {e[0]} | Nombre: {e[1]} | Correo: {e[2]} | Nota: {e[3]}")
        
        elif opcion == "7":
            print("Saliendo del programa...")
            gestor.cerrar_conexion()
            break

        else:
            print("Opción no válida. Intente de nuevo.")



if __name__ == "__main__":
    menu()