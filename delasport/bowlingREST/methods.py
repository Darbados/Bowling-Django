def is_strike(item):
    return item[0] == 10

def is_spare(item):
    return sum(item) == 10

def re_calculate(frame_results):
    temp = frame_results

    for frame in temp:
        if 'roll3' not in frame.keys():
            if frame['roll1'] == 10:
                frame['strike'] = 'X'
                frame['total'] = 10
            elif (frame['roll1']+frame['roll2']) == 10 and frame['roll1'] != 10:
                frame['spare'] = '/'
                frame['total'] = 10
            else:
                frame['total'] = frame['roll1'] + frame['roll2']
        else:
            if frame['roll1'] == 10:
                frame['strike'] = 'X'
            elif (frame['roll1']+frame['roll2']) == 10 and frame['roll1'] != 10:
                frame['spare'] = '/'
            frame['total'] = frame['roll1'] + frame['roll2'] + frame['roll3']

    for i,frame in enumerate(temp):
        if 'roll3' not in frame.keys():
            if 'strike' in frame.keys():
                if frame_results[i+1]['strike'] == 'X':
                    frame['total'] = frame['total'] + frame_results[i+1]['total'] + frame_results[i+2]['total']
                else:
                    frame['total'] = frame['total'] + frame_results[i+1]['total']
            elif 'spare' in frame.keys():
                frame['total'] = frame['total'] + frame_results[i+1]['roll1']
            else:
                frame['total'] = frame['total']
        else:
            frame['total'] = frame['roll1'] + frame['roll2'] + frame['roll3']

    return temp
