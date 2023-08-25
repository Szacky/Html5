import tornado.web
import tornado.ioloop
import subprocess
import tkinter as tk

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')
    def post(self):
        user_name = self.get_argument('name','None')
        user_name2 = self.get_argument('password','None')
        floor = self.get_argument('floor','None')
        qsh = self.get_argument('qsh','None')
        q1 = int(self.get_argument('q1','None'))
        q2 = int(self.get_argument('q2','None'))
        q3 = int(self.get_argument('q3','None'))
        q4 = int(self.get_argument('q4','None'))
        q5 = int(self.get_argument('q5','None'))
        q6 = int(self.get_argument('q6','None'))
        q7 = int(self.get_argument('q7','None'))
        q8 = int(self.get_argument('q8','None'))
        q9 = int(self.get_argument('q9','None'))
        q10 = int(self.get_argument('q10','None'))
        q11 = int(self.get_argument('q11','None'))
        q12 = int(self.get_argument('q12','None'))
        q13 = int(self.get_argument('q13','None'))
        q14 = int(self.get_argument('q14','None'))
        q15 = int(self.get_argument('q15','None'))
        q16 = int(self.get_argument('q16','None'))
        q17 = int(self.get_argument('q17','None'))
        q18 = int(self.get_argument('q18','None'))
        q19 = int(self.get_argument('q19','None'))
        q20 = int(self.get_argument('q20','None'))
        q21 = int(self.get_argument('q21','None'))
        fs = q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21
        if user_name == "ssdf" and user_name2 == "kjb":
            self.render('01.html',
                        username=user_name,
                        fs=floor+"楼"+qsh+"分数为:"+str(fs))
            try:
                desktop_path = "E:\\AI\\科技部\\tornado摸板\\自测\\"
                full_path = desktop_path + "账号" + '.txt'
                file = open(full_path, 'a')
                file.write(floor+"楼"+qsh+"分数为:"+str(fs)+"\n")
            except:
                print("404 Not Find")
        else:
            self.render('register.html')
            window = tk.Tk()
            window.title('提示')
            window.geometry('500x50')
            l = tk.Label(window, 
                text="账号或密码错误",   
                bg='white',    
                font=('微软雅黑', 12),   
                width=50, height=2)
            l.pack()    
            window.mainloop()

def make_app():
    return tornado.web.Application(
        handlers=[(r'.*',RegisterHandler)],
        template_path = '',
        debug=True)

print("Sever is running...")
print("http://localhost:8888/")
app = make_app()
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(8888)
tornado.ioloop.IOLoop.current().start()
