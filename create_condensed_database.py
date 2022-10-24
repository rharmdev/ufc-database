import pandas as pd
import ast


df = pd.read_html("http://ufcstats.com/statistics/events/completed?page=all", extract_links="all")[0]
df.drop(df.index[0], inplace=True)
df.to_csv("ufc.csv", index=False)

df = pd.read_csv("ufc.csv")
df.columns = ["Name/Data", "Location"]

UFC = pd.DataFrame()
events = (df[df.columns[0]].tolist())
counter = 0
links = []
names = []
for x in events:
    x = ast.literal_eval(x)


    names.append(x[0])

    links.append(x[1])

for x in links:
    data = pd.read_html(x)[0]




    win = []
    lose = []
    w_kd = []
    l_kd = []

    w_str = []
    l_str = []

    w_td = []
    l_td = []

    w_sub = []
    l_sub = []
    wl = (data["Fighter"].apply(lambda x: x.split("  "))).tolist()


    kd = (data["Kd"].apply(lambda x: str(x).split("  "))).tolist()
    strike = (data["Str"].apply(lambda x: str(x).split("  "))).tolist()

    td = (data["Td"].apply(lambda x: str(x).split("  "))).tolist()
    sub = (data["Sub"].apply(lambda x: str(x).split("  "))).tolist()
    data.drop(["Fighter", "Kd", "Str", "Td", "Sub"], inplace=True, axis=1)

    for i, j, k, l, m in zip(wl, kd, strike, td, sub):
        win.append(i[0])
        lose.append(i[1])
        w_kd.append(j[0])
        w_str.append(k[0])
        w_td.append(l[0])
        w_sub.append(m[0])
        try:
           
            l_kd.append(j[1])
            l_str.append(k[1])
            l_td.append(l[1])
            l_sub.append(m[1])
        except:
            l_str.append("nan")
            l_kd.append("nan")
            l_td.append("nan")
            l_sub.append("nan")

        

    
    data.insert(0, "Winner", win)
    data.insert(1, "Loser", lose)
    data.insert(0, "Event_ID", x[-16:])
    
    data.insert(4, "W_KD", w_kd)
    data.insert(5, "L_KD", l_kd)
    data.insert(6, "W_STR", w_str)
    data.insert(7, "L_STR", l_str)
    data.insert(8, "W_TD", w_td)
    data.insert(9, "L_TD", l_td)
    data.insert(10, "W_SUB", w_sub)
    data.insert(11, "L_SUB", l_sub)
    data.insert(0, "Date", str(", ".join(names[counter:counter+1])).replace('"', ''))
    data["W/L"] = data.pop("W/L")

    data.drop(data.loc[data['Weight class'].str.contains("Women's")].index, inplace=True)

    UFC = pd.concat([UFC, data])
    counter +=1
    UFC.to_csv("UFC_EVENTS.csv", index=False)
    print(UFC)

UFC.to_csv("UFC_EVENTS.csv", index=False)