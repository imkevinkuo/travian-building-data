import json
d = {}
currentB = ""
with open("building_data.txt", "r") as f:
    raw_text = f.read()
    lines = raw_text.split("\n")
    for line in lines:
        if currentB == "":
            currentB = line
            d[currentB] = []
        elif len(line) == 0:
            currentB = ""
        else:
            toks = line.split() # d[building][level] = (level_res, level_cp, total_cp)
            level_res = int(toks[5])
            total_cp = int(toks[9])
            if len(d[currentB]) == 0:
                d[currentB].append((level_res, total_cp, total_cp))
            else:
                d[currentB].append((level_res, total_cp - d[currentB][-1][2], total_cp))
ls = []
for b in d:
    res_sum = 0
    levels = []
    for lv in range(len(d[b])):
        res_sum += d[b][lv][0]
        levels.append(lv+1)
        if d[b][lv][1] != 0:
            ls.append((1.0*res_sum/d[b][lv][1], b, levels))
            res_sum = 0
            levels = []
ls.sort()
s = json.dumps(ls)
m = s.replace('"', '\\"')
print(m)
