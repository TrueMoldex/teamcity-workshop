from test.com_example_teamcity.soft_assert import SoftAssert


class BaseTest:
    def setup_method(self, method):
        self.softy = SoftAssert()

    def teardown_method(self, method):
        self.softy.assert_all()