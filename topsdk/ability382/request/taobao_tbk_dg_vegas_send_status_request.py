from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgVegasSendStatusRequest(BaseRequest):

    def __init__(
        self,
        relation_id: str = None,
        special_id: str = None,
        device_value: str = None,
        device_type: str = None,
        thor_biz_code: str = None,
        pid: str = None
    ):
        """
            渠道管理id
        """
        self._relation_id = relation_id
        """
            会员运营id
        """
        self._special_id = special_id
        """
            加密后的值(ALIPAY_ID除外)，需用MD5加密，32位小写
        """
        self._device_value = device_value
        """
            入参类型(该模式下返回的结果为模糊匹配结果，和实际情况可能存在误差)： 1. IMEI 2. IDFA 3. OAID 4. MOBILE 5. ALIPAY_ID
        """
        self._device_type = device_type
        """
            thor平台业务码， 1：coupon 超红
        """
        self._thor_biz_code = thor_biz_code
        """
            媒体pid
        """
        self._pid = pid

    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        if isinstance(relation_id, str):
            self._relation_id = relation_id
        else:
            raise TypeError("relation_id must be str")

    @property
    def special_id(self):
        return self._special_id

    @special_id.setter
    def special_id(self, special_id):
        if isinstance(special_id, str):
            self._special_id = special_id
        else:
            raise TypeError("special_id must be str")

    @property
    def device_value(self):
        return self._device_value

    @device_value.setter
    def device_value(self, device_value):
        if isinstance(device_value, str):
            self._device_value = device_value
        else:
            raise TypeError("device_value must be str")

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        if isinstance(device_type, str):
            self._device_type = device_type
        else:
            raise TypeError("device_type must be str")

    @property
    def thor_biz_code(self):
        return self._thor_biz_code

    @thor_biz_code.setter
    def thor_biz_code(self, thor_biz_code):
        if isinstance(thor_biz_code, str):
            self._thor_biz_code = thor_biz_code
        else:
            raise TypeError("thor_biz_code must be str")

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, pid):
        if isinstance(pid, str):
            self._pid = pid
        else:
            raise TypeError("pid must be str")


    def get_api_name(self):
        return "taobao.tbk.dg.vegas.send.status"

    def to_dict(self):
        request_dict = {}
        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._special_id is not None:
            request_dict["special_id"] = convert_basic(self._special_id)

        if self._device_value is not None:
            request_dict["device_value"] = convert_basic(self._device_value)

        if self._device_type is not None:
            request_dict["device_type"] = convert_basic(self._device_type)

        if self._thor_biz_code is not None:
            request_dict["thor_biz_code"] = convert_basic(self._thor_biz_code)

        if self._pid is not None:
            request_dict["pid"] = convert_basic(self._pid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

