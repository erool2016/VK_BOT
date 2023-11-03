import psycopg2


DSN = 'postgresql://postgres:qwr1d@localhost:5432/postgres'
conn = psycopg2.connect(database='postgres', user='postgres', password='qwr1d')


class Data_Base:

    def create_table():
        with conn.cursor() as cur:
            cur.execute('''
                    create table if not exists data_user_two(
                        id SERIAL PRIMARY KEY,
                        id_user int unique,
                        name varchar(50),
                        last_name varchar(50)                   

                        );
                '''
                        )
            cur.execute('''
                               create table if not exists viwed_users(
                                   id serial primary key,
                                   id_user int not null references data_user_two(id_user) on delete cascade,
                                   id_viwed_users int
                                   
                               );
                           ''')
            cur.execute('''
                                           create table if not exists viwed_users_liked(
                                               id serial primary key,
                                               id_user int not null references data_user_two(id_user) on delete cascade,
                                               user_id_liked int ,
                                               url varchar(300)
                                           );
                                       ''')
            conn.commit()
            print('создана таблица data_user_two, viwed_users , viwed_users_liked')

    def save_data_user_two(id_user,name,last_name):
        if check_user(id_user) != False:

            return
        else:
            with conn.cursor() as cur:
                cur.execute('''
                                  insert into data_user_two(id_user,name,last_name)
                                  values(%s,%s,%s); 

                              ''', (id_user,name,last_name))
                conn.commit()
                print(f'данные{id_user}{name}{last_name} внесены')
    def save_viwed_users(id_user,id):
        print('save viwed user')
        if check_user_viwed(id) != False:
            print('есть в просмотренных')
            return
        else:
            with conn.cursor() as cur:
                cur.execute('''
                                  insert into viwed_users(id_user,id_viwed_users)
                                  values(%s,%s); 

                              ''', (id_user,id))
                conn.commit()
                print(f'данные user_id {id_user} viwed_user_id{id} внесены в viwed_users')


    def save_viwed_users_liked(id_user,id,url):
        if check_user_liked(id) != False:

            return
        else:

            with conn.cursor() as cur:
                cur.execute('''
                                  insert into viwed_users_liked(id_user,user_id_liked,url)
                                  values(%s,%s,%s); 

                              ''', (id_user,id,url,))
                conn.commit()
                print(f'данные{id_user}просмотренного {id} url {url} внесены в viwed_users_liked')
    def drop_table():
        with conn.cursor() as cur:
            cur.execute('''
                            drop table viwed_users_liked
                        ''')
            cur.execute('''
                drop table viwed_users
            ''')
            cur.execute('''
                drop table data_user_two
            ''')
            conn.commit()
            print('удалена таблица data_user_two, viwed_users ,viwed_users_liked')
def check_user(id):
    with conn.cursor() as cur:
        cur.execute('''
             select * from data_user_two where id_user = %s
          ''', (id,))
        answer = cur.fetchone()
        print(answer)
        if answer:
           print('есть такой пользователь')
           return True
        else:
            return False

def check_user_viwed(id):
    with conn.cursor() as cur:
        cur.execute('''
             select * from viwed_users where id_viwed_users = %s
          ''', (id,))
        answer = cur.fetchone()
        print(answer)
        if answer:
           # print('есть такой пользователь  в просмотренных')
           return True
        else:
            return False
def check_user_liked(id_user):
    with conn.cursor() as cur:
        cur.execute('''
             select * from viwed_users_liked where id_user = %s
          ''', (id_user,))
        answer = cur.fetchone()
        print(answer)
        if answer:
           print(f'лайк пользователю {id_user} стоит')
           return True
        else:
            return False




    # def save_tabel_data(id_user,name,last_name):
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                               insert into data_user_two(id_user,name,last_name)
    #                               values(%s,%s,%s);
    #
    #                           ''', (id_user,name,last_name))
    #         conn.commit()
    #         print('данные data_user_two внесены')
    # def check_user_data_user_two(id):
    #     '''Проверка наличия user_id'''
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                     select * from data_user_two where id_user = %s
    #                 ''', (id,))
    #         answer = cur.fetchone()
    #         if answer:
    #             return True
    #         else:
    #             return False
    # def create_table_viwed():
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                 create table if not exists viwed_user(
    #                     id serial primary key,
    #                     id_user int not null references data_user_two(id_user) on delete cascade,
    #                     name varchar(50),
    #                     last_name varchar(50),
    #                     id_foto_user int
    #
    #                     );
    #             '''
    #                     )
    #         conn.commit()
    #         print('создана таблица viwed_user')
    #
    # def save_tabel_viwed(id_user,name,last_name,id_foto_user):
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                               insert into viwed_user(id_user,name,last_name,id_foto_user)
    #                               values(%s,%s,%s,%s);
    #
    #                           ''', (id_user,name,last_name,id_foto_user))
    #         conn.commit()
    #         print('данные data_user_two внесены')
    # def create_table_viwed_liked():
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                 create table if not exists viwed_user_liked(
    #                     id serial primary key,
    #                     id_user int not null references data_user_two(id) on delete cascade,
    #                     name varchar(50),
    #                     last_name varchar(50),
    #                     id_foto_user int not null,
    #                     url VARCHAR(255) NOT NULL
    #
    #                     );
    #             '''
    #                     )
    #         conn.commit()
    #         print('создана таблица viwed_user_liked')
    # def save_tabel_viwed_liked(id_user,name,last_name,id_foto_user,url):
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                               insert into viwed_user_liked(id_user,name,last_name,id_foto_user,url)
    #                               values(%s,%s,%s,%s,%s);
    #
    #                           ''', (id_user,name,last_name,id_foto_user,url))
    #         conn.commit()
    #         print('данные data_user_two внесены')
    #
    # def drop_table():
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                             drop table data_user_two;
    #
    #                         '''
    #                     )
    #     conn.commit()
    #     print('удалена таблица data_user two')
    #
    # def drop_table_viwed_user():
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                             drop table viwed_user;
    #
    #                         '''
    #                     )
    #     conn.commit()
    #     print('удалена таблица data_user two')
    # def drop_table_viwed_user_liked():
    #     with conn.cursor() as cur:
    #         cur.execute('''
    #                             drop table viwed_user_liked;
    #
    #                         '''
    #                     )
    #     conn.commit()
    #     print('удалена таблица data_user two')


    # def check_user( id: int)-> bool:
    #     with conn.cursor() as cur:
    #         cur.execute(f'''
    #             select * from data_user_two where id_user = %s;
    #             ''', (id,))
    #         resp = cur.fetchone()
    #         print('resp', resp)
    #         if resp:
    #             return True
    #         else:
    #             return False