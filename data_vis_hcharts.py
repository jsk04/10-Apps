"""
    Simple Web App--with HighCharts graphs--using Justpy, a Python Web Framework
    Graphs include:
    Average Ratings by Day, Week, and Month
    Average Ratings by Course by Month(in StreamChart and AreaSpline)
    Average Ratings by Weekday to find Happiest Day of the Week
    Pie Chart of Percentage of Ratings for each Course

Usage: data_vis_hcharts.py <TimePeriod/Condition> [Type of Graph]

Example1: data_vis_hcharts.py Day
Example2: data_vis_hcharts.py Course Area
Example3: data-vis_hcharts.py Pie
"""

import sys
import justpy as jp
import pandas
import datetime as datetime

time = datetime.datetime

spline_chart = """
    {
        chart: {
            type: 'spline',
            inverted: false
        },
        title: {
            text: 'Atmosphere Temperature by Altitude'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            reversed: false,
            title: {
                enabled: true,
                text: 'Date'
            },
            labels: {
                format: '{value}'
            },
            accessibility: {
                rangeDescription: 'Range: 0 to 80 km.'
            },
            maxPadding: 0.05,
            showLastLabel: true
        },
        yAxis: {
            title: {
                text: 'Average Rating'
            },
            labels: {
                format: '{value}'
            },
            accessibility: {
                rangeDescription: 'Range: -90°C to 20°C.'
            },
            lineWidth: 2
        },
        legend: {
            enabled: false
        },
        tooltip: {
            headerFormat: '<b>{series.name}</b><br/>',
            pointFormat: '{point.y}'
        },
        plotOptions: {
            spline: {
                marker: {
                    enable: false
                }
            }
        },
        series: [{
            name: 'Average Rating',
            data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
                [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
        }]
    }
    """
area_spline_chart = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""
stream_chart = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    // Make sure connected countries have similar colors

    title: {
        floating: true,
        align: 'left',
        text: 'Winter Olympic Medal Wins'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: reviews.csv'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Course Launched'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Course Launched'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [{
        name: "Finland",
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7,
            7, 6, 12, 7, 9, 5, 5
        ]
    }, {
        name: "Austria",
        data: [
            0, 3, 4, 2, 4, 0, 0, 8, 8, 11, 6, 12, 11, 5, 6, 7, 1, 10,
            21, 9, 17, 17, 23, 16, 17
        ]
    }, {
        name: "Sweden",
        data: [
            0, 2, 5, 3, 7, 0, 0, 10, 4, 10, 7, 7, 8, 4, 2, 4, 8, 6, 4,
            3, 3, 7, 14, 11, 15
        ]
    }, {
        name: "Norway",
        data: [
            0, 17, 15, 10, 15, 0, 0, 10, 16, 4, 6, 15, 14, 12, 7, 10,
            9, 5, 20, 26, 25, 25, 19, 23, 26
        ]
    }, {
        name: "U.S.",
        data: [
            0, 4, 6, 12, 4, 0, 0, 9, 11, 7, 10, 7, 7, 8, 10, 12, 8, 6,
            11, 13, 13, 34, 25, 37, 28
        ]
    }, {
        name: "East Germany",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 14, 19, 23, 24, 25,
            0, 0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "West Germany",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 10, 5, 4, 8, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Germany",
        data: [
            0, 0, 1, 2, 6, 0, 0, 0, 7, 2, 8, 9, 0, 0, 0, 0, 0, 0, 26,
            24, 29, 36, 29, 30, 19
        ]
    }, {
        name: "Netherlands",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 9, 9, 6, 4, 0, 7, 4,
            4, 11, 8, 9, 8, 24
        ]
    }, {
        name: "Italy",
        data: [
            0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 4, 4, 5, 4, 2, 2, 5, 14,
            20, 10, 13, 11, 5, 8
        ]
    }, {
        name: "Canada",
        data: [
            0, 1, 1, 7, 1, 0, 0, 3, 2, 3, 4, 3, 3, 1, 3, 2, 4, 5, 7,
            13, 15, 17, 24, 26, 25
        ]
    }, {
        name: "Switzerland",
        data: [
            0, 3, 1, 1, 3, 0, 0, 10, 2, 6, 2, 0, 6, 10, 5, 5, 5, 15,
            3, 9, 7, 11, 14, 9, 11
        ]
    }, {
        name: "Great Britain",
        data: [
            0, 4, 1, 0, 3, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0,
            2, 1, 2, 1, 1, 4
        ]
    }, {
        name: "France",
        data: [
            0, 3, 1, 1, 1, 0, 0, 5, 1, 0, 3, 7, 9, 3, 1, 1, 3, 2, 9,
            5, 8, 11, 9, 11, 15
        ]
    }, {
        name: "Hungary",
        data: [
            0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Unified Team",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Soviet Union",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 21, 25, 13, 16, 27, 22, 25,
            29, 0, 0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Russia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 18, 13, 22, 15, 33
        ]
    }, {
        name: "Japan",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 1, 1, 1, 7,
            5, 10, 2, 1, 5, 8
        ]
    }, {
        name: "Czechoslovakia",
        data: [
            0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 4, 3, 1, 1, 6, 3, 3,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Poland",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 2, 6, 6
        ]
    }, {
        name: "Spain",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "China",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
            3, 8, 8, 11, 11, 9
        ]
    }, {
        name: "South Korea",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,
            6, 6, 4, 11, 14, 8
        ]
    }, {
        name: "Czech Republic",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 3, 4, 6, 8
        ]
    }, {
        name: "Belarus",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 2, 1, 1, 3, 6
        ]
    }, {
        name: "Kazakhstan",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            3, 2, 0, 0, 1, 1
        ]
    }, {
        name: "Bulgaria",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 1, 3, 1, 0, 0
        ]
    }, {
        name: "Denmark",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0
        ]
    }, {
        name: "Ukraine",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 0, 2, 0, 2
        ]
    }, {
        name: "Australia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 2, 2, 3, 3
        ]
    }, {
        name: "Belgium",
        data: [
            0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0
        ]
    }, {
        name: "Romania",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Liechtenstein",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 2, 1, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Yugoslavia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Luxembourg",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "New Zealand",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "North Korea",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        name: "Slovakia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 3, 1
        ]
    }, {
        name: "Croatia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 4, 3, 3, 1
        ]
    }, {
        name: "Slovenia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            3, 0, 1, 0, 3, 8
        ]
    }, {
        name: "Latvia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 2, 4
        ]
    }, {
        name: "Estonia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 3, 3, 1, 0
        ]
    }, {
        name: "Uzbekistan",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""
pie_chart = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Rating Counts'
    },
    tooltip: {
        pointFormat: '<b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def main() -> None:
    jp.justpy(app)


def app():
    # Getting the data
    data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])

    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews',
                 classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')

    if sys.argv[1] == 'Course':
        if sys.argv[2] == 'Area':
            hc = jp.HighCharts(a=wp, options=area_spline_chart)
            by_course_app(hc, data)
        else:
            hc = jp.HighCharts(a=wp, options=stream_chart)
            by_course_app(hc, data)
    elif sys.argv[1] == 'Pie':
        hc = jp.HighCharts(a=wp, options=pie_chart)
        by_count(hc, data)
    else:
        hc = jp.HighCharts(a=wp, options=spline_chart)
        if sys.argv[1] == 'Day':
            by_day_app(hc, data)
        elif sys.argv[1] == 'Week':
            by_week_app(hc, data)
        elif sys.argv[1] == 'Month':
            by_month_app(hc, data)
        else:
            by_day_of_week(hc, data)

    return wp


def by_day_app(hc, data):
    data['Day'] = data['Timestamp'].dt.date
    day_average = data.groupby(['Day']).mean()

    hc.options.title.text = 'Average Rating by Day'
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average['Rating'])


def by_week_app(hc, data):
    data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
    week_average = data.groupby(['Week']).mean()

    hc.options.title.text = 'Average Rating by Week'
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])


def by_day_of_week(hc, data):
    data['Weekday'] = data['Timestamp'].dt.strftime('%A')
    data['Daynumber'] = data['Timestamp'].dt.strftime('%w')
    weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
    weekday_average = weekday_average.sort_values('Daynumber')

    hc.options.title.text = 'Average Rating by Day of Week'
    hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
    hc.options.series[0].data = list(weekday_average['Rating'])


def by_month_app(hc, data):
    data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
    month_average = data.groupby(['Month']).mean()

    hc.options.title.text = 'Average Rating by Month'
    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average['Rating'])


def by_course_app(hc, data):
    data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
    month_average_crs = data.groupby(['Month', 'Course Name']).mean().unstack()

    hc.options.title.text = 'Average Rating by Course by Month'
    hc.options.xAxis.categories = list(month_average_crs.index)
    hc_data = [{'name': course_name, 'data': [ratings for ratings in month_average_crs[course_name]]}
               for course_name in month_average_crs.columns]
    hc.options.series = hc_data


def by_count(hc, data):
    share = data.groupby(['Course Name'])['Rating'].count()

    hc_data = [{'name': course_name, 'y': count}
               for course_name, count in zip(share.index, share)]
    for pie in hc_data:
        if pie['y'] == share.max():
            pie['sliced'] = 'true'
            pie['selected'] = 'true'
    hc.options.series[0].data = hc_data


if __name__ == '__main__':
    main()

