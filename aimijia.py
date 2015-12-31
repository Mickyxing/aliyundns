import aliyun.api
import urllib2

class DNS:
    aliyun.setDefaultAppInfo("WIQF3T75AAcjjQ4p","d5ecsG9an8VjSxXDXLK3pxl10ZNQ0O")
    def getDNSIp(self):
        b = aliyun.api.Dns20150109DescribeDomainRecordInfoRequest()
        try:
            f = b.getResponse()
            return (f['Value'])
        except Exception,e:
            print('getDNSIp:',e)
            return None

    def getMyIp(self):
        try:
            u = urllib2.urlopen('http://members.3322.org/dyndns/getip')
            return u.read().strip('\n')
        except HTTPError as e:
            print('getMyIp:',e)
            return None;

    def main(self,newIp):
        a = aliyun.api.Dns20150109UpdateDomainRecordRequest(newIp);
        a.DBInstanceId = ""
        try:
            print("start")
            f = a.getResponse();
            print(f)
        except Exception , e:
            print('main:',e)


if __name__ =='__main__':
    d = DNS()
    oldip = d.getDNSIp()
    newip = d.getMyIp()
    print('oldIp:',oldip)
    print('newIp:',newip)
    if(oldip != newip and oldip is not None):
        d.main(newip)
