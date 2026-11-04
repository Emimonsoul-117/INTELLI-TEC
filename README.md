# 🎓 Matatucas LMS — Plataforma Inteligente de Gestión Académica y Tutoría con IA

[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask%203.0-green.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/database-MySQL%20%7C%20TiDB%20%7C%20SQLite-orange.svg)](https://www.mysql.com/)
[![AI Powered](https://img.shields.io/badge/AI-Google%20Gemini-purple.svg)](https://aistudio.google.com/)
[![Authentication](https://img.shields.io/badge/auth-Microsoft%20Entra%20ID%20%26%20Local-0078D4.svg)](https://entra.microsoft.com/)
[![Security](https://img.shields.io/badge/CSRF%20%26%20RBAC-Protected-success.svg)](SECURITY.md)

**Matatucas** es un ecosistema integral de aprendizaje en línea (LMS) diseñado para instituciones educativas de nivel superior (orientado originalmente al sistema **TecNM / ITST**). Integra generación asistida de contenido y ejercicios con modelos de **Inteligencia Artificial (Google Gemini)**, analítica pedagógica en tiempo real, gamificación por cohortes (XP, rachas, avatares, tienda de recompensas) y auditoría inmutable de eventos.

---

## 📑 Tabla de Contenidos

- [Características Principales](#-características-principales)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación Paso a Paso (Cualquier Equipo)](#-instalación-paso-a-paso-cualquier-equipo)
- [Configuración de Variables de Entorno (.env)](#-configuración-de-variables-de-entorno-env)
- [Puesta en Marcha](#-puesta-en-marcha)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Roles y Permisos](#-roles-y-permisos)
- [Auditoría y Seguridad](#-auditoría-y-seguridad)
- [Despliegue en Producción](#-despliegue-en-producción)
- [Propiedad Intelectual y Patentes](#-propiedad-intelectual-y-patentes)
- [Licencia y Contribución](#-licencia-y-contribución)

---

## 🌟 Características Principales

### 1. 🤖 Generación y Tutoría con Inteligencia Artificial
- **Generador de Ejercicios Didácticos**: Crea ejercicios matemáticos con fórmulas renderizadas en LaTeX y múltiples formatos:
  - Opción múltiple
  - Verdadero o falso
  - Cálculo numérico
  - Completar espacios en blanco
  - Ordenar pasos de resolución
  - Respuesta corta con tolerancias
- **Generador de Teoría Estructurada**: Redacta unidades teóricas didácticas en HTML limpio con ejemplos paso a paso.
- **Tutor Virtual "MathBot"**: Chatbot conversacional enfocado en matemáticas que guía al alumno sin darle la respuesta directa.
- **Explicación Paso a Paso de Errores**: Si el estudiante falla un ejercicio, la IA analiza su respuesta y genera retroalimentación formativa personalizada.

### 2. 🎮 Sistema de Gamificación Integral (Fase 3)
- **Monedas Institucionales (Matacoins)** y puntos de experiencia (XP) otorgados por actividad continua.
- **Rachas de Estudio Diarias**: Cálculo automático de racha consecutiva por inicio de sesión y resolución de actividades.
- **Tienda de Recompensas**: Catálogo de cosméticos (avatares personalizados y marcos visuales por rareza: común, raro, épico, legendario).
- **Ranking y Leaderboard Dinámico**: Posicionamiento global y por cohortes con opción de privacidad.
- **Insignias y Logros Automatizados**: Desbloqueo programático por constancia, exploración y excelencia académica.

### 3. 👨‍🏫 Panel Docente y Analítica Pedagógica
- **Gestión Integral de Cursos**: Creación, edición, duplicación rápida, publicación directa y códigos de acceso privados (`MTC-XXXXXXXX`).
- **Editor Modular de Lecciones**: Soporte para bloques combinables de Teoría (HTML/LaTeX), Videos de YouTube con auto-completado y Baterías de Ejercicios interactivos con drag-and-drop.
- **Métricas de Desempeño**: Tasa de retención, tiempo promedio, análisis de ejercicios con mayor tasa de error y exportación de reportes a **Excel (.xlsx)** y **PDF oficial**.
- **Gestión de Alumnos**: Monitoreo individual de avance, capacidad de bloqueo/desbloqueo de acceso y expulsión con limpieza de intentos.

### 4. 🛡️ Panel de Administración y Auditoría
- **Control de Acceso Basado en Roles (RBAC)**: Administradores, Docentes y Estudiantes estrictamente segregados con decoradores `@admin_required`, `@docente_required` y `@curso_owner_required`.
- **Registro Inmutable de Auditoría**: Captura de IP, timestamp, usuario y payload JSON de acciones críticas (eliminación de cursos, cambio de roles, publicación).
- **Certificados Oficiales PDF**: Generación en tiempo real con ReportLab tras alcanzar el 100% de progreso con validación de lecciones completadas.

---

## 🏗️ Arquitectura del Sistema

El proyecto sigue una arquitectura en capas basada en **Application Factory Pattern** y **Blueprints** de Flask:

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
  │ • ServicioGamificacion (XP, Matacoins, Logros, Rachas)    │
  │ • CloudinaryServicio (Optimización WebP & CDN)            │
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

## 💻 Requisitos Previos

- **Python**: Versión `3.10`, `3.11`, `3.12` o superior.
- **Gestor de paquetes**: `pip` y `venv`.
- **Base de Datos**: 
  - Para producción: MySQL 8.0+ o TiDB Cloud.
  - Para desarrollo rápido: MySQL (XAMPP/Laragon/Docker) o SQLite (cero configuración).
- **Git**: Para control de versiones y clonación.

---

## 🚀 Instalación Paso a Paso (Cualquier Equipo)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Emimonsoul-117/INTELLI-TEC.git
cd INTELLI-TEC/proyecto-matatucas
```

### 2. Crear y Activar un Entorno Virtual
En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows (CMD):
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

En Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instalar Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚙️ Configuración de Variables de Entorno (.env)

Copia la plantilla de configuración:
```bash
cp .env.example .env
```

Edita `.env` con un editor de texto:
```ini
# Configuración Flask
FLASK_CONFIG=desarrollo
FLASK_APP=run.py
SECRET_KEY=clave_secreta_super_segura_de_tu_eleccion

# Base de datos
# Opción A (MySQL XAMPP local por defecto):
DATABASE_URL=mysql+pymysql://root:@localhost/Matatucas-db

# Opción B (SQLite local cero-configuración):
# DATABASE_URL=sqlite:///matatucas.db

# Credenciales de Cloudinary (imágenes y portadas)
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret

# Google Gemini AI (Tutor y generador de contenidos)
GOOGLE_API_KEY=tu_google_gemini_api_key

# Microsoft SSO (Opcional para entornos locales, obligatorio para SSO ITST)
MICROSOFT_CLIENT_ID=
MICROSOFT_CLIENT_SECRET=
MICROSOFT_TENANT_ID=common
```

---

## 🗄️ Inicialización de Base de Datos y Datos Semilla

1. **Crear la base de datos** (Si usas MySQL):
   Abre phpMyAdmin o tu cliente MySQL y crea la base:
   ```sql
   CREATE DATABASE IF NOT EXISTS `Matatucas-db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. **Crear el usuario Administrador Inicial**:
   ```bash
   python scripts/crear_usuario_admin.py
   ```
   *Credenciales por defecto:*
   - **Correo**: `admin@mathai.com`
   - **Contraseña**: `admin123`

3. **Poblar Insignias y Catálogo de la Tienda (Semillas)**:
   ```bash
   python scripts/sembrar_insignias.py
   python scripts/sembrar_tienda.py
   ```

---

## ▶️ Puesta en Marcha

Inicia el servidor de desarrollo:
```bash
python run.py
```
Abre tu navegador en: **`http://localhost:5000`** (o `https://localhost:5000` si habilitas `FLASK_USE_SSL=true`).

Inicia sesión con:
- **Opción 1**: Botón **Microsoft 365** (si tienes cuenta institucional `@teziutlan.tecnm.mx` y Azure AD configurado).
- **Opción 2**: Formulario local con correo `admin@mathai.com` y contraseña `admin123` (ideal para cualquier equipo de desarrollo).

---

## 📁 Estructura del Proyecto

```
proyecto-matatucas/
├── app/
│   ├── __init__.py               # Factory de la aplicación, CSRF, login manager y extensiones
│   ├── config.py                 # Clases de configuración (Desarrollo / Producción)
│   ├── modelos.py                # Modelos ORM (Usuario, Estudiante, Docente, Curso, etc.)
│   ├── decoradores.py            # Guardias RBAC (@admin_required, @docente_required, etc.)
│   ├── admin/                    # Rutas y vistas de administración del sistema
│   ├── auth/                     # Autenticación Dual (Microsoft OAuth 2.0 + Contraseña Local)
│   ├── cursos/                   # Gestión didáctica, lecciones, ejercicios y APIs IA
│   ├── docente/                  # Dashboard y analítica docente
│   ├── main/                     # Home, perfil, tienda de cosméticos, rankings
│   ├── servicios/                # Servicios desacoplados (IA, Cloudinary, Excel, PDF, Auditoría)
│   ├── static/                   # Hojas de estilo CSS, variables y recursos visuales
│   └── templates/                # Plantillas Jinja2 organizadas por módulo
├── scripts/                      # Scripts de mantenimiento, migraciones y datos semilla
├── .env.example                  # Plantilla de variables de entorno documentada
├── .gitignore                    # Exclusiones de Git (seguridad y archivos temporales)
├── esquema.sql                   # Esquema DDL canónico para MySQL
├── esquema_tidb.sql              # Esquema DDL adaptado para TiDB Cloud Serverless
├── requirements.txt              # Especificación de dependencias de producción
├── run.py                        # Punto de entrada de la aplicación
├── CONTRIBUTING.md               # Guía de contribución para GitHub
├── SECURITY.md                   # Política de seguridad y reporte de vulnerabilidades
└── DOCUMENTO_TECNICO_PROPIEDAD_INTELECTUAL_IMPI_INDAUTOR.md # Memoria técnica para registro y patentes
```

---

## 🔒 Auditoría y Seguridad

- **Protección CSRF**: Toda petición destructiva (POST, PUT, DELETE) está blindada con `Flask-WTF` y `X-CSRFToken` inyectado en formularios y llamadas `fetch`.
- **Hasheo Criptográfico**: Almacenamiento de contraseñas locales con algoritmo moderno `scrypt` vía `werkzeug.security`.
- **Prevención de Inyecciones SQL**: Consultas parametrizadas a través del ORM SQLAlchemy.
- **Validación de Archivos Multimedia**: El servicio de portadas valida cabeceras MIME (`image/jpeg`, `image/png`, `image/webp`), limita el peso a 5 MB y convierte a formato WebP optimizado en Cloudinary.
- **Segregación de Roles**: Verificación en backend de permisos antes de cada acción sobre cursos o lecciones.

---

## 📜 Propiedad Intelectual y Patentes

Para fines de registro ante el **Instituto Mexicano de la Propiedad Industrial (IMPI)** y el **Instituto Nacional del Derecho de Autor (INDAUTOR)**, consulta el documento técnico integral:

👉 **[DOCUMENTO_TECNICO_PROPIEDAD_INTELECTUAL_IMPI_INDAUTOR.md](DOCUMENTO_TECNICO_PROPIEDAD_INTELECTUAL_IMPI_INDAUTOR.md)**

Dicho documento contiene:
1. Memoria técnica descriptiva completa de la arquitectura y algoritmos.
2. Análisis de patentabilidad de Invenciones Implementadas en Computadora (CII) bajo la Ley Federal de Protección a la Propiedad Industrial (LFPPI).
3. Pliego de reivindicaciones técnicas formales.
4. Guía para el Registro de Obra de Software ante INDAUTOR (Formato RPDA-01).
5. Registro de Marca "MATATUCAS" ante el IMPI (Clases 42 y 41 de Niza).

---

## 👥 Contribución

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para conocer las pautas de estilo de código, convenciones de Git y el proceso para proponer mejoras.

---

*Desarrollado con pasión para transformar la educación matemática e informática.*
