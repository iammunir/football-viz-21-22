# Top 5 European Football Leagues Data Visualization 2021-2022

Interactive dashboard data visualization for 5 Major European football leagues season 2021-2022

Data Source: [Kaggle](https://www.kaggle.com/datasets/vivovinco/20212022-football-player-stats?select=2021-2022+Football+Player+Stats.csv)

Interactive Dashboard: [https://football-viz-21-22.mmunir.dev/](https://football-viz-21-22.mmunir.dev/)

## Objectives

- Players with most goals
- Players with most assists
- Players with most successfull dribbles
- Players with most aerial won
- Players with most tackle won
- Teams with youngest average of age
- Teams with oldest average of age
- Teams with most total minutes played by young players (20 years old and below)
- Teams with most total minutes played by old players (30 years old and above)

## How to run the code

You can pull the docker images [here](https://hub.docker.com/repository/docker/mmunir/football-viz-21-22/tags?page=1&ordering=last_updated) and create a container with port binding 8501.

Or you can clone this repository and run it locally

`git clone https://github.com/iammunir/football-viz-21-22.git`

Change working directory

`cd football-viz-21-22`

Install dependencies package (assuming you have Python3 installed)

`pip3 install -r requirements.txt`

Run the code

`streamlit run main.py`

Open browser and hit `http://localhost:8501`