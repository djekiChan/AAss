import vk_api
import random
from config_ import *
import requests

def last_post(owner_id, count, offset, filter):
    response = vk_bot_user.method('wall.get',
                                  {'owner_id': owner_id, 'count': count, 'offset': offset, 'filter': filter})

    return response['items'][0]['id']



vk_bot_user = vk_api.VkApi(token=ACCOUNT_TOKEN)



def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0,5000)})

def write_msg_attach(user_id, text, att_url):
    vk_bot.method('messages.send', {'user_id': user_id, 'attachment': att_url, 'message': text, 'random_id': random.randint(0, 5000)})





vk_bot = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print('Готов к работе')
# + str(long_pool))


while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=5000000'.format(server=server,
                                                                      act='a_check',
                                                                      key=key,
                                                                      ts=ts)).json()

    update = long_poll['updates']
    print(long_poll)
    if update[0][0] == 4:
        print(long_poll)
        #print(update)
        user_id = update[0][3]
        user_name = vk_bot.method('users.get', {'user_ids': user_id})
        # write_msg(user_id, 'привет, ' + (user_name[0]['first_name'])) #сообщение пользователю
        if 'Картинк' in update[0][6]:
            write_msg_attach(user_id,
                             'Вот тебе хорошие картинки',
                             'wall-31466113_230927')

        elif 'Скинь годный мемас' in update[0][6]:
            group_id = -45745333
            post_id = last_post(group_id, 1, 1, 'owner')
            attach = 'wall' + str(group_id) + '_' + str(post_id)
            write_msg_attach(user_id, 'Вот тебе мемас', attach)
        else:
            write_msg(user_id, 'Привет, ' + (user_name[0]['first_name']))
        print(str(user_name[0]['first_name']) + ' ' +
              str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6])) #сообщение нам

        #Меняем ts для следущего запроса
    ts = long_poll['ts']








