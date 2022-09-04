class GameStats():
    """Отслеживание статистики игры"""
    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Рекорд не должен сбрасываться
        self.high_score = 0

    
    def reset_stats(self):
        """Инициализирует статистику, меняющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        self.game_active = False