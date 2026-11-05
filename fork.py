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
GUÍA EXPLICATIVA: CÓMO HACER UN FORK Y CLONAR
===================================================

1. ¿QUÉ ES UN FORK?
   - Un 'Fork' es una copia independiente de un repositorio ajeno en tu propia cuenta de GitHub.
   - Permite trabajar y modificar el código sin alterar el proyecto original.

2. PASOS PARA HACER UN FORK Y CLONARLO:
   1. Ingresa en GitHub al repositorio original que deseas copiar.
   2. Presiona el botón 'Fork' (ubicado arriba a la derecha).
   3. Entra a tu perfil de GitHub y abre tu copia recién creada.
   4. Haz clic en el botón verde '<> Code' y copia la URL.
   5. En tu terminal ejecuta:
      git clone https://github.com/TU_USUARIO/NOMBRE_REPOSITORIO.git
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": (
            "ERROR 1: Repository not found (404).\nCAUSA: La URL ingresada es"
            " incorrecta o el repositorio es privado.\nSOLUCIÓN: Verifica la URL"
            " en GitHub o solicita acceso al propietario."
        ),
        "error_2.txt": (
            "ERROR 2: Destination path already exists.\nCAUSA: Ya existe una"
            " carpeta con el mismo nombre en la ruta actual.\nSOLUCIÓN: Borra"
            " la carpeta previa o cambia de ubicación."
        ),
        "error_3.txt": (
            "ERROR 3: Authentication failed.\nCAUSA: Credenciales de GitHub no"
            " válidas o desactualizadas.\nSOLUCIÓN: Genera un Personal Access"
            " Token (PAT) o configura SSH."
        ),
        "error_4.txt": (
            "ERROR 4: Connection timed out / Could not resolve host.\nCAUSA:"
            " Sin acceso a internet o bloqueo de red.\nSOLUCIÓN: Revisa tu"
            " conexión o desactiva la VPN."
        ),
        "error_5.txt": (
            "ERROR 5: SSL certificate problem.\nCAUSA: Incompatibilidad con"
            " el certificado SSL local.\nSOLUCIÓN: Ejecuta 'git config"
            " --global http.sslVerify false'."
        ),
        "error_6.txt": (
            "ERROR 6: Early EOF / index-pack failed.\nCAUSA: Desconexión al"
            " descargar un proyecto muy pesado.\nSOLUCIÓN: Clona con 'git clone"
            " --depth 1 <URL>'."
        ),
        "error_7.txt": (
            "ERROR 7: Filename too long.\nCAUSA: Windows limita la longitud"
            " de las rutas de archivos.\nSOLUCIÓN: Ejecuta 'git config --global"
            " core.longpaths true'."
        ),
        "error_8.txt": (
            "ERROR 8: Git LFS (Large File Storage) missing.\nCAUSA: El"
            " proyecto requiere soporte para archivos pesados.\nSOLUCIÓN:"
            " Instala Git LFS e inicialízalo con 'git lfs install'."
        ),
    }

    for nombre, contenido in errores.items():
        (carpeta_errores / nombre).write_text(contenido, encoding="utf-8")

    print(
        "📄 Carpeta 'fork' actualizada en:"
        f" {carpeta_opcion.relative_to(carpeta_opcion.parents[1])}"
    )


def clonar_o_forkear():
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "fork"
    generar_archivos_fork(carpeta_opcion)

    print("\n" + "=" * 55)
    print("      GUÍA EDUCATIVA: PROCESO PARA HACER UN FORK")
    print("=" * 55)
    print("1. Ve al repositorio original en GitHub.com")
    print("2. Presiona el botón 'Fork' (arriba a la derecha).")
    print("3. Copia la URL de la copia generada en tu perfil.")
    print("4. En terminal ejecuta: git clone <URL_DE_TU_FORK>")
    print("=" * 55)
    print("✓ Guía y 8 archivos de error generados en github_ayuda/fork.\n")