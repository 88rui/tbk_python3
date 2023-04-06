from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgVegasSendReportRequest(BaseRequest):

    def __init__(
        self,
        biz_date: str = None,
        relation_id: int = None,
        activity_id: int = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            统计日期
        """
        self._biz_date = biz_date
        """
            渠道关系id
        """
        self._relation_id = relation_id
        """
            已下线，后续不需要填写
        """
        self._activity_id = activity_id
        """
            页码
        """
        self._page_no = page_no
        """
            每页大小
        """
        self._page_size = page_size

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, biz_date):
        if isinstance(biz_date, str):
            self._biz_date = biz_date
        else:
            raise TypeError("biz_date must be str")

    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        if isinstance(relation_id, int):
            self._relation_id = relation_id
        else:
            raise TypeError("relation_id must be int")

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        if isinstance(activity_id, int):
            self._activity_id = activity_id
        else:
            raise TypeError("activity_id must be int")

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")


    def get_api_name(self):
        return "taobao.tbk.dg.vegas.send.report"

    def to_dict(self):
        request_dict = {}
        if self._biz_date is not None:
            request_dict["biz_date"] = convert_basic(self._biz_date)

        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._activity_id is not None:
            request_dict["activity_id"] = convert_basic(self._activity_id)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

