import pandas as pd
import matplotlib.pyplot as plt

from frames import games, info, events

plays = games.query("type == 'play' & event != 'NP'")
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year' ]

pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name= 'PA') 
events = events.set_index(['year', 'game_id', 'team', 'event_type'])
events = events.unstack().fillna(0).reset_index()

print (events)
