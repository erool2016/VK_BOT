import vk_api
from operator import itemgetter

def create_list(list_):
    result = []

    for item in list_:
        list = []
        if item['is_closed'] == False:
            list.append(item['id'])
            list.append(item['first_name'])
            list.append(item['last_name'])

            result.append(list)
    return result
    # print('create list',result)
def get_foto_likes_list(list_users):
    # print('get foto likes',list_users)
    for item in list_users:
        lists,url = get_user_foto(item[0])
        item.append(sum(lists))
        item.append(url)
    # print('get foto liike',list_users)
    return list_users

def get_user_foto(i):
    '''Принимает список айди  возвращает список списков [ количество лайков,самых популярных id] '''
    list = []
    from config import token_
    vk = vk_api.VkApi(token=token_)
    session = vk_api.VkApi(token=token_)
    response = session.method('photos.get', {
        'owner_id': i,
        'album_id': 'profile',
        'extended': 1,
        'photo_sizes': 1})
    answer = response['items']

    for item in answer:

        list.append(item['likes']['count'])
        url = item['sizes'][0]['url']

    return list,url
def sorted_list(list_:list)->list:
    list_ = (sorted(list_, key=itemgetter(3), reverse=True))
    # print('отсортированный список', list)
    return list_