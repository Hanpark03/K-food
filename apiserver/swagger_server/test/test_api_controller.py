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

    def test_get_foodby_category(self):
        """Test case for get_foodby_category

        return food list by category and restaurant list by user info
        """
        body = Data()
        response = self.client.open(
            '//getFoodbyCategory',
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

    def test_get_restaurantby_default(self):
        """Test case for get_restaurantby_default

        return restaurant list by user info
        """
        body = Data()
        response = self.client.open(
            '//getRestaurantbyDefault',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_restaurantby_food(self):
        """Test case for get_restaurantby_food

        return restaurant list by food and user
        """
        body = Data()
        response = self.client.open(
            '//getRestaurantbyFood',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_restaurantby_keyword(self):
        """Test case for get_restaurantby_keyword

        return restaurant list by keyword and user info
        """
        body = Data()
        response = self.client.open(
            '//getRestaurantbyKeyword',
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
