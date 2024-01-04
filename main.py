#pip install hypercorn #파이썬 기반 ASGI서버(파이썬 3.6이상부터 지원)
#pip install asgiref  #플라스크 앱을 Wsgi로 변환용
#pip install uvicorn  #파이썬 기반 ASGI서버(파이썬 3.7이상부터 지원)
from app import app #플라스크 어플리케이션
from asgiref.wsgi import WsgiToAsgi
import uvicorn


asgi_app = WsgiToAsgi(app)#플라스크 앱을 ASGI와 호환되는 WSGI 앱으로 변환

if __name__ == '__main__':
    uvicorn.run(asgi_app,host='0.0.0.0',port=5001)
