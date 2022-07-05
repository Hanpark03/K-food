import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util


def get_food_history(body):  # noqa: E501
    """return food list that the target user selected

     # noqa: E501

    :param body: User Information
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_food_history!'


def get_restaurant_history(body):  # noqa: E501
    """return restaurant list that the target user selected

     # noqa: E501

    :param body: User Information
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic get_restaurant_history!'
