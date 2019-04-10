#!/usr/bin/env python

import pandocfilters as pf

def latex(x):
    return pf.RawInline('latex', x)

# This deals with the labels.
def is_label(key, value):
    if (key == 'Span' and
        value[0][0].startswith(u'ex:') and
        value[0][1] == [] and
        value[0][2] == [] and
        value[1] == []):
        return True
    else:
        return False

def label_name(key, value):
    if is_label(key, value):
        return str(value[0][0])
    
def makelabel(key, value, format, meta):
    if is_label(key, value):
        return [latex('\\label{' + label_name(key, value) + '}')]
    
# # This deals with the references.      
def is_reference(key, value):
    if (key == "Link" and
        value[1][0]['c'].startswith(u'ex:') and
        value[0] == [u'', [],[]] and
        value[1][0]['t'] == u'Str' and
        value[2][1] == u''):
        return True
    else:
        return False

def ref_name(key, value):
    if is_reference(key, value):
        return value[1][0]['c']

def makeref(key, value, format, meta):
    if is_reference(key, value):
        return [latex('(\\ref{' + ref_name(key, value) + '})')]
    
if __name__ == '__main__':
    pf.toJSONFilters([makelabel, makeref])
