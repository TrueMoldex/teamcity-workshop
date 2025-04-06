from framework.com_example_teamcity_api.enum.endpoit import Endpoint


class Request:
    """
    Request - это класс, описывающий меняющиеся параметры запроса, такие как:
    спецификация, эндпоинт (relative URL, model)
    """

    def __init__(self, spec, endpoint: Endpoint):
        self.spec = spec  # Экземпляр Specification
        self.endpoint = endpoint  # f Относительный URL (или объект, если потребуется)
