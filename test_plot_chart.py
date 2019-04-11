from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.piecharts import Pie

def autoLegender( chart,title=''):
    width = 448
    height = 230
    d = Drawing(width,height)
    lab = Label()
    lab.x = 220  #x和y是文字的位置坐标
    lab.y = 210
    lab.setText(title)
    # lab.fontName = 'song' #增加对中文字体的支持
    lab.fontSize = 20
    d.add(lab)
    d.background = Rect(0,0,width,height,strokeWidth=1,strokeColor="#868686",fillColor=None) #边框颜色
    d.add(chart)

    return d


def draw_pie(data=[], labels=[], use_colors=[], width=360,):
    '''更多属性请查询reportlab.graphics.charts.piecharts.WedgeProperties'''

    pie = Pie()
    pie.x = 60 # x,y饼图在框中的坐标
    pie.y = 20
    pie.slices.label_boxStrokeColor = colors.white  #标签边框的颜色

    pie.data = data      # 饼图上的数据
    pie.labels = labels  # 数据的标签
    pie.simpleLabels = 0 # 0 标签在标注线的右侧；1 在线上边
    pie.sameRadii = 1    # 0 饼图是椭圆；1 饼图是圆形

    pie.slices.strokeColor = colors.red       # 圆饼的边界颜色
    pie.strokeWidth=1                         # 圆饼周围空白区域的宽度
    pie.strokeColor= colors.white             # 整体饼图边界的颜色
    pie.slices.label_pointer_piePad = 10       # 圆饼和标签的距离
    pie.slices.label_pointer_edgePad = 25    # 标签和外边框的距离
    pie.width = width
    pie.direction = 'clockwise'
    pie.pointerLabelMode  = 'LeftRight'
    # for i in range(len(labels)):
    #     pie.slices[i].fontName = 'song' #设置中文
    for i, col in enumerate(use_colors):
         pie.slices[i].fillColor  = col
    return pie


data = [10,9,8,7,6,5,4,3,2,1]
labs = ['0000000','1111111','2222222','3333333','4444444',
        '5555555','6666666','7777777','8888888','9999999']
color = [HexColor("#696969"),HexColor("#A9A9A9"),HexColor("#D8BFD8"),
         HexColor("#DCDCDC"),HexColor('#E6E6FA'),HexColor("#B0C4DE"),
         HexColor("#778899"),HexColor('#B0C4DE'),HexColor("#6495ED"),
         HexColor("#483D8B")
         ]
z = autoLegender(draw_pie(data,labs,color),labs,color)

pdf=SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([z])