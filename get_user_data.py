import vk_api
from config import token_
vk2 = vk_api.VkApi(token=token_)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def start_find_data_user(self):
        '''получаем информацию о пользователе и заносим в словарь, возвращаем словарь'''
        data_user_for_find = {}  # словарь с данными для поиска id , sity, sex

        req = vk2.method('users.get',
                             {
                                 'user_id': self.user_id,
                                 'fields': 'first_name,last_name,bdate,city,sex,photo_id,about'
                             }
                             )


        data_user_for_find['bdate']=req[0]['bdate']
        data_user_for_find['city'] = req[0]['city']['id']
        data_user_for_find['sex'] = self.change_sex(req[0]['sex']) #req[0]['sex']
        data_user_for_find['first_name'] = req[0]['first_name']
        data_user_for_find['last_name'] = req[0]['last_name']
        #print('user data',data_user_for_find)

        return data_user_for_find
    # @time_decorator
    def change_sex(self, sex):
        # print('sex',sex)
        if sex == 1:
            return 2
        else:
            return 1