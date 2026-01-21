from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import socket
import threading

class MobileControlApp(App):
    def build(self):
        self.ip = "192.168.1.10" # ТУТ БУДЕТ IP ТВОЕГО КОМПА
        self.port = 9999
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.status = Label(text="Статус: Ожидание...")
        layout.add_widget(self.status)
        
        btn_connect = Button(text="ПОДКЛЮЧИТЬ К ПК", background_color=(0, 1, 0, 1))
        btn_connect.bind(on_press=self.start_conn)
        layout.add_widget(btn_connect)
        
        # Кнопки быстрого управления
        btn_block = Button(text="БЛОК МЫШИ", on_press=lambda x: self.send_cmd("BLOCK"))
        layout.add_widget(btn_block)
        
        btn_bsod = Button(text="BSOD", background_color=(1, 0, 0, 1), on_press=lambda x: self.send_cmd("BSOD"))
        layout.add_widget(btn_bsod)
        
        return layout

    def start_conn(self, instance):
        threading.Thread(target=self.connect_to_pc, daemon=True).start()

    def connect_to_pc(self):
        try:
            self.s = socket.socket()
            self.s.connect((self.ip, self.port))
            self.status.text = "Статус: В СЕТИ"
        except Exception as e:
            self.status.text = f"Ошибка: {e}"

    def send_cmd(self, cmd):
        try:
            self.s.send(cmd.encode())
        except:
            self.status.text = "Статус: СВЯЗЬ ПОТЕРЯНА"

if __name__ == '__main__':
    MobileControlApp().run()