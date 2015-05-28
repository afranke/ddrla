# application.py
#
# Copyright (c) 2015, Alexandre Franke <afranke@gnome.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ddrla.window import Window
from gi.repository import Gio, GLib, Gtk


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id='com.hackcendo.ddrla',
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        GLib.set_application_name("ddrescue log analyzer")
        self._window = None

    def do_activate(self):
        if not self._window:
            self._window = Window(self)
            self._window.show_all()
        self._window.present()
