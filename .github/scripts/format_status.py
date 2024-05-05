import re


def format_status(compose_ps_output):
    # Разбить вывод на строки
    lines = compose_ps_output.split('\n')

    # Извлечь только строки с информацией о контейнерах
    container_lines = [line for line in lines if re.match(r'^\s*[^_]', line)]

    # Форматировать строки для удобства чтения
    formatted_output = "\n".join(container_lines)

    return formatted_output


if __name__ == "__main__":
    import sys

    # Получить вывод команды docker-compose ps из аргументов командной строки
    compose_ps_output = sys.argv[1]

    # Форматировать вывод
    formatted_output = format_status(compose_ps_output)

    # Вывести отформатированный результат
    print(formatted_output)
