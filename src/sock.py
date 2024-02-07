import tornado.websocket

activeClients = []


class sockHandler (tornado.websocket.WebSocketHandler):

    async def open(self):
        print("Opened")
        for i in activeClients:
            await i.write_message("SomeoneEntered the CHat")
        activeClients.append(self)
        
    async def on_message(self,msg):
        print("Message")
        for i in activeClients:
            await i.write_message(msg)
    
    def on_close(self):
        print("Closed")

        for i in range(len(activeClients)):
            if activeClients[i] == self:
                del activeClients[i]
                break

        for i in activeClients:
            i.write_message("Someone Left the Chat")                 

    def check_origin(self,*args):
        print(args)
        return True # trusting everyone