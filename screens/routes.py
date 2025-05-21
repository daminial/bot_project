from .base import Screen, Button, SourceTypes
from config import BUSES_SCREEN_DESCRIPTION

def create_route_screen(route_data: dict) -> type:
    class RouteScreen(Screen):
        description = f"🚌 Маршрут {route_data['name']},\nСледует пути {route_data['path']}"
        
        async def add_default_keyboard(self, _update, _context):
            from .start import StartScreen
            from .buses import BusesScreen
            return [
                [Button(
                    '🗺 Посмотреть на карте',
                    route_data['map_url'],
                    source_type=SourceTypes.URL_SOURCE_TYPE
                )],
                [
                    Button(
                        '⬅️ Назад к маршрутам',
                        BusesScreen,
                        source_type=SourceTypes.MOVE_SOURCE_TYPE
                    ),
                    Button(
                        '🏠 На главную',
                        StartScreen,
                        source_type=SourceTypes.MOVE_SOURCE_TYPE
                    )
                ]
            ]
    
    RouteScreen.__name__ = f"Route_{route_data['id']}"
    RouteScreen.route_data = route_data 
    return RouteScreen