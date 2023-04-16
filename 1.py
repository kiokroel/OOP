import datetime as dt
from pprint import pprint
from collections import defaultdict
import copy


class Cinema:
    def __init__(self, name):
        self.name = name
        self.halls = dict()


class Movie:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration


class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.tickets = list()

    def buy_ticket(self, cinema_name, movie_name, date, hall, seats):
        seats = list(map(int, seats.split()))
        for i in range(len(schedule[cinema_name])):
            if schedule[cinema_name][i].movie == movie_name and schedule[cinema_name][i].start == date and schedule[cinema_name][i].hall == hall:
                if schedule[cinema_name][i].seats[seats[0]-1][seats[1]-1] == True:
                    schedule[cinema_name][i].seats[seats[0] - 1][seats[1] - 1] = False
                    self.tickets.append(schedule[cinema_name][i])
                    return
                else:
                    print(f'{seats[1]} место в {seats[0]} ряду уже занято')
                    return
        print("Такого сеанса не существует")
        return


class Admin:
    def __init__(self, name):
        self.name = name

    def add_cinema(self, cinema_add):
        if cinema_add.name in cinema.keys():
            print(f'Кинотеатр {cinema_add.name} уже есть в списке')
            return
        cinema[cinema_add.name] = cinema_add

    def add_session(self, session):
        for s in schedule[session.cinema]:
            if s.hall == session.hall and (
                    session.start <= s.end and session.start <= s.start or session.end <= s.end and session.start >= s.start):
                print("Это время уже занято")
                return
        schedule[session.cinema].append(session)

    def add_movie(self, movie):
        if movie.name in movies.keys():
            print(f'Фильм {movie.name} уже есть в списке')
            return
        movies[movie.name] = movie

    def add_hall(self, cinema_name, number, hall):
        if number in cinema[cinema_name].halls.keys():
            print(f"Зал под номером {number} в кинотеатре {cinema_name} уже существует")
            return
        cinema[cinema_name].halls[number] = hall


class Hall:
    def __init__(self, seats):
        seats = list(map(int, seats.split(' ')))
        self.seats = [''] * seats[0]
        for i in range(len(self.seats)):
            self.seats[i] = [True] * seats[1]


class Session:
    def __init__(self, cinema_name, movie_name, hall, cost, date):
        self.cinema = cinema_name
        self.movie = movie_name
        self.hall = hall
        self.cost = cost
        self.start = date
        self.end = date + movies[movie_name].duration
        self.seats = copy.deepcopy(cinema[cinema_name].halls[hall].seats)


cinema = {
    "Кристалл": Cinema("Кристалл"),
    'Маяковский': Cinema('Маяковский')
}

movies = {
    'Джон Уик 4': Movie('Джон Уик 4', dt.timedelta(hours=2, minutes=49)),
    'Чебурашка': Movie('Чебурашка', dt.timedelta(hours=2, minutes=7))
}

schedule = defaultdict(list)


a = Admin('admin')
a.add_hall('Кристалл', 0, Hall('3 4'))
#a.add_hall('Кристалл', 0, Hall('3 4'))
#pprint(cinema['Кристалл'].halls[0].seats)

a.add_movie(Movie('Шазам! Ярость Богов', dt.timedelta(hours=2, minutes=10)))
#pprint(movies)

a.add_session(Session('Кристалл', 'Шазам! Ярость Богов', 0, 150, dt.datetime(2023, 4, 11, 17, 36, 56), ))
#a.add_session(Session('Кристалл', 'Шазам! Ярость Богов', 0, 150, dt.datetime(2023, 4, 11, 17, 36, 56), ))
#pprint(schedule['Кристалл'])

a.add_cinema(Cinema("Первомайский"))
#pprint(cinema)

#pprint(schedule['Кристалл'][0].seats)
u = User(User)
u.buy_ticket('Кристалл', 'Шазам! Ярость Богов', dt.datetime(2023, 4, 11, 17, 36, 56),0, '2 2' )
#u.buy_ticket('Кристалл', 'Шазам! Ярость Богов', dt.datetime(2023, 4, 11, 17, 36, 56),0, '2 2' )
#u.buy_ticket('Крисwталл', 'Шазам! Яроwсть Богов', dt.datetime(2023, 4, 11, 17, 36, 56),0, '2 2' )
#pprint(schedule['Кристалл'][0].seats)
#pprint(u.tickets[0].movie)

