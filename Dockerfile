# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію усередині контейнера
WORKDIR $APP_HOME


COPY poetry.lock $APP_HOME/poetry.lock
COPY pyproject.toml $APP_HOME/pyproject.toml

# Встановимо залежності усередині контейнера
RUN pip install poetry
RUN poetry install --only __main__

# Скопіюємо інші файли до робочої директорії контейнера
COPY . .

# Позначимо порт де працює програма всередині контейнера
EXPOSE 5000

# Запустимо нашу програму всередині контейнера
CMD ["python", "__main__.py"]