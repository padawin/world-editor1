# -*- coding: utf8 -*-

from PyQt4 import QtGui


class menu(QtGui.QMenuBar):
	"""
	Class to create the window's menu.
	"""

	# actions
	_exportAction = None
	_zoominAction = None
	_zoomoutAction = None

	def __init__(self, window):
		"""
		Construct of the menu. The menu's items are defined here.
		"""
		super(menu, self).__init__(window)

		# new action
		newAction = QtGui.QAction('&New...', window)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip('Create new map')
		newAction.triggered.connect(window.newMap)

		# open action
		openAction = QtGui.QAction('&Open...', window)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open map')
		openAction.triggered.connect(window.openMapAction)

		# export action
		self._exportAction = QtGui.QAction('&Export', self)
		self._exportAction.setShortcut('Ctrl+E')
		self._exportAction.setStatusTip('Export map')
		self._exportAction.triggered.connect(window.exportMap)

		# exit action
		exitAction = QtGui.QAction('&Exit', window)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtGui.qApp.quit)

		# zoom in action
		self._zoominAction = QtGui.QAction('Zoom &in', self)
		self._zoominAction.setShortcut('Ctrl++')
		self._zoominAction.setStatusTip('Zoom in')
		self._zoominAction.triggered.connect(window.zoomInMap)

		# zoom out action
		self._zoomoutAction = QtGui.QAction('Zoom o&ut', self)
		self._zoomoutAction.setShortcut('Ctrl+-')
		self._zoomoutAction.setStatusTip('Zoom out')
		self._zoomoutAction.triggered.connect(window.zoomOutMap)

		self._exportAction.setEnabled(False)
		self._zoominAction.setEnabled(False)
		self._zoomoutAction.setEnabled(False)

		fileMenu = self.addMenu('&File')
		mapMenu = self.addMenu('&Map')

		fileMenu.addAction(newAction)
		#~fileMenu.addAction(openAction)
		fileMenu.addAction(self._exportAction)
		fileMenu.addAction(exitAction)

		mapMenu.addAction(self._zoominAction)
		mapMenu.addAction(self._zoomoutAction)
