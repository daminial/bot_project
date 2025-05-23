from screens.base import Screen, Button, SourceTypes

from config import ADV_SCREEN_DESCRIPTION

import screens.start as start

class AdvScreen(Screen):
    """The class implements AdvScreen, which is always sent as a new message."""

    description = ADV_SCREEN_DESCRIPTION

    async def add_default_keyboard(self, _update, _context):
        """Set up the default keyboard for the screen."""
        return [[
            Button(
                '🏠 На главную',
                start.StartScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE,
            ),
        ]]