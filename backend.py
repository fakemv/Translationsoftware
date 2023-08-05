import json
import urllib
from urllib import request
from win11toast import toast


class trans(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    def tran(self, texts):

        self.formData = {
            'i': texts,
            'from': 'English',
            'to': 'Chinese',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '1538959984992',
            'sign': 'e2fd5830da31a783b6c1f83b522a7d7c',
            'doctype': 'json',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false',
        }
        from_data_parse = urllib.parse.urlencode(self.formData).encode('utf-8')
        response = request.urlopen(self.url, data=from_data_parse)
        response_str = response.read().decode('utf-8')
        response_dict = json.loads(response_str)
        result = ''
        for i in response_dict['translateResult'][0]:
            result += i['tgt']
            result = result.replace('。', '.')
        try:
            self.result = result
        except:
            self.result = "翻译失败......."

        toast("内容",
              f"{self.result}",
              audio={'silent': 'true'})
