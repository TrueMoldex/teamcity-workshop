from http import HTTPStatus


class ValidationResponseSpecifications:
    @staticmethod
    def check_duplicate_build_type_error(build_type_id, response, soft_assert):
        expected_error = f'The build configuration / template ID "{build_type_id}" is already used by another configuration or template'
        soft_assert.assert_equal(
            response.status_code,
            HTTPStatus.BAD_REQUEST,
            "Status code should be 400 for duplicate build type",
        )
        soft_assert.assert_true(
            expected_error in response.text,
            f"Response should contain error message: {expected_error}",
        )
