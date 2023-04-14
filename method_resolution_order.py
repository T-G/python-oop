'''
If we have the same method in different classes in the 
inheritance chain, Python will execute the nearest one (nearest ancestor).
This rule is called MRO - Method Resolution Order, which is 
important when we have multi-level inheritance
'''


# SandWatch Class
class SandWatch(object):

    def __init__(self):
        self.start_sand_watch()

    def start_sand_watch(self):
        print('Sand Watch started.')


# Clock Class
class Clock(SandWatch):
    '''Simulates the clock'''

    def __init__(self, hours, minutes, seconds):
        super().__init__()  # calling the SanndWatch.__init__() method

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def set_clock(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def time(self):
        return f'{self.__hours}:{self.__minutes}:{self.__seconds}'

    # method overloading /method overriding
    def start_sand_watch(self):
        print('Sand Watch started in Clock Class')


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


# create a ClockCalendar class which inherits from Clock and Calendar class
class CalendarClock(Clock, Calendar):
    '''Keeps calendar anf clock together'''

    def __init__(self, day, month, year, hours, minutes, seconds):

        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, day, month, year)


# create a CalendarClock object
calendar_clock = CalendarClock(14, 4, 2023, 12, 4, 20)

# MRO for CalendarClock
# __mro__

print(f'MRO for CalendarClock')
# for m in CalendarClock.__mro__:
for m in CalendarClock.mro():
    print(m)
