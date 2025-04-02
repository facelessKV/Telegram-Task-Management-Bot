✅ Telegram Task Management Bot

Need to stay on top of your tasks and boost productivity? This bot helps you manage tasks efficiently, set deadlines, and track progress—all within Telegram!
With this bot, you can organize your workflow, assign tasks, and receive timely reminders to stay productive.

✅ What does it do?

 • 📌 Allows you to create, update, and complete tasks
 • ⏳ Sets deadlines and sends reminders
 • 📊 Tracks progress and organizes tasks by priority
 • 🔄 Assigns tasks to team members (if needed)

🔧 Features

✅ Simple and intuitive task management system
✅ Automated reminders to keep you on schedule
✅ Task delegation for better team collaboration

📩 Want to streamline your task management?

Contact me on Telegram, and I’ll help you set up this bot to boost your productivity! 🚀

# Instructions for installing and launching the task scheduler bot

This guide will help you install and run a telegram bot for managing tasks, even if you are new to programming. The instructions are compiled for Windows and Linux operating systems.

## Content
1. [Python Installation](#1-installation-python)
2. [Creating a bot in Telegram] (#2-creating-a-bot-in-telegram)
3. [Installing Necessary Libraries](#3-installing-necessary-libraries)
4. [Setting up and launching the bot] (#4-setting up and launching the bot)
5. [Using a Bot] (#5-using a bot)

## 1. Installing Python

### For Windows:

1. Download Python 3.10 from the official website: https://www.python.org/downloads/release/python-31012/
   Select the "Windows installer (64-bit)" version if you have a 64-bit system.

2. Run the downloaded installer and **make sure to check the box "Add Python 3.10 to PATH"** at the bottom of the installer window.

3. Click "Install Now" and wait for the installation to complete.

4. To check that Python is installed correctly:
- Open the command prompt (press Win+R, type "cmd" and press Enter)
   - Enter the command: `python --version`
   - You should see the Python version (for example, "Python 3.10.12")

### For Linux:

1. Open a terminal (you can usually press Ctrl+Alt+T).

2. Install Python 3.10 using the package manager:

   **For Ubuntu/Debian:**
   ```
   sudo apt update
   sudo apt install python3.10 python3-pip
   ```

   **For Fedora:**
``
   sudo dnf install python3.10 python3-pip
   ```

3. Check the installation:
``
   python3 --version
   ```

## 2. Creating a bot in Telegram

1. Open Telegram and find the bot @BotFather (this is the official Telegram bot for creating bots).

2. Write the command `/newbot` to the bot

3. Follow the instructions of the BotFather:
   - Specify a name for your bot (for example, "My Task Scheduler")
- Specify the username for the bot (must end with "bot", for example, "MyTaskPlannerBot")

4. BotFather will give you a token for the bot API. It looks something like this: `1234567890:AAHfiqksKZ8WmR2zSjiQ7_0dps1sdLa4gNs`

5. **Important!** Save this token in a safe place — you will need it to set up the bot.

## 3. Installing the necessary libraries

### For Windows:

1. Open the command prompt as an administrator:
   - Press Win+R
- Type "cmd"
   - Press Ctrl+Shift+Enter

2. Install the aiogram library:
   ```
   pip install aiogram>=3.0.0
   ```

### For Linux:

1. Open a terminal and run:
   ```
   pip3 install aiogram>=3.0.0
   ```

##4. Setting up and launching the bot

### For Windows:

1. Create a new folder on the desktop (for example, "my_task_bot").

2. Copy the files `database.py `and `main.py `to this folder.

3. Open the file `main.py ` using a Notepad:
   - Right-click on the file
   - Select "Open with" -> "Notepad"

4. Find the string `API_TOKEN = 'YOUR_BOT_TOKEN' (approximately the 16th line).

5. Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather (along with the quotes).

6. Save the file (Ctrl+S) and close Notepad.

7. Launching the bot:
   - Open the command prompt
   - Go to the bot folder, for example:
     ```
     cd C:\Users\USER_NAME\Desktop\my_task_bot
     ``
- Launch the bot with the command:
``
     python main.py
     ```

### For Linux:

1. Create a new folder for the bot:
   ```
   mkdir ~/my_task_bot
   cd ~/my_task_bot
   ```

2. Copy the files `database.py `and `main.py `to this folder.

3. Edit the file `main.py `:
``
   nano main.py
   ```

4. Find the string `API_TOKEN = 'YOUR_BOT_TOKEN'

5. Replace 'YOUR_BOT_TOKEN' with your BotFather token.

6. Save the file (Ctrl+O, then Enter) and exit the editor (Ctrl+X).

7. Launch the bot:
   ```
   python3 main.py
   ```

## 5. Using a bot

1. Open Telegram and find your bot by the name you specified when creating it.

2. Press the "Start" button or send the `/start` command.

3. The bot will respond with a greeting and list the available commands.:
   - `/add` — add a new task
   - `/list` — view all tasks
- `/done` — mark the task as completed
   - `/remove` — delete an issue

4. To add a task:
   - Send the `/add` command
   - The bot will ask you to enter the text of the task
- Send a description of your task

5. To view the task list:
- Send the command `/list`

6. To mark a task as completed:
- Send the command `/done`
   - Select an issue number from the list and send it.

7. To delete an issue:
   - Send the `/remove` command
   - Select an issue number from the list and send it.

## Possible problems and their solutions

1. **Error "python is not an internal or external command"**
   - Reinstall Python and make sure to check the box "Add Python to PATH"

2. **Error when installing libraries**
- Try to run the command prompt as an administrator

3. **The bot does not respond in Telegram**
- Make sure that the program is running and running (there should be activity on the command line)
- Check the correctness of the entered token

4. **Error accessing the database file**
- Make sure that you have write permissions to the bot folder
