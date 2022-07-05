from swagger_server.controllers.database_controller import mongodb

class Userinfo(mongodb.Document):
    name = mongodb.StringField()    
    restaurantlist = mongodb.ListField(mongodb.StringField())
    foodlist = mongodb.ListField(mongodb.StringField())    
    def to_json(self):        
        return  {
                    "name": self.name,
                    "restaurantlist": self.restaurantlist,
                    "foodlist": self.foodlist
                }


    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id) 