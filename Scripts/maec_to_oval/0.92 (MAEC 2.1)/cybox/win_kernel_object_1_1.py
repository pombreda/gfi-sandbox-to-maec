#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Apr 10 13:54:57 2012 by generateDS.py version 2.7b.
#

import sys
import getopt
import re as re_
import common_types_1_0 as common

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace,name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class WindowsKernelObjectType(common.DefinedObjectType):
    """The WindowsKernelObjectType type is intended to characterize Windows
    Kernel structures."""
    subclass = None
    superclass = common.DefinedObjectType
    def __init__(self, IDT=None, SSDT=None):
        super(WindowsKernelObjectType, self).__init__(None)
        self.IDT = IDT
        self.SSDT = SSDT
    def factory(*args_, **kwargs_):
        if WindowsKernelObjectType.subclass:
            return WindowsKernelObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsKernelObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IDT(self): return self.IDT
    def set_IDT(self, IDT): self.IDT = IDT
    def get_SSDT(self): return self.SSDT
    def set_SSDT(self, SSDT): self.SSDT = SSDT
    def export(self, outfile, level, namespace_='WinKernelObj:', name_='WindowsKernelObjectType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsKernelObjectType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinKernelObj:', name_='WindowsKernelObjectType'):
        super(WindowsKernelObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsKernelObjectType')
    def exportChildren(self, outfile, level, namespace_='WinKernelObj:', name_='WindowsKernelObjectType', fromsubclass_=False):
        if self.IDT is not None:
            self.IDT.export(outfile, level, 'WinKernelObj:', name_='IDT')
        if self.SSDT is not None:
            self.SSDT.export(outfile, level, 'WinKernelObj:', name_='SSDT')
    def hasContent_(self):
        if (
            self.IDT is not None or
            self.SSDT is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='WindowsKernelObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.IDT is not None:
            showIndent(outfile, level)
            outfile.write('IDT=model_.IDTEntryListType(\n')
            self.IDT.exportLiteral(outfile, level, name_='IDT')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SSDT is not None:
            showIndent(outfile, level)
            outfile.write('SSDT=model_.SSDTEntryListType(\n')
            self.SSDT.exportLiteral(outfile, level, name_='SSDT')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IDT':
            obj_ = IDTEntryListType.factory()
            obj_.build(child_)
            self.set_IDT(obj_)
        elif nodeName_ == 'SSDT':
            obj_ = SSDTEntryListType.factory()
            obj_.build(child_)
            self.set_SSDT(obj_)
        super(WindowsKernelObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsKernelObjectType


class SSDTEntryListType(GeneratedsSuper):
    """The SSDTEntryListType type specifies a listing of the entries in the
    System Service Descriptor Table (SSDT)."""
    subclass = None
    superclass = None
    def __init__(self, SSDT_Entry=None):
        if SSDT_Entry is None:
            self.SSDT_Entry = []
        else:
            self.SSDT_Entry = SSDT_Entry
    def factory(*args_, **kwargs_):
        if SSDTEntryListType.subclass:
            return SSDTEntryListType.subclass(*args_, **kwargs_)
        else:
            return SSDTEntryListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_SSDT_Entry(self): return self.SSDT_Entry
    def set_SSDT_Entry(self, SSDT_Entry): self.SSDT_Entry = SSDT_Entry
    def add_SSDT_Entry(self, value): self.SSDT_Entry.append(value)
    def insert_SSDT_Entry(self, index, value): self.SSDT_Entry[index] = value
    def export(self, outfile, level, namespace_='WinKernelObj:', name_='SSDTEntryListType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SSDTEntryListType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinKernelObj:', name_='SSDTEntryListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='WinKernelObj:', name_='SSDTEntryListType', fromsubclass_=False):
        for SSDT_Entry_ in self.SSDT_Entry:
            SSDT_Entry_.export(outfile, level, namespace_, name_='SSDT_Entry')
    def hasContent_(self):
        if (
            self.SSDT_Entry
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SSDTEntryListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('SSDT_Entry=[\n')
        level += 1
        for SSDT_Entry_ in self.SSDT_Entry:
            showIndent(outfile, level)
            outfile.write('model_.SSDTEntryType(\n')
            SSDT_Entry_.exportLiteral(outfile, level, name_='SSDTEntryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'SSDT_Entry':
            obj_ = SSDTEntryType.factory()
            obj_.build(child_)
            self.SSDT_Entry.append(obj_)
# end class SSDTEntryListType


class SSDTEntryType(GeneratedsSuper):
    """The SSDTEntryType type specifies a single entry in the System
    Service Descriptor Table (SSDT).The hooked attribute specifies
    whether the SSDT entry is hooked."""
    subclass = None
    superclass = None
    def __init__(self, hooked=None, Service_Table_Base=None, Service_Counter_Table_Base=None, Number_Of_Services=None, Argument_Table_Base=None):
        self.hooked = _cast(bool, hooked)
        self.Service_Table_Base = Service_Table_Base
        self.Service_Counter_Table_Base = Service_Counter_Table_Base
        self.Number_Of_Services = Number_Of_Services
        self.Argument_Table_Base = Argument_Table_Base
    def factory(*args_, **kwargs_):
        if SSDTEntryType.subclass:
            return SSDTEntryType.subclass(*args_, **kwargs_)
        else:
            return SSDTEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Service_Table_Base(self): return self.Service_Table_Base
    def set_Service_Table_Base(self, Service_Table_Base): self.Service_Table_Base = Service_Table_Base
    def get_Service_Counter_Table_Base(self): return self.Service_Counter_Table_Base
    def set_Service_Counter_Table_Base(self, Service_Counter_Table_Base): self.Service_Counter_Table_Base = Service_Counter_Table_Base
    def get_Number_Of_Services(self): return self.Number_Of_Services
    def set_Number_Of_Services(self, Number_Of_Services): self.Number_Of_Services = Number_Of_Services
    def get_Argument_Table_Base(self): return self.Argument_Table_Base
    def set_Argument_Table_Base(self, Argument_Table_Base): self.Argument_Table_Base = Argument_Table_Base
    def get_hooked(self): return self.hooked
    def set_hooked(self, hooked): self.hooked = hooked
    def export(self, outfile, level, namespace_='WinKernelObj:', name_='SSDTEntryType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SSDTEntryType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinKernelObj:', name_='SSDTEntryType'):
        if self.hooked is not None and 'hooked' not in already_processed:
            already_processed.append('hooked')
            outfile.write(' hooked="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.hooked)), input_name='hooked'))
    def exportChildren(self, outfile, level, namespace_='WinKernelObj:', name_='SSDTEntryType', fromsubclass_=False):
        if self.Service_Table_Base is not None:
            self.Service_Table_Base.export(outfile, level, namespace_, name_='Service_Table_Base')
        if self.Service_Counter_Table_Base is not None:
            self.Service_Counter_Table_Base.export(outfile, level, namespace_, name_='Service_Counter_Table_Base')
        if self.Number_Of_Services is not None:
            self.Number_Of_Services.export(outfile, level, namespace_, name_='Number_Of_Services')
        if self.Argument_Table_Base is not None:
            self.Argument_Table_Base.export(outfile, level, namespace_, name_='Argument_Table_Base')
    def hasContent_(self):
        if (
            self.Service_Table_Base is not None or
            self.Service_Counter_Table_Base is not None or
            self.Number_Of_Services is not None or
            self.Argument_Table_Base is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SSDTEntryType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.hooked is not None and 'hooked' not in already_processed:
            already_processed.append('hooked')
            showIndent(outfile, level)
            outfile.write('hooked = %s,\n' % (self.hooked,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Service_Table_Base is not None:
            showIndent(outfile, level)
            outfile.write('Service_Table_Base=%s,\n' % quote_python(self.Service_Table_Base).encode(ExternalEncoding))
        if self.Service_Counter_Table_Base is not None:
            showIndent(outfile, level)
            outfile.write('Service_Counter_Table_Base=%s,\n' % quote_python(self.Service_Counter_Table_Base).encode(ExternalEncoding))
        if self.Number_Of_Services is not None:
            showIndent(outfile, level)
            outfile.write('Number_Of_Services=%s,\n' % quote_python(self.Number_Of_Services).encode(ExternalEncoding))
        if self.Argument_Table_Base is not None:
            showIndent(outfile, level)
            outfile.write('Argument_Table_Base=%s,\n' % quote_python(self.Argument_Table_Base).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('hooked', node)
        if value is not None and 'hooked' not in already_processed:
            already_processed.append('hooked')
            if value in ('true', '1'):
                self.hooked = True
            elif value in ('false', '0'):
                self.hooked = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Service_Table_Base':
            Service_Table_Base_ = child_.text
            Service_Table_Base_ = self.gds_validate_string(Service_Table_Base_, node, 'Service_Table_Base')
            self.Service_Table_Base = Service_Table_Base_
        elif nodeName_ == 'Service_Counter_Table_Base':
            Service_Counter_Table_Base_ = child_.text
            Service_Counter_Table_Base_ = self.gds_validate_string(Service_Counter_Table_Base_, node, 'Service_Counter_Table_Base')
            self.Service_Counter_Table_Base = Service_Counter_Table_Base_
        elif nodeName_ == 'Number_Of_Services':
            Number_Of_Services_ = child_.text
            Number_Of_Services_ = self.gds_validate_string(Number_Of_Services_, node, 'Number_Of_Services')
            self.Number_Of_Services = Number_Of_Services_
        elif nodeName_ == 'Argument_Table_Base':
            Argument_Table_Base_ = child_.text
            Argument_Table_Base_ = self.gds_validate_string(Argument_Table_Base_, node, 'Argument_Table_Base')
            self.Argument_Table_Base = Argument_Table_Base_
# end class SSDTEntryType


class IDTEntryListType(GeneratedsSuper):
    """The IDTEntryListType type specifies a listing of the entries in the
    Interrupt Descriptor Table (IDT). The IDT is specific to the
    I386 architecture, indicating where the Prtoetcted mode
    Interrupt Service Routines (ISR) are located. See
    http://wiki.osdev.org/Interrupt_Descriptor_Table"""
    subclass = None
    superclass = None
    def __init__(self, IDT_Entry=None):
        if IDT_Entry is None:
            self.IDT_Entry = []
        else:
            self.IDT_Entry = IDT_Entry
    def factory(*args_, **kwargs_):
        if IDTEntryListType.subclass:
            return IDTEntryListType.subclass(*args_, **kwargs_)
        else:
            return IDTEntryListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IDT_Entry(self): return self.IDT_Entry
    def set_IDT_Entry(self, IDT_Entry): self.IDT_Entry = IDT_Entry
    def add_IDT_Entry(self, value): self.IDT_Entry.append(value)
    def insert_IDT_Entry(self, index, value): self.IDT_Entry[index] = value
    def export(self, outfile, level, namespace_='WinKernelObj:', name_='IDTEntryListType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IDTEntryListType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinKernelObj:', name_='IDTEntryListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='WinKernelObj:', name_='IDTEntryListType', fromsubclass_=False):
        for IDT_Entry_ in self.IDT_Entry:
            IDT_Entry_.export(outfile, level, namespace_, name_='IDT_Entry')
    def hasContent_(self):
        if (
            self.IDT_Entry
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IDTEntryListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('IDT_Entry=[\n')
        level += 1
        for IDT_Entry_ in self.IDT_Entry:
            showIndent(outfile, level)
            outfile.write('model_.IDTEntryType(\n')
            IDT_Entry_.exportLiteral(outfile, level, name_='IDTEntryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IDT_Entry':
            obj_ = IDTEntryType.factory()
            obj_.build(child_)
            self.IDT_Entry.append(obj_)
# end class IDTEntryListType


class IDTEntryType(GeneratedsSuper):
    """The IDTEntryType type specifies a single entry in the Interrupt
    Descriptor Table (IDT). Entries can be interrupt gates, task
    gates, and trap gates."""
    subclass = None
    superclass = None
    def __init__(self, Type_Attr=None, Offset_High=None, Offset_Low=None, Offset_Middle=None, Selector=None):
        self.Type_Attr = Type_Attr
        self.Offset_High = Offset_High
        self.Offset_Low = Offset_Low
        self.Offset_Middle = Offset_Middle
        self.Selector = Selector
    def factory(*args_, **kwargs_):
        if IDTEntryType.subclass:
            return IDTEntryType.subclass(*args_, **kwargs_)
        else:
            return IDTEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type_Attr(self): return self.Type_Attr
    def set_Type_Attr(self, Type_Attr): self.Type_Attr = Type_Attr
    def get_Offset_High(self): return self.Offset_High
    def set_Offset_High(self, Offset_High): self.Offset_High = Offset_High
    def get_Offset_Low(self): return self.Offset_Low
    def set_Offset_Low(self, Offset_Low): self.Offset_Low = Offset_Low
    def get_Offset_Middle(self): return self.Offset_Middle
    def set_Offset_Middle(self, Offset_Middle): self.Offset_Middle = Offset_Middle
    def get_Selector(self): return self.Selector
    def set_Selector(self, Selector): self.Selector = Selector
    def export(self, outfile, level, namespace_='WinKernelObj:', name_='IDTEntryType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IDTEntryType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinKernelObj:', name_='IDTEntryType'):
        pass
    def exportChildren(self, outfile, level, namespace_='WinKernelObj:', name_='IDTEntryType', fromsubclass_=False):
        if self.Type_Attr is not None:
            self.Type_Attr.export(outfile, level, namespace_, name_='Type_Attr')
        if self.Offset_High is not None:
            self.Offset_High.export(outfile, level, namespace_, name_='Offset_High')
        if self.Offset_Low is not None:
            self.Offset_Low.export(outfile, level, namespace_, name_='Offset_Low')
        if self.Offset_Middle is not None:
            self.Offset_Middle.export(outfile, level, namespace_, name_='Offset_Middle')
        if self.Selector is not None:
            self.Selector.export(outfile, level, namespace_, name_='Selector')
    def hasContent_(self):
        if (
            self.Type_Attr is not None or
            self.Offset_High is not None or
            self.Offset_Low is not None or
            self.Offset_Middle is not None or
            self.Selector is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IDTEntryType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Type_Attr is not None:
            showIndent(outfile, level)
            outfile.write('Type_Attr=%s,\n' % quote_python(self.Type_Attr).encode(ExternalEncoding))
        if self.Offset_High is not None:
            showIndent(outfile, level)
            outfile.write('Offset_High=%s,\n' % quote_python(self.Offset_High).encode(ExternalEncoding))
        if self.Offset_Low is not None:
            showIndent(outfile, level)
            outfile.write('Offset_Low=%s,\n' % quote_python(self.Offset_Low).encode(ExternalEncoding))
        if self.Offset_Middle is not None:
            showIndent(outfile, level)
            outfile.write('Offset_Middle=%s,\n' % quote_python(self.Offset_Middle).encode(ExternalEncoding))
        if self.Selector is not None:
            showIndent(outfile, level)
            outfile.write('Selector=%s,\n' % quote_python(self.Selector).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type_Attr':
            Type_Attr_ = child_.text
            Type_Attr_ = self.gds_validate_string(Type_Attr_, node, 'Type_Attr')
            self.Type_Attr = Type_Attr_
        elif nodeName_ == 'Offset_High':
            Offset_High_ = child_.text
            Offset_High_ = self.gds_validate_string(Offset_High_, node, 'Offset_High')
            self.Offset_High = Offset_High_
        elif nodeName_ == 'Offset_Low':
            Offset_Low_ = child_.text
            Offset_Low_ = self.gds_validate_string(Offset_Low_, node, 'Offset_Low')
            self.Offset_Low = Offset_Low_
        elif nodeName_ == 'Offset_Middle':
            Offset_Middle_ = child_.text
            Offset_Middle_ = self.gds_validate_string(Offset_Middle_, node, 'Offset_Middle')
            self.Offset_Middle = Offset_Middle_
        elif nodeName_ == 'Selector':
            Selector_ = child_.text
            Selector_ = self.gds_validate_string(Selector_, node, 'Selector')
            self.Selector = Selector_
# end class IDTEntryType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Kernel'
        rootClass = WindowsKernelObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag, 
        namespacedef_='')
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Kernel'
        rootClass = WindowsKernelObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Windows_Kernel",
        namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Kernel'
        rootClass = WindowsKernelObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from Win_Kernel_Object import *\n\n')
    sys.stdout.write('import Win_Kernel_Object as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


__all__ = [
    "IDTEntryListType",
    "IDTEntryType",
    "SSDTEntryListType",
    "SSDTEntryType",
    "WindowsKernelObjectType"
    ]
