from Modelo.estudiantes import RepositorioNotas


class GestorEstudiantes:
    def __init__(self):
        self.repo = RepositorioNotas()

    def agregar_estudiante(self, nombre, correo, nota):
        """

        Agrega un nuevo estudiante al repositorio.
        Verifica que el nombre y correo no estén vacíos y que la nota esté entre 0 y 5.

        Args:
            nombre (str): Nombre del estudiante.
            correo (str): Correo del estudiante.
            nota (float): Nota del estudiante.

        Returns:
            str: Mensaje de éxito o error.

        """

        if not nombre or not correo:
            return "Nombre y correo son obligatorios."
        try:
            nota = float(nota)
        except ValueError:
            return "La nota debe ser un número."
        if nota < 0 or nota > 5:
            return "La nota debe estar entre 0 y 5."
        self.repo.agregar_estudiante(nombre, correo, nota)
        return f"Estudiante '{nombre}' agregado correctamente."

    def listar_estudiantes(self):
        """

        Lista todos los estudiantes en el repositorio.

        Args:
            None

        Returns:
            list: Lista de tuplas con los datos de los estudiantes.

        """

        return self.repo.listar_estudiantes()


    def actualizar_nota(self, correo, nueva_nota):
        """
        
        Actualiza la nota de un estudiante en el repositorio.

        Args:
            correo (str): Correo del estudiante.
            nueva_nota (float): Nueva nota del estudiante.

        Returns:
            str: Mensaje de éxito o error.

        """

        try:
            nueva_nota = float(nueva_nota)
        except ValueError:
            return "La nota debe ser numérica."
        if nueva_nota < 0 or nueva_nota > 5:
            return "La nota debe estar entre 0 y 5."
        self.repo.actualizar_nota(correo, nueva_nota)
        return f"Nota actualizada para {correo}"

    def eliminar_estudiante(self, correo):
        """

        Elimina un estudiante del repositorio.
        Args:
            correo (str): Correo del estudiante a eliminar.
        Returns:
            str: Mensaje de éxito o error.

        """

        self.repo.eliminar_estudiante(correo)
        return f"Estudiante con correo {correo} eliminado."

    def buscar_por_nombre(self, patron):
        """

        Busca estudiantes por nombre en el repositorio.
        Args:
            patron (str): Patrón a buscar en los nombres de los estudiantes.
        Returns:
            list: Lista de tuplas con los datos de los estudiantes que coinciden.

        """

        query = f"%{patron}%"
        self.repo.cursor.execute("SELECT * FROM notas WHERE nombre LIKE ?", (query,))
        resultados = self.repo.cursor.fetchall()
        return resultados if resultados else "No se encontraron coincidencias."

    def eliminar_notas_bajas(self):
        """

        Elimina estudiantes con nota inferior a 3.0.

        Args:
            None

        Returns:
            str: Mensaje de éxito.

        """

        self.repo.cursor.execute("DELETE FROM notas WHERE nota < 3.0")
        self.repo.conexion.commit()
        return "Se eliminaron estudiantes con nota inferior a 3.0."

    def cerrar_conexion(self):
        """

        Cierra la conexión con la base de datos.

        Args:
            None

        Returns:
            None

        """

        self.repo.cerrar()

    def listar_por_nota_desc(self):
        estudiantes = self.repo.listar_por_nota_desc()
        return estudiantes if estudiantes else "No hay estudiantes registrados."
