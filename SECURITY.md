# Política de Seguridad: INTELLI-TEC LMS

La seguridad, confidencialidad e integridad de la información académica del **Instituto Tecnológico Superior de Teziutlán (ITST)** constituyen una prioridad absoluta.

---

## 1. Versiones con Soporte

| Versión | Estado de Soporte | Entorno Destino |
| ------- | ----------------- | --------------- |
| 1.x     | Soportada         | Producción ITST |
| < 1.0   | No soportada      | Obsoleta        |

---

## 2. Reporte Responsable de Incidentes y Vulnerabilidades

Al tratarse de una plataforma institucional privada, el canal para reportar incidentes de seguridad o vulnerabilidades técnicas es estrictamente interno:

1. **Canal Institucional Oficial**: Remitir un informe técnico detallado al correo del administrador del sistema: `l23te0030@teziutlan.tecnm.mx` o a la jefatura del departamento de cómputo y sistemas del ITST.
2. **Información Requerida**:
   - Descripción técnica de la vulnerabilidad o anomalía detectada.
   - Pasos para reproducir el escenario en entornos de prueba.
   - Componente involucrado (autenticación SSO, gestión de calificaciones, evaluación por IA, almacenamiento en la nube, etc.).
   - Evaluación del impacto potencial sobre la privacidad de estudiantes o docentes.

---

## 3. Capas de Seguridad Implementadas

1. **Protección Integral Anti-CSRF**: La totalidad de peticiones con estado mutante (POST, PUT, DELETE) requieren validación del token sincronizado provisto por Flask-WTF.
2. **Control de Acceso Basado en Roles (RBAC)**: Segregación técnica estricta entre estudiantes, docentes y administradores a través de decoradores en el backend (`@curso_owner_required`, `@docente_required`, `@admin_required`).
3. **Criptografía de Contraseñas Locales**: Implementación del estándar scrypt con salting individual mediante Werkzeug para almacenamiento irreversible de credenciales.
4. **Seguridad en Almacenamiento de Archivos**:
   - Inspección estricta de tipos MIME permitidos (`image/jpeg`, `image/png`, `image/webp`).
   - Límite de tamaño máximo por archivo (5 MB).
   - Conversión obligatoria a formato WebP optimizado en Cloudinary.
5. **Auditoría Inmutable de Eventos Críticos**: Registro persistente de dirección IP, identificador de usuario, timestamp y payload estructurado en JSON ante cambios de estado de cursos, modificaciones de rol o eliminaciones.
6. **Aislamiento de Cursos Privados**: Cursos en borrador o configurados como privados no son indexados en catálogos y exigen validación del código alfanumérico generado con entropía criptográfica segura (`secrets`).
