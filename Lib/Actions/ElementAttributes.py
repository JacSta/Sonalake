from .BaseActions import BaseActions


class ElementAttributes(BaseActions):
    """Class contains helpers to test attribute element and its value."""

    def has_attribute(self, element, attr_name):
        # Tests if element has expected attribute and returns its value.
        attribute_value = self.get_element_locator(element).get_attribute(attr_name)

        if attribute_value in ("", None):
            raise self.exception.NoSuchAttributeException("Given element has not expected attribute: {}".
                                                          format(attr_name))
        return attribute_value

    def attribute_has_value(self, element, attr_name, expected_value):
        # Tests if element attribute has expected value.
        attr_value = self.has_attribute(element, attr_name)
        assert expected_value in attr_value, \
            "Expected value is not contained in given attribute. " \
            "Given attribute values: {}. " \
            "Expected attribute value: {}".format(attr_value, expected_value)
