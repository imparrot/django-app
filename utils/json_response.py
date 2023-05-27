from django.http.response import JsonResponse


class JsonResponse(JsonResponse):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"

    OK_CODE = 200
    FAIL_CODE = -1

    def __init__(self, code: int = 200, result: str = SUCCESS, data: dict = None, msg: str = "", **kwargs):
        json_dumps_params = {
            "ensure_ascii": False
        }
        rst_data = {
            "code": code,
            "result": result,
            "msg": msg,
            "data": data
        }
        super(JsonResponse, self).__init__(rst_data, json_dumps_params=json_dumps_params, **kwargs)
