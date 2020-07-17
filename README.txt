# Limitingservice
#run "uvicorn number:app --reload" and "python manage.py runserver 8001" in different terminal

RUN pip install -r requirements.txt && uvicorn number:app --reload && python manage.py runserver 8001
