from app import app #플라스크 어플리케이션
from asgiref.wsgi import WsgiToAsgi
import uvicorn


asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    uvicorn.run(asgi_app,host='0.0.0.0',port=5001)