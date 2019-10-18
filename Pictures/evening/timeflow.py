import chart_studio.plotly as plotly
import plotly.figure_factory as ff

gantt = [
    dict(Task='WFI start-up', Resource='WFI restart', 
        Start='2019-04-25 18:16:28', Finish='2019-04-25 18:20:22'),
    dict(Task='WFI start-up', Resource='WFI panels & filtre wheel',
        Start='2019-04-25 18:20:22', Finish='2019-04-25 18:22:25'),
    dict(Task='WFI start-up', Resource='WFI test OB', 
        Start='2019-04-25 18:22:55', Finish='2019-04-25 18:23:55'),
    dict(Task='TCS start-up', Resource='VME reboot & hydraulics', Group='G1', 
        Start='2019-04-25 18:16:28', Finish='2019-04-25 18:18:28'),
    dict(Task='TCS start-up', Resource='TCS initial checks',
        Start='2019-04-25 18:18:58', Finish='2019-04-25 18:19:58'),
    dict(Task='TCS start-up', Resource='TCS restart', 
        Start='2019-04-25 18:20:22', Finish='2019-04-25 18:27:03'),
    dict(Task='TCS start-up', Resource='Preset check', 
        Start='2019-04-25 18:27:44', Finish='2019-04-25 18:30:56'),
    dict(Task='TCS start-up', Resource='Focus check', 
        Start='2019-04-25 18:30:56', Finish='2019-04-25 18:32:28'),
    dict(Task='TCS start-up', Resource='Panels & final checks', 
        Start='2019-04-25 18:32:28', Finish='2019-04-25 18:34:52'),
    dict(Task='FEROS start-up', Resource='Start-up window 1',
        Start='2019-04-25 18:27:44', Finish='2019-04-25 18:29:47'),
    dict(Task='FEROS start-up', Resource='Start-up window 2',
        Start='2019-04-25 18:29:47', Finish='2019-04-25 18:33:47'),
    dict(Task='FEROS start-up', Resource='FEROS online',
        Start='2019-04-25 18:33:47', Finish='2019-04-25 18:34:47'),
    dict(Task='FEROS start-up', Resource='FEROS test OB',
        Start='2019-04-25 18:35:17', Finish='2019-04-25 18:36:17'),
    dict(Task='GROND start-up', Resource='Reset bob & shutters',
        Start='2019-04-25 18:16:28', Finish='2019-04-25 18:18:28'),
    dict(Task='GROND start-up', Resource='Test OBs with TCS ON',
        Start='2019-04-25 18:27:44', Finish='2019-04-25 18:30:44'),
    dict(Task='Guide cameras', Resource='GROND & FEROS AG',
        Start='2019-04-25 18:27:44', Finish='2019-04-25 18:30:44'),
    dict(Task='Guide cameras', Resource='WFI AG',
        Start='2019-04-25 18:32:28', Finish='2019-04-25 18:33:28'),
    dict(Task='WFI flats', Resource='Open covers and load OB', Group='G3',
        Start='2019-04-25 18:27:44', Finish='2019-04-25 18:29:44'),
    dict(Task='WFI flats', Resource='Preset to screen',
        Start='2019-04-25 18:30:56', Finish='2019-04-25 18:31:56'),
    dict(Task='WFI flats', Resource='Execute flats', 
        Start='2019-04-25 18:32:28', Finish='2019-04-25 18:38:28'),
    dict(Task='WFI flats', Resource='Park & close covers', 
        Start='2019-04-25 18:38:28', Finish='2019-04-25 18:39:28'),
    dict(Task='FEROS calibration', Resource='Set DRS date',
        Start='2019-04-25 18:16:28', Finish='2019-04-25 18:17:28'),
    dict(Task='FEROS calibration', Resource='Launch calibration',
        Start='2019-04-25 18:36:47', Finish='2019-04-25 18:37:47'),
]

color1a='rgb(200,0,0)'
color1b='rgb(199,0,0)'
color1c='rgb(198,0,0)'
color1d='rgb(197,0,0)'
color1e='rgb(196,0,0)'
color1f='rgb(195,0,0)'
color2a='rgb(0,200,0)'
color2b='rgb(0,199,0)'
color2c='rgb(0,198,0)'
color3a='rgb(0,0,200)'
color3b='rgb(0,0,199)'
color3c='rgb(0,0,198)'
color3d='rgb(0,0,197)'
color3e='rgb(0,0,196)'
color3f='rgb(0,0,195)'
color3g='rgb(0,0,194)'
color3h='rgb(0,0,193)'
color3i='rgb(0,0,192)'
color3j='rgb(0,0,191)'
color4a='rgb(80,80,80)'
color4b='rgb(79,79,79)'
color5a='rgb(100,0,100)'
color5b='rgb(99,0,99)'
color5c='rgb(98,0,98)'
colors={'Set DRS date': color1a,
        'WFI restart': color1b, 
        'Set DRS date': color1c,
        'VME reboot & hydraulics': color1d,
        'TCS initial checks': color1e,
        'Reset bob & shutters': color1f,
        'WFI panels & filtre wheel': color2a,
        'WFI test OB': color2b,
        'TCS restart': color2c,
        'Preset check': color3a,
        'Start-up window 1': color3b,
        'Start-up window 2': color3c,
        'FEROS online': color3d,
        'FEROS test OB': color3e,
        'Launch calibration': color3f,
        'Test OBs with TCS ON': color3g,
        'Open covers and load OB': color3h,
        'GROND & FEROS AG': color3i,
        'WFI AG': color3j,
        'Focus check': color4a,
        'Preset to screen': color4b,
        'Panels & final checks': color5a,
        'Execute flats': color5b,
        'Park & close covers': color5c,
       }

fig = ff.create_gantt(gantt, 
        title='Daily start-up & calibration',
        group_tasks=True, 
        index_col='Resource', colors=colors 
      )
fig.write_html('first_figure.html', auto_open=True)

