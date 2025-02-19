import os
import posixpath
import salah.system.path.tools as path_tools

def get_python_file_as_list(path):
    file_content = path_tools.get_content(path)
    lines = file_content.split('\n')[:-1]
    return lines

def get_variables_content(list_item):
    list_variables = []
    for line in list_item:
        if line[0:1] != ' ' and line[0:1] != '#' and ' = ' in line:
            list_variables.append(line)
    return list_variables

def get_functions_content(list_file):
    list_functions = []
    for line in list_file:
        if "def" in line and line.find("def") == 0 and line[-1] == ':':
            function1 = list_file[list_file.index(line):]
            tab_spaces = ""
            get_spaces_line = ""
            for line in function1:
                if '  ' in line[:4]:
                    get_spaces_line = line
                    break
            for char in get_spaces_line:
                if char != ' ':
                    break
                tab_spaces += " "
            function2 = [function1[0]]
            for line in function1[1:]:
                if (line[0:len(tab_spaces)] == tab_spaces or line.replace(' ', '') == '' or '#' in line[0:len(tab_spaces)]) and not(line[0:1] == '#'):
                    function2.append(line.replace(' ', '')) if line.replace(' ', '') == '' else function2.append(line)
                else:
                    break
            for line in range(len(function2)):
                if function2[-1] == '':
                    function2 = function2[:-1]
            list_functions.append(function2)
    return list_functions

def get_classes_content(list_file):
    list_classes = []
    for line in list_file:
        if "class" in line and line.find("class") == 0 and line[-1] == ':':
            class1 = list_file[list_file.index(line):]
            tab_spaces = ""
            get_spaces_line = ""
            for line in class1:
                if '  ' in line[:8] and (not("class" in line) or not("def" in line)):
                    get_spaces_line = line
                    break
            for char in get_spaces_line:
                if char != ' ':
                    break
                tab_spaces += " "
            class2 = [class1[0]]
            for line in class1[1:]:
                if (line[0:len(tab_spaces)] == tab_spaces or line.replace(' ', '') == '' or '#' in line[0:len(tab_spaces)]) and not(line[0:1] == '#'):
                    class2.append(line.replace(' ', '')) if line.replace(' ', '') == '' else class2.append(line)
                else:
                    break
            for line in range(len(class2)):
                if class2[-1] == '':
                    class2 = class2[:-1]
            list_classes.append(class2)
    return list_classes

def get_functions(functions):
    list_functions = []
    for f in functions:
        list_functions.append(f[0][:-1])
    return list_functions

def get_classes(classes):
    list_classes = []
    for c in classes:
        list_classes.append(c[0][:-1])
    return list_classes

def get_variables_name(variables):
    list_variables_name = []
    for variable_name in variables:
        list_variables_name.append(variable_name[:variable_name.find('=')-1])
    return list_variables_name

def get_functions_name(functions):
    list_functions_name = []
    for f in functions:
        function_name = f[0]
        list_functions_name.append(function_name[function_name.find("def")+4:function_name.find('(')])
    return list_functions_name

def get_classes_name(classes):
    list_name_classes = []
    for c in classes:
        class_name = c[0]
        list_name_classes.append(class_name[class_name.find("class")+6:class_name.find('(')])
    return list_name_classes

def get_description_of_functions(functions):
    list_description_functions = []
    for f in functions:
        tab_spaces = ""
        get_spaces_line = ""
        for line in f:
            if '  ' in line[:8]:
                get_spaces_line = line
                break
        for char in get_spaces_line:
            if char != ' ':
                break
            tab_spaces += " "
        function_description = []
        for line in f:
            if "'''" == line[len(tab_spaces):len(tab_spaces)+3] or '"""' == line[len(tab_spaces):len(tab_spaces)+3]:
                function_description = f[f.index(line)+1:]
                break
            elif ("'''" == line[len(tab_spaces):len(tab_spaces)+3] or '"""' == line[len(tab_spaces):len(tab_spaces)+3]) and (line.count("'''") == 2 or line.count('"""') == 2):
                function_description = f[line]
                break
        for line in function_description:
            if "'''" == line[len(tab_spaces):len(tab_spaces)+3] or '"""' == line[len(tab_spaces):len(tab_spaces)+3] and len(f) > 1:
                function_description = function_description[:function_description.index(line)]
                break
        list_description_functions.append(function_description)
    return list_description_functions

def get_description_of_classes(classes):
    list_description_classes = []
    class_description = []
    for c in classes:
        tab_spaces = ""
        get_spaces_line = ""
        for line in c:
            if '  ' in line[:8]:
                get_spaces_line = line
                break
        for char in get_spaces_line:
            if char != ' ':
                break
            tab_spaces += " "
        for line in c:
            if "'''" == line[len(tab_spaces):len(tab_spaces)+3] or '"""' == line[len(tab_spaces):len(tab_spaces)+3]:
                class_description = c[c.index(line)+1:]
                break
            elif ("'''" == line[len(tab_spaces):len(tab_spaces)+3] or '"""' == line[len(tab_spaces):len(tab_spaces)+3]) and (line.count("'''") == 2 or line.count('"""') == 2):
                class_description = c[line]
                break
        for line in class_description:
            if "'''" == line[len(tab_spaces):len(tab_spaces)+3] or '"""' == line[len(tab_spaces):len(tab_spaces)+3] and len(c) > 1:
                class_description = class_description[:class_description.index(line)]
                break
        list_description_classes.append(class_description)
    return list_description_classes

