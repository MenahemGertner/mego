# # Taken from husano896's PR thread (slightly modified)
# import pygame
# from pygame.locals import *
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
#
# def main():
#    while True:
#       for event in pygame.event.get():
#             if event.type == QUIT:
#                pygame.quit()
#                return
#             elif event.type == MOUSEWHEEL:
#                print(event)
#                print(event.x, event.y)
#                print(event.flipped)
#                print(event.which)
#                # can access properties with
#                # proper notation(ex: event.y)
#       clock.tick(60)
#
# # Execute game:
# main()

# הגדרת PyCharm:
# התקן את PyCharm מהאתר הרשמי 2.
# פתח את PyCharm וצור פרויקט חדש.
# בגדרות הפרויקט, בחר את הגרסה הנכונה של Python ב-Project Interpreter.
# באותו מקום, הוסף את הספריות הצד ג’ הבאות: pyqt5, pyqt5-sip, ו-pyqt5-tools.
# הגדרת QtDesigner:
# התקן את QtDesigner (כלי לעיצוב ממשקי משתמש) מהאתר הרשמי.
# ב-PyCharm, בגדרות הכלי החיצוניים, הוסף את QtDesigner והגדר את הנתיב לקובץ המבוצע (לדוגמה: designer.exe).
# גם קובץ ה-troubleshooting שלי יכול לעזור לך בהגדרה המדויקת של QtDesigner.
# הגדרת PyUIC:
# התקן את PyUIC (כלי להמרת קבצי .ui לקוד Python) מהאתר הרשמי.
# ב-PyCharm, בגדרות הכלי החיצוניים, הוסף את PyUIC והגדר את הנתיב לקובץ המבוצע (לדוגמה: python.exe).
# גם קובץ ה-troubleshooting שלי יכול לעזור לך בהגדרה המדויקת של PyUIC.

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)