'''
Created by auto_sdk on 2015.09.18
'''
from aliyun.api.base import RestApi
class Dns20150109DescribeDomainRecordInfoRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.RecordId = "73609022"

	def getapiname(self):
		return 'dns.aliyuncs.com.DescribeDomainRecordInfo.2015-01-09'
