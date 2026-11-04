# Guía de Contribución a Matatucas LMS 🤝

¡Gracias por tu interés en contribuir a **Matatucas**! Este documento contiene los lineamientos y estándares técnicos necesarios para colaborar de manera ordenada y segura en este repositorio.

---

## 📋 Código de Conducta

Nos comprometemos a brindar un entorno inclusivo, respetuoso y profesional para todos los colaboradores, estudiantes y educadores.

---

## 🛠️ Flujo de Trabajo Recomendado

1. **Haz un Fork** del repositorio a tu cuenta personal de GitHub.
2. **Clona tu fork** localmente:
   ```bash
   git clone https://github.com/<tu-usuario>/INTELLI-TEC.git
   cd INTELLI-TEC/proyecto-matatucas
   ```
3. **Crea una rama descriptiva** para tu funcionalidad o corrección:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   # o para corrección de bugs:
   git checkout -b fix/correccion-bug
   ```
4. **Instala las dependencias y crea tu archivo `.env`**:
   ```bash
   cp .env.example .env
   pip install -r requirements.txt
   ```
5. **Realiza tus cambios** manteniendo los estándares de código.
6. **Ejecuta las pruebas de sintaxis**:
   ```bash
   python -m py_compile $(find app/ -name "*.py")
   ```
7. **Haz commit con mensajes claros y concisos** siguiendo el estándar de Commits Convencionales:
   ```bash
   git commit -m "feat(cursos): agregar exportación de notas en formato CSV"
   git commit -m "fix(auth): corregir validación de token CSRF en auto-completado"
   ```
8. **Envía tus cambios a tu repositorio remoto**:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
9. **Abre un Pull Request (PR)** hacia la rama principal (`master` o `main`) describiendo los cambios realizados, el problema que resuelven y capturas de pantalla si involucra cambios en la interfaz.

---

## 📐 Estándares de Código y Buenas Prácticas

### Backend (Python / Flask)
- Seguir las pautas de estilo **PEP 8** (nombres de variables en minúsculas con guiones bajos, clases en CamelCase, 4 espacios de indentación).
- **Protección de Datos y Secretos**: NUNCA commitear archivos `.env`, contraseñas en texto plano, claves API o tokens.
- **Consultas a la Base de Datos**: Utilizar siempre el ORM SQLAlchemy con consultas parametrizadas. Evitar concatenaciones de cadenas en sentencias SQL.
- **Control de Acceso**: Todo nuevo endpoint que modifique o acceda a recursos debe estar protegido con `@login_required` y los decoradores de rol correspondientes (`@docente_required`, `@admin_required`, `@curso_owner_required`).
- **Seguridad en Formularios y APIs**: Incluir siempre el token CSRF (`csrf_token()`) en formularios POST y la cabecera `X-CSRFToken` en peticiones AJAX/fetch.

### Frontend (HTML / CSS / JavaScript)
- Mantener la coherencia con el diseño Bootstrap 5 y la paleta de colores institucional (`#0B2545`, `#1B396A`, `#F97316`).
- Fórmulas matemáticas deben escribirse con sintaxis LaTeX estándar utilizando delimitadores `\( ... \)` para fórmulas en línea o `\[ ... \]` para fórmulas destacadas (renderizadas por KaTeX).
- Manejar adecuadamente estados de carga (spinners/loaders) y mensajes de retroalimentación claros (toasts o alertas flotantes).

---

## 🐛 Reporte de Errores (Bugs)

Si encuentras un bug, por favor abre un **Issue** en GitHub detallando:
1. Pasos exactos para reproducir el problema.
2. Comportamiento observado vs. comportamiento esperado.
3. Rol del usuario autenticado (estudiante, docente o administrador).
4. Navegador y sistema operativo utilizado.
5. Capturas de pantalla o logs de consola si aplica.

---

¡Agradecemos tu valiosa colaboración para hacer de Matatucas una mejor plataforma educativa!
