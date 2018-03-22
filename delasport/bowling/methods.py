def is_strike(item):
    return item[0] == 10

def is_spare(item):
    return sum(item) == 10

def re_calculate(collected, final, first_result):
    final = []

    if len(collected) > 1:
        for i,e in enumerate(collected):
            if i != 9:
                if is_strike(e):
                    try:
                        len(collected[i+1])
                        if is_strike(collected[i+1]):
                            try:
                                len(collected[i+2])
                                final.append(sum(e)+sum(collected[i+1])+sum(collected[i+2]))
                            except IndexError:
                                if (i+1) != 9:
                                    final.append(sum(e)+sum(collected[i+1]))
                                else:
                                    final.append(sum(e)+sum(collected[i+1][:2]))
                        else:
                            if (i+1) != 9:
                                final.append(sum(e)+sum(collected[i+1]))
                            else:
                                final.append(sum(e)+sum(collected[i+1][:2]))
                    except IndexError:
                        final.append(sum(e))
                elif is_spare(e):
                    try:
                        len(collected[i+1])
                        final.append(sum(e)+collected[i+1][0])
                    except IndexError:
                        final.append(sum(e))
                else:
                    final.append(sum(e))
            else:
                final.append(sum(collected[9]))
    else:
        final.append(first_result)
    return final

def seconds_to_minutes(time_played):
    seconds_minutes = float(time_played)/60
    minutes = int(str(seconds_minutes).split('.')[0])
    seconds = int((float(seconds_minutes)-float(minutes))*60)

    if minutes > 1:
        minutes_string = "{} {}".format(minutes, "minutes")
    elif minutes == 1:
        minutes_string = "{} {}".format(minutes, "minute")
    else:
        minutes_string = ""

    if seconds == 1:
        seconds_string = "{} {}".format(seconds, "second")
    elif seconds > 1:
        seconds_string = "{} {}".format(seconds, "seconds")
    else:
        seconds_string = ""

    return {'time_played': "{} {} {}".format(minutes_string,("and" if seconds_string > 0 else ""),seconds_string)}
