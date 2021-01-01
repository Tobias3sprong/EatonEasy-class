import httplib2, base64, json, time

class EatonEasy:
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey
    def request(self, pTarget):
        header = {'Authorization': "Bearer %s" % self.apikey}
        h= httplib2.Http()
        resp, content = h.request(self.url+pTarget, method="GET",headers=header)
        return resp, content
    def isRunning(self):
        r = False
        resp, content = self.request("api/get/data?elm=STATE");
        try:
            o = json. loads(content);
            r = (o["SYSINFO"]["STATE"]) == "RUN"
        except ValueError:
            print ('JSON Decoding failed')
        return r

    def setOp(self, pOp, pIndex, pVal):
        url = "api/set/op?op="+pOp+"&index="+str(pIndex)+"&val="+str(pVal)
        return self.request(url)

    def getElm(self, Type, ElmNo):
        resp, content = self.request("api/get/data?elm="+str(Type)+"("+str(ElmNo)+")");
        try:
            o = json.loads(content);
            r = (o["OPERANDS"][Type+"SINGLE"][0]["V"])
        except ValueError:
            print ('JSON Decoding failed')
        return r
