import os
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


def generar_archivos_crear_repo(carpeta_opcion):
    guia = """===================================================
GUÍA DE USO: CREAR REPOSITORIO LOCAL
===================================================

1. ¿QUÉ HACE ESTA OPCIÓN?
   - Crea una nueva carpeta local.
   - Inicializa la estructura interna de Git (.git) mediante 'git init'.

2. PASOS MANUALES EN TERMINAL:
   - mkdir <nombre_carpeta>
   - cd <nombre_carpeta>
   - git init
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": """===================================================
ERROR 1: 'git' no se reconoce como un comando
===================================================
CAUSA: Git no está instalado en el sistema o falta agregarlo al PATH.
SOLUCIÓN: Descarga el instalador desde https://git-scm.com/ y reinicia la terminal.""",
        "error_2.txt": """===================================================
ERROR 2: Permission denied (Permiso denegado)
===================================================
CAUSA: El usuario no posee privilegios de escritura en el directorio destino.
SOLUCIÓN: Ejecuta VS Code como Administrador o elige una ruta con permisos.""",
        "error_3.txt": """===================================================
ERROR 3: Invalid argument / Caracteres no permitidos
===================================================
CAUSA: El nombre de la carpeta contiene caracteres prohibidos (<, >, :, ", /, \\, |, ?, *).
SOLUCIÓN: Utiliza únicamente letras, números, guiones bajos (_) o guiones medios (-).""",
        "error_4.txt": """===================================================
ERROR 4: No space left on device (Sin espacio)
===================================================
CAUSA: La unidad de almacenamiento no cuenta con espacio libre suficiente.
SOLUCIÓN: Libera espacio en el disco o selecciona otra ubicación.""",
        "error_5.txt": """===================================================
ERROR 5: Repositorio ya existente / Corrupto
===================================================
CAUSA: La carpeta ya contiene una estructura de Git previa o dañada.
SOLUCIÓN: Muestra archivos ocultos, elimina la carpeta '.git' y vuelve a intentar.""",
        "error_6.txt": """===================================================
ERROR 6: UNC paths are not supported / Ruta de red no mapeada
===================================================
CAUSA: Intentas inicializar un repositorio en una ruta de red compartida (\\\\servidor\\carpeta).
SOLUCIÓN: Mapea la carpeta de red a una letra de unidad local (ej. Z:) o trabaja en una ruta local.""",
        "error_7.txt": """===================================================
ERROR 7: Operation not permitted / Bloqueo de Antivirus
===================================================
CAUSA: Windows Defender o un antivirus externo bloqueó la creación de carpetas ocultas.
SOLUCIÓN: Agrega la carpeta de tu proyecto a las excepciones de tu software antivirus.""",
        "error_8.txt": """===================================================
ERROR 8: warning: LF will be replaced by CRLF
===================================================
CAUSA: Diferencia entre los saltos de línea de Windows (CRLF) y Linux/Mac (LF).
SOLUCIÓN: Ejecuta en la terminal 'git config --global core.autocrlf true' para normalizar los saltos.""",
    }

    for nombre_archivo, contenido in errores.items():
        (carpeta_errores / nombre_archivo).write_text(
            contenido, encoding="utf-8"
        )

    print(
        f"📄 Guía y 8 archivos de error independientes creados en: {carpeta_opcion}"
    )


def crear_repositorio_local(nombre_repo):
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "crear_repo"
    generar_archivos_crear_repo(carpeta_opcion)

    try:
        os.makedirs(nombre_repo, exist_ok=True)
        subprocess.run(["git", "init"], cwd=nombre_repo, check=True)
        print(
            f"✓ Repositorio '{nombre_repo}' creado e inicializado correctamente."
        )
    except Exception as e:
        print(f"❌ Error al crear el repositorio: {e}")