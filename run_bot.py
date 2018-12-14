import vk_api
import random
from config_ import *
import requests
from errors import *
from opr import *

def last_post(owner_id, count, offset, filter):
    response = vk_bot_user.method('wall.get',
                                  {'owner_id': owner_id, 'count': count, 'offset': offset, 'filter': filter})

    return response['items'][0]['id']



vk_bot_user = vk_api.VkApi(token=ACCOUNT_TOKEN)



def write_msg(user_id, text):
    vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 5000)})

def write_msg_attach(user_id, text, att_url):
    vk_bot.method('messages.send', {'user_id': user_id, 'attachment': att_url, 'message': text, 'random_id': random.randint(0, 5000)})





vk_bot = vk_api.VkApi(token=ACCESS_TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print('Готов к работе')
# + str(long_pool))


while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=99999999'.format(server=server,
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
        if 'команды' in update[0][6]:
            comand = '"ошибка" - рассказать об ошибке.\n' \
                     '\n' \
                     '"операторы и функции(операт)" - расскажет об том, что тебе не понятно.\n' \
                     '\n' \
                     '"мем" - скину годный мемас' \
                     '\n' \
                     'P.S.Пока что, я знаю только "Pascal", но в дальнейшем я буду умнее)\n' \
                     '\n' \
                     '"музон" - скину музычки\n' \
                     '\n' \
                     'Пример ошибок:\n' \
                     'Вы: Unknown identifier\n' \
                     'Я: Unknown identifier -  Неизвестный идентификатор\n'
            write_msg(user_id, comand)

            if 'ошиб' in update[0][6]:                   #тут ошибки перечисляются
                write_msg(user_id, 'Отправь мне ошибку.')

                if 'Disk full' in update[0][6]:
                    write_msg(user_id, (errors[14]))
                if 'Out of memory' in update[0][6]:
                    write_msg(user_id, (errors[0]))
                if 'Identifier expected' in update[0][6]:
                    write_msg(user_id, (errors[1]))
                if 'Unknown identifier' in update[0][6]:
                    write_msg(user_id, (errors[2]))
                if 'Duplicate identifier' in update[0][6]:
                    write_msg(user_id, (errors[3]))
                if 'Syntax error' in update[0][6]:
                    write_msg(user_id, (errors[4]))
                if 'Error in real constant' in update[0][6]:
                    write_msg(user_id, (errors[5]))
                if 'Error in integer constant' in update[0][6]:
                    write_msg(user_id, (errors[6]))
                if 'String constant exceeds line' in update[0][6]:
                    write_msg(user_id, (errors[7]))
                if 'Unexpected end of file' in update[0][6]:
                    write_msg(user_id, (errors[8]))
                if 'Line too long' in update[0][6]:
                    write_msg(user_id, (errors[9]))
                if 'Type identifier expected' in update[0][6]:
                    write_msg(user_id, (errors[10]))
                if 'Too many open files' in update[0][6]:
                    write_msg(user_id, (errors[11]))
                if 'Invalid file name' in update:
                    write_msg(user_id, (errors[12]))
                if 'File not found' in update[0][6]:
                    write_msg(user_id, (errors[13]))
                if 'Invalid compiler directive' in update[0][6]:
                    write_msg(user_id, (errors[17]))
                if 'Too many files' in update[0][6]:
                    write_msg(user_id, (errors[16]))
                if 'Undefined type in pointer def' in update[0][6]:
                    write_msg(user_id, (errors[15]))
                if 'Error in type' in update[0][6]:
                    write_msg(user_id, (errors[18]))
                if 'BEGIN expected' in update[0][6]:
                    write_msg(user_id, (errors[19]))
                if 'END expected' in update[0][6]:
                    write_msg(user_id, (errors[20]))
                if 'Division by zero' in update[0][6]:
                    write_msg(user_id, (errors[21]))
            # if ' ";" expected ' in update[0][6]:
            #     write_msg(user_id, (errors[22]))
            # if ' ":" expected ' in update[0][6]:
            #     write_msg(user_id, (errors[23]))
            # if ' "," expected ' in update[0][6]:
            #     write_msg(user_id, (errors[24]))
            # if ' "(" expected ' in update[0][6]:
            #     write_msg(user_id, (errors[25]))
            # if ' ")" expected ' in update[0][6]:
            #     write_msg(user_id, (errors[26]))            Не работает/ don`t working
            # if ' "=" expected ' in update[0][6]:
            #     write_msg(user_id, (errors[27]))
            # if ' ":=" expected ' in update[0][6]:
            #     write_msg(user_id, (errors[28]))
            # if ' "[" or "(." expected ' in update:
            #     write_msg(user_id, (errors[29]))
            # if ' "]" or ".)" expected ' in update:
            #     write_msg(user_id, (errors[30]))
            # if ' "." expected ' in update:
            #     write_msg(user_id, (errors[31]))
            # if  "'..' expected" in update:
            #      write_msg(user_id, (errors[31]))
                if 'No enclosing For, While or Repeat statement' in update[0][6]:
                    write_msg(user_id, (errors[32]))

            if 'операт' in update[0][6]:
                op = "writeln - оператор вывода данных.\n" \
                    "\n" \
                    "readln - оператор ввода данных с клавиатуры.\n" \
                    "\n" \
                    ":= - оператор присваивания\n" \
                    "\n" \
                    "var - переменная\n" \
                    "\n" \
                    "program - названия программы\n" \
                    "\n" \
                    "abs - функция модуля\n" \
                    "\n" \
                    "sqr - функция возведения в квадрат\n" \
                    "\n" \
                    "sqrt - функция извлечений квадратного корня\n" \
                    "\n" \
                    "Sin - функция нахождения синуса числа\n" \
                    "\n" \
                    "Cos - функция нахождения косинуса числа\n" \
                    "\n" \
                    "Exp - возведение числа в определенную степень\n" \
                    "\n" \
                    "Pi - нахождения числа pi\n" \
                    "\n" \
                    "And, or, not - логические операции\n" \
                    "\n"
                write_msg(user_id, op)

            if 'мем' in update[0][6]:
                if random.randint(0, 10) > 1:
                    group_id = -45745333
                    post_id = last_post(group_id, 1, 1, 'owner')
                    attach = 'wall' + str(group_id) + '_' + str(post_id)
                    write_msg_attach(user_id, 'Вот тебе годный мемас', attach)
                elif random.randint(0, 10) > 5:
                    group_id = -172949311
                    post_id = last_post(group_id, 1, 1, 'owner')
                    attach = 'wall' + str(group_id) + '_' + str(post_id)
                    write_msg_attach(user_id, 'Вот тебе годный мемас', attach)
                elif random.randint(0, 10) < 10:
                    group_id = -112996378
                    post_id = last_post(group_id, 1, 1, 'owner')
                    attach = 'wall' + str(group_id) + '_' + str(post_id)
                    write_msg_attach(user_id, 'Вот тебе годный мемас', attach)


            if 'муз' in update[0][6]:

                if random.randint(0, 70) > 1:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[0]))
                elif random.randint(0, 70) >= 8:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[1]))
                elif random.randint(0, 70) >= 4:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[2]))
                elif random.randint(0, 70) >= 6:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[3]))
                elif random.randint(0, 70) >= 9:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[4]))
                elif random.randint(0, 70) >= 17:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[5]))
                elif random.randint(0, 70) >= 36:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[6]))
                elif random.randint(0, 70) >= 45:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[7]))
                elif random.randint(0, 70) >= 69:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[8]))
                elif random.randint(0, 70) >= 30:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[9]))
                elif random.randint(0, 70) >= 14:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[10]))
                elif random.randint(0, 70) >= 58:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[11]))
                elif random.randint(0, 70) >= 42:
                    write_msg_attach(user_id, 'вот тебе музончик', (msc[12]))

            if 'прив' in update[0][6]:
                    write_msg(user_id, 'привет, ' + (user_name[0]['first_name']))

        else:
            write_msg(user_id, 'Ты ввёл что-то не правильно, или я этого не знаю.(попробуй написать с маленькой буквы)')








        print(str(user_name[0]['first_name']) + ' ' +
              str(user_name[0]['last_name']) + ' написал(а) боту - ' + str(update[0][6])) #сообщение нам

        #Меняем ts для следущего запроса
    ts = long_poll['ts']








