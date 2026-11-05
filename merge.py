from pathlib import Path


def obtener_ruta_escritorio():
    home = Path.home()
    for item in home.iterdir():
        if item.is_dir() and ("OneDrive" in item.name or "Personal" in item.name):
            if (item / "Escritorio").exists():
                return item / "Escritorio"
            if (item / "Desktop").exists():
                return item / "Desktop"
    if (home / "Escritorio").exists():
        return home / "Escritorio"
    return home / "Desktop"


def generar_archivos_merge(carpeta_opcion):
    guia = """===================================================
GUÍA DE USO: FUSIONAR RAMAS (MERGE)
===================================================

1. ¿QUÉ HACE ESTA OPCIÓN?
   - Explica el flujo para integrar modificaciones entre dos ramas.

2. PASOS MANUALES EN TERMINAL:
   git checkout main
   git merge feature
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": (
            "ERROR 1: CONFLICT (content).\nCAUSA: Cambios contradictorios en"
            " el mismo archivo.\nSOLUCIÓN: Resuelve conflictos en VS Code,"
            " guarda, haz 'git add .' y 'git commit'."
        ),
        "error_2.txt": (
            "ERROR 2: pathspec did not match any file(s).\nCAUSA: La rama no"
            " existe localmente.\nSOLUCIÓN: Consulta las ramas disponibles con"
            " 'git branch'."
        ),
        "error_3.txt": (
            "ERROR 3: Local changes would be overwritten.\nCAUSA: Tienes"
            " cambios sin guardar.\nSOLUCIÓN: Haz 'git commit' o resérvalos"
            " con 'git stash'."
        ),
        "error_4.txt": (
            "ERROR 4: Refusing to merge unrelated histories.\nCAUSA: Sin"
            " commits iniciales en común.\nSOLUCIÓN: Usa 'git merge <rama>"
            " --allow-unrelated-histories'."
        ),
        "error_5.txt": (
            "ERROR 5: Detached HEAD state.\nCAUSA: Estás sobre un commit y no"
            " una rama.\nSOLUCIÓN: Vuelve con 'git checkout main'."
        ),
        "error_6.txt": (
            "ERROR 6: Automatic merge failed.\nCAUSA: Proceso de fusión"
            " interrumpido por conflictos.\nSOLUCIÓN: Cancela con 'git merge"
            " --abort'."
        ),
        "error_7.txt": (
            "ERROR 7: Not possible to fast-forward.\nCAUSA: Divergencia entre"
            " ramas.\nSOLUCIÓN: Fuerza un commit de fusión con 'git merge"
            " --no-ff <rama>'."
        ),
        "error_8.txt": (
            "ERROR 8: index.lock activo.\nCAUSA: Proceso de Git"
            " bloqueado.\nSOLUCIÓN: Elimina el archivo '.git/index.lock'."
        ),
    }

    for nombre, contenido in errores.items():
        (carpeta_errores / nombre).write_text(contenido, encoding="utf-8")

    print(
        "📄 Carpeta 'merge' actualizada en:"
        f" {carpeta_opcion.relative_to(carpeta_opcion.parents[1])}"
    )


def fusionar_ramas():
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "merge"
    generar_archivos_merge(carpeta_opcion)

    print("\n" + "=" * 55)
    print("      GUÍA EDUCATIVA: FUSIONAR RAMAS (MERGE)")
    print("=" * 55)
    print("1. Cambia a la rama destino: git checkout main")
    print("2. Fusiona la rama secundaria: git merge <nombre_rama>")
    print("3. Si hay conflictos, resuélvelos en el editor y haz commit.")
    print("=" * 55)
    print("✓ Guía y 8 archivos de error generados en github_ayuda/merge.\n")