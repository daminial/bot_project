from .base import Screen, Button, SourceTypes
from config import CONTACT_SCREEN_DESCRIPTION

class ContactScreen(Screen):
    """The class implements ContactScreen, which is always sent as a new message."""

    description = CONTACT_SCREEN_DESCRIPTION

    async def add_default_keyboard(self, _update, _context):
        from .start import StartScreen
        """Set up the default keyboard for the screen."""
        return [[
            Button(
                '🏠 На главную',
                StartScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE,
            ),
        ]]
