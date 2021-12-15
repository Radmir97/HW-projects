import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day(start_karma, goal):
    while start_karma < goal:
        chance = random.randint(1, 8)
        fail = random.randint(1, 6)
        if fail == 1:
            with open('karma.log.txt', 'a') as log:
                log.write('KillError')
                log.write('\n')
            try:
                pass
            except:
                raise KillError('KillError')
        if fail == 2:
            with open('karma.log.txt', 'a') as log:
                log.write('DrunkError')
                log.write('\n')
            try:
                pass
            except:
                raise DrunkError('DrunkError')
        if fail == 3:
            with open('karma.log.txt', 'a') as log:
                log.write('CarCrashError')
                log.write('\n')
            try:
                pass
            except:
                raise CarCrashError('CarCrashError')
        if fail == 4:
            with open('karma.log.txt', 'a') as log:
                log.write('GluttonyError')
                log.write('\n')
            try:
                pass
            except:
                raise GluttonyError('GluttonyError')
        if fail == 5:
            with open('karma.log.txt', 'a') as log:
                log.write('DepressionError')
                log.write('\n')
            try:
                pass
            except:
                raise DepressionError('DepressionError')
        start_karma += chance
        if start_karma >= goal:
            print(start_karma, 'очков кармы')


one_day(0, 500)

# зачтено
