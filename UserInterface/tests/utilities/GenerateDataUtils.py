import random
import string


class GenerateDataUtils:
    @staticmethod
    def generate_password(email, length=12):
        password = ''.join(random.choice(string.ascii_lowercase) for _ in range(length - 1))

        password = random.choice(string.ascii_uppercase) + password[1:]
        password = password[:length - 3] + random.choice(string.digits) + password[length - 2:]
        password = password[:length - 4] + random.choice(email) + password[length - 3:]

        cyrillic_char = random.choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
        position = random.randint(0, length - 2)
        password = password[:position] + cyrillic_char + password[position + 1:]

        return password

    @staticmethod
    def generate_dropdown():
        dropdowns = [".org", ".co.uk", ".net", ".gov", ".de", ".fr", ".nl", ".com", ".be", ".jpg"]
        random_index = random.randint(0, len(dropdowns) - 1)
        return dropdowns[random_index]

    @staticmethod
    def generate_interests(length=3):
        interests = ["Ponies", "Polo", "Dough", "Snails",
                     "Balls", "Post-its", "Faucets", "Envelopes",
                     "Cables", "Questions", "Squares", "Purple",
                     "Cotton", "Dry-wall", "Closets", "Tires",
                     "Windows", "Mullets", "Cinnamon"]

        random_interest = random.sample(interests, min(length, len(interests)))
        return random_interest
