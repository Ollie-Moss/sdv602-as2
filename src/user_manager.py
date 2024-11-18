from jsn_drop_service import jsnDrop
from datetime import datetime
from uuid import uuid4
from hashlib import sha256


class UserManager:
    instance = None
    current_user = None
    jsn_tok = "46a30b6c-586f-43eb-aeb5-079986f6b359"

    def __init__(self):
        self.jsnDrop = jsnDrop(UserManager.jsn_tok,
                               "https://newsimland.com/~todd/JSON")

        result = self.jsnDrop.create("tblUser", {"personID PK": "A_LOOONG_NAME"+('X'*50),
                                                 "username": "A_LOOONG_PASSWORD"+('X'*50),
                                                 "password": "A_LOOONG_PASSWORD"+('X'*50)})

        result = self.jsnDrop.create("tblChat", {"chatID PK": "A_LOOONG_NAME"+('X'*50),
                                                 "personID FK": "A_LOOONG_DES_ID"+('X'*50),
                                                 "des_title": "A_LOOONG_DES_ID"+('X'*50),
                                                 "chat": "A_LOONG____CHAT_ENTRY"+('X'*255),
                                                 "time_sent": datetime.now().timestamp()})
        UserManager.instance = self

    def login(self, username, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        self.jsnDrop.select(
            "tblUser", f"username = '{username}' AND password = '{password}'")
        if "DATA_ERROR" in self.jsnDrop.jsnStatus:
            UserManager.current_user = None
            return "Failed"
        else:
            UserManager.current_user = self.jsnDrop.jsnResult[0]
            return "Success"

    def signup(self, username, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        self.jsnDrop.select(
            "tblUser", f"username = '{username}' AND password = '{password}'")
        if "DATA_ERROR" in self.jsnDrop.jsnStatus:
            self.jsnDrop.store("tblUser", [{"personID": str(
                uuid4()), "username": username, "password": password}])
            return "Success"
        else:
            return "Failed"

    def send_chat(self, chat, des_title):
        if UserManager.current_user:
            return self.jsnDrop.store("tblChat", [{"chatID": str(uuid4()), "personID": UserManager.current_user["personID"],
                                                     "des_title": des_title, "chat": chat, "time_sent": datetime.now().timestamp()}])

    def get_chats(self, title):
        if UserManager.current_user:
            result = self.jsnDrop.select("tblChat", f"des_title = '{title}'")

            if "Data error" in result:
                return []
            else:
                return result
        return []


if __name__ == "__main__":
    UserManager()

    result = UserManager.instance.signup("ollie", "ollie")
    result = UserManager.instance.login("ollie", "ollie")

    UserManager.instance.send_chat("HI", "DES 1")
    UserManager.instance.get_chats("DES 1")