from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgOptimusMaterialRequest(BaseRequest):

    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        adzone_id: int = None,
        material_id: int = None,
        device_value: str = None,
        device_encrypt: str = None,
        device_type: str = None,
        content_id: int = None,
        content_source: str = None,
        item_id: str = None,
        favorites_id: str = None
    ):
        """
            页大小，默认20，1~100
        """
        self._page_size = page_size
        """
            第几页，默认：1
        """
        self._page_no = page_no
        """
            mm_xxx_xxx_xxx的第三位
        """
        self._adzone_id = adzone_id
        """
            官方的物料Id(详细物料id见：https://market.m.taobao.com/app/qn/toutiao-new/index-pc.html#/detail/10628875?_k=gpov9a)
        """
        self._material_id = material_id
        """
            智能匹配-设备号加密后的值（MD5加密需32位小写），类型为OAID时传原始OAID值
        """
        self._device_value = device_value
        """
            智能匹配-设备号加密类型：MD5，类型为OAID时不传
        """
        self._device_encrypt = device_encrypt
        """
            智能匹配-设备号类型：IMEI，或者IDFA，或者UTDID（UTDID不支持MD5加密），或者OAID
        """
        self._device_type = device_type
        """
            内容专用-内容详情ID
        """
        self._content_id = content_id
        """
            内容专用-内容渠道信息
        """
        self._content_source = content_source
        """
            商品ID，用于相似商品推荐
        """
        self._item_id = item_id
        """
            选品库投放id
        """
        self._favorites_id = favorites_id

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

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
    def adzone_id(self):
        return self._adzone_id

    @adzone_id.setter
    def adzone_id(self, adzone_id):
        if isinstance(adzone_id, int):
            self._adzone_id = adzone_id
        else:
            raise TypeError("adzone_id must be int")

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        if isinstance(material_id, int):
            self._material_id = material_id
        else:
            raise TypeError("material_id must be int")

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
    def device_encrypt(self):
        return self._device_encrypt

    @device_encrypt.setter
    def device_encrypt(self, device_encrypt):
        if isinstance(device_encrypt, str):
            self._device_encrypt = device_encrypt
        else:
            raise TypeError("device_encrypt must be str")

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
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        if isinstance(content_id, int):
            self._content_id = content_id
        else:
            raise TypeError("content_id must be int")

    @property
    def content_source(self):
        return self._content_source

    @content_source.setter
    def content_source(self, content_source):
        if isinstance(content_source, str):
            self._content_source = content_source
        else:
            raise TypeError("content_source must be str")

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, str):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be str")

    @property
    def favorites_id(self):
        return self._favorites_id

    @favorites_id.setter
    def favorites_id(self, favorites_id):
        if isinstance(favorites_id, str):
            self._favorites_id = favorites_id
        else:
            raise TypeError("favorites_id must be str")


    def get_api_name(self):
        return "taobao.tbk.dg.optimus.material"

    def to_dict(self):
        request_dict = {}
        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._material_id is not None:
            request_dict["material_id"] = convert_basic(self._material_id)

        if self._device_value is not None:
            request_dict["device_value"] = convert_basic(self._device_value)

        if self._device_encrypt is not None:
            request_dict["device_encrypt"] = convert_basic(self._device_encrypt)

        if self._device_type is not None:
            request_dict["device_type"] = convert_basic(self._device_type)

        if self._content_id is not None:
            request_dict["content_id"] = convert_basic(self._content_id)

        if self._content_source is not None:
            request_dict["content_source"] = convert_basic(self._content_source)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._favorites_id is not None:
            request_dict["favorites_id"] = convert_basic(self._favorites_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

