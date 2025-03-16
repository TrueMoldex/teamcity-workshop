import time

import pytest

from pytest_httpserver import HTTPServer

@pytest.fixture(scope="function")
def httpserver():
    server = HTTPServer(host="localhost", port=8090)
    server.start()
    yield server
    server.clear()
    server.stop()

@pytest.fixture(autouse=True)
def setup_httpserver(httpserver):
    """Запускает мок-сервер и добавляет мок-ответ."""
    fake_build = {"state": "finished", "status": "SUCCESS"}
    httpserver.expect_request("/app/rest/buildQueue", method="POST").respond_with_json(fake_build, status=200)
    print(f"🚀 Мок-сервер стартует на {httpserver.host}:{httpserver.port}")
    yield
    print("🛑 Остановка мок-сервера")