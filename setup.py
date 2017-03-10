import gi
import signal
import os
gi.require_version('Gtk' , '3.0')
gi.require_version('AppIndicator3' , '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator 

APPINDICATOR_ID = 'go_360'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'key_indi', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
	menu = gtk.Menu()
	item_quit = gtk.MenuItem('Quit')
	item_quit.connect('activate' , quit)
	menu.append(item_quit)

	item_on = gtk.MenuItem('Go 360')
	item_on.connect('activate' , go360)
	
	item_off = gtk.MenuItem('No 360')
	item_off.connect('activate' , no_go360)
	
	menu.append(item_on)
	menu.append(item_off)
	menu.show_all()
	return menu

def quit(source):
	gtk.main_quit()

def go360(source):
	os.system("xinput -disable 14")

def no_go360(source):
	os.system("xinput -enable 14")  
	
if __name__ == "__main__":
	signal.signal(signal.SIGINT , signal.SIG_DFL)
	main()