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
