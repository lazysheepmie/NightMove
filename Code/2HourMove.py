import os
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'

textSize = 9
tickSize = 7
lineWidth = 1
markerSize = 5
colors = ['#4575B4', '#91BFDB', '#FC8D59', '#D73027']

def DrawLine(ax, xs, ys, marker, label):
    ax.plot(xs, ys, lw=lineWidth, label=label, ls='dotted', marker=marker, markersize=markerSize)

if __name__ == '__main__':
    fig = plt.figure(figsize=(4, 3), dpi=600)
    ax = fig.add_subplot(111)
    
    for date in ['20180704', '20180707', '20190501', '20190505']:
        hourPNums = {}   # 这一天每个小时的出行人数，key为小时，value为出行人数
        fr = open(f'{os.getcwd()}/Data/Move/{date}.csv', 'r')
        fr.readline()
        while True:
            line = fr.readline()
            if not line:
                break
            items = line.split(',')
            date = items[0]    # 日期
            sHour = int(items[1])  # 出发小时
            sLatIndex = int(items[2])   # 出发网格纬度索引，除以100+0.005得到纬度
            sLonIndex = int(items[3])   # 出发网格经度索引，除以100+0.005得到经度
            pNum = int(items[4])   # 从该网格出发的出行人数
            vNum = int(items[5])   # 从该网格出发的出行次数
            if sHour == 0:
                sHour = 24
            if sHour not in hourPNums:
                hourPNums[sHour] = 0
            hourPNums[sHour] += pNum
        fr.close()
        
        hourPNums = dict(sorted(hourPNums.items(), key=lambda x: x[0]))   # 按小时排序

        hours = list(hourPNums.keys())
        pNums = list(hourPNums.values())

        index = ['20180704', '20180707', '20190501', '20190505'].index(date)

        DrawLine(ax, hours, pNums, marker='*', label=date)

        maxPNumIndex = pNums.index(max(pNums))
        ax.axvline(hours[maxPNumIndex], c='black', lw=lineWidth, ls='dotted')   # 每一天最大出行人数的小时

    ax.tick_params(labelsize=tickSize)
    ax.set_xlabel('时刻(小时)', fontsize=textSize)
    ax.set_ylabel('出行人数(人)', fontsize=textSize)
    ax.legend(fontsize=tickSize)
    ax.ticklabel_format(axis='y', style='plain')

    fig.tight_layout()
    fig.savefig(f'{os.getcwd()}/Results/hour_move.eps', bbox_inches='tight', dpi=600, pad_inches=0.1)

