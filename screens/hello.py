from .base import Screen, register_command_handler
from config import HELLO_SCREEN_DESCRIPTION

class HelloScreen(Screen):
    """The class implements HelloScreen.
    """

    description = HELLO_SCREEN_DESCRIPTION

    @register_command_handler('say_hello')
    async def handle_typing_say_hello_command(self, update, context):
        """Send HelloScreen as a response to the /say_hello command."""
        return await self.jump(update, context)
