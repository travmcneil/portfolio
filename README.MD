Create new conda env
    conda create -n portfolio

Install requirements
    pip install -r requirements.txt  

Activate flask
    Windows
    cd OneDrive\Documents\development\portfolio
    conda activate portfolio
    set FLASK_CONFIG=%cd%\config.py
    set FLASK_DEBUG=1
    set FLASK_APP=portfolio.py
    flask run

    Mac
    