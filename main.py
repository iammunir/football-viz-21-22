import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Dashboard Top European Football Leagues Season 2021-2022",
    page_icon=":bar_chart:",
    layout="wide"
)

df = pd.read_csv('recreate_stats-2021-2022.csv', delimiter=",", encoding="utf-8")


# SIDEBAR

st.sidebar.header("Please filter here:")

selected_league = st.sidebar.multiselect(
    "Select the League:",
    options=df["League"].unique(),
    default=df["League"].unique(),
)

position_opts = df["Pos"].unique()
position_opts = [p for p in position_opts if len(p) == 2]

selected_position = st.sidebar.multiselect(
    "Select the Position:",
    options=position_opts,
    default=position_opts,
)

def is_position_selected(row):
    for pos in selected_position:
        if pos in row["Pos"]:
            return True
    return False

df_selection = df[df["League"].isin(selected_league) & df.apply(is_position_selected, axis=1)]

# st.dataframe(df_selection)

data_to_show = st.sidebar.selectbox(
    "How many data to show?",
    ('5', '10', '15')
)

# MAIN PAGE

st.title(":bar_chart: Top European Football Leagues Season 2021-2022")
st.markdown("###")

total_teams = df_selection["Squad"].unique().size
total_players = df_selection["Player"].unique().size
total_nations = df_selection["Nation"].unique().size

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Teams")
    st.subheader(f"{str(total_teams)} teams")
with middle_column:
    st.subheader("Total Players")
    st.subheader(f"{str(total_players)} players")
with right_column:
    st.subheader("Total Nations")
    st.subheader(f"{str(total_nations)} nations")

st.markdown("---")

########### MOST GOALS #############

player_with_most_goals = (
    df_selection.sort_values('Goals', ascending=False).head(int(data_to_show))
)

if len(player_with_most_goals) > 0:
    fig_most_goals = px.bar(
        player_with_most_goals,
        x="Goals",
        y="Player",
        labels={"Player": "", "Goals": "Goal Scored"},
        orientation="h",
        color="GoalsPerShoot",
        color_continuous_scale="viridis",
        hover_data=["Player", "Goals", "Squad", "Pos"],
        title="<b>Players with most Goals</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_goals, use_container_width=True)

########### MOST ASSISTS #############

player_with_most_assists = (
    df_selection.sort_values('Assist', ascending=False).head(int(data_to_show))
)

if len(player_with_most_assists) > 0:
    fig_most_assist = px.bar(
        player_with_most_assists,
        x="Assist",
        y="Player",
        color="PassComp%",
        color_continuous_scale="haline",
        labels={"Player": "", "Assist": "Assist Created"},
        orientation="h",
        hover_data=["Player", "Assist", "Squad", "Pos"],
        title="<b>Players with most Assist</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_assist, use_container_width=True)

########### PLAYER WITH MOST SUCCESSFULL DRIBBLE #############

player_with_most_success_drible = (
    df_selection.sort_values('SuccDribble', ascending=False).head(int(data_to_show))
)

if len(player_with_most_success_drible) > 0:
    fig_most_success_dribble = px.bar(
        player_with_most_success_drible,
        y=["SuccDribble", "Dribble"],
        x="Player",
        orientation="v",
        barmode="group",
        labels={"Player": ""},
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data=["Squad", "Pos", "DribbleComp%"],
        title="<b>Player with most Successfull Dribbles</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_success_dribble, use_container_width=True)

########### PLAYER WITH MOST AERIAL WON #############

player_with_most_aerial_won = (
    df_selection.sort_values('AerWon', ascending=False).head(int(data_to_show))
)

if len(player_with_most_aerial_won) > 0:
    fig_most_aerial_won = px.bar(
        player_with_most_aerial_won,
        y=["AerWon", "AerLost"],
        x="Player",
        orientation="v",
        barmode="group",
        labels={"Player": ""},
        color_discrete_sequence=px.colors.qualitative.Vivid,
        hover_data=["Squad", "Pos", "AerWon%"],
        title="<b>Players with most Aerial Won</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_aerial_won, use_container_width=True)

########### PLAYER WITH MOST TACKLE WON #############

player_with_most_tackle_won = (
    df_selection.sort_values('TackleWon', ascending=False).head(int(data_to_show))
)

if len(player_with_most_tackle_won) > 0:
    fig_most_tackle_won = px.bar(
        player_with_most_tackle_won,
        y=["TackleWon", "TackleLost"],
        x="Player",
        orientation="v",
        barmode="group",
        labels={"Player": ""},
        color_discrete_sequence=px.colors.qualitative.Antique,
        hover_data=["Squad", "Pos", "TackleWon%"],
        title="<b>Players with most Tackle Won</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_tackle_won, use_container_width=True)


st.markdown("---")

########### MOST YOUNGEST TEAMS #############

avg_age = df_selection.groupby(['Squad']).agg({'Age': lambda x: x.mean(skipna=True)}).round(4)
avg_age = pd.DataFrame(avg_age).reset_index()
avg_age.columns = ['Squad', 'AvgAge']

team_with_youngest_avg_age = (
    avg_age.sort_values('AvgAge', ascending=True).head((int(data_to_show)))
)

if len(team_with_youngest_avg_age) > 0:
    fig_most_youngest_team = px.bar(
        team_with_youngest_avg_age,
        x="AvgAge",
        y="Squad",
        labels={"Squad": "", "AvgAge": "Age Average in Years Old"},
        orientation="h",
        title="<b>Teams with youngest average of age</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_youngest_team, use_container_width=True)

########### MOST OLDEST TEAMS #############

team_with_oldest_avg_age = (
    avg_age.sort_values('AvgAge', ascending=False).head((int(data_to_show)))
)

if len(team_with_oldest_avg_age) > 0:
    fig_most_oldest_team = px.bar(
        team_with_oldest_avg_age,
        x="AvgAge",
        y="Squad",
        labels={"Squad": "", "AvgAge": "Age Average in Years Old"},
        orientation="h",
        title="<b>Teams with oldest average of age</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_most_oldest_team, use_container_width=True)

# Top teams with most minutes played by young players (20 years and below) ##########

young_players_df = df_selection[df_selection['Age'] <= 20]
club_young_players_minutes = young_players_df.groupby(['Squad', 'League'])\
                                .agg({'Min': 'sum', 'Player': 'count'})\
                                .reset_index()\
                                .rename(columns={'Min':'TotalMinutes', 'Player': 'TotalPlayer'})

club_young_players_minutes.columns = ['Squad', 'League', 'TotalMinutes', 'TotalPlayer']
club_young_players = pd.merge(club_young_players_minutes, avg_age, how='inner', on='Squad')

team_with_most_young_play = (
    club_young_players.sort_values('TotalMinutes', ascending=False).head(int(data_to_show))
)

if len(team_with_most_young_play) > 0:
    fig_team_most_young = px.bar(
        team_with_most_young_play,
        y="TotalMinutes",
        x="Squad",
        color="TotalPlayer",
        color_continuous_scale="ylgnbu",
        hover_data=["TotalMinutes", "TotalPlayer", "League"],
        labels={"Squad": "", "TotalMinutes": "Total Minutes Played by Young Players"},
        orientation="v",
        title="<b>Teams with most total minutes played by young players (20 years old and below)</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_team_most_young, use_container_width=True)

# Top teams with most minutes played by old players (30 years old and above) ##########

old_players_df = df_selection[df_selection['Age'] >= 30]
club_old_players_minutes = old_players_df.groupby(['Squad', 'League'])\
                                .agg({'Min': 'sum', 'Player': 'count'})\
                                .reset_index()\
                                .rename(columns={'Min':'TotalMinutes', 'Player': 'TotalPlayer'})

club_old_players_minutes.columns = ['Squad', 'League', 'TotalMinutes', 'TotalPlayer']
club_old_players = pd.merge(club_old_players_minutes, avg_age, how='inner', on='Squad')

team_with_most_old_play = (
    club_old_players.sort_values('TotalMinutes', ascending=False).head(int(data_to_show))
)

if len(team_with_most_old_play) > 0:
    fig_team_most_old = px.bar(
        team_with_most_old_play,
        y="TotalMinutes",
        x="Squad",
        color="TotalPlayer",
        color_continuous_scale="sunset",
        hover_data=["TotalMinutes", "TotalPlayer", "League"],
        labels={"Squad": "", "TotalMinutes": "Total Minutes Played by Old Players"},
        orientation="v",
        title="<b>Teams with most total minutes played by old players (30 years old and above)</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig_team_most_old, use_container_width=True)