import maps, os, time,items
import keyboard
from player import Player

pl = Player()

class Game:
    def __init__(self):
        self.cursor_position = 0
        self.running = True
        self.width = 15
        self.height = 14
        self.main_map = maps.main_map
        self.tick = 0

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_main_menu(self):
        menu = ['Новая игра     ', 'Загрузить игру ', 'Обучение       ']
        print('╔═════════════════ By Fire and Blood ══════════════════╗')
        for count, item in enumerate(menu):
            if self.cursor_position == count:
                print(f'║> {item}                                     ║')
            else:
                print(f'║  {item}                                     ║')
        print('╚══════════════════════════════════════════════════════╝')

    def help(self):
        self.clean()  # Очищаем экран один раз перед отображением обучения
        print('╔═══════════════ By Fire and Blood ═══════════════╗')
        print('║ W, A, S, D - Перемещение                        ║')
        print('║ Q, E - Переключение оружия                      ║')
        print('║ T, Y - Переключение предмета инвентаря          ║')
        print('║ F, G - Взаимодействие                           ║')
        print('║ R - Использовать предмет из инвентаря           ║')
        print('║ ↓, ↑ - Перемещение курсора в меню               ║')
        print('║ Enter - Выбор в меню                            ║')
        print('╚═════════════════════════════════════════════════╝')
        print('Для выхода в главное меню нажмите esc.............')

        # Ожидание нажатия 'esc' для выхода в главное меню
        while not self.running:
            if keyboard.is_pressed('esc'):
                self.running = True
                break
            time.sleep(0.2)

    def load_game(self):
        pass


    def action_in_main_menu(self):
        # Проверка клавиш и изменение позиции курсора
        if keyboard.is_pressed('up') and self.cursor_position > 0:
            self.cursor_position -= 1
            self.clean()
            self.print_main_menu()
        elif keyboard.is_pressed('down') and self.cursor_position < 2:
            self.cursor_position += 1
            self.clean()
            self.print_main_menu()
        elif keyboard.is_pressed('enter'):
            if self.cursor_position == 0:
                self.game()
            elif self.cursor_position == 1:
                self.load_game()
            elif self.cursor_position == 2:
                self.running = False
                self.help()
            self.clean()
            self.print_main_menu()

    def main_menu(self):
        self.clean()
        self.print_main_menu()
        while self.running:
            self.action_in_main_menu()
            time.sleep(0.1)

    def bar(self,current, maximum, length, fill_char, empty_char):
        progress_ratio = current / maximum
        filled_length = int(length * progress_ratio)
        bar = fill_char * filled_length + empty_char * (length - filled_length)
        return f"{bar} {current}/{maximum}"

    def hunger(self):
        pl.hunger = pl.hunger - 1

    def exhaustion(self):
        if pl.hunger == 0:
            pl.health = pl.health - 1

    def business_restaurant (self):
        if pl.business_restaurant == True:
            pl.profit_business_restaurant = pl.profit_business_restaurant + 0.7

    def business_stall (self):
        if pl.business_stall == True:
            pl.profit_business_stall = pl.profit_business_stall + 0.15




    def death(self):
        if pl.health == 0:
            pl.health = 50
            pl.hunger = 50
            pl.position = (1, 3)
            self.hint1, self.hint2, self.hint3, self.hint4 = '', ' ', ' ', ' '
            pl.hint1 = 'Потрачено'
            pl.money = pl.money - pl.money / 100

    def time_event(self):
        if self.tick % 6 == 0 and pl.hunger != 0:
            self.hunger()
        elif self.tick % 5 == 0 and pl.health != 0:
            self.exhaustion()
        elif self.tick % 1 == 0:
            self.business_restaurant()
            self.business_stall()
        self.death()

    def display_sparse_map(self, side_text=None):
        side_text = side_text or [""] * self.height
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (x, y) in self.main_map:
                    row.append(self.main_map[(x, y)])
                else:
                    row.append(maps.obj_build['empty'])
            text = side_text[y] if y < len(side_text) else ""
            print('  '.join(row) + "  " + text)







    def information_obj(self,position):
        obj = maps.two_main_map.get(pl.position)

        if obj == maps.obj_build['home']:
            return 'Незанятый дом. Для покупки нажмите F. Цена 30000$'
        elif obj == maps.obj_build['bought_home']:
            return 'Ваш дом. Нажмите F для сохранения игры.'
        elif obj == maps.obj_build['medical']:
            return 'Больница. Для того что бы вылечится нажмите F. Для того что бы купить аптечку нажмите G.'
        elif obj == maps.obj_build['port']:
            return 'Порт. Для того что бы продать ящик за 14.23$ нажмите F.'
        elif obj == maps.obj_build['industrial']:
            return 'Завод. Для того что бы продать материал за 30.78$ нажмите F.'
        elif obj == maps.obj_build['food']:
            return 'Закусочная. 1.Картошка фри 2.Снэк Бокс 3.Комбо 4.Большое комбо. Для покупки нажмите цифру'
        elif obj == maps.obj_build['job']:
            return 'Работа. Для того что бы взять ящик нажмите F. Для того что бы купить материал нажмите G.'
        elif obj == maps.obj_build['weapons_store']:
            return 'Магазин оружия. 1.Нож 2.Топор 3.Glock-18 4.UZI Для покупки нажмите цифру'
        elif obj == maps.obj_build['store']:
            return 'Магазин. 1.Сигарета 2.Чипсы 3.Газировка. Для покупки нажмите цифру'
        elif obj == maps.obj_build['casino']:
            return 'Казино. Нажмите F что бы сыграть на 50$'
        elif obj == maps.obj_build['business_restaurant']:
            return 'Ресторан. Бизнес который вы можете купить. Цена 35000$. Нажмите F для покупки'
        elif obj == maps.obj_build['business_stall']:
            return 'Ларек. Бизнес который вы можете купить. Цена 2000$. Нажмите F для покупки'

        elif obj == maps.obj_build['business_restaurant_bought']:
            return f'Прибыль ресторана {round(pl.profit_business_restaurant,2)}$ Нажмите F для сбора прибыли'
        elif obj == maps.obj_build['business_stall_bought']:
            return f'Прибыль ларька {round(pl.profit_business_stall, 2)}$ Нажмите F для сбора прибыли'
        else:
            return ''



    def game(self):
        while True:
            time.sleep(0.05)
            self.clean()
            pl.keyboard_action(self.main_map)
            if pl.last_object is not None:
                self.main_map[pl.last_position] = pl.last_object
            pl.last_object = self.main_map.get(pl.position, maps.obj_build['empty'])
            self.main_map[pl.position] = maps.obj_build['player']
            side_text = [
                f"Здоровье:  {self.bar(current=pl.health, maximum=100, length=10, fill_char='\033[38;5;196m─\033[0m', empty_char=' ')}",
                f'Пища:      {self.bar(current=pl.hunger, maximum=100, length=10, fill_char='\033[38;5;130m─\033[0m', empty_char=' ')}',
                f"Деньги:    \033[32m{round(pl.money, 2)}$\033[0m",
                f"Розыск:    {self.bar(current=pl.search, maximum=5, length=5, fill_char='\033[38;5;220m*\033[0m', empty_char='\033[90m*\033[0m')}",
                f"Оружие:   {pl.print_action_weapon()}",
                f'Инвентарь:{pl.print_action_inventory()}',
                f'{self.information_obj(position=pl.position)}',
                f"{pl.hint1}",
                f"{pl.hint2}",
                f"{pl.hint3}",
                f"{pl.hint4}",
                f"{self.tick // 300}",
                f'{self.tick}'
            ]
            self.tick = self.tick + 1
            self.time_event()
            self.display_sparse_map(side_text)






