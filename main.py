from crearepo import crear_repositorio_local
from fork import clonar_o_forkear
from merge import fusionar_ramas
from subir_cambios import subir_cambios_git


def mostrar_menu():
    print("\n" + "=" * 45)
    print("   ASISTENTE DE AUTOMATIZACIÓN GIT & GUÍAS")
    print("=" * 45)
    print("1. Crear repositorio local")
    print("2. Clonar / Forkear repositorio")
    print("3. Fusionar ramas (Merge)")
    print("4. Subir cambios (Commit & Push)")
    print("5. Salir")


def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ").strip()

        if opcion == "1":
            crear_repositorio_local()
        elif opcion == "2":
            clonar_o_forkear()
        elif opcion == "3":
            fusionar_ramas()
        elif opcion == "4":
            subir_cambios_git()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    ejecutar()