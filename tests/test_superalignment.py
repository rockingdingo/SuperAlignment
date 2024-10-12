# -*- coding: utf-8 -*-
# @Time    : 2024/06/27

import SuperAlignment as sa
import json

def test_arxiv_api():

    input_dict = {"text": "SuperAlignment"}
    res = sa.api(input_dict, model=None, api_name="ArxivPaperAPI", start=0, max_results = 10)
    paper_list = json.loads(res["text"])
    print ("###### SuperAlignment Recent Paper List:")
    for (i, paper_json) in enumerate(paper_list):
        print ("|" + paper_json["id"] + "|" + paper_json["title"].replace("\n", "") + "|" + paper_json["updated"] )

def main():
    test_arxiv_api()

if __name__ == '__main__':
    main()
