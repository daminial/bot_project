from .base import StartMixin, Button, SourceTypes
from config import START_SCREEN_DESCRIPTION
from .buses import BusesScreen
from .adv import AdvScreen
from .contacts import ContactScreen

class StartScreen(StartMixin):
    
    description = START_SCREEN_DESCRIPTION
    
    async def add_default_keyboard(self, _update, _context):
        return [
            [Button(
                '🚌 Маршруты автобусов',
                BusesScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE,
            )],
            [Button(
                '📄 Объявления',
                AdvScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            )],
            [Button(
                '📞 Контакты',
                ContactScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            )],
        ]