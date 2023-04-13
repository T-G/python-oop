# Clock Class
class Clock:
    '''Simulates the clock'''

    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def set_clock(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def time(self):
        return f'{self.__hours}:{self.__minutes}:{self.__seconds}'


# create clock object
clock = Clock(0, 0, 0)
print(f'Start Time: {clock.time()}')

clock = Clock(13, 4, 22)
print(f'End Time: {clock.time()}')


# Calendar Class
class Calendar(object):
    '''Simulates the calendar'''

    def __init__(self, d, m, y):
        self.set_calendar(d, m, y)

    def set_calendar(self, d, m, y):
        self.__d = d
        self.__m = m
        self.__y = y

    def date(self):
        return f'{self.__d}, {self.__m}, {self.__y}'


# create a Calendar object
calendar = Calendar(13, 4, 2023)
print(calendar.date())

# set calendar date
calendar.set_calendar(13, 4, 2022)
print(calendar.date())


# create a ClockCalendar class which inherits from Clock and Calendar class
class ClockCalendar(Clock, Calendar):
    '''Keeps calendar anf clock together'''

    def __init__(self, day, month, year, hours, minutes, seconds):

        super().__init__(hours, minutes, seconds)
