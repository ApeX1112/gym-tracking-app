from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.clock import Clock
import numpy as np
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from database import create_gymdata,arms_data_insert,legs_data_insert,pushups_data_insert,running_data_insert,get_arms_data,get_legs_data,get_pushups_data,get_running_data,get_date
from datetime import timedelta


class CurvearmsWidget1(BoxLayout):
    def __init__(self, **kwargs):
        super(CurvearmsWidget1, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui) 
        self.conn , self.cursor = create_gymdata()
        

    def init_ui(self,dt):
        y_points=get_arms_data(self.cursor)[0]
        y_points=[0 if (x is None or x=='')else int(x) for x in y_points ]
        n=len(y_points)
        x_points=np.arange(1,10*n,10)
        self.draw_curve(x_points,y_points)

    def draw_curve(self,x_points,y_points):
        with self.canvas:
            self.canvas.clear()
            Color(1, 0, 0, 1)    
            points = list(zip(x_points, y_points))
            Line(points=points)

class CurvearmsWidget2(BoxLayout):
    def __init__(self, **kwargs):
        super(CurvearmsWidget2, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui) 
        self.conn , self.cursor = create_gymdata()
        

    def init_ui(self,dt):
        y_points=get_arms_data(self.cursor)[1]
        y_points=[0 if (x is None or x=='')else int(x) for x in y_points ]
        n=len(y_points)
        x_points=np.arange(1,10*n,10)
        self.draw_curve(x_points,y_points)

    def draw_curve(self,x_points,y_points):
        with self.canvas:
            self.canvas.clear()
            Color(0, 0, 1, 1)    
            points = list(zip(x_points, y_points))
            Line(points=points)



class CurvelegsWidget1(BoxLayout):
    def __init__(self, **kwargs):
        super(CurvelegsWidget1, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui) 
        self.conn , self.cursor = create_gymdata()

    def init_ui(self, dt):
        y_points=get_legs_data(self.cursor)[0]
        y_points=[0 if (x is None or x=='')else int(x) for x in y_points ]
        n=len(y_points)
        x_points=np.arange(1,10*n,10)
        self.draw_curve(x_points,y_points)

    def draw_curve(self,x_points,y_points):
        with self.canvas:
            self.canvas.clear()
            Color(0, 1, 0, 1)   
            points = list(zip(x_points, y_points))
            Line(points=points)

class CurvelegsWidget2(BoxLayout):
    def __init__(self, **kwargs):
        super(CurvelegsWidget2, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui) 
        self.conn , self.cursor = create_gymdata()

    def init_ui(self, dt):
        y_points=get_legs_data(self.cursor)[1]
        y_points=[0 if (x is None or x=='')else int(x) for x in y_points ]
        n=len(y_points)
        x_points=np.arange(1,10*n,10)
        self.draw_curve(x_points,y_points)

    def draw_curve(self,x_points,y_points):
        with self.canvas:
            self.canvas.clear()
            Color(0.9, 0, 0.7, 1)   
            points = list(zip(x_points, y_points))
            Line(points=points)

class CurverunningWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CurverunningWidget, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui) 
        self.conn , self.cursor = create_gymdata()

    def init_ui(self, dt):
        y_points=get_running_data(self.cursor)
        y_points=[0 if (x is None or x=='')else int(x) for x in y_points ]
        n=len(y_points)
        x_points=np.arange(1,10*n,10)
        self.draw_curve(x_points,y_points)

    def draw_curve(self,x_points,y_points):
        with self.canvas:
            self.canvas.clear()
            Color(0, 0, 1, 1)  
             
            points = list(zip(x_points, y_points))
            Line(points=points)

class CurvepushupsWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CurvepushupsWidget, self).__init__(**kwargs)
        Clock.schedule_once(self.init_ui) 
        self.conn , self.cursor = create_gymdata()

    def init_ui(self, dt):
        y_points=get_pushups_data(self.cursor)
        y_points=[0 if (x is None or x=='')else int(x) for x in y_points ]
        n=len(y_points)
        x_points=np.arange(1,10*n,10)
        self.draw_curve(x_points,y_points)

    def draw_curve(self,x_points,y_points):
        with self.canvas:
            self.canvas.clear()
            Color(0.5, 0.5, 0, 1)    
            points = list(zip(x_points, y_points))
            Line(points=points)

class InsertValueLayout(BoxLayout):
    pass

class Accueil(FloatLayout):
    def __init__(self, **kwargs):
        super(Accueil, self).__init__(**kwargs)
        self.conn , self.cursor = create_gymdata()
 
        self.curve_wid=CurvearmsWidget1(size_hint=(None,None),size=(600,600),opacity=0)
        self.curve_wid.pos_hint={'center_x':0.5,'center_y':0.5}
        self.add_widget(self.curve_wid)
         
        self.curve_wida1=CurvearmsWidget2(size_hint=(None,None),size=(600,600),opacity=0)
        self.curve_wida1.pos_hint={'center_x':0.5,'center_y':0.5}
        self.add_widget(self.curve_wida1)
       


 
        self.curve_wid1=CurvelegsWidget1(size_hint=(None,None),size=(600,600),opacity=0)
        self.curve_wid1.pos_hint={'center_x':0.5,'center_y':0.5}
        self.add_widget(self.curve_wid1)

        self.curve_widl1=CurvelegsWidget2(size_hint=(None,None),size=(600,600),opacity=0)
        self.curve_widl1.pos_hint={'center_x':0.5,'center_y':0.5}
        self.add_widget(self.curve_widl1)


        self.curve_wid2=CurverunningWidget(size_hint=(None,None),size=(600,600),opacity=0)
        self.curve_wid2.pos_hint={'center_x':0.5,'center_y':0.5}
        self.add_widget(self.curve_wid2)


 
        self.curve_wid3=CurvepushupsWidget(size_hint=(None,None),size=(600,600),opacity=0)
        self.curve_wid3.pos_hint={'center_x':0.5,'center_y':0.5}
        self.add_widget(self.curve_wid3)

        self.arms_lift = TextInput(size_hint=(0.1, None), height=30, pos_hint={'center_x': 0.8, 'center_y': 0.85})
        self.add_widget(self.arms_lift)
        self.arms_series = TextInput(size_hint=(0.1, None), height=20, pos_hint={'center_x': 0.8, 'center_y': 0.8})
        self.add_widget(self.arms_series)

        self.insert_button = Button(text="Insert Data", size_hint=(0.1, None), height=50, pos_hint={'center_x': 0.8, 'center_y': 0.7})
        self.insert_button.bind(on_press=lambda instance: arms_data_insert(self.conn, self.cursor, self.arms_lift.text, self.arms_series.text))
        self.add_widget(self.insert_button)


        self.legs_lift = TextInput(size_hint=(0.1, None), height=30,width=40, pos_hint={'center_x': 0.6, 'center_y': 0.85})
        self.add_widget(self.legs_lift)
        self.legs_series = TextInput(size_hint=(0.1, None), height=20,width=40, pos_hint={'center_x': 0.6, 'center_y': 0.8})
        self.add_widget(self.legs_series)

        self.insert_button1 = Button(text="Insert Data", size_hint=(0.1, None), height=50, pos_hint={'center_x': 0.6, 'center_y': 0.7})
        self.insert_button1.bind(on_press=lambda instance: legs_data_insert(self.conn, self.cursor, self.legs_lift.text, self.legs_series.text))
        self.add_widget(self.insert_button1)

        
        self.running_time = TextInput(size_hint=(0.1, None), height=20,width=40, pos_hint={'center_x': 0.4, 'center_y': 0.8})
        self.add_widget(self.running_time)

        self.insert_button2 = Button(text="Insert Data", size_hint=(0.1, None), height=50, pos_hint={'center_x': 0.4, 'center_y': 0.7})
        self.insert_button2.bind(on_press=lambda instance: running_data_insert(self.conn, self.cursor, self.running_time.text))
        self.add_widget(self.insert_button2)

        self.num_pushups = TextInput(size_hint=(0.1, None), height=20,width=40, pos_hint={'center_x': 0.2, 'center_y': 0.8})
        self.add_widget(self.num_pushups)

        self.insert_button3 = Button(text="Insert Data", size_hint=(0.1, None), height=50, pos_hint={'center_x': 0.2, 'center_y': 0.7})
        self.insert_button3.bind(on_press=lambda instance: pushups_data_insert(self.conn, self.cursor, self.num_pushups.text))
        self.add_widget(self.insert_button3)

        self.curve_wid.opacity=0
        self.arms_lift.opacity=0
        self.arms_series.opacity=0
        self.insert_button.opacity=0
        self.legs_lift.opacity=0
        self.legs_series.opacity=0
        self.insert_button1.opacity=0
        self.running_time.opacity=0
        self.insert_button2.opacity=0
        self.num_pushups.opacity=0
        self.insert_button3.opacity=0
        self.curve_wida1.opacity=0
        self.curve_widl1.opacity=0
        


    def show_curve(self, curve_number):
        if curve_number == 1:
            self.curve_wid.opacity=1
            self.curve_wida1.opacity=1
            self.arms_lift.opacity=1
            self.arms_series.opacity=1
            self.insert_button.opacity=1
            self.legs_lift.opacity=0
            self.legs_series.opacity=0
            self.insert_button1.opacity=0
            self.running_time.opacity=0
            self.insert_button2.opacity=0
            self.num_pushups.opacity=0
            self.insert_button3.opacity=0
            self.curve_wid1.opacity=0
            self.curve_widl1.opacity=0
            self.curve_wid3.opacity=0
            self.curve_wid2.opacity=0
        if curve_number == 2:
            self.curve_wid.opacity=0
            self.curve_wida1.opacity=0
            self.curve_wid.opacity=0
            self.arms_lift.opacity=0
            self.arms_series.opacity=0
            self.legs_lift.opacity=1
            self.legs_series.opacity=1
            self.insert_button1.opacity=1
            self.insert_button.opacity=0
            self.running_time.opacity=0
            self.insert_button2.opacity=0
            self.num_pushups.opacity=0
            self.insert_button3.opacity=0
            self.curve_wid1.opacity=1
            self.curve_widl1.opacity=1
            self.curve_wid3.opacity=0
            self.curve_wid2.opacity=0
        if curve_number == 3:
            self.curve_wid.opacity=0
            self.curve_wida1.opacity=0
            self.arms_lift.opacity=0
            self.arms_series.opacity=0
            self.insert_button.opacity=0
            self.legs_lift.opacity=0
            self.legs_series.opacity=0
            self.insert_button1.opacity=0
            self.running_time.opacity=1
            self.insert_button2.opacity=1
            self.num_pushups.opacity=0
            self.insert_button3.opacity=0
            self.curve_wid1.opacity=0
            self.curve_widl1.opacity=0
            self.curve_wid3.opacity=0
            self.curve_wid2.opacity=1
        if curve_number == 4:
            self.curve_wid.opacity=0
            self.curve_wida1.opacity=0
            self.arms_lift.opacity=0
            self.arms_series.opacity=0
            self.insert_button.opacity=0
            self.legs_lift.opacity=0
            self.legs_series.opacity=0
            self.insert_button1.opacity=0
            self.running_time.opacity=0
            self.insert_button2.opacity=0
            self.curve_wid1.opacity=0
            self.curve_widl1.opacity=0
            self.num_pushups.opacity=1
            self.insert_button3.opacity=1
            self.curve_wid3.opacity=1
            self.curve_wid2.opacity=0
        print('widget{}'.format(curve_number))

    def draw_axes(self):
        with self.canvas:
            
            Color(0, 0, 0, 1)  
            Line(points=[0, 50, 600, 50]) 
            
            Line(points=[50, 0, 50, 400])  

            
            
            for y in range(10, 501, 40):
                self.add_widget(Label(text=str(y/10), size_hint=(None, None), size=(40, 20), pos=(30, y-10)))

class GymApp(App):
    def build(self):
        return Accueil()  

if __name__ == '__main__':
    GymApp().run()