# coding:utf8

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx #导入wxpyhton，pyhton自带的GUI库
#import wx.xrc

import pymysql #用于操作数据库
import sys
import importlib
importlib.reload(sys)


###########################################################################
## Class MyFrame1
###########################################################################

#建一个窗口类MyFrame1继承wx.Frame
class MyFrame1(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"桃太郎外卖信息管理系统", pos=wx.DefaultPosition, size=wx.Size(610, 400),style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.Center()

 # 小构件，如按钮，文本框等被放置在面板窗口。 wx.Panel类通常是被放在一个wxFrame对象中。这个类也继承自wxWindow类。
        self.m_panel1 = wx.Panel(self)
 # 标签，一行或多行的只读文本，Wx.StaticText(parent, id, label, position, size, style)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"外卖菜品：", (20, 20))
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"菜品信息", (130, 20), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"菜品上架", (250, 20), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button3 = wx.Button(self.m_panel1, wx.ID_ANY, u"菜品下架", (370, 20), wx.DefaultSize,style=wx.BORDER_MASK)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"派送员管理：", (20, 90))
        self.m_button4 = wx.Button(self.m_panel1, wx.ID_ANY, u"派送员信息", (130, 90), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button5 = wx.Button(self.m_panel1, wx.ID_ANY, u"聘请派送员", (250, 90), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button6 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇派送员", (370, 90), wx.DefaultSize,style=wx.BORDER_MASK)

        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"客服人员管理：", (20, 160))
        self.m_button7 = wx.Button(self.m_panel1, wx.ID_ANY, u"客服人员信息", (130, 160), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button8 = wx.Button(self.m_panel1, wx.ID_ANY, u"聘请客服人员", (250, 160), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button9 = wx.Button(self.m_panel1, wx.ID_ANY, u"解雇客服人员", (370, 160), wx.DefaultSize,style=wx.BORDER_MASK)

        self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"订单管理：", (20, 230))
        self.m_button10 = wx.Button(self.m_panel1, wx.ID_ANY, u"订单信息", (130, 230), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button11 = wx.Button(self.m_panel1, wx.ID_ANY, u"学生订餐", (250, 230), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button12 = wx.Button(self.m_panel1, wx.ID_ANY, u"取消订单", (370, 230), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button13 = wx.Button(self.m_panel1, wx.ID_ANY, u"修改订单", (490, 230), wx.DefaultSize,style=wx.BORDER_MASK)

        self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"物流管理：", (20, 300))
        self.m_button14 = wx.Button(self.m_panel1, wx.ID_ANY, u"配送信息", (130, 300), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button15 = wx.Button(self.m_panel1, wx.ID_ANY, u"安排配送", (250, 300), wx.DefaultSize,style=wx.BORDER_MASK)
        self.m_button16 = wx.Button(self.m_panel1, wx.ID_ANY, u"取消配送", (370, 300), wx.DefaultSize,style=wx.BORDER_MASK)


 #按钮绑定对话框的弹出
 #在创建应用程序时，Bind函数可以将按钮的动作与特定的函数绑定，当按钮上有动作时，这个函数就会启动，从而处理响应的事件。
 #个Button被单击发生了EVT_BUTTON事件
        self.m_button1.Bind(wx.EVT_BUTTON, MyDialog11(None).OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, MyDialog12(None).OnClick)
        self.m_button3.Bind(wx.EVT_BUTTON, MyDialog13(None).OnClick)

        self.m_button4.Bind(wx.EVT_BUTTON, MyDialog21(None).OnClick)
        self.m_button5.Bind(wx.EVT_BUTTON, MyDialog22(None).OnClick)
        self.m_button6.Bind(wx.EVT_BUTTON, MyDialog23(None).OnClick)

        self.m_button7.Bind(wx.EVT_BUTTON, MyDialog31(None).OnClick)
        self.m_button8.Bind(wx.EVT_BUTTON, MyDialog32(None).OnClick)
        self.m_button9.Bind(wx.EVT_BUTTON, MyDialog33(None).OnClick)

        self.m_button10.Bind(wx.EVT_BUTTON, MyDialog41(None).OnClick)
        self.m_button11.Bind(wx.EVT_BUTTON, MyDialog42(None).OnClick)
        self.m_button12.Bind(wx.EVT_BUTTON, MyDialog43(None).OnClick)
        self.m_button13.Bind(wx.EVT_BUTTON, MyDialog44(None).OnClick)

        self.m_button14.Bind(wx.EVT_BUTTON, MyDialog51(None).OnClick)
        self.m_button15.Bind(wx.EVT_BUTTON, MyDialog52(None).OnClick)
        self.m_button16.Bind(wx.EVT_BUTTON, MyDialog53(None).OnClick)

 #设置按钮的背景颜色
        self.m_button1.SetBackgroundColour('#0a74f7')
        self.m_button1.SetForegroundColour('white')
        self.m_button2.SetBackgroundColour('#0a74f7')
        self.m_button2.SetForegroundColour('white')
        self.m_button3.SetBackgroundColour('#0a74f7')
        self.m_button3.SetForegroundColour('white')

        self.m_button4.SetBackgroundColour('#238E23')
        self.m_button4.SetForegroundColour('white')
        self.m_button5.SetBackgroundColour('#238E23')
        self.m_button5.SetForegroundColour('white')
        self.m_button6.SetBackgroundColour('#238E23')
        self.m_button6.SetForegroundColour('white')

        self.m_button7.SetBackgroundColour('#6F4242')
        self.m_button7.SetForegroundColour('white')
        self.m_button8.SetBackgroundColour('#6F4242')
        self.m_button8.SetForegroundColour('white')
        self.m_button9.SetBackgroundColour('#6F4242')
        self.m_button9.SetForegroundColour('white')

        self.m_button10.SetBackgroundColour('#8E6B23')
        self.m_button10.SetForegroundColour('white')
        self.m_button11.SetBackgroundColour('#8E6B23')
        self.m_button11.SetForegroundColour('white')
        self.m_button12.SetBackgroundColour('#8E6B23')
        self.m_button12.SetForegroundColour('white')
        self.m_button13.SetBackgroundColour('#8E6B23')
        self.m_button13.SetForegroundColour('white')

        self.m_button14.SetBackgroundColour('#545454')
        self.m_button14.SetForegroundColour('white')
        self.m_button15.SetBackgroundColour('#545454')
        self.m_button15.SetForegroundColour('white')
        self.m_button16.SetBackgroundColour('#545454')
        self.m_button16.SetForegroundColour('white')

        self.m_panel1.SetBackgroundColour('white') #设置面板的背景颜色


###########################################################################
## Class MyDialog11
###########################################################################

#一个对话框的类继承wx.Dialog
class MyDialog11(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品信息", pos=wx.DefaultPosition, size=wx.Size(302, 362),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "菜品名称", (20, 20))
        wx.StaticText(self.panel, -1, "月销量", (80, 20))

    def OnClick(self, event):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()
        try:
            sql = "select * from foodshop"
            cursor.execute(sql)
            rs = cursor.fetchall()
            h = 30
            for row in rs:
                h = h + 20
                shop_name = row[0]
                salenum = row[1] #注意数据库中的数据为数字 int 类型时的读取方式 id = '%d' % i[0]
                wx.StaticText(self.panel, -1, shop_name, (20, h))
                wx.StaticText(self.panel, -1, salenum, (80, h))
        except:
          conn.rollback()
        finally:
          cursor.close()
          conn.close() 

        self.ShowModal()


###########################################################################
## Class MyDialog12
###########################################################################

class MyDialog12(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品上架", pos=wx.DefaultPosition, size=wx.Size(302, 250),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入菜品名称：", (20, 20))
 # 可编辑文本框的创建使用wx.TextCtrl，默认情况下，文本框只能编辑一行文字（无论文字多长均不换行）
        self.t1 = wx.TextCtrl(self.panel, pos=(130, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入月销量：", (20, 80))
        self.t2 = wx.TextCtrl(self.panel, pos=(130, 80), size=(120, 25))


    def OnClick(self, e):
        dialog12 = MyDialog12(None)
        btn = wx.Button(parent=dialog12.panel, label="上架", pos=(20, 150), size=(100, 45), style=wx.BORDER_MASK)
        btn.Bind(wx.EVT_BUTTON, dialog12.insert)
        dialog12.ShowModal()

    def insert(self, event):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()

        shop_name = self.t1.GetValue().encode('utf8') #注意GetValue()获取的是unicode编码，
        salenum = self.t2.GetValue().encode('utf8') #你使用的#coding=utf8，那就对获取的数据.encode('utf8')重新编码
        data = (shop_name, salenum)
        try:
            sql = "insert into foodshop values (%s,%s)"
            cursor.execute(sql, data)
            conn.commit() #提交给后台数据库
            dial = wx.MessageDialog(None, '成功上架!', '结果', wx.YES_NO) # 创建一个带按钮的消息框, 语法是(self, 框中内容, 框标题, ID)
            dial.ShowModal() # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

###########################################################################
## Class MyDialog13
###########################################################################

class MyDialog13(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"菜品下架", pos=wx.DefaultPosition, size=wx.Size(200, 200),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "菜品名称：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))


    def OnClick(self, e):
        dialog13 = MyDialog13(None)
        btn = wx.Button(parent=dialog13.panel, label="下架", pos=(20, 90), size=(90, 40))
        btn.Bind(wx.EVT_BUTTON, dialog13.delete)
        dialog13.ShowModal()

    def delete(self, e):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()

        shop_name = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码
        try:
            sql = "delete from foodshop where shop_name=%s"
            cursor.execute(sql, shop_name)
            conn.commit()
            dial = wx.MessageDialog(None, '成功下架!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal() # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

###########################################################################
## Class MyDialog21
###########################################################################

class MyDialog21(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"派送员信息", pos=wx.DefaultPosition, size=wx.Size(400, 415),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "菜品名称：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        #btn = wx.Button(parent=self.panel, label="查询", pos=(240, 20), size=(70, 25))
        #btn.Bind(wx.EVT_BUTTON, self.find)
        wx.StaticText(self.panel, -1, "派送员编号", (20, 60))
        wx.StaticText(self.panel, -1, "派送员姓名", (120, 60))
        wx.StaticText(self.panel, -1, "派送员电话", (220, 60))

    def OnClick(self, event):
        dialog21 = MyDialog21(None)
        btn = wx.Button(parent=dialog21.panel, label="查询", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog21.find)
        dialog21.ShowModal()

    def find(self, event):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor=conn.cursor()
        try:
            sql = "select * from courier"
            cursor.execute(sql)
            rs = cursor.fetchall()
            h = 80
            for row in rs:
                if row[3] == self.t1.GetValue():
                    h = h + 20
                    courier_id = row[0]
                    courier_name = row[1]
                    courier_phone = row[2]
                    wx.StaticText(self.panel, -1, courier_id, (20, h))
                    wx.StaticText(self.panel, -1, courier_name, (120, h))
                    wx.StaticText(self.panel, -1, courier_phone, (220, h))
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog22
###########################################################################

class MyDialog22(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"聘请派送员", pos=wx.DefaultPosition, size=wx.Size(400, 350),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入菜品名称：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(140, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入派送员编号：", (20, 80))
        self.t2 = wx.TextCtrl(self.panel, pos=(140, 80), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入派送员姓名：", (20, 140))
        self.t3 = wx.TextCtrl(self.panel, pos=(140, 140), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入派送员电话：", (20, 200))
        self.t4 = wx.TextCtrl(self.panel, pos=(140, 200), size=(120, 25))

    def OnClick(self, e):
        dialog22 = MyDialog22(None)
        btn = wx.Button(parent=dialog22.panel, label="聘请", pos=(20, 250), size=(100, 45))
        btn.Bind(wx.EVT_BUTTON, dialog22.insert)
        dialog22.ShowModal()

    def insert(self, e):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()

        shop_name = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码，
        courier_id = self.t2.GetValue().encode('utf8') # 你使用的#coding=utf8，那就对获取的数据.encode('utf8')
        courier_name = self.t3.GetValue().encode('utf8')
        courier_phone = self.t4.GetValue().encode('utf8')

        data = (courier_id, courier_name, courier_phone, shop_name)

        try:
            sql = "insert into courier values (%s,%s,%s,%s)"
            cursor.execute(sql, data)
            conn.commit()
            dial = wx.MessageDialog(None, '成功聘请派送员!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal() # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog23
###########################################################################

class MyDialog23(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"解雇派送员", pos=wx.DefaultPosition, size=wx.Size(200, 200),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "派送员编号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))

    def OnClick(self, e):
        dialog23 = MyDialog23(None)
        btn = wx.Button(parent=dialog23.panel, label="解雇", pos=(20, 90), size=(90, 40))
        btn.Bind(wx.EVT_BUTTON, dialog23.delete)
        dialog23.ShowModal()

    def delete(self, e):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()
        courier_id = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码
        try:
            sql = "delete from courier where courier_id=%s"
            cursor.execute(sql, courier_id)
            conn.commit()
            dial = wx.MessageDialog(None, '成功解雇派送员!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal() # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog31
###########################################################################

class MyDialog31(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"客服人员信息", pos=wx.DefaultPosition, size=wx.Size(400, 401),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "菜品名称：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
        wx.StaticText(self.panel, -1, "客服人员编号", (20, 60))
        wx.StaticText(self.panel, -1, "客服人员姓名", (120, 60))

    def OnClick(self, e):
        dialog31 = MyDialog31(None)
        btn = wx.Button(parent=dialog31.panel, label="查询", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog31.find)
        dialog31.ShowModal()

    def find(self, event):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()
        try:
            sql = "select * from server"
            cursor.execute(sql)
            rs = cursor.fetchall()
            h = 80
            for row in rs:
                if row[2] == self.t1.GetValue():
                    h = h + 20
                    server_id = row[0]
                    server_name = row[1]
                    wx.StaticText(self.panel, -1, server_id, (20, h))
                    wx.StaticText(self.panel, -1, server_name, (120, h))
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog32
###########################################################################

class MyDialog32(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"聘请客服人员", pos=wx.DefaultPosition, size=wx.Size(400, 300),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "请输入菜品名称：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(160, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入客服人员编号：", (20, 80))
        self.t2 = wx.TextCtrl(self.panel, pos=(160, 80), size=(120, 25))

        wx.StaticText(self.panel, -1, "请输入客服人员姓名：", (20, 140))
        self.t3 = wx.TextCtrl(self.panel, pos=(160, 140), size=(120, 25))


    def OnClick(self, e):
        dialog32 = MyDialog32(None)
        btn = wx.Button(parent=dialog32.panel, label="聘请", pos=(20, 200), size=(100, 45))
        btn.Bind(wx.EVT_BUTTON, dialog32.insert)
        dialog32.ShowModal()

    def insert(self, e):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()

        shop_name = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码，
        server_id = self.t2.GetValue().encode('utf8') # 你使用的#coding=utf8，那就对获取的数据.encode('utf8')
        server_name = self.t3.GetValue().encode('utf8')

        data = (server_id, server_name, shop_name)

        try:
            sql = "insert into server values(%s,%s,%s)"
            cursor.execute(sql, data)
            conn.commit()
            dial = wx.MessageDialog(None, '成功聘请客服!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal() # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog33
###########################################################################

class MyDialog33(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"解雇客服人员", pos=wx.DefaultPosition, size=wx.Size(200, 200),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "客服人员编号：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))

    def OnClick(self, e):
        dialog33 = MyDialog33(None)
        btn = wx.Button(parent=dialog33.panel, label="解雇", pos=(20, 90), size=(90, 40))
        btn.Bind(wx.EVT_BUTTON, dialog33.delete)
        dialog33.ShowModal()

    def delete(self, e):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()
        server_id = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码
        try:
            sql = "delete from server where server_id=%s"
            cursor.execute(sql, server_id)
            conn.commit()
            dial = wx.MessageDialog(None, '成功解雇客服!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
            dial.ShowModal() # 显示对话框
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog41
###########################################################################

class MyDialog41(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"订单信息", pos=wx.DefaultPosition, size=wx.Size(500, 400),style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
        self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))

        wx.StaticText(self.panel, -1, "客服人员编号", (20, 60))
        wx.StaticText(self.panel, -1, "订单编号", (120, 60))
        wx.StaticText(self.panel, -1, "订单金额", (220, 60))
        wx.StaticText(self.panel, -1, "订餐方式", (320, 60))

    def OnClick(self, e):
        dialog41 = MyDialog41(None)
        btn = wx.Button(parent=dialog41.panel, label="查询", pos=(240, 20), size=(70, 25))
        btn.Bind(wx.EVT_BUTTON, dialog41.find)
        dialog41.ShowModal()

    def find(self, event):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
        cursor = conn.cursor()
        try:
            sql = "select * from book"
            cursor.execute(sql)
            rs = cursor.fetchall()
            h = 80
            for row in rs:
                if row[0] == self.t1.GetValue():
                    h = h + 20
                    server_id = row[1]
                    order_id = row[2]
                    order_money = row[3]
                    order_way = row[4]
                    wx.StaticText(self.panel, -1, server_id, (20, h))
                    wx.StaticText(self.panel, -1, order_id, (120, h))
                    wx.StaticText(self.panel, -1, order_money, (220, h))
                    wx.StaticText(self.panel, -1, order_way, (320, h))
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


###########################################################################
## Class MyDialog42
###########################################################################

class MyDialog42(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"学生订餐", pos=wx.DefaultPosition, size=wx.Size(400, 400),style=wx.DEFAULT_DIALOG_STYLE)
		self.Center()
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('white')
		wx.StaticText(self.panel, -1, "请输入买家电话：", (20, 20))
	
		self.t1 = wx.TextCtrl(self.panel, pos=(150, 20), size=(120, 25))
		wx.StaticText(self.panel, -1, "请输入客服人员编号：", (20, 80))
		self.t2 = wx.TextCtrl(self.panel, pos=(150, 80), size=(120, 25))
		wx.StaticText(self.panel, -1, "请输入订单编号：", (20, 140))
		self.t3 = wx.TextCtrl(self.panel, pos=(150, 140), size=(120, 25))
		wx.StaticText(self.panel, -1, "请输入订单金额：", (20, 200))
		self.t4 = wx.TextCtrl(self.panel, pos=(150, 200), size=(120, 25))
		wx.StaticText(self.panel, -1, "请输入订餐方式：", (20, 260))
		self.t5 = wx.TextCtrl(self.panel, pos=(150, 260), size=(120, 25))
	
	def OnClick(self, e):
		dialog42 = MyDialog42(None)
		btn = wx.Button(parent=dialog42.panel, label="订餐", pos=(20, 310), size=(100, 45))
		btn.Bind(wx.EVT_BUTTON, dialog42.insert)
		dialog42.ShowModal()

	def insert(self, e):
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
		cursor = conn.cursor()
		student_phone = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码，
		server_id = self.t2.GetValue().encode('utf8') # 你使用的#coding=utf8，那就对获取的数据.encode('utf8')
		order_id = self.t3.GetValue().encode('utf8')
		order_money = self.t4.GetValue().encode('utf8')
		order_way = self.t5.GetValue().encode('utf8')
		data = (student_phone, server_id, order_id, order_money, order_way)

		try:
			sql = "insert into book values(%s,%s,%s,%s,%s)"
			cursor.execute(sql, data)
			conn.commit()
			dial = wx.MessageDialog(None, '成功订餐!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
			dial.ShowModal() # 显示对话框
		except:
			conn.rollback()
		finally:
			cursor.close()
			conn.close()


###########################################################################
## Class MyDialog43
###########################################################################

class MyDialog43(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"删除订单", pos=wx.DefaultPosition, size=wx.Size(300, 300),style=wx.DEFAULT_DIALOG_STYLE)
		self.Center()
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('white')

		wx.StaticText(self.panel, -1, "客服人员编号：", (20, 20))
		self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))

		wx.StaticText(self.panel, -1, "买家电话：", (20, 90))
		self.t2 = wx.TextCtrl(self.panel, pos=(20, 120), size=(120, 25))

	def OnClick(self, e):
		dialog43 = MyDialog43(None)
		btn = wx.Button(parent=dialog43.panel, label="取消订单", pos=(20, 170), size=(90, 40))
		btn.Bind(wx.EVT_BUTTON, dialog43.delete)
		dialog43.ShowModal()

	def delete(self, e):
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
		cursor = conn.cursor()

		server_id = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码
		student_phone = self.t2.GetValue().encode('utf8')
		data = (server_id, student_phone)

		try:
			sql = "delete from book where server_id=%s and student_phone=%s"
			cursor.execute(sql, data)
			conn.commit()
			dial = wx.MessageDialog(None, '成功删除订单!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
			dial.ShowModal() # 显示对话框
		except:
			conn.rollback()
		finally:
			cursor.close()
			conn.close()


###########################################################################
## Class MyDialog44
###########################################################################

class MyDialog44(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"修改订单", pos=wx.DefaultPosition, size=wx.Size(400, 300),style=wx.DEFAULT_DIALOG_STYLE)
		self.Center()
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('white')

		wx.StaticText(self.panel, -1, "请输入客服编号：", (20, 20))
		self.t1 = wx.TextCtrl(self.panel, pos=(160, 20), size=(120, 25))

		wx.StaticText(self.panel, -1, "请输入买家电话：", (20, 80))
		self.t2 = wx.TextCtrl(self.panel, pos=(160, 80), size=(120, 25))

		wx.StaticText(self.panel, -1, "请更正订单金额：", (20, 140))
		self.t3 = wx.TextCtrl(self.panel, pos=(160, 140), size=(120, 25))

	def OnClick(self, e):
		dialog44 = MyDialog44(None)
		btn = wx.Button(parent=dialog44.panel, label="确认修改", pos=(20, 200), size=(100, 45))
		btn.Bind(wx.EVT_BUTTON, dialog44.change)
		dialog44.ShowModal()

	def change(self, e):
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
		cursor = conn.cursor()

		server_id = self.t1.GetValue().encode('utf8')
		student_phone = self.t2.GetValue().encode('utf8')
		order_money = self.t3.GetValue().encode('utf8')
		data = (order_money, server_id, student_phone)

		try:
			sql = "update book set order_money=%s where server_id=%s and student_phone=%s"
			cursor.execute(sql, data)
			conn.commit()
			dial = wx.MessageDialog(None, '成功修改订单!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
			dial.ShowModal() # 显示对话框
		except:
			conn.rollback()
		finally:
			cursor.close()
			conn.close()


###########################################################################
## Class MyDialog51
###########################################################################

class MyDialog51(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"配送信息", pos=wx.DefaultPosition, size=wx.Size(502, 362),style=wx.DEFAULT_DIALOG_STYLE)
		self.Center()
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('white')

		wx.StaticText(self.panel, -1, "买家电话：", (20, 20))
		self.t1 = wx.TextCtrl(self.panel, pos=(90, 20), size=(120, 25))
		wx.StaticText(self.panel, -1, "派送员编号", (20, 60))
		wx.StaticText(self.panel, -1, "预计派送时间", (120, 60))


	def OnClick(self, e):
		dialog51 = MyDialog51(None)
		btn = wx.Button(parent=dialog51.panel, label="查询", pos=(240, 20), size=(70, 25))
		btn.Bind(wx.EVT_BUTTON, dialog51.find)
		dialog51.ShowModal()

	def find(self, event):
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
		cursor = conn.cursor()
		try:
			sql = "select * from delivery"
			cursor.execute(sql)
			rs = cursor.fetchall()
			h = 80
			for row in rs:
				if row[0] == self.t1.GetValue():
					h = h + 20
					courier_id = row[1]
					deliver_time = row[2]
					wx.StaticText(self.panel, -1, courier_id, (20, h))
					wx.StaticText(self.panel, -1, deliver_time, (120, h))
		except:
			conn.rollback()
		finally:
			cursor.close()
			conn.close()


###########################################################################
## Class MyDialog52
###########################################################################

class MyDialog52(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"安排配送", pos=wx.DefaultPosition, size=wx.Size(400, 300),style=wx.DEFAULT_DIALOG_STYLE)
		self.Center()
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('white')

		wx.StaticText(self.panel, -1, "请输入买家电话：", (20, 20))
		self.t1 = wx.TextCtrl(self.panel, pos=(160, 20), size=(120, 25))

		wx.StaticText(self.panel, -1, "请输入派送员编号：", (20, 80))
		self.t2 = wx.TextCtrl(self.panel, pos=(160, 80), size=(120, 25))

		wx.StaticText(self.panel, -1, "请输入预计派送时间：", (20, 140))
		self.t3 = wx.TextCtrl(self.panel, pos=(160, 140), size=(120, 25))

	def OnClick(self, e):
		dialog52 = MyDialog52(None)
		btn = wx.Button(parent=dialog52.panel, label="配送", pos=(20, 200), size=(100, 45))
		btn.Bind(wx.EVT_BUTTON, dialog52.insert)
		dialog52.ShowModal()

	def insert(self, e):
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='project', charset='utf8')
		cursor = conn.cursor()

		student_phone = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码，
		courier_id = self.t2.GetValue().encode('utf8') # 你使用的#coding=utf8，那就对获取的数据.encode('utf8')
		deliver_time = self.t3.GetValue().encode('utf8')

		data = (student_phone, courier_id, deliver_time)

		try:
			sql = "insert into delivery values(%s,%s,%s)"
			cursor.execute(sql, data)
			conn.commit()
			dial = wx.MessageDialog(None, '成功安排派送!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
			dial.ShowModal() # 显示对话框
		except:
			conn.rollback()
		finally:
			cursor.close()
			conn.close()


###########################################################################
## Class MyDialog53
###########################################################################

class MyDialog53(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"取消配送", pos=wx.DefaultPosition, size=wx.Size(300, 300),style=wx.DEFAULT_DIALOG_STYLE)
		self.Center()
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('white')

		wx.StaticText(self.panel, -1, "派送员编号：", (20, 20))
		self.t1 = wx.TextCtrl(self.panel, pos=(20, 50), size=(120, 25))

		wx.StaticText(self.panel, -1, "买家电话：", (20, 90))
		self.t2 = wx.TextCtrl(self.panel, pos=(20, 120), size=(120, 25))

	def OnClick(self, e):
		dialog53 = MyDialog53(None)
		btn = wx.Button(parent=dialog53.panel, label="取消配送", pos=(20, 170), size=(90, 40))
		btn.Bind(wx.EVT_BUTTON, dialog53.delete)
		dialog53.ShowModal()

	def delete(self, e):
		conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='wm', charset='utf8')
		cursor = conn.cursor()

		courier_id = self.t1.GetValue().encode('utf8') # 注意GetValue()获取的是unicode编码
		student_phone = self.t2.GetValue().encode('utf8')
		data = (courier_id, student_phone)

		try:
			sql = "delete from delivery where courier_id=%s and student_phone=%s"
			cursor.execute(sql, data)
			conn.commit()
			dial = wx.MessageDialog(None, '成功取消配送!', '结果', wx.YES_NO) # 创建一个带按钮的对话框, 语法是(self, 内容, 标题, ID)
			dial.ShowModal() # 显示对话框
		except:
			conn.rollback()
		finally:
			cursor.close()
			conn.close()


if __name__ == "__main__":
 app = wx.App()
 MyFrame1(None).Show()
 app.MainLoop()
