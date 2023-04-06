from topsdk.client import TopApiClient, BaseRequest

class Ability3280:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-淘口令回流数据查询
    """
    def taobao_tbk_dg_tpwd_report_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
