from pytest_httpserver import HTTPServer
import json


class HttpMockServer:
    _server_instance = None

    def __init__(self, port=8081):
        if HttpMockServer._server_instance is None:
            self.httpserver = HTTPServer(host="localhost", port=port)
            self.httpserver.start()
            HttpMockServer._server_instance = self.httpserver
        else:
            self.httpserver = HttpMockServer._server_instance

    def setup_mock(self, endpoint, method="GET", status=200, model=None):
        response_body = json.dumps(model) if model else ""

        self.httpserver.expect_request(endpoint, method=method).respond_with_data(
            response_body, status=status, content_type="application/json"
        )

    def stop_server(self):
        if self.httpserver:
            self.httpserver.stop()
            HttpMockServer._server_instance = None
