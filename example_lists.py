#!/usr/bin/env python

import pandocfilters as pf

def as_latex(s):
    "Returns string s as a raw latex inline"
    return pf.RawInline('latex', s)

# This deals with the labels.
def is_label(key, value):
    if (key == 'Span' and
        value[0][1] == [] and
        value[0][2] == [] and
        value[1] == []):
        return True
    else:
        return False

def label_name(label_value):
    return str(label_value[0][0])
    
def makelabel(key, value, format, meta):
    if is_label(key, value):
        return [as_latex('\\label{' + label_name(value) + '}')]
    
# # This deals with the references.      
def is_reference(key, value):
    if (key == "Link" and
        value[0] == [u'', [],[]] and
        value[1][0]['t'] == u'Str' and
        value[2][1] == u''):
        return True
    else:
        return False

def ref_name(ref_value):
    return ref_value[1][0]['c']

def makeref(key, value, format, meta):
    if is_reference(key, value):
        return [as_latex('\\ref{' + ref_name(value) + '}')]
    
if __name__ == '__main__':
    pf.toJSONFilters([makelabel, makeref])
