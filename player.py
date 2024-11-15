import keyboard,maps,items,random
class Player:
    def __init__(self):
        self.health = 100
        self.hunger = 100
        self.money = 1111110
        self.search = 0
        self.position = (13, 2)
        self.last_position = self.position  # Отслеживание предыдущей позиции
        self.last_object = None  # Объект на предыдущей позиции
        self.weapons = ['Кулак', 'Пусто', 'Пусто', 'Пусто', 'Пусто', 'Пусто']
        self.inventory = ['Пусто', 'Пусто', 'Пусто','Пусто', 'Пусто', 'Пусто']
        self.action_weapons = 0
        self.action_inventory = 0
        self.hint1 = ''
        self.hint2 = ''
        self.hint3 = ''
        self.hint4 = ''
        self.business_restaurant = False
        self.business_stall = False
        self.profit_business_restaurant = 0
        self.profit_business_stall = 0

    def show_inventory(self, items):
        s = ''
        for i in items:
            s = s + '|' + f'{i} '
        return s

    def add_weapon(self, item):
        for i in range(len(self.weapons)):
            if self.weapons[i] == 'Пусто':
                self.weapons[i] = item
                return
        self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
        self.hint1="Инвентарь полон!"

    def add_inventory(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == 'Пусто':
                self.inventory[i] = item
                return
        self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
        self.hint1 = "Инвентарь полон!"

    def print_action_weapon(self):
        s = ''
        for i in range(len(self.weapons)):
            if i == self.action_weapons:
                s = s +'|'+ f"\033[38;5;196m{self.weapons[i]}\033[0m"
            else:
                s = s +'|'+ self.weapons[i]
        return s

    def print_action_inventory(self):
        s = ''
        for i in range(len(self.inventory)):
            if i == self.action_inventory:
                s = s +'|'+ f"\033[38;5;196m{self.inventory[i]}\033[0m"
            else:
                s = s +'|'+ self.inventory[i]
        return s

    def remove_inventory(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                self.inventory[i] = 'Пусто'
                return
        self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
        self.hint1 = "У вас нет этого предмета"



    def keyboard_action(self, game_map=maps.main_map):
        x, y = self.position
        new_x, new_y = x, y  # Создаем переменные для новой позиции

        # Обрабатываем перемещение и проверяем границы
        if keyboard.is_pressed('w') and y > 0:
            new_y -= 1
        elif keyboard.is_pressed('a') and x > 0:
            new_x -= 1
        elif keyboard.is_pressed('s') and y < 13:
            new_y += 1
        elif keyboard.is_pressed('d') and x < 14:
            new_x += 1
        elif keyboard.is_pressed('e') and self.action_weapons + 1 != 5 and self.weapons[self.action_weapons + 1] != 'Пусто':
            self.action_weapons = self.action_weapons + 1
        elif keyboard.is_pressed('q') and self.action_weapons - 1 != -1 and self.weapons[self.action_weapons - 1] != 'Пусто':
            self.action_weapons = self.action_weapons - 1

        elif keyboard.is_pressed('y') and self.action_inventory + 1 != 5 :
            self.action_inventory = self.action_inventory + 1
        elif keyboard.is_pressed('t') and self.action_inventory - 1 != -1:
            self.action_inventory = self.action_inventory - 1


        if keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['medical']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            need_hp = 100-self.health
            need_money = need_hp*0.5
            if self.money < need_money:
                self.hint1 = f'У вас недостаточно денег. Необходимо {need_money}$'
            else:
                self.health = 100
                self.hint1 = f'Вы вылечились за {need_money}$'
                self.money = self.money - need_money

        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['job']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            self.add_inventory(item='Ящик')

        elif keyboard.is_pressed('g') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['job']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if 'Пусто'  in self.inventory and self.money >= items.price_item['Материалы']['price']:
                self.hint1 = 'Вы купили материал'
                self.money = self.money - items.price_item['Материалы']['price']
                self.add_inventory(item='Материал')



        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['industrial']:
            if 'Материал' in self.inventory:
                self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
                self.remove_inventory(item='Материал')
                self.money = self.money + 30.78
                self.hint1 = 'Вы продали материал и получили 30.78$'
            else:
                self.hint1 = 'Проваливай! И без материалов не возвращайся'

        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['port']:
            if 'Ящик' in self.inventory:
                self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
                self.remove_inventory(item='Ящик')
                self.money = self.money + 14.23
                self.hint1 = 'Вы продали ящик и получили 14.23$'
            else:
                self.hint1 = 'Проваливай! И без ящиков не возвращайся'

        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['home']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= 30000:
                maps.two_main_map[self.position] = maps.obj_build['bought_home']
                self.money = self.money - 30000
                self.hint1 = 'Вы купили дом!'
            else:
                self.hint1 = 'У вас недостаточно денег'

        elif keyboard.is_pressed('1') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['weapons_store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.weapons['Нож']['price']:
                if 'Нож' in self.weapons:
                    self.hint1 = 'У вас уже есть это оружие'
                else:
                    self.add_weapon(item='Нож')
                    self.money = self.money - items.weapons['Нож']['price']
                    self.hint1 = f'Вы купили нож за {items.weapons['Нож']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.weapons['Нож']['price']}$'


        elif keyboard.is_pressed('F') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['casino']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money < 50:
                self.hint1 = 'У вас недостаточно денег'
            else:
                win = random.choice([1,2,3,0,0,0,0,0,0,0])
                if  win == 1:
                    self.money = self.money + 150
                    self.hint1 = 'Вы выиграли 150$'
                elif win == 2:
                    self.money = self.money + 100
                    self.hint1 = 'Вы выиграли 100$'
                elif win == 3:
                    self.money = self.money + 75
                    self.hint1 = 'Вы выиграли 75$'
                else:
                    self.hint1 = 'Вы проиграли 50$'
                    self.money = self.money - 50




        elif keyboard.is_pressed('2') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['weapons_store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.weapons['Топор']['price']:
                if 'Топор' in self.weapons:
                    self.hint1 = 'У вас уже есть это оружие'
                else:
                    self.add_weapon(item='Топор')
                    self.money = self.money - items.weapons['Топор']['price']
                    self.hint1 = f'Вы купили топор за {items.weapons['Топор']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.weapons['Топор']['price']}$'

        elif keyboard.is_pressed('3') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['weapons_store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.weapons['Glock-18']['price']:
                if 'Glock-18' in self.weapons:
                    self.hint1 = 'У вас уже есть это оружие'
                else:
                    self.add_weapon(item='Glock-18')
                    self.money = self.money - items.weapons['Glock-18']['price']
                    self.hint1 = f'Вы купили Glock-18 за {items.weapons['Glock-18']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.weapons['Glock-18']['price']}$'

        elif keyboard.is_pressed('4') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['weapons_store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.weapons['UZI']['price']:
                if 'UZI' in self.weapons:
                    self.hint1 = 'У вас уже есть это оружие'
                else:
                    self.add_weapon(item='UZI')
                    self.money = self.money - items.weapons['UZI']['price']
                    self.hint1 = f'Вы купили UZI за {items.weapons['UZI']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.weapons['UZI']['price']}$'



        elif keyboard.is_pressed('1') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['food']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.food['Картошка фри']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Картошка фри')
                    self.money = self.money - items.food['Картошка фри']['price']
                    self.hint1 = f'Вы купили картошку фри за {items.food['Картошка фри']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.food['Картошка фри']['price']}$'


        elif keyboard.is_pressed('2') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['food']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.food['Снэк Бокс']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Снэк Бокс')
                    self.money = self.money - items.food['Снэк Бокс']['price']
                    self.hint1 = f'Вы купили снэк бокс за {items.food['Снэк Бокс']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.food['Снэк Бокс']['price']}$'

        elif keyboard.is_pressed('3') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['food']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.food['Комбо']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Комбо')
                    self.money = self.money - items.food['Комбо']['price']
                    self.hint1 = f'Вы купили комбо за {items.food['Комбо']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.food['Комбо']['price']}$'


        elif keyboard.is_pressed('4') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['food']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.food['Большое комбо']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Большое комбо')
                    self.money = self.money - items.food['Большое комбо']['price']
                    self.hint1 = f'Вы купили большое комбо за {items.food['Большое комбо']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.food['Большое комбо']['price']}$'



        elif keyboard.is_pressed('1') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.health_item['Сигарета']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Сигарета')
                    self.money = self.money - items.health_item['Сигарета']['price']
                    self.hint1 = f'Вы купили сигарету за {items.health_item['Сигарета']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.health_item['Сигарета']['price']}$'

        elif keyboard.is_pressed('2') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.food['Чипсы']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Чипсы')
                    self.money = self.money - items.food['Чипсы']['price']
                    self.hint1 = f'Вы купили чипсы за {items.food['Чипсы']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.food['Чипсы']['price']}$'

        elif keyboard.is_pressed('3') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['store']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.food['Газировка']['price'] and 'Пусто' in self.inventory:
                    self.add_inventory(item='Газировка')
                    self.money = self.money - items.food['Газировка']['price']
                    self.hint1 = f'Вы купили газировку за {items.food['Газировка']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.food['Газировка']['price']}$'

        elif keyboard.is_pressed('g') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['medical']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= items.health_item['Аптечка']['price']and 'Пусто' in self.inventory:
                    self.add_inventory(item='Аптечка')
                    self.money = self.money - items.health_item['Аптечка']['price']
                    self.hint1 = f'Вы купили аптечку за {items.health_item['Аптечка']['price']}$'
            else:
                self.hint1 = f'Недостаточно денег. Необходимо {items.health_item['Аптечка']['price']}$'


        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['business_restaurant']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= 35000:
                maps.two_main_map[self.position] = maps.obj_build['business_restaurant_bought']
                self.money = self.money - 35000
                self.business_restaurant = True
                self.hint1 = 'Вы купили ресторан'
            else:
                self.hint1 = 'У вас недостаточно денег'


        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['business_stall']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            if self.money >= 2000:
                maps.two_main_map[self.position] = maps.obj_build['business_stall_bought']
                self.money = self.money - 2000
                self.business_stall = True
                self.hint1 = 'Вы купили ларек'
            else:
                self.hint1 = 'У вас недостаточно денег'



        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['business_restaurant_bought']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            self.hint1 = f'Вы собрали прибыль в {round(self.profit_business_restaurant,2)}$'
            self.money = self.money + self.profit_business_restaurant
            self.profit_business_restaurant = 0

        elif keyboard.is_pressed('f') and maps.two_main_map.get((x, y), maps.obj_build['empty']) == maps.obj_build['business_stall_bought']:
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            self.hint1 = f'Вы собрали прибыль в {round(self.profit_business_stall,2)}$'
            self.money = self.money + self.profit_business_stall
            self.profit_business_stall = 0

        elif keyboard.is_pressed('r') and self.inventory[self.action_inventory] != 'Пусто':
            self.use_item()



        if game_map.get((new_x, new_y)) not in {"\033[38;5;130m#\033[0m", "\033[34m~\033[0m"}:
            self.last_position = self.position
            self.position = (new_x, new_y)


    def use_food(self,item):
        self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
        self.hint1 = f'Вы съели {item}'
        self.remove_inventory(item=item)
        self.hunger = self.hunger + items.food[item]['hunger']
        if self.hunger > 100:
            self.hunger = 100

    def use_health_item(self,item):
        self.remove_inventory(item=item)
        self.health = self.health + items.health_item[item]['health']
        if self.health > 100:
            self.health = 100


    def use_item(self):
        item = self.inventory[self.action_inventory]
        if item in items.food_list:
            self.use_food(item=self.inventory[self.action_inventory])
        elif item in items.health_item_list:
            self.use_health_item(item=self.inventory[self.action_inventory])
