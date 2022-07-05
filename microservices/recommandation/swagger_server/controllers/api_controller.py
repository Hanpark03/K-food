import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util


def get_foodby_category(body):  # noqa: E501
    """return food list by category and restaurant list by user info

     # noqa: E501

    :param body: Category and User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_foodby_category!'


def get_restaurantby_default(body):  # noqa: E501
    """return restaurant list by user info

     # noqa: E501

    :param body: User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_restaurantby_default!'


def get_restaurantby_food(body):  # noqa: E501
    """return restaurant list by food and user

     # noqa: E501

    :param body: Food and User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_restaurantby_food!'


def get_restaurantby_keyword(body):  # noqa: E501
    """return restaurant list by keyword and user info

     # noqa: E501

    :param body: Keyword and User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_restaurantby_keyword!'
