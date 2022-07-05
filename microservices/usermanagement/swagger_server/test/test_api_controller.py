# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_get_food_history(self):
        """Test case for get_food_history

        return food list that the target user selected
        """
        body = Data()
        response = self.client.open(
            '//getFoodHistory',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_restaurant_history(self):
        """Test case for get_restaurant_history

        return restaurant list that the target user selected
        """
        body = Data()
        response = self.client.open(
            '//getRestaurantHistory',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
