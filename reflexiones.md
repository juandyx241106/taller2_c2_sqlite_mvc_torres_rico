# Reflexión sobre la implementación del patrón MVC

### 1. ¿Qué ventajas encontraste al aplicar el patrón MVC en tu proyecto?
Aplicar el patrón MVC facilitó la **organización del código** y la **separación de responsabilidades**. El modelo manejó toda la lógica de base de datos, el controlador la lógica de negocio y la vista la interfaz con el usuario. Esto permitió mantener el código más limpio, reutilizable y fácil de depurar.

### 2. ¿Qué dificultades surgieron al separar las responsabilidades entre modelo, vista y controlador?
Al inicio fue **difícil decidir qué parte del código pertenecía a cada capa**. Por ejemplo, algunas validaciones podían hacerse tanto en el controlador como en la vista. Además, la comunicación entre clases exigió definir métodos y parámetros con claridad para evitar dependencias innecesarias.

### 3. ¿Qué aprendiste sobre la ejecución de sentencias SQL y su relación con la estructura del código?
Aprendí que las **sentencias SQL deben estar encapsuladas dentro del modelo**, evitando mezclar consultas en la vista o el controlador. Esto mejora la seguridad, permite modificar la base de datos sin alterar el resto del programa y da una mejor visión de cómo los datos fluyen a través del sistema.

### 4. ¿Qué mejorarías si tuvieras que ampliar el sistema?
Si tuviera que ampliarlo, implementaría **validaciones más robustas**, un **manejo de errores más completo** (por ejemplo, usando excepciones personalizadas) y una **interfaz gráfica más intuitiva**. También integraría pruebas automáticas y un sistema de autenticación de usuarios.

---

**Autor:** Juan David Torres Rico  
**Repositorio:** [taller2_c2_sqlite_mvc_torres_rico](https://github.com/juandyx241106/taller2_c2_sqlite_mvc_torres_rico)
