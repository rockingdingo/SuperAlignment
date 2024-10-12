# -*- coding: utf-8 -*-
# @Time    : 2024/06/27
# @Author  : Derek

from .base import *

SUPPORTED_APIS = {
    API_NAME_ARXIV : {
        "impl":ArxivPaperAPI
    },
}

def preprocess(text):
    return text

def api(input_dict, model, api_name, **kwargs):
    api_cls = BaseAPI(None)
    res_dict = {}
    try:
        if api_name in SUPPORTED_APIS:
            attrs = SUPPORTED_APIS[api_name]
            cls_name = attrs["impl"]
            api_cls = cls_name(None)
            res_dict = api_cls.api(input_dict, model, kwargs)
        else:
            print ("WARN: Input API NAME %s not supported" % api_name)
    except Exception as e:
        print (e)
    return res_dict
