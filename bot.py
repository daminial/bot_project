from hammett.core import Bot
from hammett.core.constants import DEFAULT_STATE
from config import ROUTE_SCREENS
from screens import (
    HelloScreen,
    StartScreen,
    BusesScreen,
    AdvScreen,
    ContactScreen,
    create_route_screen
)

def create_routes():
    routes_data = [
        {
            'id': '1',
            'name': '№450',
            'path': 'Центральный рынок - село Чалтырь',
            'map_url': 'https://example.com/map1'
        },
        {
            'id': '2',
            'name': '№150',
            'path': 'Центральный рынок - село Дружба',
            'map_url': 'https://example.com/map2'
        }
    ]
    
    for data in routes_data:
        ROUTE_SCREENS.append(create_route_screen(data))

def main():
    create_routes()
    
    bot = Bot(
        'BusRoutesBot',
        entry_point=StartScreen,
        states={
            DEFAULT_STATE: {
                HelloScreen,
                StartScreen,
                BusesScreen,
                AdvScreen,
                ContactScreen,
                *ROUTE_SCREENS
            }
        },
        persistence=None
    )
    
    bot.run()

if __name__ == '__main__':
    main()