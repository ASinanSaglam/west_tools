# Copyright (C) 2013 Matthew C. Zwier and Lillian T. Chong
#
# This file is part of WESTPA.
#
# WESTPA is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WESTPA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WESTPA.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function, division; __metaclass__ = type
from westpa.progress import ProgressIndicator
from westtools.tool_classes.core import WESTToolComponent
import westpa

class ProgressIndicatorComponent(WESTToolComponent):
    def __init__(self):
        super(ProgressIndicatorComponent,self).__init__()
        self.indicator = None

    def process_args(self, args):
        self.indicator = ProgressIndicator()
        if westpa.rc.quiet_mode:
            self.indicator.do_fancy = False