# Flask - Demo

Öğrencilere flask ile github actions üzerinden dokku sunucuya oto deploy konusunu anlatacağım. amacım ci/cd konusunu uygulamalı olarak öğretmek.

Basit bir Flask uygulaması örneği:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, NAME. Welcome to the CI/CD World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

Bu örnekte NAME'i ortam değişkeninden almalı.

Ardından aşağıdaki gibi bir test olmalı:

```python
def test_home():
    from app import app
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello, CI/CD World!"
```

python'u ve sanal ortamı uv isimli komut satırı aracıyla yöneteceğiz.

Gereken tüm komutları sanal ortamı oluşturduktan sonra çalıştır.
