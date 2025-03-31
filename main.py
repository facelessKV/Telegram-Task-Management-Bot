import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from database import Database

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен бота из BotFather (заменить на свой)
API_TOKEN = 'YOUR_BOT_TOKEN'

# Инициализация базы данных
db = Database('tasks.db')

# Состояния для машины состояний
class Form(StatesGroup):
    add_task = State()  # Состояние добавления задачи
    done_task = State()  # Состояние отметки выполнения задачи
    remove_task = State()  # Состояние удаления задачи

# Обработчик команды /start
async def send_welcome(message: types.Message):
    """
    Обработчик команды /start - приветствие пользователя
    """
    await message.reply(
        "Привет! Я бот для управления задачами.\n"
        "Используйте следующие команды:\n"
        "/add - добавить новую задачу\n"
        "/list - просмотреть все задачи\n"
        "/done - отметить задачу как выполненную\n"
        "/remove - удалить задачу"
    )

# Обработчик команды /add
async def add_task_start(message: types.Message, state: FSMContext):
    """
    Начало процесса добавления новой задачи
    """
    await state.set_state(Form.add_task)
    await message.reply("Введите текст задачи:")

# Обработчик для получения текста задачи
async def add_task_process(message: types.Message, state: FSMContext):
    """
    Получение текста задачи и сохранение её в базе данных
    """
    user_id = message.from_user.id
    task_text = message.text
    
    # Добавляем задачу в базу данных
    task_id = db.add_task(user_id, task_text)
    
    await message.reply(f"Задача #{task_id} добавлена!")
    await state.clear()  # Завершаем состояние

# Обработчик команды /list
async def list_tasks(message: types.Message):
    """
    Отображение списка всех задач пользователя
    """
    user_id = message.from_user.id
    tasks = db.get_all_tasks(user_id)
    
    if not tasks:
        await message.reply("У вас пока нет задач!")
        return
    
    response = "Ваши задачи:\n\n"
    for task in tasks:
        task_id, text, done, date = task
        status = "✅" if done else "❌"
        response += f"{task_id}. {status} {text} ({date})\n"
    
    await message.reply(response)

# Обработчик команды /done
async def done_task_start(message: types.Message, state: FSMContext):
    """
    Начало процесса отметки задачи как выполненной
    """
    user_id = message.from_user.id
    tasks = db.get_all_tasks(user_id)
    
    if not tasks:
        await message.reply("У вас нет задач для отметки!")
        return
    
    # Формируем список невыполненных задач
    response = "Введите номер задачи, которую хотите отметить как выполненную:\n\n"
    has_undone_tasks = False
    
    for task in tasks:
        task_id, text, done, date = task
        if not done:
            has_undone_tasks = True
            response += f"{task_id}. {text}\n"
    
    if not has_undone_tasks:
        await message.reply("У вас нет невыполненных задач!")
        return
    
    await state.set_state(Form.done_task)
    await message.reply(response)

# Обработчик для отметки задачи как выполненной
async def done_task_process(message: types.Message, state: FSMContext):
    """
    Обработка номера задачи и отметка её как выполненной
    """
    user_id = message.from_user.id
    
    try:
        task_id = int(message.text)
        
        # Отмечаем задачу как выполненную
        success = db.mark_done(task_id, user_id)
        
        if success:
            await message.reply(f"Задача #{task_id} отмечена как выполненная!")
        else:
            await message.reply(f"Задача #{task_id} не найдена или не принадлежит вам!")
        
        await state.clear()  # Завершаем состояние
    except ValueError:
        await message.reply("Пожалуйста, введите корректный номер задачи!")

# Обработчик команды /remove
async def remove_task_start(message: types.Message, state: FSMContext):
    """
    Начало процесса удаления задачи
    """
    user_id = message.from_user.id
    tasks = db.get_all_tasks(user_id)
    
    if not tasks:
        await message.reply("У вас нет задач для удаления!")
        return
    
    # Формируем список задач
    response = "Введите номер задачи, которую хотите удалить:\n\n"
    
    for task in tasks:
        task_id, text, done, date = task
        status = "✅" if done else "❌"
        response += f"{task_id}. {status} {text}\n"
    
    await state.set_state(Form.remove_task)
    await message.reply(response)

# Обработчик для удаления задачи
async def remove_task_process(message: types.Message, state: FSMContext):
    """
    Обработка номера задачи и её удаление
    """
    user_id = message.from_user.id
    
    try:
        task_id = int(message.text)
        
        # Удаляем задачу
        success = db.remove_task(task_id, user_id)
        
        if success:
            await message.reply(f"Задача #{task_id} удалена!")
        else:
            await message.reply(f"Задача #{task_id} не найдена или не принадлежит вам!")
        
        await state.clear()  # Завершаем состояние
    except ValueError:
        await message.reply("Пожалуйста, введите корректный номер задачи!")

# Обработчик для остальных сообщений
async def echo(message: types.Message):
    """
    Обработчик для всех остальных сообщений
    """
    await message.reply(
        "Я не понимаю эту команду.\n"
        "Используйте следующие команды:\n"
        "/add - добавить новую задачу\n"
        "/list - просмотреть все задачи\n"
        "/done - отметить задачу как выполненную\n"
        "/remove - удалить задачу"
    )

async def main():
    """
    Инициализация и запуск бота
    """
    # Инициализация бота и диспетчера
    bot = Bot(token=API_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрация обработчиков команд
    dp.message.register(send_welcome, Command(commands=['start']))
    dp.message.register(add_task_start, Command(commands=['add']))
    dp.message.register(add_task_process, Form.add_task)
    dp.message.register(list_tasks, Command(commands=['list']))
    dp.message.register(done_task_start, Command(commands=['done']))
    dp.message.register(done_task_process, Form.done_task)
    dp.message.register(remove_task_start, Command(commands=['remove']))
    dp.message.register(remove_task_process, Form.remove_task)
    dp.message.register(echo)  # Регистрируем обработчик для остальных сообщений
    
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        # Запуск основного обработчика
        asyncio.run(main())
    except KeyboardInterrupt:
        # Закрытие соединения с базой данных при остановке бота
        db.close()
        print("Бот остановлен")