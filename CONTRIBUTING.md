# Normativa de Desarrollo y Mantenimiento Privado: INTELLI-TEC LMS

Este proyecto es propiedad intelectual exclusiva del **Instituto Tecnológico Superior de Teziutlán (ITST)**. Al ser una plataforma institucional de uso y desarrollo estrictamente privado, **no se admiten contribuciones, bifurcaciones (forks) ni pull requests de personas externas a la institución**.

---

## 1. Alcance Institucional

El desarrollo, mantenimiento correctivo y evolutivo de **INTELLI-TEC** está reservado exclusivamente para:
- Personal docente e investigadores autorizados por la Dirección del Instituto Tecnológico Superior de Teziutlán.
- Alumnos residentes o prestadores de servicio social debidamente acreditados bajo convenios institucionales de confidencialidad y cesión de derechos.
- Administradores de sistemas y tecnologías de la información del ITST.

---

## 2. Flujo de Trabajo para Desarrolladores Autorizados

1. **Ramas de Trabajo**:
   - Todo desarrollo o corrección interna debe efectuarse en ramas designadas por el equipo institucional (`feature/nombre-modulo` o `fix/descripcion-incidencia`).
   - La rama principal (`master`) está protegida y únicamente el personal autorizado puede realizar despliegues a entornos de producción.
2. **Entorno de Pruebas**:
   - Utilizar el archivo de plantilla `.env.example` para levantar instancias locales de desarrollo.
   - Prohibido utilizar credenciales de bases de datos de producción o claves API institucionales en entornos personales no autorizados.
3. **Verificación de Sintaxis y Pruebas**:
   - Todo cambio debe compilar y ejecutarse sin errores antes de su integración:
   ```bash
   python -m py_compile $(find app/ -name "*.py")
   ```

---

## 3. Estándares Técnicos y de Seguridad

- **Protección de Datos Personales**: Conforme a la legislación de protección de datos personales en posesión de sujetos obligados, ninguna información de estudiantes (nombres, matrículas, correos institucionales, calificaciones) debe exponerse en código, logs o repositorios.
- **Consultas Parametrizadas**: Emplear siempre el ORM SQLAlchemy para interactuar con la base de datos y evitar cualquier concatenación directa de cadenas en SQL.
- **Control de Acceso (RBAC)**: Todo endpoint institucional debe validar obligatoriamente la sesión (`@login_required`) y el rol asignado (`@admin_required`, `@docente_required`, `@curso_owner_required`).
- **Seguridad en Formularios y APIs**: Incluir siempre el token CSRF (`csrf_token()`) en formularios POST y la cabecera `X-CSRFToken` en peticiones asíncronas (fetch/AJAX).

---

## 4. Confidencialidad y Propiedad Intelectual

Cualquier aportación, módulo o mejora desarrollada dentro del marco del proyecto pertenecerá en su totalidad al **Instituto Tecnológico Superior de Teziutlán**, conforme a los estatutos institucionales y a la Ley Federal de Protección a la Propiedad Industrial.
