 #Copyright (C) 2009, 2010, 2011 Jonathan Jacky
 
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.

 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 

from formula import Formula, FormulaPlaceholder, check_count

class Text(Formula):

  def __init__(self, *args):
    check_count(self, 1, *args)
    if not isinstance(args[0], str):
      raise TypeError, 'argument %s is not a string' % text
    self.text = args[0]

  def pform(self):
    return "Text('%s')" % self.text

  def ppf(self):
    return self.text

  def free(self):  # for compatibility, comment text appears in formula place
    return []  # Text is a constant not a variable

# Define a symbol for each rule.
# Rule symbols are self-evaluating, used to write proof in save file format.
 
(comment, given) = ('comment', 'given')

# Pretty-print names for rules.

rule_names = { comment: 'Comment', given : 'Given' }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1 = FormulaPlaceholder('m1')

rules = { 
           comment: [ m1 ],   # match any formula
           given:   [ m1 ]
        }
          
# Import statement to write to save file, so it in turn can be imported 

imports = 'from flip.logic.common import *' 
