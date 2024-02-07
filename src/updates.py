import tornado.web
import json
import users

class UpHandler(tornado.web.RequestHandler):
    def post(self):
        L = json.loads(self.request.body)
        uname = L["uuName"]
        if (L["uppName"] != ""):
            users.accounts[uname]["accRealName"] = L["uppName"]
        if (L["uppDOB"] != ""):
            users.accounts[uname]["accDOB"] = L["uppDOB"]
        if (L["uppEmail"] != ""):        
            users.accounts[uname]["accEmail"] = L["uppEmail"]
        if (L["uppPic"] != ""):
            users.accounts[uname]["picLink"] = "data:image/jpeg;base64," + L["uppPic"]
