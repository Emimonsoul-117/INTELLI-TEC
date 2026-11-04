from app import crear_app, bd
import os

app = crear_app(os.getenv('FLASK_CONFIG') or 'por_defecto')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    use_ssl = os.getenv('FLASK_USE_SSL', 'false').lower() in ('true', '1', 'yes')
    if use_ssl:
        app.run(host='0.0.0.0', port=port, ssl_context='adhoc')
    else:
        app.run(host='0.0.0.0', port=port)

@app.shell_context_processor
def make_shell_context():
    return {'bd': bd, 'app': app}
