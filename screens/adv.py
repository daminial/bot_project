from .base import Screen, Button, SourceTypes
from config import ADV_SCREEN_DESCRIPTION


class AdvScreen(Screen):
    """The class implements AdvScreen, which is always sent as a new message."""

    description = ADV_SCREEN_DESCRIPTION

    async def add_default_keyboard(self, _update, _context):
        from .start import StartScreen
        """Set up the default keyboard for the screen."""
        return [[
            Button(
                '⬅️ Back',
                StartScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE,
            ),
        ]]