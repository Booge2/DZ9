class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Не можна встановити від'ємний баланс")
        self._balance = value

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостатньо коштів")
        self._balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Не можна внести від'ємну суму")
        self._balance += amount


account = BankAccount(1000)

account.withdraw(500)

account.deposit(100)

print(account.balance)

try:
    account.withdraw(2000)
except ValueError as e:
    print(f"Помилка: {e}")

try:
    account.deposit(-100)
except ValueError as e:
    print(f"Помилка: {e}")

print("-----------------------")


# Завдання 2
class TemperatureSensor:

    def __init__(self, min_temperature, max_temperature):
        self._min_temperature = min_temperature
        self._max_temperature = max_temperature
        self._temperature = None

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < self._min_temperature or value > self._max_temperature:
            raise ValueError(f"Температура повинна бути в межах від {self._min_temperature} до {self._max_temperature}")
        self._temperature = value


sensor = TemperatureSensor(-50, 150)

sensor.temperature = 25

print(sensor.temperature)

try:
    sensor.temperature = 200
except ValueError as e:
    print(f"Помилка: {e}")

try:
    sensor.temperature = -100
except ValueError as e:
    print(f"Помилка: {e}")

print("-------------------")


# Завдання 3
class TextModifier:

    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def to_lower(self):
        return self.text.lower()

    def remove_spaces(self):
        return self.text.replace(" ", "")

    def encrypt(self, shift):
        alphabet = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя"
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        new_text = ""
        for char in self.text:
            if char.lower() in alphabet:
                new_text += shifted_alphabet[alphabet.index(char.lower())]
            else:
                new_text += char
        return new_text


text = "Це текст для модифікації"

modifier = TextModifier(text)

upper_text = modifier.to_upper()

lower_text = modifier.to_lower()

no_spaces_text = modifier.remove_spaces()

encrypted_text = modifier.encrypt(3)

print(f"Оригінальний текст: {text}")
print(f"Верхній регістр: {upper_text}")
print(f"Нижній регістр: {lower_text}")
print(f"Без пробілів: {no_spaces_text}")
print(f"Шифрований текст: {encrypted_text}")
