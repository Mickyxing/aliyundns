'''
Created by auto_sdk on 2015.09.18
'''
from aliyun.api.base import RestApi
import time
class Dns20150109DescribeDomainRecordInfoRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
		self.RecordId = "73609022"
		self.Timestamp = timestamp

	def getapiname(self):
		return 'dns.aliyuncs.com.DescribeDomainRecordInfo.2015-01-09'
