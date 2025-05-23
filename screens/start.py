from screens.base import StartMixin, Button, SourceTypes

from config import START_SCREEN_DESCRIPTION

import screens.buses_conf as buses
import screens.adv as adv
import screens.contacts as contacts

class StartScreen(StartMixin):
    
    description = START_SCREEN_DESCRIPTION
    
    async def add_default_keyboard(self, _update, _context):
        return [
            [Button(
                '🚌 Маршруты автобусов',
                buses.BusesScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE,
            )],
            [Button(
                '📄 Объявления',
                adv.AdvScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            )],
            [Button(
                '📞 Контакты',
                contacts.ContactScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            )],
        ]