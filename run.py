import os


if __name__ == "__main__":
    cmd1 = "python manage.py makemigrations"
    cmd2 = "python manage.py migrate"
    cmd3 = "python manage.py loaddata fixtures / initial_data.json"
    cmd4 = "python manage.py runserver 8888"
    p = os.popen(cmd4)
    print(p.read())
