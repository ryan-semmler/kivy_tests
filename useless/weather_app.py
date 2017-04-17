from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class Temperature(Widget):
    velocity_x = NumericProperty(4)
    velocity_y = NumericProperty(6)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class Weather(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(9)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class Game(Widget):
    temp = ObjectProperty(Temperature)
    conditions = ObjectProperty(None)
    paint = ObjectProperty(None)

    def update(self, dt):
        self.temp.move()
        self.conditions.move()
        if (self.temp.y < self.y) or (self.temp.top > self.top):
            self.temp.velocity_y *= -1
        if (self.conditions.y < self.y) or (self.conditions.top > self.top):
            self.conditions.velocity_y *= -1
        if (self.temp.x < self.x) or (self.temp.x > self.width):
            self.temp.velocity_x *= -1


class MyPaintApp(App):

    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    MyPaintApp().run()
