import json
import time
import urllib.request

from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_models
from alibabacloud_alidns20150109.client import Client as Client


class DNS:

    def __init__(self):
        pass

    @staticmethod
    def init(id: str, secret: str):
        config = open_api_models.Config(id, secret)
        # 访问的域名
        config.endpoint = 'alidns.cn-hangzhou.aliyuncs.com'
        client = Client(config)
        return client

    # 获取当前ip地址
    @staticmethod
    def getMyIp():
        try:
            response = urllib.request.urlopen("http://members.3322.org/dyndns/getip")
            resp = response.read().decode('utf-8')
            return resp.strip('\n')
        except Exception as e:
            DNS.print_log('getMyIp' + '|' + str(e))
            return None

    # 获取域名已经配置解析的ip地址
    @staticmethod
    def getDNSIp(client: Client, record_id: str):
        requests = alidns_models.DescribeDomainRecordInfoRequest()
        requests.record_id = record_id
        try:
            resp = client.describe_domain_record_info(requests)
            # print(resp.body)
            return resp.body.value
        except Exception as e:
            DNS.print_log('getDNSIp' + record_id + '|' + str(e))
            return None

    # 查询域名解析记录，主要用于查询解析记录的recordId
    @staticmethod
    def get_domain_info(client: Client, domain_name):

        req = alidns_models.DescribeDomainRecordsRequest()
        req.domain_name = domain_name
        try:
            resp = client.describe_domain_records(req)
            print(resp.body)
        except Exception as e:
            DNS.print_log('get_domain_info' + domain_name + '|' + str(e))

    # 更新域名解析记录
    @staticmethod
    def update_domain(client: Client, newIp, recordId, rr):
        req = alidns_models.UpdateDomainRecordRequest()
        req.record_id = recordId
        req.rr = rr
        req.type = 'A'
        req.value = newIp
        try:
            resp = client.update_domain_record(req)
            # print(resp.body)
            return resp
        except Exception as e:
            DNS.print_log('update_domain' + newIp + '|' + str(e))

    @staticmethod
    def print_log(log):
        log = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '|' + log + '\n'
        # print(log)
        with open('./result.log', 'a') as f:
            f.write(log)


if __name__ == '__main__':
    # 加载配置文件
    jsonfile = open('key.json')
    s = json.load(jsonfile)

    client = DNS.init(s['id'], s['secret'])

    # DNS.get_domain_info(client, s['domain'])

    newip = DNS.getMyIp()
    oldip = DNS.getDNSIp(client, s['recordId'])
    if oldip != newip and newip is not None:
        resp = DNS.update_domain(client, newip, s['recordId'], s['rr'])
        DNS.print_log(newip + '|' + oldip + '|' + resp.body.request_id)
