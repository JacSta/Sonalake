from settings import (is_session_headless)


class BaseDriver(object):
    """Base class with obligatory attributes to create webdriver session"""

    def __init__(self):
        # Before returning objects checks if given values has expected types.
        self.is_session_headless = self._test_obj_type(is_session_headless, bool)

    @staticmethod
    def _test_obj_type(obj, obj_type):
        # Checks if given obj has expected type.
        if not isinstance(obj, obj_type):
            raise TypeError("Given object is type of {current_type} should be {obj_type}".format(
                current_type=type(obj), obj_type=obj_type
            ))
        else:
            if isinstance(obj_type, bool):
                # If obj_type is type of bool checks if given obj is not None.
                assert obj is not None, "Given object must be True/False"

        return obj
