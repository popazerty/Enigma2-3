from MenuList import MenuList
from Tools.Directories import resolveFilename, SCOPE_CURRENT_SKIN
from enigma import eListboxPythonMultiContent, eListbox, gFont, RT_HALIGN_LEFT, RT_VALIGN_CENTER, getDesktop
from Tools.LoadPixmap import LoadPixmap

selectionpng = LoadPixmap(cached=True, path=resolveFilename(SCOPE_CURRENT_SKIN, "skin_default/icons/lock_on.png"))

def SelectionEntryComponent(description, value, index, selected):
	screenwidth = getDesktop(0).size().width()
	if screenwidth and screenwidth == 1920:
		res = [
			(description, value, index, selected),
			(eListboxPythonMultiContent.TYPE_TEXT, 80, 5, 900, 55, 1, RT_HALIGN_LEFT, description)
		]
	else:
		res = [
			(description, value, index, selected),
			(eListboxPythonMultiContent.TYPE_TEXT, 25, 3, 650, 30, 0, RT_HALIGN_LEFT, description)
		]
	if selected:
		if screenwidth and screenwidth == 1920:
			res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST, 10, 5, 50, 50, selectionpng))
		else:
			res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST, 0, 2, 25, 24, selectionpng))
	return res

class SelectionList(MenuList):
	def __init__(self, list = None, enableWrapAround = False):
		MenuList.__init__(self, list or [], enableWrapAround, content = eListboxPythonMultiContent)
		self.l.setFont(0, gFont("Regular", 20))
		self.l.setFont(1, gFont("Regular", 32))
		self.l.setItemHeight(30)

	def addSelection(self, description, value, index, selected = True):
		self.list.append(SelectionEntryComponent(description, value, index, selected))
		self.setList(self.list)

	def toggleSelection(self):
		idx = self.getSelectedIndex()
		item = self.list[idx][0]
		self.list[idx] = SelectionEntryComponent(item[0], item[1], item[2], not item[3])
		self.setList(self.list)

	def getSelectionsList(self):
		return [ (item[0][0], item[0][1], item[0][2]) for item in self.list if item[0][3] ]

	def toggleAllSelection(self):
		for idx,item in enumerate(self.list):
			item = self.list[idx][0]
			self.list[idx] = SelectionEntryComponent(item[0], item[1], item[2], not item[3])
		self.setList(self.list)

	def sort(self, sortType=False, flag=False):
		# sorting by sortType:
		# 0 - description
		# 1 - value
		# 2 - index
		# 3 - selected
		self.list.sort(key=lambda x: x[0][sortType],reverse=flag)
		self.setList(self.list)
