import webbrowser
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class KivyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.main_screen = MainScreen(name='main')
        self.orange_screen = OrangeScreen(name='orange')
        self.black_screen = BlackScreen(name='black')
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.orange_screen)
        self.screen_manager.add_widget(self.black_screen)
        return self.screen_manager

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=2)

        btn1 = Button(text='Button 1', background_color=[1, 1, 0, 1])
        btn1.bind(on_press=self.open_google)
        layout.add_widget(btn1)

        btn2 = Button(text='Button 2', background_color=[1, 1, 0, 1])
        btn2.bind(on_press=self.open_youtube)
        layout.add_widget(btn2)

        btn3 = Button(text='Button 3', background_color=[0, 0, 1, 1])
        btn3.bind(on_press=self.open_orange)
        layout.add_widget(btn3)

        btn4 = Button(text='Button 4', background_color=[1, 0, 0, 1])
        btn4.bind(on_press=self.open_black)
        layout.add_widget(btn4)

        self.add_widget(layout)

    def open_google(self, instance):
        webbrowser.open("https://www.google.com")

    def open_youtube(self,instance):
        webbrowser.open("https://www.youtube.com")

    def open_orange(self,instance):
        self.manager.current = 'orange'

    def open_black(self,instance):
        self.manager.current = 'black'

class OrangeScreen(Screen):
    def __init__(self, **kwargs):
        super(OrangeScreen, self).__init__(**kwargs)
        self.colors = [1, 0.5, 0, 1]
        self.background_color = self.colors
        layout = GridLayout()

        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

class BlackScreen(Screen):
    def __init__(self, **kwargs):
        super(BlackScreen, self).__init__(**kwargs)
        self.colors = [0, 0, 0, 1]
        self.background_color = self.colors
        layout = GridLayout()

        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

if __name__ == '__main__':
    KivyApp().run()