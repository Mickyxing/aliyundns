'''
Created by auto_sdk on 2015.05.27
'''
from top.api.base import RestApi
class PushAliyuncsComPush20150518Request(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Account = None
		self.AndroidActivity = None
		self.AndroidExtParameters = None
		self.AndroidMusic = None
		self.AndroidOpenType = None
		self.AndroidOpenUrl = None
		self.AntiHarassDuration = None
		self.AntiHarassStartTime = None
		self.AppId = None
		self.BatchNumber = None
		self.Body = None
		self.DeviceId = None
		self.DeviceType = None
		self.IOSBadge = None
		self.IOSExtParameters = None
		self.IOSMusic = None
		self.ProvinceId = None
		self.PushTime = None
		self.Remind = None
		self.SendType = None
		self.Status = None
		self.StoreOffline = None
		self.Summery = None
		self.Timeout = None
		self.Title = None
		self.Type = None

	def getapiname(self):
		return 'push.aliyuncs.com.push.20150518'
