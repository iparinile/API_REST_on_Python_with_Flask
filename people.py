from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}


# Create a handler for our read (GET) people
def read():
    """
    Эта функция отвечает на запрос для /api/people
    с полными списками людей
    :return:        отсортированный список людей
    """
    # Создать список людей из наших данных
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
