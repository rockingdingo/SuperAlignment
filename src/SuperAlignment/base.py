# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import json
import requests
from bs4 import BeautifulSoup

## constants
API_NAME_ARXIV = "ArxivPaperAPI"

class BaseAPI(object):
    """docstring for ClassName"""
    def __init__(self, configs):
        self.configs = configs
        
    def api(self, input_dict, model, kwargs):
        """
            Args:
                input_dict: dict, multi-modal input text, image, audio and video
                model: huggingface model of tf or pytoch
                kwargs: key-value args
            Return:
                res_dict: dict, multi-modal text text, image, audio and video
        """
        # input
        input_text = input_dict["text"]   # str
        input_image = input_dict["image"] # image path
        input_audio = input_dict["audio"] # audio path
        input_video = input_dict["video"] # video path

        # multi model output
        res_dict={}
        res_dict["text"] = None
        res_dict["image"] = None
        res_dict["audio"] = None
        res_dict["video"] = None
        return res_dict

class ArxivPaperAPI(BaseAPI):
    """docstring for ClassName"""
    def __init__(self, configs):
        super(ArxivPaperAPI, self).__init__(configs)
        self.name = API_NAME_ARXIV

    def api(self, input_dict, model, kwargs):
        res_dict={}
        try:
            # query keywords
            input_text = input_dict["text"]
            arxiv_paper_list = fetch_arxiv_papers(input_text, kwargs)
            output_paper_json = json.dumps(arxiv_paper_list)
            res_dict["text"] = output_paper_json
            res_dict["image"] = None
            res_dict["audio"] = None
            res_dict["video"] = None
        except Exception as e:
            print (e)
        return res_dict

def fetch_arxiv_papers(topic, kwargs):
    """
        https://info.arxiv.org/help/api/user-manual.html
        Base API: http://export.arxiv.org/api/query?search_query=all:%s
    """
    url = 'http://export.arxiv.org/api/query?search_query=all:%s' % topic
    # required fields
    start = kwargs["start"] if "start" in kwargs else 0
    max_results = kwargs["max_results"] if "max_results" in kwargs else 10
    sort_by = kwargs["sortBy"] if "sortBy" in kwargs else "lastUpdatedDate"
    sort_order = kwargs["sortOrder"] if "sortOrder" in kwargs else "descending"
    params_dict = {}
    params_dict["start"] = start
    params_dict["max_results"] = max_results
    params_dict["sortBy"] = sort_by
    params_dict["sortOrder"] = sort_order
    # optional fields
    for key in params_dict.keys():
        url = url + "&" + ("%s=%s" % (key, params_dict[key]))
    print ("### DEBUG: Calling ArxivPaperAPI input args is: %s, URL: %s" % (str(kwargs), url))

    # print ("DEBUG: Fetching Arxive Paper list from API %s" % url)
    headers = {
        'User-Agent': 'curl/7.68.0',
        'Accept': '*/*'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    entries = soup.find_all('entry')
    entry_keys = ["id", "updated", "published", "title", "summary", "author"]
    entry_json_list = []
    for entry in entries:
        try:
            entry_json = {}
            for key in entry_keys:
                value_list = entry.find_all(key)
                if len(value_list) == 1:
                    entry_json[key] = value_list[0].text.strip()
                else:
                    value_text_list = [value.text.strip() for value in value_list]
                    entry_json[key] = value_text_list
            entry_json_list.append(entry_json)
        except Exception as e:
            print (e)
    return entry_json_list
