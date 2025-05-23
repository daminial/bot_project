from screens.base import Bot
from screens.base import DEFAULT_STATE

from screens import (
    HelloScreen,
    StartScreen,
    AdvScreen,
    ContactScreen,
    BusesScreen,
    SelectedRoutes,
)

def create_routes():
    return [
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

def main():
    routes = create_routes()
    BusesScreen.set_routes(routes)
    
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
                SelectedRoutes
            }
        },
        persistence=None
    )
    
    bot.run()

if __name__ == '__main__':
    main()