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


def generar_archivos_subir_cambios(carpeta_opcion):
    guia = """===================================================
GUÍA DE USO: SUBIR CAMBIOS (PUSH)
===================================================

1. ¿QUÉ HACE ESTA OPCIÓN?
   - Explica el flujo para guardar y publicar modificaciones en GitHub.

2. PASOS MANUALES EN TERMINAL:
   git add .
   git commit -m "update"
   git push origin main
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": (
            "ERROR 1: Updates were rejected (Remote contains work).\nCAUSA:"
            " Hay cambios en GitHub que no tienes localmente.\nSOLUCIÓN:"
            " Ejecuta 'git pull origin main' antes del push."
        ),
        "error_2.txt": (
            "ERROR 2: 'origin' does not appear to be a git repository.\nCAUSA:"
            " Sin remoto configurado.\nSOLUCIÓN: Agrega la URL con 'git remote"
            " add origin <URL>'."
        ),
        "error_3.txt": (
            "ERROR 3: src refspec main does not match any.\nCAUSA: No hay"
            " commits locales previo al push.\nSOLUCIÓN: Haz 'git add .' y"
            ' \'git commit -m "commit"\'.'
        ),
        "error_4.txt": (
            "ERROR 4: Permission denied (Error 403).\nCAUSA: Credenciales sin"
            " permiso de escritura.\nSOLUCIÓN: Revisa tus credenciales en"
            " GitHub."
        ),
        "error_5.txt": (
            "ERROR 5: Nothing to commit.\nCAUSA: No hay cambios"
            " detectados.\nSOLUCIÓN: Modifica y guarda algún archivo primero."
        ),
        "error_6.txt": (
            "ERROR 6: File exceeds 100 MB.\nCAUSA: Archivo demasiado"
            " pesado.\nSOLUCIÓN: Agrégalo a '.gitignore' o usa Git LFS."
        ),
        "error_7.txt": (
            "ERROR 7: Secret Scanning rejected push.\nCAUSA: Exposición de"
            " claves/tokens.\nSOLUCIÓN: Elimina las claves expuestas del"
            " historial."
        ),
        "error_8.txt": (
            "ERROR 8: RPC failed / HTTP 413.\nCAUSA: Límite de búfer HTTP"
            " superado.\nSOLUCIÓN: Incrementa el límite con 'git config"
            " --global http.postBuffer 524288000'."
        ),
    }

    for nombre, contenido in errores.items():
        (carpeta_errores / nombre).write_text(contenido, encoding="utf-8")

    print(
        "📄 Carpeta 'subir_cambios' actualizada en:"
        f" {carpeta_opcion.relative_to(carpeta_opcion.parents[1])}"
    )


def subir_cambios_git():
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "subir_cambios"
    generar_archivos_subir_cambios(carpeta_opcion)

    print("\n" + "=" * 55)
    print("      GUÍA EDUCATIVA: SUBIR CAMBIOS A GITHUB")
    print("=" * 55)
    print("1. Prepara todos los archivos: git add .")
    print('2. Registra los cambios: git commit -m "mensaje"')
    print("3. Sube a la nube: git push origin main")
    print("=" * 55)
    print(
        "✓ Guía y 8 archivos de error generados en github_ayuda/subir_cambios.\n"
    )