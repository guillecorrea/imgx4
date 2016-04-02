#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2016 Guillermo Correa <guillecorrea@gmail.com>
# 
# img4toA4 is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# img4toA4 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
import subprocess
import shlex

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gio


def on_boton_click(self):
	etiqueta.set_text("Creando...")
	orvert = "-rotate 0  "

	if radio2.get_active():
		orvert = "-rotate 90 "	
	
	subprocess.call(shlex.split("montage -tile 2x2 -geometry 297x421 " + orvert + " '" + win.archivo + "' '" + win.archivo + "' '" + win.archivo + "' '" + win.archivo + "' '" + win.archivo[:-4]+".pdf '"))
	subprocess.call(shlex.split("xdg-open '" + win.archivo[:-4]+".pdf '"))
	
def on_file_clicked(self):
	dialog = Gtk.FileChooserDialog("Elija un archivo ", win,Gtk.FileChooserAction.OPEN,	(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,	Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

	#self.add_filters(dialog)

	response = dialog.run()
	if response == Gtk.ResponseType.OK:
		win.archivo = dialog.get_filename()
		etiqueta.set_text("Listo para crear " );
	elif response == Gtk.ResponseType.CANCEL:
		print("Cancel clicked")

	dialog.destroy()


       

win = Gtk.Window()
win.archivo =""
win.connect("delete-event", Gtk.main_quit)


grid = Gtk.Grid()



button = Gtk.Button(label="Abrir Archivo")
		#win.button.connect("clicked", win.on_button_clicked)
button.connect("clicked", on_file_clicked)

button2 = Gtk.Button(label="Crear")
button2 .connect("clicked", on_boton_click)

hbox = Gtk.Box(spacing=6)
radio =1
radio1 = Gtk.RadioButton.new_with_label_from_widget(None, "Vertical")

hbox.pack_start(radio1, False, False, 0)

radio2 = Gtk.RadioButton.new_from_widget(radio1)
radio2.set_label("Horizontal")

hbox.pack_start(radio2, False, False, 0)
		#gicon = Gio.ThemedIcon.new_with_default_fallbacks('document-new')
		#img = Gtk.Image.new_from_gicon(gicon, Gtk.IconSize.DIALOG)

etiqueta = Gtk.Label();


grid.add(button)
grid.attach_next_to(hbox, button, Gtk.PositionType.BOTTOM, 1, 2)
grid.attach_next_to(button2, hbox, Gtk.PositionType.BOTTOM, 1, 2)
grid.attach_next_to(etiqueta, button2, Gtk.PositionType.BOTTOM, 1, 2)
		#grid.attach_next_to(img, hbox, Gtk.PositionType.BOTTOM, 1, 2)
		#grid.attach_next_to(button2, img, Gtk.PositionType.BOTTOM, 1, 2)
win.add(grid)

win.show_all()
Gtk.main()

		
