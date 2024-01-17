import asyncio
import tornado.web
import Index
import users


def makeApp():
    endpoints=[
        ("/",Index.Handler),
        ("/profile/.*", users.AccHandler)
    ]
    app = tornado.web.Application(
        endpoints
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()