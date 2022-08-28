class GameStats():
    """Отслеживание статистики игры"""
    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Инициализирует статистику, меняющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit

        self.game_active = False