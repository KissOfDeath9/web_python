
import cgi
import http.cookies
import os


form = cgi.FieldStorage()

if "name" in form:
    name = form["name"].value
else:
    name = "Не вказано"

if "gender" in form:
    gender = form["gender"].value
else:
    gender = "Не вибрано"

if "interests" in form:
    interests = form.getlist("interests")
else:
    interests = []


cookies = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))


if "counter" in cookies:
    counter = int(cookies["counter"].value)
else:
    counter = 0


if "submit" in form:
    counter += 1


if "delete" in form:
    counter = 0


new_cookie = http.cookies.SimpleCookie()
new_cookie["counter"] = counter


print("Content-type: text/html\n")


print("<html>")
print("<head><title>Результати форми та cookies</title></head>")
print("<body>")
print("<h1>Результати форми</h1>")
print("<p>Ім'я: {0}</p>".format(name))
print("<p>Стать: {0}</p>".format(gender))
print("<p>Інтереси: {0}</p>".format(", ".join(interests)))
print("<h1>Лічильник: {0}</h1>".format(counter))
print('<form method="post">')
print('<input type="submit" name="delete" value="Видалити cookies">')
print('</form>')
print("</body>")
print("</html>")


print(new_cookie.output())
