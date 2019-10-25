#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = SoundButton(text="play")
        self.add_widget(self.button)


class SoundButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("badam_tss.ogg")
        self.on_press = self.play_sound

    def play_sound(self):
        if self.sound.state == "stop":
            self.sound.play()
            self.event = Clock.schedule_interval(self.play_status, 0.1)

    def play_status(self, _):
        if self.sound.state == "play":
            self.text = str(self.sound.get_pos())
        else:
            self.text = "play"
            Clock.unschedule(self.event)


class SoundIssueApp(App):
    def build(self):
        return MyBox()


if __name__ == "__main__":
    SoundIssueApp().run()
