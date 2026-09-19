class TrainSchedule:
    def __init__(self):
        self.trains = [
            {
                "number": "001A",
                "name": "Бишкек — Алматы",
                "departure": "Бишкек",
                "arrival": "Алматы",
                "departure_time": "07:30",
                "arrival_time": "15:20",
                "duration": "7 ч 50 мин",
                "type": "Скорый",
                "seats": 42
            },
            {
                "number": "002A",
                "name": "Алматы — Бишкек",
                "departure": "Алматы",
                "arrival": "Бишкек",
                "departure_time": "08:15",
                "arrival_time": "16:10",
                "duration": "7 ч 55 мин",
                "type": "Скорый",
                "seats": 35
            },
            {
                "number": "101B",
                "name": "Бишкек — Ташкент",
                "departure": "Бишкек",
                "arrival": "Ташкент",
                "departure_time": "09:00",
                "arrival_time": "21:30",
                "duration": "12 ч 30 мин",
                "type": "Пассажирский",
                "seats": 28
            },
            {
                "number": "102B",
                "name": "Ташкент — Бишкек",
                "departure": "Ташкент",
                "arrival": "Бишкек",
                "departure_time": "10:20",
                "arrival_time": "22:40",
                "duration": "12 ч 20 мин",
                "type": "Пассажирский",
                "seats": 31
            },
            {
                "number": "201C",
                "name": "Бишкек — Каракол",
                "departure": "Бишкек",
                "arrival": "Каракол",
                "departure_time": "06:45",
                "arrival_time": "13:30",
                "duration": "6 ч 45 мин",
                "type": "Скорый",
                "seats": 56
            },
            {
                "number": "202C",
                "name": "Каракол — Бишкек",
                "departure": "Каракол",
                "arrival": "Бишкек",
                "departure_time": "14:15",
                "arrival_time": "21:00",
                "duration": "6 ч 45 мин",
                "type": "Скорый",
                "seats": 47
            },
            {
                "number": "301D",
                "name": "Бишкек — Ош",
                "departure": "Бишкек",
                "arrival": "Ош",
                "departure_time": "11:00",
                "arrival_time": "22:15",
                "duration": "11 ч 15 мин",
                "type": "Пассажирский",
                "seats": 19
            },
            {
                "number": "302D",
                "name": "Ош — Бишкек",
                "departure": "Ош",
                "arrival": "Бишкек",
                "departure_time": "08:30",
                "arrival_time": "19:45",
                "duration": "11 ч 15 мин",
                "type": "Пассажирский",
                "seats": 24
            },
            {
                "number": "401E",
                "name": "Алматы — Тараз",
                "departure": "Алматы",
                "arrival": "Тараз",
                "departure_time": "12:00",
                "arrival_time": "16:10",
                "duration": "4 ч 10 мин",
                "type": "Скорый",
                "seats": 63
            },
            {
                "number": "402E",
                "name": "Тараз — Алматы",
                "departure": "Тараз",
                "arrival": "Алматы",
                "departure_time": "17:00",
                "arrival_time": "21:15",
                "duration": "4 ч 15 мин",
                "type": "Скорый",
                "seats": 51
            },
            {
                "number": "501F",
                "name": "Бишкек — Шымкент",
                "departure": "Бишкек",
                "arrival": "Шымкент",
                "departure_time": "15:30",
                "arrival_time": "23:50",
                "duration": "8 ч 20 мин",
                "type": "Пассажирский",
                "seats": 37
            },
            {
                "number": "502F",
                "name": "Шымкент — Бишкек",
                "departure": "Шымкент",
                "arrival": "Бишкек",
                "departure_time": "07:10",
                "arrival_time": "15:40",
                "duration": "8 ч 30 мин",
                "type": "Пассажирский",
                "seats": 44
            }
        ]

    def get_all_trains(self):
        return self.trains

    def find_train(self, number):
        for train in self.trains:
            if train["number"] == number:
                return train
        return None

    def search(self, query):
        query = query.strip().lower()

        if not query:
            return self.trains

        return [
            train
            for train in self.trains
            if query in train["number"].lower()
            or query in train["name"].lower()
            or query in train["departure"].lower()
            or query in train["arrival"].lower()
        ]

    def filter_by_departure(self, station):
        if station == "Все станции":
            return self.trains

        return [
            train
            for train in self.trains
            if train["departure"] == station
        ]

    def filter_by_type(self, train_type):
        if train_type == "Все типы":
            return self.trains

        return [
            train
            for train in self.trains
            if train["type"] == train_type
        ]

    def get_stations(self):
        stations = set()

        for train in self.trains:
            stations.add(train["departure"])
            stations.add(train["arrival"])

        return sorted(stations)

    def get_available_trains(self):
        return [
            train
            for train in self.trains
            if train["seats"] > 0
        ]