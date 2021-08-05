import random
import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df = pd.read_csv('medium_data.csv')
data = df['claps'].tolist()

fig = ff.create_distplot([data],['claps'],show_hist= False)


fig.show()


def RandomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],['claps'],show_hist= False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,11],mode = 'lines',name = 'mean'))
    fig.show()



population_mean = statistics.mean(data)
print(population_mean)

population_std = statistics.stdev(data)
print(population_std)
def std():
    mean_list = [] 
    for i in range(0,1000):
        SetOfMeans = RandomSetOfMean(30)
        mean_list.append(SetOfMeans)    
    
    stdevi = statistics.stdev(mean_list)    
    print(stdevi)
    

std()




