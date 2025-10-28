class Model:
    def __init__(self):
        self.__db = {}

    def query(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.__db[key] = value

    def __str__(self):
        """Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"""
        if self.__db:
            answer = "Model: "
            for key, value in self.__db.items():
                answer += f"{key} = {value}, "
            return answer[:-2]
        else:
            return "Model"
