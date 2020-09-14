#In order to run the project

1. pip install -r requirements.txt
2. create .env file in root folder and copy .env.template into it. Add your config details.
3. Open terminal and run following command to migrate database models
    ```
   from models import base
   base.metadata.createall()
   ```
4.. Now run the code using :-
    ```
    python script.py
    ```
