import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util


def get_category(body):  # noqa: E501
    """return category list

     # noqa: E501

    :param body: Nothing (Empty data)
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_category!'


def get_food(body):  # noqa: E501
    """return food list by category

     # noqa: E501

    :param body: Category
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_food!'


def get_restaurant(body):  # noqa: E501
    """return selected restaurant detail

     # noqa: E501

    :param body: restaurant
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_restaurant!'


def get_restaurants(body):  # noqa: E501
    """return restaurant list by keyword

     # noqa: E501

    :param body: Keyword
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_restaurants!'
