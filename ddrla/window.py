# window.py
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

from gi.repository import GLib, Gtk
from os.path import abspath, dirname, join


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self,
                                       application=app,
                                       show_menubar=False)
        builder = Gtk.Builder()
        filename = join(dirname(abspath(__file__)),
                        'resources/ui/ddrla-window.ui')
        builder.add_from_file(filename)
        headerbar = builder.get_object('header')
        self.set_titlebar(headerbar)

        treeview = builder.get_object('content')
        self.add(treeview)
