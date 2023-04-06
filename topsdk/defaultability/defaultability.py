from topsdk.client import TopApiClient, BaseRequest

class Defaultability:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        关键词过滤匹配
    """
    def taobao_kfc_keyword_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        淘宝客-推广者-淘口令预警及拦截查询
    """
    def taobao_tbk_dg_tpwd_risk_report(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
