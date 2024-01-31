import tornado.web


# This is a dictionary (of dictionaries) for the users
accounts = {
    "alice" : {
        "accRealName": "Alice Smith",
        "accDOB": "Jan 1",
        "accEmail": "alice@example.com",
        "picLink": "/static/alice.jpg"
    },
    "bob" : {
        "accRealName": "Bob Jones",
        "accDOB": "Dec 31",
        "accEmail": "bob@bob.xyz",
        "picLink": "/static/bob.jpg"
    },
    "carol" : {
        "accRealName": "Carol Ling",
        "accDOB": "July 17",
        "accEmail": "carol@example.com",
        "picLink": '/static/carol.jpg'
    },
    "dave" : {
        "accRealName": "Dave N. Port",
        "accDOB": "Mar 14",
        "accEmail": "dave@dave.dave",
        "picLink": '/static/dave.jpg'
    }
}

class AccHandler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path
        uname = p.split("/")[2]
        realName = accounts[uname]["accRealName"]
        DOB  = accounts[uname]["accDOB"]
        email = accounts[uname]["accEmail"]
        pic = accounts[uname]["picLink"]

        self.render( "users.html", 
                    htmluname = uname,
                    htmlrealName = realName,
                    htmlDOB = DOB,
                    htmlemail = email,
                    htmlpic = pic)