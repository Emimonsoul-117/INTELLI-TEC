"""
Servicio de Cloudinary para gestión de imágenes de portada.
Soporta subida de portadas de cursos y lecciones.
"""
import os
import cloudinary
import cloudinary.uploader
from flask import current_app

# Tipos MIME permitidos
TIPOS_PERMITIDOS = {'image/jpeg', 'image/png', 'image/webp', 'image/gif'}
MAX_BYTES = 5 * 1024 * 1024  # 5 MB


def _configurar_cloudinary():
    """Configura Cloudinary con las credenciales del entorno."""
    c_url = (current_app.config.get('CLOUDINARY_URL') if current_app else None) or os.environ.get('CLOUDINARY_URL')
    if c_url:
        cloudinary.config(cloudinary_url=c_url, secure=True)
    else:
        cloud_name = (current_app.config.get('CLOUDINARY_CLOUD_NAME') if current_app else None) or os.environ.get('CLOUDINARY_CLOUD_NAME')
        api_key = (current_app.config.get('CLOUDINARY_API_KEY') if current_app else None) or os.environ.get('CLOUDINARY_API_KEY')
        api_secret = (current_app.config.get('CLOUDINARY_API_SECRET') if current_app else None) or os.environ.get('CLOUDINARY_API_SECRET')
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True,
        )


def subir_imagen_portada(archivo, carpeta='portadas', public_id_prefix='img'):
    """
    Sube un archivo de imagen a Cloudinary.

    Args:
        archivo: Objeto FileStorage de Flask (request.files['imagen_portada']).
        carpeta: Subcarpeta en Cloudinary (ej: 'portadas/cursos' o 'portadas/lecciones').
        public_id_prefix: Prefijo para el nombre del archivo en Cloudinary.

    Returns:
        str: URL segura de la imagen subida, o None si hubo error o no se proporcionó archivo.

    Raises:
        ValueError: Si el tipo de archivo o tamaño no son válidos.
    """
    if not archivo or archivo.filename == '':
        return None

    # Validar tipo MIME
    mime = archivo.content_type or ''
    if mime not in TIPOS_PERMITIDOS:
        raise ValueError(
            f'Tipo de archivo no permitido: {mime}. '
            'Usa JPG, PNG, WEBP o GIF.'
        )

    # Validar tamaño (leer stream y volver al inicio)
    archivo.stream.seek(0, 2)
    size = archivo.stream.tell()
    archivo.stream.seek(0)
    if size > MAX_BYTES:
        raise ValueError('La imagen no puede superar 5 MB.')

    _configurar_cloudinary()

    resultado = cloudinary.uploader.upload(
        archivo.stream,
        folder=f'matatucas/{carpeta}',
        resource_type='image',
        format='webp',          # Convierte a WebP automáticamente (más ligero)
        quality='auto:good',    # Optimización automática de calidad
        width=1280,             # Máximo ancho
        crop='limit',           # No escala hacia arriba
        overwrite=True,
    )
    return resultado.get('secure_url')


def eliminar_imagen(url_cloudinary):
    """
    Elimina una imagen de Cloudinary dado su URL.
    Útil al reemplazar la portada de un curso/lección.

    Args:
        url_cloudinary: URL completa de Cloudinary a eliminar.
    """
    if not url_cloudinary:
        return
    try:
        _configurar_cloudinary()
        # Extraer el public_id del URL
        # Ejemplo URL: https://res.cloudinary.com/demo/image/upload/v123/matatucas/portadas/img.webp
        partes = url_cloudinary.split('/upload/')
        if len(partes) == 2:
            public_id_con_ext = partes[1]
            # Quitar versión si existe (v123/)
            if public_id_con_ext.startswith('v'):
                public_id_con_ext = '/'.join(public_id_con_ext.split('/')[1:])
            # Quitar extensión
            public_id = public_id_con_ext.rsplit('.', 1)[0]
            cloudinary.uploader.destroy(public_id)
    except Exception:
        pass  # No bloquear el flujo si falla la eliminación
