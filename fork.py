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


def generar_archivos_fork(carpeta_opcion):
    guia = """===================================================
GUÍA DE USO: CLONAR / FORKEAR
===================================================

1. ¿QUÉ HACE ESTA OPCIÓN?
   - Descarga una copia local exacta de un repositorio alojado en GitHub.

2. PASOS MANUALES EN TERMINAL:
   - git clone https://github.com/usuario/repositorio.git
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": """===================================================
ERROR 1: Repository not found (Error 404)
===================================================
CAUSA: La URL ingresada es incorrecta o el repositorio es privado.
SOLUCIÓN: Verifica la URL en GitHub o configura credenciales SSH/PAT.""",
        "error_2.txt": """===================================================
ERROR 2: Destination path already exists
===================================================
CAUSA: Ya existe una carpeta con el mismo nombre en la ruta actual.
SOLUCIÓN: Elimina o renombra la carpeta previa antes de clonar.""",
        "error_3.txt": """===================================================
ERROR 3: Authentication failed
===================================================
CAUSA: GitHub deshabilitó la autenticación por contraseña tradicional.
SOLUCIÓN: Genera un Personal Access Token (PAT) y úsalo en lugar de la contraseña.""",
        "error_4.txt": """===================================================
ERROR 4: Connection timed out / Could not resolve host
===================================================
CAUSA: Sin conexión a internet o la red bloquea la conexión a GitHub.
SOLUCIÓN: Revisa tu red o deshabilita temporalmente la VPN o proxy.""",
        "error_5.txt": """===================================================
ERROR 5: SSL certificate problem
===================================================
CAUSA: Certificado de seguridad no validado por el sistema de red.
SOLUCIÓN: Ejecuta 'git config --global http.sslVerify false' o actualiza certificados.""",
        "error_6.txt": """===================================================
ERROR 6: Early EOF / index-pack failed
===================================================
CAUSA: La conexión falló mientras se descargaba un repositorio muy pesado.
SOLUCIÓN: Clona con profundidad limitada ejecutando 'git clone --depth 1 <URL>'.""",
        "error_7.txt": """===================================================
ERROR 7: Filename too long / Ruta demasiado larga
===================================================
CAUSA: Windows limita las rutas a un máximo de 260 caracteres por defecto.
SOLUCIÓN: Habilita rutas largas en Git ejecutando 'git config --global core.longpaths true'.""",
        "error_8.txt": """===================================================
ERROR 8: Git LFS (Large File Storage) missing
===================================================
CAUSA: El repositorio usa punteros de archivos pesados y no tienes Git LFS instalado.
SOLUCIÓN: Descarga e instala Git LFS desde https://git-lfs.github.com/ y ejecuta 'git lfs install'.""",
    }

    for nombre_archivo, contenido in errores.items():
        (carpeta_errores / nombre_archivo).write_text(
            contenido, encoding="utf-8"
        )

    print(
        f"📄 Guía y 8 archivos de error independientes creados en: {carpeta_opcion}"
    )


def clonar_o_forkear(url_repositorio, destino="."):
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "fork"
    generar_archivos_fork(carpeta_opcion)

    try:
        subprocess.run(
            ["git", "clone", url_repositorio], cwd=destino, check=True
        )
        print(f"✓ Repositorio '{url_repositorio}' clonado correctamente.")
    except Exception as e:
        print(f"❌ Error al clonar el repositorio: {e}")