from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.colors import HexColor


def draw_bar_chart(min, max, x_list, data=[()], x_label_angle=0, bar_color=HexColor("#7BB8E7"), height=125, width=280):
    '''
    :param min: 设置y轴的最小值
    :param max: 设置y轴的最大值
    :param x_list: x轴上的标签
    :param data: y轴对应标签的值
    :param x_label_angle: x轴上标签的倾斜角度
    :param bar_color: 柱的颜色  可以是含有多种颜色的列表
    :param height: 柱状图的高度
    :param width: 柱状图的宽度
    :return:
    '''
    bc = VerticalBarChart()
    bc.x = 50            # x和y是柱状图在框中的坐标
    bc.y = 50
    bc.height = height  # 柱状图的高度
    bc.width = width    # 柱状图的宽度
    bc.data = data
    for j in xrange(len(x_list)):
        setattr(bc.bars[j], 'fillColor', bar_color)  # bar_color若含有多种颜色在这里分配bar_color[j]
    # 调整step
    minv = min * 0.5
    maxv = max * 1.5
    maxAxis = int(height/10)
    # 向上取整
    minStep = int((maxv-minv+maxAxis-1)/maxAxis)

    bc.valueAxis.valueMin = min * 0.5      #设置y轴的最小值
    bc.valueAxis.valueMax = max * 1.5      #设置y轴的最大值
    bc.valueAxis.valueStep = (max-min)/4   #设置y轴的最小度量单位
    if bc.valueAxis.valueStep < minStep:
        bc.valueAxis.valueStep = minStep
    if bc.valueAxis.valueStep == 0:
        bc.valueAxis.valueStep = 1
    bc.categoryAxis.labels.boxAnchor = 'ne'   # x轴下方标签坐标的开口方向
    bc.categoryAxis.labels.dx = -5           # x和y是x轴下方的标签距离x轴远近的坐标
    bc.categoryAxis.labels.dy = -5
    bc.categoryAxis.labels.angle = x_label_angle   # x轴上描述文字的倾斜角度
    # bc.categoryAxis.labels.fontName = 'song'
    x_real_list = []
    if len(x_list) > 10:
        for i in range(len(x_list)):
            tmp = '' if i%5 != 0 else x_list[i]
            x_real_list.append(tmp)
    else:
        x_real_list = x_list
    bc.categoryAxis.categoryNames = x_real_list
    return bc


z = autoLegender(draw_bar_chart(100, 300, ['a', 'b', 'c'], [(100, 200, 120)]))

pdf=SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([z])