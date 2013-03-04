#
# main.py
# copyright (c) 2013 by Alexander Lehmann <afwlehmann@googlemail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# 
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
    
from PyKDE4 import plasmascript
from PyKDE4.plasma import Plasma
from PyKDE4.kdeui import KIcon, KMessageBox
from PyQt4.QtCore import QUrl, QString, QRegExp
from PyQt4.QtGui import QDesktopServices, QIcon
 
class HoogleRunner(plasmascript.Runner):
    def init(self):
        """
        Initialize and register with Plasma.
        """
        self.myIcon = QIcon("contents/images/lambda.svg")
        self.regExp = QRegExp("^hoogle (.*)$")
        syntax = Plasma.RunnerSyntax("hoogle :q:", "Query hoogle for :q:")
        self.addSyntax(syntax)
 
    def match(self, context):
        """
        Add a match to the given `context` iff the query starts with 'hoogle'.
        """
        if context.isValid() and self.regExp.exactMatch(context.query()):
            term = self.regExp.cap(1)
            m = Plasma.QueryMatch(self.runner)
            m.setText("Query Hoogle for '%s'" % term)
            m.setType(Plasma.QueryMatch.ExactMatch)
            m.setIcon(self.myIcon)
            m.setData(term)
            context.addMatch(term, m)
 
    def run(self, context, match):
        """
        Have KDE open the query in the browser.
        """
        urlString = QString("http://www.haskell.org/hoogle/?hoogle=")
        # Apparently Hoogle doesn't like percent encoded URLs.
        # urlString.append(QUrl.toPercentEncoding(match.data().toString()))
        urlString.append(match.data().toString())
        QDesktopServices().openUrl(QUrl(urlString))
 
 
def CreateRunner(parent):
    return HoogleRunner(parent)

