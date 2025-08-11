import pandas as pd

def load_players(file_path):
    return pd.read_csv("C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\cricket_players_analysis\\data\\players.csv")
    

def load_matches(file_path):
    return pd.read_csv("C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\cricket_players_analysis\\data\\matches.csv")

def merge_players_matches(players_df, matches_df):
    merged = pd.merge(players_df, matches_df, on="PlayerID")
    return merged

    
    

def total_runs_per_team(merged_df):
    df = merged_df.groupby("Team", as_index=False)["Runs"].sum()
    return df

def calculate_strike_rate(merged_df):
    df = merged_df.copy()
    df["StrikeRate"] = (df["Runs"] / df["Balls"]) * 100
    result = df[["PlayerID", "Name", "Runs", "Balls", "StrikeRate"]]
    return result

def runs_agg_per_player(merged_df):
     agg_df = merged_df.groupby(["PlayerID", "Name"])["Runs"].agg(["mean", "max", "min"]).reset_index()
     return agg_df

def avg_age_by_role(players_df):
    
    return players_df.groupby('Role')['Age'].mean().reset_index()

def total_matches_per_player(matches_df):
    
    counts = matches_df.groupby('PlayerID')['MatchID'].count().reset_index()
    counts.columns = ['PlayerID', 'MatchCount']  
    return counts

    

    # Step 1: Get counts (index: PlayerID, column: count)
    
    # Step 2: Rename columns explicitly and cleanly
   

    # Ensure columns are in correct order
   
    



def top_wicket_takers(merged_df):
    top_n = 3  # hardcoded inside the function
    return (merged_df.groupby(['PlayerID', 'Name'])['Wickets']
                    .sum()
                    .reset_index()
                    .sort_values(by='Wickets', ascending=False)
                    .head(top_n))

def avg_strike_rate_per_team(merged_df):
    df = merged_df.copy()
    df["StrikeRate"] = (df["Runs"] / df["Balls"]) * 100
    result = df.groupby("Team", as_index=False)["StrikeRate"].mean()
    return result

def catch_to_match_ratio(merged_df):
    catches = merged_df.groupby("PlayerID", as_index=False)["Catches"].sum()
    matches = merged_df.groupby("PlayerID").size().reset_index(name="MatchCount")
    merged = pd.merge(catches, matches, on="PlayerID")
    merged["CatchToMatchRatio"] = merged["Catches"] / merged["MatchCount"]
    result = merged[["PlayerID", "CatchToMatchRatio"]]
    return result
