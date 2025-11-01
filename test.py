class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        for string in lst_in:
            mail_from, title, content = string.split(";")
            item = MailItem(mail_from, title, content)
            self.inbox_list.append(item)


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read

    def __repr__(self):
        return f"{self.mail_from} ({self.title}): {self.content} [{self.is_read}]"


mail = MailBox()
mail.receive()
mail.inbox_list[0].is_read = True
mail.inbox_list[-1].is_read = True

inbox_list_filtered = list(filter(bool, mail.inbox_list))
