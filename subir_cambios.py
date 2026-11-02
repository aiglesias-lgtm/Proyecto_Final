import subprocess
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
   - Prepara los archivos ('git add .').
   - Registra el punto de control ('git commit -m').
   - Sube los cambios al remoto ('git push origin <rama>').

2. PASOS MANUALES EN TERMINAL:
   - git add .
   - git commit -m "mensaje"
   - git push origin main
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": """===================================================
ERROR 1: Updates were rejected (Remote contains work)
===================================================
CAUSA: Hay cambios remotos en GitHub que no has bajado a tu equipo.
SOLUCIÓN: Ejecuta 'git pull origin main' antes de realizar el push.""",
        "error_2.txt": """===================================================
ERROR 2: 'origin' does not appear to be a git repository
===================================================
CAUSA: El proyecto local no está vinculado a una URL en GitHub.
SOLUCIÓN: Ejecuta 'git remote add origin <URL_del_repositorio>'.""",
        "error_3.txt": """===================================================
ERROR 3: src refspec main does not match any
===================================================
CAUSA: Intentas hacer push sin ningún commit previo en la rama.
SOLUCIÓN: Ejecuta 'git add .' y realiza tu primer 'git commit -m "primer commit"'.""",
        "error_4.txt": """===================================================
ERROR 4: Permission to user denied (Error 403)
===================================================
CAUSA: La cuenta autenticada no posee permisos de colaborador o dueño.
SOLUCIÓN: Solicita permisos de acceso o actualiza las credenciales.""",
        "error_5.txt": """===================================================
ERROR 5: Nothing to commit, working tree clean
===================================================
CAUSA: No hay cambios detectados respecto al último commit.
SOLUCIÓN: Modifica y guarda algún archivo antes de ejecutar la opción.""",
        "error_6.txt": """===================================================
ERROR 6: File exceeds GitHub's file size limit of 100 MB
===================================================
CAUSA: Intentas subir un archivo individual que supera los 100 MB.
SOLUCIÓN: Quita el archivo del commit, agregalo a '.gitignore' o utiliza Git LFS.""",
        "error_7.txt": """===================================================
ERROR 7: Push rejected due to Secret Scanning / Protection
===================================================
CAUSA: GitHub detectó claves API, tokens o contraseñas en el código comiteado.
SOLUCIÓN: Elimina los secretos expuestos del historial o genera nuevas credenciales.""",
        "error_8.txt": """===================================================
ERROR 8: RPC failed; result=22, HTTP code = 413 / Out of memory
===================================================
CAUSA: El volumen de datos subidos en el push supera el límite de búfer HTTP de Git.
SOLUCIÓN: Incrementa el límite ejecutando 'git config --global http.postBuffer 524288000'.""",
    }

    for nombre_archivo, contenido in errores.items():
        (carpeta_errores / nombre_archivo).write_text(
            contenido, encoding="utf-8"
        )

    print(
        f"📄 Guía y 8 archivos de error independientes creados en: {carpeta_opcion}"
    )


def subir_cambios_git(mensaje_commit, rama="main"):
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "subir_cambios"
    generar_archivos_subir_cambios(carpeta_opcion)

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)
        subprocess.run(["git", "push", "origin", rama], check=True)
        print(f"✓ Cambios subidos con éxito a la rama '{rama}'.")
    except Exception as e:
        print(f"❌ Error al subir cambios: {e}")