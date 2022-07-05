import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util
import requests
import json

from swagger_server.models.userinfo import Userinfo

def get_category(body):  # noqa: E501
    """return category list

     # noqa: E501

    :param body: Nothing (Empty data)
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://datalookup:8080/getCategory'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_food(body):  # noqa: E501
    """return food list by category

     # noqa: E501

    :param body: Category
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://datalookup:8080/getFood'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_food_history(body):  # noqa: E501
    """return food list that the target user selected

     # noqa: E501

    :param body: User Information
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://usermanagement:8080/getFoodHistory'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_foodby_category(body):  # noqa: E501
    """return food list by category and restaurant list by user info

     # noqa: E501

    :param body: Category and User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://recommandation:8080/getFoodbyCategory'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_restaurant(body):  # noqa: E501
    """return selected restaurant detail

     # noqa: E501

    :param body: restaurant
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://datalookup:8080/getRestaurant'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_restaurant_history(body):  # noqa: E501
    """return restaurant list that the target user selected

     # noqa: E501

    :param body: User Information
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://usermanagement:8080/getRestaurantHistory'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_restaurantby_default(body):  # noqa: E501
    """return restaurant list by user info

     # noqa: E501

    :param body: User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://recommandation:8080/getRestaurantbyDefault'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_restaurantby_food(body):  # noqa: E501
    """return restaurant list by food and user

     # noqa: E501

    :param body: Food and User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://recommandation:8080/getRestaurantbyFood'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_restaurantby_keyword(body):  # noqa: E501
    """return restaurant list by keyword and user info

     # noqa: E501

    :param body: Keyword and User Info
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://recommandation:8080/getRestaurantbyKeyword'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)


def get_restaurants(body):  # noqa: E501
    """return restaurant list by keyword

     # noqa: E501

    :param body: Keyword
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        url = 'http://datalookup:8080/getRestaurants'
        myobj = connexion.request.get_json()
        x = requests.post(url, json = myobj)        
    return json.loads(x.text)

def get_user_info(body):
    """return restaurant list by keyword

     # noqa: E501

    :param body: Keyword
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        # body = connexion.request.get_json()  # noqa: E501
        Users = Userinfo.objects(name="Guest")
        if len(Users) < 1:
            User = Userinfo(name="Guest",
                restaurantlist=[],
                foodlist=[])
            User.save() 
        User = Userinfo.objects(name="Guest").first()


    return User.to_json()