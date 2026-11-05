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
GUÍA DE USO: CREAR Y CONECTAR REPOSITORIO
===================================================

1. ¿QUÉ HACE ESTA OPCIÓN?
   - Muestra la secuencia para inicializar un repositorio local.
   - Vincula el repositorio local con tu repositorio remoto en GitHub.

2. PASOS MANUALES EN TERMINAL:
   echo "# t" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git branch -M main
   git remote add origin https://github.com/aiglesias-lgtm/t.git
   git push -u origin main
"""
    carpeta_opcion.mkdir(parents=True, exist_ok=True)
    (carpeta_opcion / "guia.txt").write_text(guia, encoding="utf-8")

    carpeta_errores = carpeta_opcion / "errores"
    carpeta_errores.mkdir(parents=True, exist_ok=True)

    errores = {
        "error_1.txt": (
            "ERROR 1: 'git' no se reconoce como un comando.\nCAUSA: Git no está"
            " instalado o no se agregó al PATH.\nSOLUCIÓN: Descarga e instala"
            " Git desde https://git-scm.com/"
        ),
        "error_2.txt": (
            "ERROR 2: Permission denied.\nCAUSA: Falta de permisos en la"
            " carpeta.\nSOLUCIÓN: Ejecuta la terminal como Administrador."
        ),
        "error_3.txt": (
            "ERROR 3: remote origin already exists.\nCAUSA: Ya existe un"
            " remoto configurado.\nSOLUCIÓN: Ejecuta 'git remote remove origin'"
            " antes de vincular."
        ),
        "error_4.txt": (
            "ERROR 4: Sin espacio libre en disco.\nCAUSA: Unidad de"
            " almacenamiento llena.\nSOLUCIÓN: Libera espacio en el disco."
        ),
        "error_5.txt": (
            "ERROR 5: Repositorio corrupto.\nCAUSA: Error interno en"
            " '.git'.\nSOLUCIÓN: Elimina la carpeta oculta '.git' y ejecuta"
            " 'git init'."
        ),
        "error_6.txt": (
            "ERROR 6: Repository not found (404).\nCAUSA: La URL remota es"
            " errónea o no existe.\nSOLUCIÓN: Revisa la URL de tu repositorio"
            " en GitHub."
        ),
        "error_7.txt": (
            "ERROR 7: Authentication failed.\nCAUSA: Credenciales"
            " rechazadas.\nSOLUCIÓN: Inicia sesión en GitHub o usa un Personal"
            " Access Token."
        ),
        "error_8.txt": (
            "ERROR 8: LF sustituido por CRLF.\nCAUSA: Incompatibilidad de"
            " saltos de línea.\nSOLUCIÓN: Ejecuta 'git config --global"
            " core.autocrlf true'."
        ),
    }

    for nombre, contenido in errores.items():
        (carpeta_errores / nombre).write_text(contenido, encoding="utf-8")

    print(
        "📄 Carpeta 'crear_repo' actualizada en:"
        f" {carpeta_opcion.relative_to(carpeta_opcion.parents[1])}"
    )


def crear_repositorio_local():
    escritorio = obtener_ruta_escritorio()
    carpeta_opcion = escritorio / "github_ayuda" / "crear_repo"
    generar_archivos_crear_repo(carpeta_opcion)

    print("\n" + "=" * 55)
    print("      GUÍA EDUCATIVA: CREAR Y CONECTAR REPOSITORIO")
    print("=" * 55)
    print('1. echo "# t" >> README.md')
    print("2. git init")
    print("3. git add README.md")
    print('4. git commit -m "first commit"')
    print("5. git branch -M main")
    print("6. git remote add origin https://github.com/aiglesias-lgtm/t.git")
    print("7. git push -u origin main")
    print("=" * 55)
    print(
        "✓ Guía y 8 archivos de error generados en github_ayuda/crear_repo.\n"
    )