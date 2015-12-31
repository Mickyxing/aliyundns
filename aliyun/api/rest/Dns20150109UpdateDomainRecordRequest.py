'''
Created by auto_sdk on 2015.09.21
'''
from aliyun.api.base import RestApi
class Dns20150109UpdateDomainRecordRequest(RestApi):
	def __init__(self,address,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Line = "default"
		self.Priority = None
		self.RR = "ssh"
		self.RecordId = "73609022"
		self.TTL = None
		self.Type = "A"
		self.Value = address

	def getapiname(self):
		return 'dns.aliyuncs.com.UpdateDomainRecord.2015-01-09'

	def getIp(self):
		print self.Value
