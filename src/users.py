import tornado.web


# This is a dictionary (of dictionaries) for the users
accounts = {
    "alice" : {
        "accRealName": "Alice Smith",
        "accDOB": "Jan 1",
        "accEmail": "alice@example.com"
    },
    "bob" : {
        "accRealName": "Bob Jones",
        "accDOB": "Dec 31",
        "accEmail": "bob@bob.xyz"
    },
    "carol" : {
        "accRealName": "Carol Ling",
        "accDOB": "July 17",
        "accEmail": "carol@example.com"
    },
    "dave" : {
        "accRealName": "Dave N. Port",
        "accDOB": "Mar 14",
        "accEmail": "dave@dave.dave"
    }
}

class AccHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path
        uname = p.split("/")[2]
        realName = accounts[uname]["accRealName"]
        DOB  = accounts[uname]["accDOB"]
        email = accounts[uname]["accEmail"]

        self.render( "users.html", 
                    htmluname = uname,
                    htmlrealName = realName,
                    htmlDOB = DOB,
                    htmlemail = email)