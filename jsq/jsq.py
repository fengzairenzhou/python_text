from tkinter import *
import math

class Jsq:      
      
      def __init__(self):
            root = Tk()
            self.root = root
            #界面布局
            self.root.title('计算器')            
            self.v = StringVar()
            self.v.set('0')

            self.a = False
            self.i = 1
            self.isysf = False
            self.lists = []

            self.menu()
            self.show_label()
            self.show_bord()
            root.mainloop()

      def menu(self):
            allmenu = Menu(self.root)
            findmenu = Menu(allmenu,tearoff=0)
            allmenu.add_cascade(menu = findmenu,label = '查看(V)')
            findmenu.add_command(label = '标准型')
            findmenu.add_command(label = '科学型')
            findmenu.add_command(label = '程序员')
            findmenu.add_command(label = '统计信息')

            editmenu = Menu(allmenu,tearoff=0)
            allmenu.add_cascade(menu = editmenu,label = '编辑(E)')
            editmenu.add_command(label = '复制')
            editmenu.add_command(label = '粘贴')
            editmenu.add_separator()
            editmenu.add_command(label = '历史记录')

            helpmenu = Menu(allmenu,tearoff=0)
            allmenu.add_cascade(menu = helpmenu,label = '帮助(H)')
            helpmenu.add_command(label = '查看帮助')
            helpmenu.add_separator()
            helpmenu.add_command(label = '关于计算器')

            self.root.config(menu = allmenu)

      def show_label(self):
            label = Label(self.root,textvariable =self.v, bg = '#888888',
                          width=15,height=2,font=("黑体", 20, "bold"),anchor='e')
            label.pack(padx = 10,pady = 10)

      def show_bord(self):
            frame_bord = Frame(width=400,height=350,bg='#cccccc')
            frame_bord.pack(padx = 10,pady = 10)

            button_qm = Button(frame_bord,text = '%',width = 7,bg='orange',
                                command=lambda:self.ysf('%'),
                               height =2).grid(row = 0,column = 0)
            button_kf = Button(frame_bord,text = '√',width = 7,bg='orange',
                                  command = self.kf,
                               height =2).grid(row = 0,column = 1)
            button_pf = Button(frame_bord,text = 'x²',width = 7,bg='orange',
                                command=self.pf,
                               height =2).grid(row = 0,column = 2)
            button_x = Button(frame_bord,text = '¹/x',width = 7,bg='orange',
                                command=self.qd,
                              height =2).grid(row = 0,column = 3)

            button_del = Button(frame_bord,text = '←',width = 7,bg='orange',
                                command = self.delete,
                                height =2).grid(row = 1,column = 2)
            button_ce = Button(frame_bord,text = 'CE',width = 7,bg='orange',
                                  command=self.ce,
                               height =2).grid(row = 1,column = 0)
            button_clear = Button(frame_bord,text = 'C',width = 7,bg='orange',
                                command=self.clear,
                                  height =2).grid(row = 1,column = 1)
            button_chu = Button(frame_bord,text = '÷',width = 7,bg='orange',
                               command=lambda:self.ysf('÷'),
                                height =2).grid(row = 1,column = 3)


            button_7 = Button(frame_bord,text = '7',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('7')).grid(row = 2,column = 0)
            button_8 = Button(frame_bord,text = '8',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('8')
                              ).grid(row = 2,column = 1)
            button_9 = Button(frame_bord,text = '9',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('9')
                              ).grid(row = 2,column = 2)
            button_cheng = Button(frame_bord,text = '×',width = 7,height =2,bg='orange',
                                command=lambda:self.ysf('×')).grid(row = 2,column = 3)

            button_4 = Button(frame_bord,text = '4',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('4')
                              ).grid(row = 3,column = 0)
            button_5 = Button(frame_bord,text = '5',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('5')
                              ).grid(row = 3,column = 1)
            button_6 = Button(frame_bord,text = '6',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('6')
                              ).grid(row = 3,column = 2)
            button_jian = Button(frame_bord,text = '-',width = 7,height =2,bg='orange',
                                 command=lambda:self.ysf('-')
                                 ).grid(row = 3,column = 3)

            button_1 = Button(frame_bord,text = '1',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('1')
                              ).grid(row = 4,column = 0)
            button_2 = Button(frame_bord,text = '2',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('2')
                              ).grid(row = 4,column = 1)
            button_3 = Button(frame_bord,text = '3',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('3')
                              ).grid(row = 4,column = 2)
            button_jia = Button(frame_bord,text = '+',width = 7,height =2,bg='orange',
                                  command=lambda:self.ysf('+')
                                ).grid(row = 4,column = 3)

            button_0 = Button(frame_bord,text = '0',width = 7,height =2,bg='orange',
                              command=lambda:self.shu('0')).grid(row = 5,column = 1)
            button_dian = Button(frame_bord,text = '.',width = 7,height =2,bg='orange',
                                 command=self.dian
                                 ).grid(row = 5,column = 2)
            button_deng = Button(frame_bord,text = '=',width = 7,height =2,bg='orange',
                                 command=self.jg
                                 ).grid(row = 5,column = 3)
            button_fan = Button(frame_bord,text = '±',width = 7,height =2,bg='orange',
                                command = self.qf
                                ).grid(row = 5,column = 0)

           
            
      def shu(self,num):
            #global isysf
            if self.a == True:
                  self.v.set(num)
                  self.a = False
                  return 
            if self.isysf == False:
                  if self.v.get()=='0':
                        self.v.set(num)
                  else:
                        result = self.v.get()+num
                        result = result[0:14]
                        self.v.set(result)
            else:
                  self.v.set(num)
                  self.isysf = False

      def dian(self):
            str1 = self.v.get()
            if '.' in str1:
                  pass
            else:
                  self.v.set(str1+'.')

      def ysf(self,sign):
            #global isysf
            #global lists
            self.isysf = True
            #print('ysf第几次',self.i)
            if self.i>1:                  
                  #print('0.0.0.0')
                  if sign == '+':
                        if self.lists != []:
                              self.lists.pop()
                        self.lists.append('+')
                  if sign == '-':
                        if self.lists != []:
                              self.lists.pop()
                        self.lists.append('-')
                  if sign == '×':
                        if self.lists != []:
                              self.lists.pop()
                        self.lists.append('*')
                  if sign == '÷':
                        if self.lists != []: 
                              self.lists.pop()
                        self.lists.append('/')
                  if sign == '%' :
                        if self.lists != []:
                              self.lists.pop()
                        self.lists.append('%')
                  print(self.lists)
                  
            else:
                  self.i = self.i+1
                  self.lists.append(self.v.get())
                  #print(self.lists)
                  if sign == '+':
                        self.lists.append('+')
                  if sign == '-':
                        self.lists.append('-')
                  if sign == '×':
                        self.lists.append('*')
                  if sign == '÷':
                        self.lists.append('/')
                  if sign == '%' :
                        self.lists.append('%')
                  #return self.i
            #print('ysf第几次',self.i)
                  print(self.lists)
                  

      def jg(self):
            #global lists
            self.i=1
            if self.lists != []:
                  if self.lists[-1] == '/':
                        if self.v.get()!='0.0' and self.v.get()!= '0':
                              self.lists.append(self.v.get())
                              print(self.lists)
                              strs = ''.join(self.lists)
                              if strs[-1] in '+-*/%':
                                    strs = strs[0:-1]
                              result = eval(strs)
                              result = str(result)
                              result = result[0:14]
                              print(result)
                              self.lists.clear()
                              self.v.set(result)
                              self.a= True
                        else:
                              self.v.set('除数不能为零')
                              self.lists.clear()
                              self.a= True
                        
                  else:
                        self.lists.append(self.v.get())
                        print(self.lists)
                        strs = ''.join(self.lists)
                        if strs[-1] in '+-*/%':
                              strs = strs[0:-1]
                        result = eval(strs)
                        result = str(result)
                        result = result[0:14]
                        print(result)
                        self.lists.clear()
                        self.v.set(result)
                        self.a= True
            else:
                  #strs = ''.join(self.lists)
                  #result = eval(strs)
                  #print(result)
                  #self.lists.clear()
                  self.v.set(self.v.get())
                  self.a = True
            #self.lists = []
      
      def delete(self):
            if self.isysf == True:
                  pass
            else:
                  num = len (self.v.get())
                  if num>1 :
                        str1 = self.v.get()
                        print(str1)
                        str1 = str1[0:num-1]
                        self.v.set(str1)
                  else:
                        self.v.set('0')
      
      def clear(self):
            self.lists = []
            self.v.set('0')

      def ce(self):
            
            self.v.set('0')

      def qf(self):
            num = self.v.get()
            if num[0] == '-':
                  self.v.set(num[1:])
            elif num[0] != '-'and num != '0':
                  self.v.set('-'+num)
      
      def kf(self):
            num = self.v.get()
            print(num)
            result = math.sqrt(float(num))
            result = str(result)
            if len(result)>10:
                  result = float(result)
                  result = '{:.10f}'.format(result)
            print(result)
            self.v.set(result)
            self.a = True

      def pf(self):
            num = self.v.get()
            print(num)
            result = math.pow(float(num),2)
            result = str(result)
            if len(result)>10:
                  result = float(result)
                  result = '{:.10f}'.format(result)
            print(result)
            self.v.set(result)
            self.a = True

      def qd(self):
            num = self.v.get()
            print(num)
            result = 1/float(num)
            result = str(result)
            if len(result)>10:
                  result = float(result)
                  result = '{:.10f}'.format(result)
            print(result)
            self.v.set(result)
            self.a = True
      #以上三个方法可以写成一个方法
            
jsq = Jsq()




