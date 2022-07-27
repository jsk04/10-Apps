"""
    Detect moving objects and making a graph of this motion
"""

import cv2, time, pandas
from datetime import datetime

import bokeh.plotting as plotting
figure = plotting.figure

import bokeh.io as io
output_file = io.output_file
show = io.show

import bokeh.models as models
HoverTool = models.HoverTool
ColumnDataSource = models.ColumnDataSource

def main():
    first_frame = None
    status_list = [None, None]
    times = []
    time_stamps = pandas.DataFrame(columns = ["Start", "End"])

    video = cv2.VideoCapture(0)
    video.read()
    time.sleep(1)

    while True:
        check, frame = video.read()
        status = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21, 21), 0)

        if first_frame is None:
            first_frame = gray
            continue

        delta_frame = cv2.absdiff(first_frame, gray)
        thresh_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 4)

        (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 6000:
                continue
            status = 1
            (row, column, width, height) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (row, column), (row + width, column + height),
                          (0,255, 0), 3)

        status_list.append(status)
        status_list = status_list[-2:]
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())

        cv2.imshow("Capturing", gray)
        cv2.imshow("Diff", delta_frame)
        cv2.imshow("Threshold", thresh_frame)
        cv2.imshow('Color Frame', frame)

        key = cv2.waitKey(1000)

        if key == ord('q'):
            if status == 1:
                times.append(datetime.now())
            break

    for i in range(0, len(times), 2):
        time_stamps = time_stamps.append({'Start': times[i], 'End': times[i + 1]}, ignore_index = True)

    time_stamps.to_csv('Times.csv')

    video.release()
    plotting(time_stamps)
    cv2.destroyAllWindows()


def plotting(time_stamps):
    time_stamps['Start_str'] = time_stamps['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
    time_stamps['End_str'] = time_stamps['End'].dt.strftime('%Y-%m-%d %H:%M:%S')
    data = ColumnDataSource(time_stamps)
    plot = figure(x_axis_type='datetime', height=100, width=500,
                  sizing_mode="scale_both", title='Motion Graph')

    plot.yaxis.minor_tick_line_color = None
    plot.yaxis[0].ticker.desired_num_ticks = 1

    plot.quad(left='Start', right='End',
                      top=1, bottom=0, color='green', source=data)

    hover = models.HoverTool(tooltips=[('Start', '@Start_str'), ('End', '@End_str')])
    plot.add_tools(hover)
    output_file('Graph.html')
    show(plot)


if __name__ == '__main__':
    main()