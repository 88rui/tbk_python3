from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgTpwdRiskReportRequest(BaseRequest):

    def __init__(
        self,
        pid: str = None,
        offset: int = None,
        limit: int = None
    ):
        """
            如有pid，则查询pid下的relationid名单；如没有pid，则查询appkey关联userid下的pid名单
        """
        self._pid = pid
        """
            分页参数
        """
        self._offset = offset
        """
            分页参数，一次最多不能超过1000
        """
        self._limit = limit

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, pid):
        if isinstance(pid, str):
            self._pid = pid
        else:
            raise TypeError("pid must be str")

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        if isinstance(offset, int):
            self._offset = offset
        else:
            raise TypeError("offset must be int")

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        if isinstance(limit, int):
            self._limit = limit
        else:
            raise TypeError("limit must be int")


    def get_api_name(self):
        return "taobao.tbk.dg.tpwd.risk.report"

    def to_dict(self):
        request_dict = {}
        if self._pid is not None:
            request_dict["pid"] = convert_basic(self._pid)

        if self._offset is not None:
            request_dict["offset"] = convert_basic(self._offset)

        if self._limit is not None:
            request_dict["limit"] = convert_basic(self._limit)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

