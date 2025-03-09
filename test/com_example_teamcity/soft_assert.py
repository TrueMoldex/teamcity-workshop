class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_true(self, expr, msg=""):
        try:
            assert expr, msg
        except AssertionError as e:
            self.errors.append(e)

    def assert_equal(self, actual, expected, msg=""):
        try:
            assert actual == expected, msg or f"Expected {expected}, got {actual}"
        except AssertionError as e:
            self.errors.append(e)

    def assert_all(self):
        if self.errors:
            error_msgs = "\n".join(str(e) for e in self.errors)
            raise AssertionError(f"Soft assertion failures:\n{error_msgs}")