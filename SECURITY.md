# Política de Seguridad de Matatucas LMS 🛡️

La seguridad y la integridad de los datos de nuestros estudiantes, docentes y administradores son una prioridad fundamental.

---

## 📌 Versiones con Soporte

| Versión | Soportada          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |
| < 1.0   | :x:                |

---

## 🚨 Reporte de Vulnerabilidades

Si descubres una vulnerabilidad de seguridad en esta plataforma, por favor **NO** abras un Issue público en GitHub. En su lugar, repórtala de manera confidencial y responsable:

1. **Contacto Privado**: Envía los detalles a los mantenedores del repositorio a través de GitHub Security Advisories o al correo institucional del administrador: `l23te0030@teziutlan.tecnm.mx`.
2. **Información requerida**:
   - Descripción detallada de la vulnerabilidad.
   - Pasos para reproducirla o código de prueba de concepto (PoC).
   - Componente afectado (autenticación, subida de archivos, API de ejercicios, etc.).
   - Impacto potencial estimado.

Nos comprometemos a:
- Acusar recibo de tu reporte en un plazo menor a 48 horas hábiles.
- Investigar y validar el problema reportado.
- Publicar una corrección en el menor tiempo posible antes de hacer pública la divulgación.

---

## 🔒 Mecanismos de Seguridad Implementados

El sistema cuenta con las siguientes capas defensivas de fábrica:

1. **Protección Anti-CSRF**: Integración de `Flask-WTF` con generación de tokens sincronizados y validación obligatoria en todas las peticiones con estado mutante.
2. **Control de Acceso Basado en Roles (RBAC)**: Decoradores estrictos que previenen escalamiento horizontal o vertical de privilegios (`@curso_owner_required`, `@docente_required`, `@admin_required`).
3. **Criptografía de Contraseñas**: Uso del algoritmo `scrypt` con salting automático para almacenar hashes seguros.
4. **Validación de Archivos (Upload Security)**:
   - Verificación estricta de listas blancas MIME (`image/jpeg`, `image/png`, `image/webp`).
   - Límite máximo de tamaño de carga a nivel de stream (5 MB).
   - Sanitización de identificadores y conversión a formato WebP seguro en Cloudinary.
5. **Auditoría de Eventos Sensibles**: Registro persistente de dirección IP, timestamp, tipo de evento y payload JSON ante cualquier acción administrativa de riesgo.
6. **Aislamiento de Cursos Privados**: Cursos en estado borrador o con visibilidad privada no son indexados ni accesibles por estudiantes sin código de acceso criptográficamente aleatorio (`secrets`).
