
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import bot_token
from random import randrange

class LongPoll_session:
    def __init__(self, token_, bot_token):
        self.token = token_
        self.bot_token = bot_token
    # @time_decorator
    def session_longpoll(self):
        '''получаем ответ в чате бота'''
        vk = vk_api.VkApi(token=self.bot_token)

        longpoll = VkLongPoll(vk)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                user_id = event.user_id
                # self.write_msg(user_id, f"Хай, {event.user_id}")
                request_user  = event.text.lower()

                return request_user,user_id

    # @time_decorator
def write_msg(user_id, message, attachment=None,keyboard=None):
        vk = vk_api.VkApi(token=bot_token)

        post = {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), 'attachment': attachment}
        if keyboard:
            post['keyboard'] = keyboard.get_keyboard()
        else:
            post = post
        vk.method('messages.send', post)

def find_users(data_user_for_find:dict)->dict:
    '''Поиски подходящих вариантов'''
    bdate = data_user_for_find['bdate'].split('.')
    from config import token_,bot_token
    vk2 = vk_api.VkApi(token=token_)

    resp = vk2.method('users.search', {
        #'age_from' : int(n[2]) - 3, вот здесь я так и не понял почему - но если раскоментировать строку - все падает
        'age_to' : int(bdate[2]) + 3,
        'sex': data_user_for_find['sex'],
        'city': data_user_for_find['city'],
        'fields': 'bdate,sex,photo_id,about,city,relation,inerests,domain',
        'status': 6,
        'count': 25,
        'has_photo': 1,
        'v': 5.131
    })
    return resp

