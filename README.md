# REA25_M4-5
Репозиторий для задачи мульти-регрессии по табличным данным
# Структура репозитория
- REA25_M4-5/
  - C9_M4.html
  - C9_M5.html
  - catboost_metrics.txt
  - Dockerfile
  - min-max.csv
  - pipeline.py
  - requirements.txt
  - C9_M4.ipynb
  - C9_M5.ipynb
  - catboost_model.pkl
  - metrics.txt
  - model.pkl
  - README.md
# Описание файлов репозитория
| Файл | Тип | Описание |
|---|---|---|
| `model.pkl` | Модель в формате pkl | Обученная модель hgb для мульти-регрессии сериализованная в формат pkl |
| `catboost_model.pkl` | Модель в формате pkl | Обученная модель catboost для мульти-регрессии сериализованная в формат pkl
| `metrics.txt` | Текстовый файл | Метрики валидации модели catboost_model.pkl на валидационном датасете |
| `catboost_metrics.txt` | Текстовый файл | Метрики валидации модели model.pkl на валидационном датасете |
| `Dockerfile` | Dockerfile | Dockerfile для сборки изображения пайплайна для обучения catboost регрессора |
| `min-max.csv` | csv файл | Таблица с min и max для нормализации входных данных |
| `pipeline.py` | Python скрипт | Скрипт для обучения catboost регрессора |
| `requirements.txt` | Текстовый файл | Текстовый файл со списком библиотек для DockerFile |
| `C9_M4.ipynb` | jupyter notebook | Jupyter notebook с кодом для обработки датасета и сокращению его объема |
| `C9_M4.html` | html страница | Jupyter notebook с кодом для обработки датасета и сокращению его объема |
| `C9_M5.ipynb` | jupyter notebook | Jupyter notebook с кодом для обучения модели hgb для мульти-регрессии табличных данных |
| `C9_M5.html` | html страница | Jupyter notebook с кодом для обучения модели hgb для мульти-регрессии табличных данных |
| `README.md` | Markdown | Описание проекта |
