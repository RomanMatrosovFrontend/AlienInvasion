class Settings():
    """Класс для хранения настроек игры Aliens Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (120, 230, 130)

        # Стартовое кол-во жизней корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 3

        # Параметры пришельца
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, меняющиеся в ходе игры"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.1

        # Направление (1 - вправо, -1 - влево)
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale