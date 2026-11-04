# INTELLI-TEC LMS — Plataforma de Gestión Académica y Tutoría con Inteligencia Artificial

[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask%203.0-green.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/database-MySQL%20%7C%20TiDB%20%7C%20SQLite-orange.svg)](https://www.mysql.com/)
[![AI Powered](https://img.shields.io/badge/AI-Google%20Gemini-purple.svg)](https://aistudio.google.com/)
[![Authentication](https://img.shields.io/badge/auth-Microsoft%20Entra%20ID%20%26%20Local-0078D4.svg)](https://entra.microsoft.com/)
[![Access](https://img.shields.io/badge/access-Proprietary%20%7C%20ITST-red.svg)](LICENSE)

**INTELLI-TEC** es un ecosistema integral de aprendizaje en línea (LMS) desarrollado como proyecto tecnológico institucional para el **Instituto Tecnológico Superior de Teziutlán (ITST / TecNM)**, quien es el titular y propietario del sistema. La plataforma integra modelos generativos de **Inteligencia Artificial (Google Gemini)** para la creación y evaluación adaptativa de contenidos, analítica pedagógica en tiempo real, gamificación orientada al aprendizaje (puntos de experiencia, rachas consecutivas, catálogo de incentivos) y registro inmutable de auditoría institucional.

---

## Tabla de Contenidos

- [Propiedad y Titularidad Institucional](#propiedad-y-titularidad-institucional)
- [Funcionalidades Principales](#funcionalidades-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Instalación en Nuevos Equipos](#instalación-en-nuevos-equipos)
- [Configuración de Entorno (.env)](#configuración-de-entorno-env)
- [Inicialización de Base de Datos y Datos Semilla](#inicialización-de-base-de-datos-y-datos-semilla)
- [Puesta en Marcha](#puesta-en-marcha)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Auditoría y Seguridad](#auditoría-y-seguridad)
- [Propiedad Intelectual y Patentes](#propiedad-intelectual-y-patentes)

---

## Propiedad y Titularidad Institucional

Este software, su arquitectura, código fuente, modelos de datos y documentación asociada son propiedad exclusiva del **Instituto Tecnológico Superior de Teziutlán**. 

El repositorio y sus recursos tienen carácter estrictamente privado e institucional. No está permitida su distribución comercial externa ni se admiten colaboraciones públicas ajenas al personal y estudiantes formalmente autorizados por el ITST.

---

## Funcionalidades Principales

### 1. Tutoría y Generación Asistida con Inteligencia Artificial
- **Generador de Reactivos Didácticos**: Construcción algorítmica de reactivos con renderizado matemático en LaTeX/KaTeX bajo seis modalidades:
  - Opción múltiple
  - Verdadero o falso
  - Cálculo numérico con tolerancia diferencial
  - Completar texto con delimitadores
  - Ordenamiento lógico de procedimientos paso a paso
  - Respuesta corta con tolerancias sintácticas
- **Generador de Unidades Teóricas**: Redacción estructurada de contenido conceptual en HTML validado.
- **Tutor Virtual "MathBot"**: Asistente pedagógico conversacional para resolución guiada de problemas sin provisión directa de respuestas.
- **Explicación Causal de Errores**: Descomposición pedagógica de fallos cometidos por el alumno, asistida por modelos LLM.

### 2. Gamificación Académica Reactiva
- **Sistema de Puntos (XP) y Moneda Institucional**: Estímulo al esfuerzo y regularidad académica.
- **Cálculo de Racha Diaria**: Algoritmo por ventana temporal de calendario real para incentivar el estudio continuo.
- **Tienda de Incentivos Visuales**: Personalización mediante avatares y marcos clasificados por nivel de rareza.
- **Tableros de Posición (Leaderboard)**: Métricas comparativas de avance con respeto a preferencias de privacidad del estudiante.
- **Insignias Institucionales**: Adquisición programática de reconocimientos por constancia y dominio conceptual.

### 3. Gestión y Analítica Docente
- **Administración de Cursos**: Creación, edición, duplicación ágil y publicación de contenidos, con generación de códigos de acceso alfanuméricos (`MTC-XXXXXXXX`).
- **Editor Modular de Lecciones**: Ensamblaje modular de teoría, videos externos con sincronización de estado y ejercicios interactivos.
- **Supervisión de Alumnos**: Monitoreo de progreso individual, control de acceso (bloqueo/desbloqueo) y remoción segura de inscripciones.
- **Generación de Reportes Formales**: Exportación de listas y calificaciones a formato Excel (.xlsx) y generación de reportes docentes en PDF.

### 4. Módulo de Administración y Auditoría
- **Control de Acceso Basado en Roles (RBAC)**: Separación jerárquica estricta de perfiles (Administrador, Docente, Estudiante).
- **Trazabilidad Inmutable**: Registro de dirección IP, sello temporal, usuario y payload estructurado en JSON de eventos de modificación crítica.
- **Emisión de Certificados de Acreditación**: Generación automatizada de diplomas en formato PDF con ReportLab al validar el 100% de lecciones concluidas.

---

## Arquitectura del Sistema

El sistema implementa el patrón de factoría de aplicaciones con modularización por Blueprints sobre Flask y SQLAlchemy:

```
[ Cliente Web (HTML5 / Bootstrap 5 / KaTeX / Fetch API) ]
                     │  (HTTPS / CSRF Token)
                     ▼
           [ Capa de Enrutamiento ]
  ┌──────────────┬──────────────┬──────────────┬──────────────┐
  │  auth (SSO)  │ cursos (LMS) │ docente (BI) │  admin (Ops) │
  └──────────────┴──────────────┴──────────────┴──────────────┘
                     │
      [ Capa de Servicios / Negocio ]
  ┌───────────────────────────────────────────────────────────┐
  │ • ServicioIA (Gemini Flash API & Prompt Orchestrator)    │
  │ • ServicioGamificacion (XP, Monedas, Logros, Rachas)      │
  │ • CloudinaryServicio (Optimización WebP & Almacenamiento) │
  │ • ExcelServicio (OpenPyXL) / ReportesServicio (ReportLab) │
  │ • AuditoriaServicio (Registro inmutable JSON)             │
  └───────────────────────────────────────────────────────────┘
                     │
         [ Capa de Datos (SQLAlchemy ORM) ]
  ┌───────────────────────────────────────────────────────────┐
  │ MySQL 8.0+ / TiDB Cloud Serverless / SQLite               │
  └───────────────────────────────────────────────────────────┘
```

---

## Requisitos Técnicos

- **Intérprete Python**: Versión 3.10, 3.11, 3.12 o 3.14.
- **Gestión de Entornos**: Herramientas nativas `pip` y `venv`.
- **Motor de Base de Datos**:
  - Entorno de producción / institucional: MySQL 8.0+ o TiDB Cloud.
  - Entorno local / portátil: MySQL o SQLite (cero configuración externa).
- **Herramienta Git**: Para sincronización con el repositorio privado.

---

## Instalación en Nuevos Equipos

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Emimonsoul-117/INTELLI-TEC.git
cd INTELLI-TEC
```

### 2. Creación y Activación del Entorno Virtual
En sistemas Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

En sistemas Windows (Símbolo del sistema):
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

En sistemas Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instalación de Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Configuración de Entorno (.env)

Genere su archivo local a partir de la plantilla:
```bash
cp .env.example .env
```

Parámetros fundamentales en `.env`:
```ini
FLASK_CONFIG=desarrollo
FLASK_APP=run.py
SECRET_KEY=clave_secreta_institucional_segura

# Conexión a Base de Datos
# MySQL local:
DATABASE_URL=mysql+pymysql://root:@localhost/intelli_tec_db
# O SQLite para pruebas rápidas:
# DATABASE_URL=sqlite:///intelli_tec.db

# Almacenamiento de Portadas e Imágenes (Cloudinary)
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret

# Motor de Inteligencia Artificial (Google Gemini)
GOOGLE_API_KEY=tu_google_gemini_api_key

# Autenticación Institucional Microsoft 365 / Entra ID
MICROSOFT_CLIENT_ID=
MICROSOFT_CLIENT_SECRET=
MICROSOFT_TENANT_ID=common
```

---

## Inicialización de Base de Datos y Datos Semilla

1. **Creación de la base de datos** (en entornos MySQL):
   ```sql
   CREATE DATABASE IF NOT EXISTS `intelli_tec_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. **Creación del Usuario Administrador Inicial**:
   ```bash
   python scripts/crear_usuario_admin.py
   ```
   *Valores predeterminados:*
   - **Correo institucional**: `admin@mathai.com`
   - **Contraseña inicial**: `admin123`

3. **Carga de Catálogos Semilla (Insignias e Incentivos)**:
   ```bash
   python scripts/sembrar_insignias.py
   python scripts/sembrar_tienda.py
   ```

---

## Puesta en Marcha

Inicie el servidor de aplicación:
```bash
python run.py
```

Acceda desde el navegador a: `http://localhost:5000`

Mecanismos de autenticación disponibles:
1. **Acceso Institucional Microsoft 365**: Para docentes y alumnos con cuenta `@teziutlan.tecnm.mx`.
2. **Acceso con Credenciales Locales**: Para el personal de administración técnica o desarrollo local sin conexión Azure AD.

---

## Estructura del Proyecto

```
INTELLI-TEC/
├── app/
│   ├── __init__.py               # Factoría de la aplicación y extensiones
│   ├── config.py                 # Entornos de configuración
│   ├── modelos.py                # Definición de entidades ORM
│   ├── decoradores.py            # Guardas de seguridad RBAC
│   ├── admin/                    # Módulo de administración
│   ├── auth/                     # Autenticación (Microsoft SSO y Local)
│   ├── cursos/                   # Gestión didáctica y APIs de IA
│   ├── docente/                  # Métricas e informes docentes
│   ├── main/                     # Vistas principales y tienda institucional
│   ├── servicios/                # Lógica de negocio desacoplada
│   ├── static/                   # Hojas de estilo y activos visuales
│   └── templates/                # Vistas en plantillas Jinja2
├── scripts/                      # Procedimientos de mantenimiento e inicialización
├── .env.example                  # Plantilla documentada de variables de entorno
├── .gitignore                    # Reglas de exclusión para control de versiones
├── esquema.sql                   # Definición DDL para bases de datos MySQL
├── esquema_tidb.sql              # Definición DDL optimizada para TiDB Cloud
├── requirements.txt              # Requerimientos de dependencias del proyecto
├── run.py                        # Script de ejecución del servidor
├── CONTRIBUTING.md               # Normativa interna de desarrollo privado
├── SECURITY.md                   # Protocolo interno de seguridad técnica
└── DOCUMENTO_TECNICO_PROPIEDAD_INTELECTUAL_IMPI_INDAUTOR.md # Memoria técnica y patentes
```

---

## Auditoría y Seguridad

- **Blindaje Anti-CSRF**: Validación obligatoria de tokens en solicitudes mutantes.
- **Algoritmo Criptográfico Seguro**: Empleo de `scrypt` para resguardo de contraseñas.
- **Sanitización de Subidas**: Comprobación de cabeceras MIME y compresión a WebP.
- **Trazabilidad Forense**: Almacenamiento estructurado de registros de auditoría en base de datos.

---

## Propiedad Intelectual y Patentes

Para fines del registro de obra de software ante el **Instituto Nacional del Derecho de Autor (INDAUTOR)** y la tramitación de patente de invención implementada en computadora (CII) y marca registrada ante el **Instituto Mexicano de la Propiedad Industrial (IMPI)** a nombre del Instituto Tecnológico Superior de Teziutlán, consulte el documento técnico:

- **[DOCUMENTO_TECNICO_PROPIEDAD_INTELECTUAL_IMPI_INDAUTOR.md](DOCUMENTO_TECNICO_PROPIEDAD_INTELECTUAL_IMPI_INDAUTOR.md)**
