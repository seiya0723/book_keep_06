
import datetime

def callender(dt,topics):

    #来月と先月のリンクを作る(timedeltaでmonthを加算することはできない。別途ライブラリを使うか、下記のように計算する。)
    #https://stackoverflow.com/questions/546321/how-do-i-calculate-the-date-six-months-from-the-current-date-using-the-datetime
    if dt.month == 12:
        #来月の計算はyearを1追加、monthを1にする。先月はそのまま1減らす。
        next_month  = "?year=" + str(dt.year + 1) + "&month=" + str(1)
        prev_month  = "?year=" + str(dt.year) + "&month=" + str(dt.month -1)

    elif dt.month == 1:
        #先月の計算はyearを1減らす、monthを12にする。来月はそのまま1追加。
        next_month  = "?year=" + str(dt.year) + "&month=" + str(dt.month + 1)
        prev_month  = "?year=" + str(dt.year - 1) + "&month=" + str(12)

    else:
        #来月、先月それぞれ1追加、1減らすだけでいい
        next_month  = "?year=" + str(dt.year) + "&month=" + str(dt.month + 1)
        prev_month  = "?year=" + str(dt.year) + "&month=" + str(dt.month - 1)

    #topicsの中にある日付のリストを作る
    topic_dts   = []
    for topic in topics:
        topic_dts.append(str(topic.dt.year) + str(topic.dt.month) + str(topic.dt.day))

    print(topic_dts)

    year        = dt.year
    month       = dt.month
    days        = []
    weekdays    = []

    #.weekday()で数値化した曜日が出力される(月曜日が0、日曜日が6)
    #一ヶ月の最初が日曜日であればそのまま追加、それ以外の曜日であれば、曜日の数値に1追加した数だけ空文字を追加
    if dt.weekday() != 6:
        for i in range(dt.weekday()+1):
            weekdays.append("")

    #1日ずつ追加して月が変わったらループ終了
    while month == dt.month:
        dic = { "num":"","id":"" }

        #カレンダーの日付に投稿した日記がある場合、idに年月日の文字列型をセットする。(このidがリンクになる)
        for topic_dt in topic_dts:
            str_dt  = str(year) + str(month) + str(dt.day)
            if topic_dt == str_dt:
                dic["id"]   = str_dt
                break

        dic["num"]  = dt.day

        weekdays.append(dic)

        dt  = dt + datetime.timedelta(days=1)
        if dt.weekday() == 6:
            days.append(weekdays)
            weekdays    = []

    if dt.weekday() != 6:
        days.append(weekdays)
        weekdays    = []

    return days,year,month,next_month,prev_month



