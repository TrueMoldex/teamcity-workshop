#!/bin/bash

echo "Install packages..."

# Определяем команду Python в зависимости от операционной системы
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OSTYPE" == "cygwin" ]]; then
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo "Используется команда Python: $PYTHON_CMD"

# Установка необходимых пакетов (только для CI/CD)
if [ "$CI" = "true" ]; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $PYTHON_CMD get-pip.py

    $PYTHON_CMD -m pip install python-pip
    $PYTHON_CMD -m pip install -r requirements.txt
fi

# Установка необходимых python пакетов
$PYTHON_CMD -m pip install -r requirements.txt

# Удаляем старый .env файл, если он существует
if [ -f ".env" ]; then
    rm -f .env
fi

# Генерация .env файла
echo "Generating .env file..."
cat >> .env << 'END'
PASSWORD
USERNAME
END