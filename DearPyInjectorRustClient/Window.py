import dearpygui.dearpygui as x
import Inject as ix
import os
class Window:
    def MainWindow():
        x.create_context()
        with x.font_registry():
            comic_sans = x.add_font(file="{}".format(os.getcwd() + "\\ComicSansMS.ttf"), size=16)
        with x.window(label="DearPyInjector", height=500, width=500, no_move=True, no_collapse=True, no_close=True) as xsl:
            x.add_text("It's My First Injector on Python", color=[200, 45, 155])
            x.add_input_text(label="Path", tag="input_path")
            x.add_button(label="Inject", callback=Window.Inject)
        x.create_viewport(title='DearPyInjector(RustClient) by GangOfFloppa', width=500, height=500, clear_color=[230, 155, 58])
        x.bind_font(comic_sans)
        x.setup_dearpygui()
        x.set_primary_window(xsl, True)
        x.show_viewport()
        x.start_dearpygui()
        x.destroy_context()
    def Inject():
        str_path = x.get_value("input_path")
        return ix.Injector.InjectDLL(str_path)