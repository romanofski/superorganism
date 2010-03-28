import superorganism.database
import superorganism.app
import superorganism.config
import superorganism.gui.app
import superorganism.gui.interfaces
import urwid.curses_display
import zope.component
import zope.interface


def main(ZCONFIG, configfile):
    tui = urwid.curses_display.Screen()
    zope.interface.directlyProvides(tui,
                                    superorganism.gui.interfaces.IScreen)
    database = superorganism.database.Database(ZCONFIG)
    zope.component.provideUtility(database, superorganism.interfaces.IDatabase)

    cfg = superorganism.config.Configuration(configfile)
    cfg.configure_colors(tui)
    zope.component.provideUtility(cfg, superorganism.interfaces.IConfiguration)

    app = superorganism.app.Application()
    view = zope.component.getMultiAdapter((app, tui),
        superorganism.gui.interfaces.ITerminalView)
    tui.run_wrapper(view.run) #XXX keydispatcher?
