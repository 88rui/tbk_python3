from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgTpwdReportGetRequest(BaseRequest):

    def __init__(
        self,
        tao_password: str = None,
        adzone_id: str = None
    ):
        """
            待查询的口令
        """
        self._tao_password = tao_password
        """
            mm_xxx_xxx_xxx的第3段数字
        """
        self._adzone_id = adzone_id

    @property
    def tao_password(self):
        return self._tao_password

    @tao_password.setter
    def tao_password(self, tao_password):
        if isinstance(tao_password, str):
            self._tao_password = tao_password
        else:
            raise TypeError("tao_password must be str")

    @property
    def adzone_id(self):
        return self._adzone_id

    @adzone_id.setter
    def adzone_id(self, adzone_id):
        if isinstance(adzone_id, str):
            self._adzone_id = adzone_id
        else:
            raise TypeError("adzone_id must be str")


    def get_api_name(self):
        return "taobao.tbk.dg.tpwd.report.get"

    def to_dict(self):
        request_dict = {}
        if self._tao_password is not None:
            request_dict["tao_password"] = convert_basic(self._tao_password)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

