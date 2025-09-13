🌐 Host Checker
<div align="center">
Show Image
Show Image
Show Image

Маленькая CLI-утилита для проверки доступности хостов из списка

Простота запуска • Читаемые логи • Внятная структура

</div>
🎯 Зачем это нужно
⚡ Быстро понять, что пингуется, а что нет
📊 Сохранить результат в CSV для отчётов и аналитики
🧭 Показать аккуратный репозиторий с прозрачной структурой
📋 Требования
🐍 Python 3.10+
📡 Системная команда ping в PATH
Windows: встроено
Linux: пакет iputils-ping (обычно уже установлен)
🚀 Установка
bash
git clone https://github.com/n0teternal/host-checker.git
cd host-checker

# (опционально) виртуальное окружение
# python -m venv .venv && source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate                               # Windows

# Зависимостей нет — используется стандартная библиотека Python
🏁 Быстрый старт
1. Создайте файл hosts.csv в корне проекта
8.8.8.8
1.1.1.1
ya.ru
vvsu.ru
2. Запустите скрипт
bash
python main.py
3. Смотрите результат
Вывод появится в консоли. Если включено логирование в файл — проверьте log.csv.

Примечание: Формат входа максимально простой — одна колонка host (IP или DNS-имя). Если нужны комментарии к каждой строке — см. Roadmap.

📸 Примеры
Консольный вывод
[12:03:11] ya.ru        OK    23 ms
[12:03:12] 8.8.8.8      OK    21 ms
[12:03:13] 1.1.1.1      FAIL  timeout
[12:03:14] vvsu.ru      OK    34 ms
CSV лог
csv
timestamp,host,status,rtt_ms
2025-09-14T12:03:11,ya.ru,OK,23
2025-09-14T12:03:12,8.8.8.8,OK,21
2025-09-14T12:03:13,1.1.1.1,FAIL,
2025-09-14T12:03:14,vvsu.ru,OK,34
💡 Подсказки по платформам
<details> <summary><strong>🪟 Windows</strong></summary>
ping принимает таймаут в миллисекундах (ключ /w)
Команда доступна по умолчанию
</details> <details> <summary><strong>🐧 Linux</strong></summary>
ping может требовать RAW-сокеты (иногда нужен sudo)
Таймаут обычно через -W (секунды)
Удобно вызывать системный ping через subprocess без привилегий
</details>
❓ FAQ
<details> <summary><strong>Почему некоторые домены пингуются нестабильно?</strong></summary>
CDN, фильтры ICMP, блокировки на стороне провайдера. Пинг — не гарантия доступности сервиса (только сети/хоста).

</details> <details> <summary><strong>Можно ли запускать проверки параллельно?</strong></summary>
Сейчас — последовательно. Параллельность легко добавить через concurrent.futures (см. Roadmap). 🔧

</details> <details> <summary><strong>Нужен ли requirements.txt?</strong></summary>
Нет. Проект использует только стандартную библиотеку Python. Если добавите тесты/линтеры — тогда да.

</details>
🗺️ Roadmap
 CLI-параметры (argparse): --hosts hosts.csv, --count 3, --interval 1.0, --timeout 1000, --out log.csv
 CSV-лог с заголовком (timestamp,host,status,rtt_ms) и корректным flush
 Параллельные проверки (ThreadPool) с ограничением --workers
 Поле «описание» во входном CSV: host,desc → логировать обе колонки
 Коды возврата процесса: 0 (всё ок), 1 (есть недоступные), 2 (ошибка ввода)
 GitHub Actions (CI): линтер/тесты по push
 LICENSE (MIT) в корне
📁 Структура проекта
host-checker/
├─ main.py              # основной скрипт
├─ hosts.csv            # пример входного файла
├─ log.csv              # (опционально) результат проверки
├─ README.md            # этот файл
├─ .gitignore           # игнорируемые файлы
└─ tests/               # (опционально) юнит-тесты
🧪 Разработка
bash
# Если используете форматтер/линтеры/тесты:
# pip install black flake8 pytest
# black .
# flake8 .
# pytest -q
🤝 Вклад в проект
Форкните репозиторий
Создайте ветку для новой функции (git checkout -b feature/amazing-feature)
Зафиксируйте изменения (git commit -m 'Add amazing feature')
Отправьте ветку (git push origin feature/amazing-feature)
Откройте Pull Request
📄 Лицензия
Этот проект лицензирован под MIT License - подробности см. в файле LICENSE.

<div align="center">
Сделано с ❤️ для удобства сетевых администраторов

⭐ Поставьте звезду, если проект оказался полезным!

</div>
