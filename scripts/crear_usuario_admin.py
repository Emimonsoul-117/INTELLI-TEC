import os
import sys

# Permitir ejecutar el script directamente desde cualquier directorio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import crear_app, bd
from app.modelos import Usuario, Docente, asegurar_fila_docente_si_falta
from werkzeug.security import generate_password_hash

app = crear_app()

def crear_admin():
    with app.app_context():
        email = os.environ.get('ADMIN_EMAIL', 'admin@itst.edu.mx')
        password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        
        # Buscar si ya existe
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario:
            print(f"El usuario {email} ya existe. Actualizando contraseña y rol...")
            usuario.password_hash = generate_password_hash(password, method='scrypt')
            usuario.rol = 'administrador'
        else:
            print(f"Creando nuevo usuario administrador {email}...")
            usuario = Usuario(
                email=email,
                nombre='Administrador Sistema',
                password_hash=generate_password_hash(password, method='scrypt'),
                rol='administrador',
                numero_control='ADM001'
            )
            bd.session.add(usuario)
            bd.session.flush()

        asegurar_fila_docente_si_falta(usuario)
        
        try:
            bd.session.commit()
            print("¡Éxito! Usuario administrador configurado.")
            print(f"Email: {email}")
            print(f"Password: {password}")
        except Exception as e:
            bd.session.rollback()
            print(f"Error al guardar en base de datos: {e}")

if __name__ == '__main__':
    crear_admin()
