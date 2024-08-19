from datetime import datetime

def get_chinese_zodiac(year):
    zodiacs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return zodiacs[year % 12]

def get_astrological_sign(day, month):
    if month == 12:
        sign = "Sagittarius" if day < 22 else "Capricorn"
    elif month == 1:
        sign = "Capricorn" if day < 20 else "Aquarius"
    elif month == 2:
        sign = "Aquarius" if day < 19 else "Pisces"
    elif month == 3:
        sign = "Pisces" if day < 21 else "Aries"
    elif month == 4:
        sign = "Aries" if day < 20 else "Taurus"
    elif month == 5:
        sign = "Taurus" if day < 21 else "Gemini"
    elif month == 6:
        sign = "Gemini" if day < 21 else "Cancer"
    elif month == 7:
        sign = "Cancer" if day < 23 else "Leo"
    elif month == 8:
        sign = "Leo" if day < 23 else "Virgo"
    elif month == 9:
        sign = "Virgo" if day < 23 else "Libra"
    elif month == 10:
        sign = "Libra" if day < 23 else "Scorpio"
    elif month == 11:
        sign = "Scorpio" if day < 22 else "Sagittarius"
    return sign

def get_birthstone(month):
    stones = {
        1: "Garnet",
        2: "Amethyst",
        3: "Aquamarine",
        4: "Diamond",
        5: "Emerald",
        6: "Pearl",
        7: "Ruby",
        8: "Peridot",
        9: "Sapphire",
        10: "Opal",
        11: "Topaz",
        12: "Turquoise"
    }
    return stones.get(month, "Unknown")

def get_birth_flower(month):
    flowers = {
        1: "Carnation",
        2: "Violet",
        3: "Daffodil",
        4: "Daisy",
        5: "Lily",
        6: "Rose",
        7: "Larkspur",
        8: "Gladiolus",
        9: "Aster",
        10: "Marigold",
        11: "Chrysanthemum",
        12: "Poinsettia"
    }
    return flowers.get(month, "Unknown")

def get_birthday_specialties(birth_date):
    date_obj = datetime.strptime(birth_date, '%Y-%m-%d')
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    chinese_zodiac = get_chinese_zodiac(year)
    astrological_sign = get_astrological_sign(day, month)
    birthstone = get_birthstone(month)
    birth_flower = get_birth_flower(month)
    
    return {
        "Chinese Zodiac": chinese_zodiac,
        "Astrological Sign": astrological_sign,
        "Birthstone": birthstone,
        "Birth Flower": birth_flower
    }

# Example Usage
birth_date = input()
specialties = get_birthday_specialties(birth_date)
for key, value in specialties.items():
    print(f"{key}: {value}")
