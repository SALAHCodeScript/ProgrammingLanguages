"""hey there, you are in SALAH his 'Package Management' library (Python3.13)"""
import os
import sys
import posixpath
import salah.system.os.tools as os_tools
import salah.system.path.tools as path_tools
import salah.parsing.python.tools as parse_tools
from rich.console import Console
from rich.table import Table
import click

console = Console()

def get_data(get_file, function, arg):
    data = {}
    directory = ["__init__.py", "__main__.py"]
    grandparent = get_file
    parent = path_tools.get_basename(path_tools.get_parent_path(get_file)) if path_tools.get_basename(get_file) in directory else path_tools.get_file_basename(get_file)
    child = function(arg)
    data[grandparent] = {}
    data[grandparent][parent] = child
    return data

def display(library, data):
    keys = list(data.keys())
    for key in keys:
        if library == key:
            directory = ["__init__.py", "__main__.py"]
            parent = path_tools.get_basename(path_tools.get_parent_path(library)) if path_tools.get_basename(library) in directory else path_tools.get_file_basename(library)
            return data[key][parent]

def display_all(list_file):
    variables = parse_tools.get_variables_content(list_file)
    functions = parse_tools.get_functions(parse_tools.get_functions_content(list_file))
    classes = parse_tools.get_classes(parse_tools.get_classes_content(list_file))
    return {"Variables": variables, "Functions": functions, "Classes": classes}

def display_as_table(key, value):
    table = Table()
    table.add_column(key)
    table.add_row(value)
    return table

@click.command(help=__doc__)
@click.argument("library", required=False)
@click.option('-t', "--get-type", type=click.Choice(["all", "variable", "function", "class"]), required=False, help="display all, variable, function or class of library")
@click.option('-f', "--get-file", default="init", type=click.Choice(["init", "main"]), required=False, help="choose bettween '__init__.py' or '__main__.py' file")
@click.option('-l', "--get-list", is_flag=True, required=False, help="listing all existing packages and its tools")
@click.option('-h', "--get-help", is_flag=True, required=False, help="get help of library")
@click.option('-p', "--path", is_flag=True, required=False, help="print path of library")
@click.option('-e', "--tree", is_flag=True, required=False, help="display tree of library")
@click.option('-o', "--open-as", required=False, help="open file of library as")
@click.option('-d', "--display-content", type=click.Choice(["all", "variable", "function", "class"]), required=False, help="display all, variable, function or class content of library")
@click.option('-dh', "--display-help", is_flag=True, required=False, help="get help of something in library")
@click.option('-n', "--name", is_flag=True, required=False, help="print name of library")
def main(library, get_type, get_file, get_list, get_help, path, tree, open_as, display_content, display_help, name):
    os.system("clear") if os_tools.get_machine_name() == "Linux" else os.system("cls")

    cmd = "salah.package.display"
    library = library if library != None else cmd
    path_lib = os_tools.get_output_command(["py", "-c", f"import {library} as pack; print(pack.__file__)"])
    get_file = "__init__.py" if get_file == "init" else "__main__.py"
    library_path = f"{path_tools.get_parent_path(path_lib)}{path_tools.get_symbol_path()}{get_file}" if path_lib != "" else  ""

    libs = library.split('.')
    parent = libs[0]
    lib = libs[-1]

    tested_lib = ""
    for l in libs:
        get_error_import = os_tools.get_error_command(["py", "-c", f"import {'.'.join(libs[:libs.index(l)+1])} as pack; print(pack.__name__)"])
        if get_error_import:
            break
        tested_lib = '.'.join(libs[:libs.index(l)+1])

    list_pack = sys.path[1:]
    packages = {}
    for pack in list_pack:
        if posixpath.isdir(pack):
            packages[pack] = []
            for item in os.listdir(pack):
                full_path = f"{pack}{path_tools.get_symbol_path()}{item}"
                skip_items = ['DLLs', 'Doc', 'etc', 'include', 'Lib', 'libs', 'Scripts', 'share']
                if ((posixpath.isfile(full_path) and full_path.endswith(".py")) or posixpath.isdir(full_path)) and item[0] != '_' and not(item.endswith("-info")) and not(item.endswith(".libs")) and not(item in skip_items):
                    packages[pack].append(item[:-3]) if item.endswith(".py") else packages[pack].append(item)
    for packs in packages:
        for pack in packages[packs]:
            if packages[packs] == []:
                del packages[packs]
            new_pack = pack.split('-')
            item = ""
            for p in new_pack:
                if p[0].isalpha():
                    item += f"{p}-"
            packages[packs][packages[packs].index(pack)] = item[:-1]

    possible_packages = {}
    for packs in packages:
        possible_packages[packs] = []
        for pack in packages[packs]:
            if parent in pack or parent.lower() in pack.lower():
                possible_packages[packs].append(pack)
        if possible_packages[packs] == []:
            del possible_packages[packs]

    get_error_import = os_tools.get_error_command(["py", "-c", f"import {library} as pack; print(pack.__file__)"]).split('\n')
    modules_not_found_error = [error for error in get_error_import if "ModuleNotFoundError: No module named" in error]
    other_errors = get_error_import[-1] if len(get_error_import) == 1 else None
    if modules_not_found_error != []:
        module_name = modules_not_found_error[0].split(' ')[-1][1:-2] if os_tools.get_machine_name() == "Windows" else modules_not_found_error[0].split(' ')[-1][1:-1]
        if parent == module_name or module_name in library:
            module_name = ""

    displayed_issue = f"[yellow]'{lib}'[/]"
    if len(libs) == 2:
        displayed_issue = f"[yellow]'{lib}'[/] in parent [yellow]'{parent}'[/]"
    elif len(libs) > 2:
        displayed_issue = f"[yellow]'{lib}'[/] in [yellow]'{'.'.join(libs[1:-1])}'[/] of parent [yellow]'{libs[0]}'[/]"

    import_parent_lib = os_tools.get_output_command(["py", "-c", f"import {parent} as pack; print(pack.__file__)"])
    import_lib_as_name = os_tools.get_output_command(["py", "-c", f"import {library} as pack; print(pack.__name__)"])

    if path_lib == "":
        if import_parent_lib == "" and len(libs) > 1:
            issue = f"[[red1]ERROR[/]] the parent package: [yellow]'{parent}'[/] is not exists.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
        elif not(posixpath.exists(library_path)):
            issue = f"[[red1]ERROR[/]] there is no package named: {displayed_issue}.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
        elif import_lib_as_name != "" and import_parent_lib == "":
            issue = f"[[red1]ERROR[/]] there is package with name: {displayed_issue} but can't find where is it located.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
        list_possible_packages = []
        for packs in possible_packages:
            if not(parent in possible_packages[packs]) and len(possible_packages[packs]) > 0:
                list_possible_packages.append(f"'{packs}': {possible_packages[packs]}")
        if list_possible_packages != []:
            directory = ':'.join(list_possible_packages[0][::-1].split(':')[1:])[::-1][1:-1] if os_tools.get_machine_name() == "Windows" else list_possible_packages[0].split(':')[0][1:-1]
            issue_sentence = f"[[red1]ERROR[/]] there is no package named: [yellow]'{parent}'[/].\n[[green1]INFO[/]] maybe you meant this library: \n[cyan]{'\n'.join(list_possible_packages)}[/]" if len(list_possible_packages) == 1 and len(possible_packages[directory]) == 1 else f"[[red1]ERROR[/]] there is no package named: [yellow]'{parent}'[/].\n[[green1]INFO[/]] maybe you meant one of these libraries: \n[cyan]{'\n'.join(list_possible_packages)}[/]"
            issue = f"{issue_sentence}.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
        if get_error_import != []:
            if module_name != "":
                issue = f"[[red1]ERROR[/]] something went wrong, module not found: [cyan]'{module_name}'[/] for package: {displayed_issue}.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
            elif other_errors != "":
                issue_sentence = f"[[red1]ERROR[/]] {other_errors}.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
        console.print(issue)
        sys.exit()
    elif not(posixpath.exists(library_path)) and path_tools.get_basename(library_path) == "__main__.py":
        issue = f"[[red1]ERROR[/]] there is package with name: {displayed_issue}, but it doesn't have '__main__.py' file.\n\n[[green1]INFO[/]] type 'py -m {cmd} --help' for more information."
        console.print(issue)
        sys.exit()

    list_file = parse_tools.get_python_file_as_list(library_path)
    variables_content = parse_tools.get_variables_content(list_file)
    functions_content = parse_tools.get_functions_content(list_file)
    classes_content = parse_tools.get_classes_content(list_file)

    if not(get_list) and not(get_help) and not(path) and not(tree) and not(name) and open_as == None and not(display_help) and display_content == None:
        if not(path_tools.get_content(library_path)):
            console.print(f"the file: [cyan]'{library_path}'[/] is [red1]empty[/].")
            sys.exit()
        if get_type == "variable":
            variables = get_data(library_path, parse_tools.get_variables_content, list_file)
            console.print(display(library_path, variables))
        elif get_type == "function":
            functions = get_data(library_path, parse_tools.get_functions, functions_content)
            console.print(display(library_path, functions))
        elif get_type == "class":
            classes = get_data(library_path, parse_tools.get_classes, classes_content)
            console.print(display(library_path, classes))
        elif get_type == "all":
            console.print(display_all(list_file))
        elif get_type == None:
            console.print(display_as_table(library_path, path_tools.get_content(library_path)))
            print("press CTRL-D or Enter to exit")

    elif get_help and not(get_list) and not(path) and not(tree) and not(name) and open_as == None and not(display_help) and get_type == None and display_content == None:
        get_help_for_pack = os_tools.get_output_command(["py", "-c", f"import {library} as pack; print(pack.__doc__)"])
        console.print(get_help_for_pack)

    elif get_list and not(get_help) and not(path) and not(tree) and not(name) and open_as == None and not(display_help) and get_type == None and display_content == None:
        console.print(packages)

    elif path and not(get_help) and not(get_list) and not(tree) and not(name) and open_as == None and not(display_help) and get_type == None and display_content == None:
        console.print(f"[light_cyan1]{library_path}[/]")

    elif tree and not(get_list) and not(path) and not(get_help) and not(name) and open_as == None and not(display_help) and get_type == None and display_content == None:
        get_path_of_pack = os_tools.get_output_command(["py", "-c", f"import {library} as pack; print(pack.__file__)"])[:-1]
        if path_tools.get_basename(get_path_of_pack) == "__init__.py":
            tree = path_tools.get_tree(path_tools.get_parent_path(get_path_of_pack))
            items = []
            for item in tree:
                items.append(item)
            path_tools.display_tree(path_tools.get_parent_path(get_path_of_pack), items)

    elif open_as != None and not(get_list) and not(path) and not(get_help) and not(tree) and not(display_help) and get_type == None and display_content == None:
        text_editor = "xed" if os_tools.get_machine_name() == "Linux" else "notepad"
        test = os_tools.get_output_command(["which", open_as])
        open_as = open_as if test != "" else text_editor
        os.system(f"{open_as} '{library_path}'")

    elif display_content != None and not(get_list) and not(path) and not(get_help) and not(tree) and not(name) and open_as == None:
        list_file = parse_tools.get_python_file_as_list(library_path)
        get_content = functions_content if display_content == "function" else classes_content
        if display_content == "variable":
            get_content = variables_content
        if get_content != []:
            for index in range(len(get_content)):
                title_content = f"[light_cyan1]Function:[/] [light_sky_blue1]{parse_tools.get_functions_name(functions_content)[index]}[/]" if display_content == "function" else f"[light_cyan1]Class:[/] [light_sky_blue1]{parse_tools.get_classes_name(classes_content)[index]}[/]"
                if display_content == "variable":
                    title_content = f"[light_cyan1]Variable:[/] [light_sky_blue1]{parse_tools.get_variables_name(variables_content)[index]}[/]"
                get_content = '\n'.join(get_content[index]) if display_content == "function" or display_content == "class" else get_content
                console.print(display_as_table(title_content, get_content))

    elif name and not(get_help) and not(get_list) and not(tree) and open_as == None and not(display_help) and get_type == None and display_content == None:
        console.print(f"[light_cyan1]Package Name:[/] [light_sky_blue1]'{import_lib_as_name}'[/]")

    elif display_help and display_content != None and not(get_list) and not(path) and not(get_help) and not(tree) and not(name) and open_as == None:
        pass

if __name__ == "__main__":
    main()
