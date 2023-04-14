import datetime as dt
from pprint import pprint
import os



class Cinema:
    def __init__(self, name_cinema):
        self.name = name_cinema
        self.rooms = dict()
        self.movies = dict()
        self.schedule = dict()

    class Room:
        def __init__(self, number, seats):
            self.number = int(number)
            seats = list(map(int, seats.split(' ')))
            self.seats = [''] * seats[0]

            for i in range(len(self.seats)):
                self.seats[i] = ['0'] * seats[1]

    class Movie:
        def __init__(self, duration, genre=None):
            if genre is None:
                genre = set()
            self.duration = duration
            self.genre = genre

    def add_room(self, number, seats):
        number = int(number)

        if number in self.rooms.keys():
            print("Зал под таким номером уже существует")
            return

        self.rooms[number] = self.Room(number, seats)

    def add_movie(self, name_movie, duration, genre=None):
        if name_movie in self.movies.keys():
            print("Фильм с таким названием уже есть")
            return

        self.movies[name_movie] = self.Movie(duration, genre)

    def add_session(self, name_movie, number_room, time, price):
        if name_movie not in self.movies.keys():
            print("Фильма с таким названием нет в списке")
            return

        session_end = time + self.movies[name_movie].duration
        number_room = int(number_room)

        if name_movie in self.schedule.keys():
            for session in self.schedule[name_movie]:
                if session["room"] == number_room and (
                        (time < session["session_end"] and time > session["session_start"]) or 
                        (session_end < session["session_end"] and session_end > session["session_start"])):
                    print("На это время сеанс уже есть")
                    return

        number_room = int(number_room)
        session = {
            "room": number_room,
            "session_start": time,
            "session_end": session_end,
            "seats": self.rooms[number_room].seats.copy(),
            "price": price
            }

        if name_movie in self.schedule.keys():
            self.schedule[name_movie].append(session)
        else:
            self.schedule[name_movie] = [session]

    def buy_ticket(self, name_movie, date, place):
        place = list(map(int, place.split(' ')))
        for i in range(len(self.schedule[name_movie])):
            if self.schedule[name_movie][i]["session_start"] == date:
                self.schedule[name_movie][i]["seats"][place[0]-1][place[1]-1] = '1'


a = Cinema("йцуйцуйц")
a.add_movie("qwe qwewqe", dt.timedelta(hours=1, minutes=51, seconds=23))
a.add_movie("qwe qwewqe", dt.timedelta(hours=3, minutes=51, seconds=23))
a.add_room(0, "10 5")
a.add_room(0, "0 0")
a.add_session("qwe qwewqe", 0, dt.datetime(2023, 4, 11, 17, 36, 56), 150)
a.add_session("qwe qwewqe", 0, dt.datetime(2023, 4, 11, 16, 36, 56), 150)
a.add_session("qwe qwewqe", 0, dt.datetime(2023, 4, 14, 16, 36, 56), 150)
a.buy_ticket("qwe qwewqe", dt.datetime(2023, 4, 11, 17, 36, 56), '3 2')

'''pprint(a.name)
print(a.movies)
print(a.movies['qwe qwewqe'].duration)'''
#print(a.rooms[0].seats)
#pprint(a.schedule)
#pprint(a.schedule["qwe qwewqe"][1]["seats"])

'''while(True):
    os.system('cls')
    print('wqeqweqwe')
    input()'''

