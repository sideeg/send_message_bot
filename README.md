# Telegram Message Sender Bot

This is a Telegram bot that receives a user ID and a message in the bot chat and sends the message to the specified user ID. The bot uses the `python-telegram-bot` library to handle the communication with Telegram.

## Features

- Start a conversation to send a message.
- Input the user ID.
- Input the message to be sent.
- Send the message to the specified user ID.
- Cancel the operation at any time.

## Prerequisites

- Python 3.7+
- A Telegram bot token from [BotFather](https://core.telegram.org/bots#6-botfather).

## Installation

1. Clone the repository or download the script.

```bash
git clone https://github.com/yourusername/telegram-message-sender-bot.git
cd telegram-message-sender-bot
```

2. Create a virtual environment and activate it.

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages.

```bash
pip install python-telegram-bot --upgrade
```

4. Replace `YOUR_TOKEN` in the script with your actual bot token from BotFather.

## Usage

1. Run the bot.

```bash
python telegram_bot.py
```

2. Open Telegram and start a chat with your bot.

3. Use the `/start` command to initiate the process.

4. Follow the prompts to enter the user ID and the message you want to send.

5. The bot will send the message to the specified user ID.

## Code Explanation

Here's a brief explanation of the main parts of the code:

### Importing Libraries

```python
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
```

### Logging Setup

```python
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
```

### Constants

```python
TOKEN = 'YOUR_TOKEN'
USER_ID, MESSAGE = range(2)
```

### Handlers

- `start`: Initiates the conversation.
- `get_user_id`: Receives the user ID.
- `get_message`: Receives the message and sends it to the specified user ID.
- `cancel`: Cancels the operation.

### Main Function

```python
def main() -> None:
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            USER_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_user_id)],
            MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_message)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conv_handler)
    application.run_polling()
```

### Running the Bot

```python
if __name__ == '__main__':
    main()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

If you have any questions or suggestions, feel free to contact me at sideegmohammednoor@gmail.com.
