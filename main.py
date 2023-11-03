
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from lp_session import LongPoll_session,find_users,write_msg
from config import token_,bot_token
from get_user_data import User
from db import Data_Base
from add_pair import create_list,get_foto_likes_list,sorted_list


def start():
    '''Старт '''

    request_user, user_id =LongPoll_session(token_, bot_token).session_longpoll()

    if request_user == 'ы':
        user_dict =User(user_id).start_find_data_user()

        Data_Base.save_data_user_two(user_id,user_dict['first_name'],user_dict['last_name'])

        start_add_pair(user_dict,user_id)
def start_add_pair(user_dict:dict,user_id:int):
    '''Поиск подходящих вариантов и подбор пары'''

    find_resp = find_users(user_dict)['items']

    list_users = create_list(find_resp)

    foto_like_list = get_foto_likes_list(list_users)

    sorted_foto_like_list = sorted_list(foto_like_list)

    prezentation(sorted_foto_like_list,user_id)

def prezentation(list_for_presentation:list,user_id:int):
    '''Вывод результатов пользователю'''

    for item in list_for_presentation:



        write_msg(user_id,message=f'name {item[1]} last name {item[2]} лайков {item[3]} id {item[0]}',attachment=item[4])


        write_msg(user_id, message=f'наберите - далее - для дальнейшего просмотра, или - выход - для нового просмотра, или лайк')

        request,id = LongPoll_session(token_, bot_token).session_longpoll()
        if request == 'далее':
            print(user_id,item[1],item[2],item[0])
            Data_Base.save_viwed_users(user_id,item[0])
            print(request)
            continue
        if request == 'лайк':
            Data_Base.save_viwed_users(user_id,item[0])
            print('item',item)
            Data_Base.save_viwed_users_liked(user_id, item[0], item[4])
            print(request)
            continue

        if request == 'выход':
            print('пока')
            # exit()
            write_msg(user_id,
                      message=f'для начала просмотра наберите ы')
            start()



if __name__ == '__main__':

    # Data_Base.drop_table()
    # Data_Base.drop_table()
    Data_Base.create_table()

    start()
    # print(len('https://sun9-40.userapi.com/impg/H9CD5F2ya_RhufJqho9E0hcOoFe-r7ixHTLctQ/sDh1cWsURJI.jpg?size=56x75&quality=95&sign=413e60bbe1ec615c7254a878aedb7cea&c_uniq_tag=l2JXGQsBAYJmgOV_psX2DlYAQ8ttF9PKHrUSiAuD6dE&type=album'))