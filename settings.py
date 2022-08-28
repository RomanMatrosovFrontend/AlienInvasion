class Settings():
    """Класс для хранения настроек игры Aliens Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (120, 230, 130)

        # Скорость корабля
        self.ship_speed = 1.5
        # Стартовое кол-во жизней корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 60, 60)
        self.bullets_allowed = 3

        # Параметры пришельца
        self.alien_speed = 0.1
        self.fleet_drop_speed = 80
        # Направление (1 - вправо, -1 - влево)
        self.fleet_direction = 1