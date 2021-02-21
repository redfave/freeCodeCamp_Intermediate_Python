try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('Everything is fine')
finally:
    print('Just cleaning here')


class ValueTooLowError(Exception):
    def __init__(self):
        self.err = 'Argument should be positive'
        super().__init__(self.err)

    def __init__(self, number):
        self.err = f'Argument should be positive: {number}'
        super().__init__(self.err)


x = -5
if x < 5:
    raise ValueTooLowError(x)
# assert (x < 5), 'Argument should be positive'
