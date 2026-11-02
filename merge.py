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


def generar_archivos_merge(carpeta_opcion):
    guia = """===================================================
GUÍA DE USO: FUSIONAR RAMAS (MERGE)
===================================================

1. ¿QUÉ HACE ESTA OPCIÓN?
   - Integra las modificaciones de una rama secundaria hacia una rama principal.

2. PASOS MANUALES EN TERMINAL:
   - git checkout main
   - git merge <rama_origen>
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": """===================================================
ERROR 1: CONFLICT (content): Merge conflict
===================================================
CAUSA: Cambios contradictorios en las mismas líneas de código.
SOLUCIÓN: Abre los archivos en VS Code, resuelve los cambios, haz 'git add .' y luego 'git commit'.""",
        "error_2.txt": """===================================================
ERROR 2: pathspec 'rama' did not match any file
===================================================
CAUSA: La rama de origen no existe en la base de datos local de Git.
SOLUCIÓN: Revisa los nombres con 'git branch' o ejecuta 'git fetch'.""",
        "error_3.txt": """===================================================
ERROR 3: Local changes would be overwritten
===================================================
CAUSA: Tienes archivos modificados sin comitear que chocan con la fusión.
SOLUCIÓN: Ejecuta 'git commit -m "guardado"' o resérvalos con 'git stash'.""",
        "error_4.txt": """===================================================
ERROR 4: Refusing to merge unrelated histories
===================================================
CAUSA: Las ramas no comparten un commit inicial común.
SOLUCIÓN: Ejecuta 'git merge <rama_origen> --allow-unrelated-histories'.""",
        "error_5.txt": """===================================================
ERROR 5: Detached HEAD state
===================================================
CAUSA: Estás apuntando a un commit específico en lugar de a una rama activa.
SOLUCIÓN: Regresa a la rama principal ejecutando 'git checkout main'.""",
        "error_6.txt": """===================================================
ERROR 6: Automatic merge failed; fix conflicts and then commit
===================================================
CAUSA: Hubo conflictos no resueltos y la operación de merge quedó pausada a la mitad.
SOLUCIÓN: Si deseas cancelar la fusión completa, ejecuta en terminal 'git merge --abort'.""",
        "error_7.txt": """===================================================
ERROR 7: Fatal: Not possible to fast-forward, aborting
===================================================
CAUSA: Git está configurado para requerir integraciones limpia estilo Fast-Forward sin divergencias.
SOLUCIÓN: Permite la creación de un commit de fusión ejecutando 'git merge --no-ff <rama_origen>'.""",
        "error_8.txt": """===================================================
ERROR 8: Another git process seems to be running (.git/index.lock)
===================================================
CAUSA: Un proceso anterior de Git se interrumpió abruptamente dejando el archivo de bloqueo activo.
SOLUCIÓN: Cierra todos los editores o elimina manualmente el archivo dentro de tu proyecto '.git/index.lock'.""",
    }

    for nombre_archivo, contenido in errores.items():
        (carpeta_errores / nombre_archivo).write_text(
            contenido, encoding="utf-8"
        )

    print(
        f"📄 Guía y 8 archivos de error independientes creados en: {carpeta_opcion}"
    )


def fusionar_ramas(rama_origen, rama_destino="main"):
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "merge"
    generar_archivos_merge(carpeta_opcion)

    try:
        subprocess.run(["git", "checkout", rama_destino], check=True)
        subprocess.run(["git", "merge", rama_origen], check=True)
        print(
            f"✓ Rama '{rama_origen}' fusionada exitosamente en '{rama_destino}'."
        )
    except Exception as e:
        print(f"❌ Error durante el merge: {e}")