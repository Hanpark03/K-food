# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_get_category(self):
        """Test case for get_category

        return category list
        """
        body = Data()
        response = self.client.open(
            '//getCategory',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_food(self):
        """Test case for get_food

        return food list by category
        """
        body = Data()
        response = self.client.open(
            '//getFood',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_restaurant(self):
        """Test case for get_restaurant

        return selected restaurant detail
        """
        body = Data()
        response = self.client.open(
            '//getRestaurant',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_restaurants(self):
        """Test case for get_restaurants

        return restaurant list by keyword
        """
        body = Data()
        response = self.client.open(
            '//getRestaurants',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
