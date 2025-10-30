import sqlite3
import os

class RepositorioNotas:
    """
    Clase que gestiona todas las operaciones con la base de datos SQLite.
    """

    def __init__(self):
        # Crear carpeta "notas" si no existe
        base_directory = os.path.dirname(os.path.abspath(__file__))
        carpeta = os.path.join(base_directory, "..", "notas")
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Ruta del archivo de base de datos
        self.db_path = os.path.join(carpeta, "notas.db")

        # Conexión a la base de datos
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

        # Crear tabla si no existe
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            nota REAL NOT NULL
        )
        ''')
        self.conexion.commit()

    def agregar_estudiante(self, nombre, correo, nota):
        """Agrega un estudiante a la base de datos."""
        try:
            self.cursor.execute(
                "INSERT INTO notas (nombre, correo, nota) VALUES (?, ?, ?)",
                (nombre, correo, nota)
            )
            self.conexion.commit()
        except sqlite3.IntegrityError:
            print(f"⚠️ El correo '{correo}' ya existe en la base de datos.")

    def listar_estudiantes(self):
        """Lista todos los estudiantes por orden de ID (ascendente)."""
        self.cursor.execute("SELECT * FROM notas ORDER BY id ASC")
        return self.cursor.fetchall()

    def actualizar_nota(self, correo, nueva_nota):
        """Actualiza la nota de un estudiante según su correo."""
        self.cursor.execute(
            "UPDATE notas SET nota = ? WHERE correo = ?",
            (nueva_nota, correo)
        )
        self.conexion.commit()

    def eliminar_estudiante(self, correo):
        """Elimina un estudiante usando su correo."""
        self.cursor.execute("DELETE FROM notas WHERE correo = ?", (correo,))
        self.conexion.commit()

    def cerrar(self):
        """Cierra la conexión a la base de datos."""
        self.conexion.close()

    def listar_por_nota_desc(self):
        """
        Muestra todos los estudiantes ordenados de mayor a menor nota.
        SQL: SELECT * FROM notas ORDER BY nota DESC
        """
        self.cursor.execute("SELECT * FROM notas ORDER BY nota DESC")
        return self.cursor.fetchall()

    def buscar_por_nombre(self, patron):
        """
        Busca estudiantes cuyo nombre contenga el patrón dado.
        SQL: SELECT * FROM notas WHERE nombre LIKE ?
        """
        self.cursor.execute("SELECT * FROM notas WHERE nombre LIKE ?", (f"%{patron}%",))
        return self.cursor.fetchall()
