# Часто при зачислении средств на счет с клиента взымают комиссию.
# Реализуйте похожий механизм с помощью дескрипторов.
# Напишите дескриптор Value, который будет использоваться в классе Account.


class Value:
    """Class Value"""

    def __init__(self):
        """Initialization method"""

        self.cash = None

    def __get__(self, instance, owner):
        """Get cash item"""

        return self.cash

    def __set__(self, instance, value):
        """Set cash item"""

        if value < 0:
            raise ValueError('Value can\'t be negative!')
        if isinstance(value, (float, int)) is False:
            raise TypeError('Value can\'t be None!')

        self.cash = int(value - value * instance.commission)


class Account:
    """Class Account"""

    amount = Value()

    def __init__(self, commission):
        """Initialisation method"""

        if isinstance(commission, float) and commission > 0:
            self.commission = commission
        else:
            raise ValueError('Commission assumes an invalid value!')


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
