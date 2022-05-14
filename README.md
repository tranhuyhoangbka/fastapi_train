Project key:

Key Name:    nir9gi
Key Description:  Project Key: nir9gi
Project Key:   c0onrnyn_UxdzwAhpr8D1DkcLWkhLjCniW3BehtfB


deta new --python deta-fastapi

pip install virtualenv
virtualenv venv

source /home/huyhoang/Documents/projects/deta-fastapi/venv
 6238  pip install deta
 6239  touch requirements.txt
 6240  pip freeze > requirements.txt
 6241  python3 -m uvicorn main:app --reload

deta deploy
deta details   # url endpoint