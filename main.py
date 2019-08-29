from todoist.api import TodoistAPI
import sys

token = sys.argv[1]
api = TodoistAPI(token)
api.sync()

api.user.update(theme=3)


def enable_dark_mode():
    api.user.update(theme=11)


def enable_light_mode():
    api.user.update(theme=6)


def choose_theme():
    themeName = sys.argv[2]
    if themeName == 'dark':
        enable_dark_mode()
    else:
        enable_light_mode()


if __name__ == '__main__':
    choose_theme()
    api.commit()
