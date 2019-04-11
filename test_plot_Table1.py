from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('hei', 'SIMHEI.TTF'))
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
import time

elements = []

# TableStyle Commands
#  BACKGROUND, and TEXTCOLOR commands
data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data, colWidths=[100, 100, 100, 100, 100])
t.setStyle(TableStyle([('BACKGROUND', (1, 1), (-1, -1), colors.green),
                       ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))

elements.append(t)

data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data, colWidths=[100, 100, 100, 100, 100],
          style=[('GRID', (1, 1), (-2, -2), 1, colors.green),
                 ('BOX', (0, 0), (1, -1), 2, colors.red),
                 ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
                 ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
                 ])

elements.append(t)

data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data, 5 * [0.4 * inch], 4 * [0.4 * inch])
t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                       ('TEXTCOLOR', (1, 1), (-1, -2), colors.red),
                       ('VALIGN', (0, 0), (0, -1), 'TOP'),
                       ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                       ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                       ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                       ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                       ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                       ]))

elements.append(t)
# print(elements)

# TableStyle Line Commands

data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data, style=[('GRID', (1, 1), (-2, -2), 1, colors.green),
                       ('BOX', (0, 0), (1, -1), 2, colors.red),
                       ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
                       ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
                       ])

elements.append(t)

data = [['00', '01', '闪电', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
t = Table(data, style=[
    ('FONTNAME', (0, 0), (-1, -1), 'hei'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('GRID', (1, 1), (-2, -2), 1, colors.green),
    ('BOX', (0, 0), (1, -1), 2, colors.red),
    ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
    ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
    ('BACKGROUND', (0, 0), (0, 1), colors.pink),
    ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
    ('BACKGROUND', (2, 2), (2, 3), colors.orange),
])

elements.append(t)

# TableStyle Span Commands

data = [['Top\nLeft', '', '02', '03', '04'],
        ['', '', '12', '13', '14'],
        ['20', '21', '22', 'Bottom\nRight', ''],
        ['30', '31', '32', '', '']]
T = Table(data, style=[
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('BACKGROUND', (0, 0), (1, 1), colors.palegreen),
    ('SPAN', (0, 0), (1, 1)),
    ('BACKGROUND', (-2, -2), (-1, -1), colors.pink),
    ('SPAN', (-2, -2), (-1, -1)),
])

elements.append(T)

print(elements)
doc = SimpleDocTemplate('demo5.pdf')
doc.build(elements)
