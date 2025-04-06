import string
import random


class RandomData:

    TEST_PREFIX = "test_"
    MAX_LENGTH = 10

    @staticmethod
    def get_string() -> str:
        return RandomData.TEST_PREFIX + "".join(
            random.choices(string.ascii_letters, k=RandomData.MAX_LENGTH)
        )

    @staticmethod
    def get_int() -> int:
        return random.randint(0, 10**RandomData.MAX_LENGTH - 1)
