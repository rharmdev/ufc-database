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
del events[0]
for x in events:
    x = ast.literal_eval(x)


    names.append(x[0])

    links.append(x[1])

for x in links:
    data = pd.read_html(x, extract_links="all")[0]
    fights = (data[data.columns[0]].tolist())
    fight_links = []
    for i in fights:

        fight_links.append(i[1])
        fighters = []
        strike = []
        kd = []
        ctrl = []
        td = []
        sub = []
        rev = []
    try:
        for k in fight_links:
            fight = pd.read_html(k)[0]
            fighters += (fight["Fighter"].tolist())
            strike += (fight["Sig. str."].apply(lambda x: str(x).split("  "))).tolist()
            kd += (fight["KD"].apply(lambda x: str(x).split("  "))).tolist()
            ctrl += (fight["Ctrl"].apply(lambda x: str(x).split("  "))).tolist()
            td += (fight["Td"].apply(lambda x: str(x).split("  "))).tolist()
            sub += (fight["Sub. att"].apply(lambda x: str(x).split("  "))).tolist()
            rev += (fight["Rev."].apply(lambda x: str(x).split("  "))).tolist()
    except:
        
        data = pd.read_html(x)[0]
        win = []
        lose = []
        wl = (data["Fighter"].apply(lambda x: x.split("  "))).tolist()
   
        c = 0
        for i in wl:
            win.append(i[0])
            lose.append(i[1])
        data.drop(["Fighter", "Kd", "Str", "Td", "Sub"], inplace=True, axis=1)
        data.insert(1, "Winner", win)
        data.insert(2, "Loser", lose)
        data.insert(3, "W_Str", None)
        data.insert(4, "L_Str", None)
        data.insert(5, "W_Kd", None)
        data.insert(6, "L_Kd", None)
        data.insert(7, "W_Ctrl", None)
        data.insert(8, "L_Ctrl", None)
        data.insert(9, "W_Td", None)
        data.insert(10, "L_Td", None)
        data.insert(11, "W_SubAtt", None)
        data.insert(12, "L_SubAtt", None)
        data.insert(13, "W_Rev", None)
        data.insert(14, "L_Rev", None)
        data.insert(0, "Date", str(", ".join(names[counter:counter+1])).replace('"', ''))
        data["W/L"] = data.pop("W/L")
        data.drop(data.loc[data['Weight class'].str.contains("Women's")].index, inplace=True)

        UFC = pd.concat([UFC, data])
        
        print(UFC)
        counter +=1
    
        continue

      



    data = pd.read_html(x)[0]

        
    win = []
    lose = []
    w_str = []
    l_str = []
    w_kd = []
    l_kd = []
    w_ctrl = []
    l_ctrl = []
    w_td = []
    l_td = []
    w_sub = []
    l_sub = []
    w_rev = []
    l_rev = []

    
    
    wl = (data["Fighter"].apply(lambda x: x.split("  "))).tolist()
   
    c = 0
    for i, j in zip(wl, fighters):
        win.append(i[0])
        lose.append(i[1])
        if j.find(i[0]) ==0:
            c+=1
            continue
        else:
            
            strike[c][0], strike[c][1] = strike[c][1], strike[c][0]
            kd[c][0], kd[c][1] = kd[c][1], kd[c][0]
            ctrl[c][0], ctrl[c][1] = ctrl[c][1], ctrl[c][0]
            td[c][0], td[c][1] = td[c][1], td[c][0]
            sub[c][0], sub[c][1] = sub[c][1], sub[c][0]
            rev[c][0], rev[c][1] = rev[c][1], rev[c][0]
            c+=1
        
        

    for i, j, k, l,m,n in zip(strike, kd, ctrl, td, sub, rev):
        w_str.append(i[0])
        l_str.append(i[1])
        w_kd.append(j[0])
        l_kd.append(j[1])
        w_ctrl.append(k[0])
        l_ctrl.append(k[1])
        w_td.append(l[0])
        l_td.append(l[1])
        w_sub.append(m[0])
        l_sub.append(m[1])
        w_rev.append(n[0])
        l_rev.append(n[1])


    data.drop(["Fighter", "Kd", "Str", "Td", "Sub"], inplace=True, axis=1)
    data.insert(1, "Winner", win)
    data.insert(2, "Loser", lose)
    data.insert(3, "W_Str", w_str)
    data.insert(4, "L_Str", l_str)
    data.insert(5, "W_Kd", w_kd)
    data.insert(6, "L_Kd", l_kd)
    data.insert(7, "W_Ctrl", w_ctrl)
    data.insert(8, "L_Ctrl", l_ctrl)
    data.insert(9, "W_Td", w_td)
    data.insert(10, "L_Td", l_td)
    data.insert(11, "W_SubAtt", w_sub)
    data.insert(12, "L_SubAtt", l_sub)
    data.insert(13, "W_Rev", w_rev)
    data.insert(14, "L_Rev", l_rev)
    data.insert(0, "Date", str(", ".join(names[counter:counter+1])).replace('"', ''))
   
    data.drop(data.loc[data['Weight class'].str.contains("Women's")].index, inplace=True)

    UFC = pd.concat([UFC, data])
    
    print(UFC)
    counter +=1

   

UFC.to_csv("UFC_EVENTS_DETAILED.csv", index=False)