from waitress import serve
import app

serve(app.app, host='10.182.52.170', port=2222, url_prefix='/scheduler')