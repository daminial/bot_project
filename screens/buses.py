from .base import Screen, Button, SourceTypes
from screens.routes import create_route_screen

from config import BUSES_SCREEN_DESCRIPTION
from config import ROUTE_SCREENS

import screens.start as start
class BusesScreen(Screen):
    """Экран со списком маршрутов автобусов"""
    
    description = BUSES_SCREEN_DESCRIPTION
    
    async def add_default_keyboard(self, _update, _context):
        """Создает клавиатуру с кнопками маршрутов"""
        buttons = []
        current_row = []
        
        for i, route_screen in enumerate(ROUTE_SCREENS, 1):
            current_row.append(
                Button(
                    f"🚌 {route_screen.route_data['name']}",
                    route_screen,
                    source_type=SourceTypes.JUMP_SOURCE_TYPE
                )
            )
            
            if i % 3 == 0 or i == len(ROUTE_SCREENS):
                buttons.append(current_row)
                current_row = []

        buttons.append([
            Button(
                '🏠 На главную',
                start.StartScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            )
        ])
        
        return buttons