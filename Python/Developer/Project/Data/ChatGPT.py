#!/usr/bin/python3.13
import sys
import json
import salah.math.number.tools as math_tools
import salah.system.path.tools as path_tools
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
import click

console = Console()

def display_as_table(key, value):
    table = Table()
    table.add_column(f"[sky_blue1]{key}[/]", justify="center")
    table.add_row(value)
    return table

def display_chat_as_tables(chat):
    for line in chat:
        table = Table()
        talker_is_you = True if math_tools.is_odd(chat.index(line)+1) else False
        if talker_is_you:
            table.add_column(f"[sky_blue1]{line}[/]", justify="center")
            table.add_row(Markdown(chat[chat.index(line)+1]))
        console.print(table)

path = "D:\\Data\\SALAH\\Linux\\home\\salah\\Documents\\.openai\\ChatGPT\\conversations.json"
conversations = json.load(open(path, 'r', encoding="utf-8"))[:-1]

titles = []
for index in range(len(conversations)):
    title = conversations[index]['title']
    titles.append(title)

ids_dict = {}
for index in range(len(conversations)):
    conversation = conversations[index]
    ids_dict[titles[index]] = []
    for id in conversation["mapping"]:
        ids_dict[titles[index]].append(id)

if len(titles) != len(list(ids_dict.keys())):
    display = ""
    for title in titles:
        display = f"{title}: {titles.count(title)}" if not(title in display) and titles.count(title) > 1 else display
    print(display)
    sys.exit()

conversations_dict = {}
for title in ids_dict:
    index = list(ids_dict.keys()).index(title)
    conversations_dict[title] = []
    for id in ids_dict[title]:
        if  "message" in list(conversations[index]["mapping"][id].keys()):
            if conversations[index]["mapping"][id]["message"] != None and "parts" in list(conversations[index]["mapping"][id]["message"]["content"].keys()) and "recipient" in list(conversations[index]["mapping"][id]["message"].keys()):
                conversation = conversations[index]["mapping"][id]["message"]["content"]["parts"][0]
                if conversation != "" and conversations[index]["mapping"][id]["message"]["recipient"] == "all":
                    content = conversation
                    conversations_dict[title].append(content)

conversation_with_talker_dict = {}
for title in titles:
    conversation_with_talker_dict[title] = []
    for chat in conversations_dict[title]:
        talker = "`You:`" if math_tools.is_odd(conversations_dict[title].index(chat)+1) else "`AI:`"
        conversation_with_talker_dict[title].append(f"{talker} {chat}") if conversations_dict[title].index(chat) == conversations_dict[title][-1] else conversation_with_talker_dict[title].append(f"{talker} {chat}\n")

@click.command(help="All your conversations chat with ChatGPT")
@click.argument("chat", required=False)
@click.option('-p', "--print-chat", required=False, is_flag=True, help="Print specific chat by name")
@click.option('-i', "--print-chat-element", required=False, type=int, help="Display specific chat by name with specific element")
@click.option('-d', "--display-all", required=False, is_flag=True, help="Display all your chats")
@click.option('-l', "--list-names", required=False, is_flag=True, help="Print your chats name")
@click.option('-s', "--save-as-json", required=False, is_flag=True, help="Save your chat as JSON file")
@click.option('-S', "--save-all-as-json", required=False, help="Save all your chats as JSON file")
@click.option('-m', "--markdown-chat", required=False, is_flag=True, help="Save your chat as Markdown file")
@click.option('-M', "--markdown-chats", required=False, help="Save all your chats as Markdown file")
def main(chat, print_chat, print_chat_element, display_all, save_as_json, save_all_as_json, list_names, markdown_chat, markdown_chats):
    possible_chat = []
    if chat != None:
        for title in titles:
            if chat == title:
                possible_chat = []
                break
            possible_chat.append(title) if chat in title else None
        if possible_chat != []:
            error = f"[[red1]ERROR[/]] [cyan]'{chat}'[/] was not found.\n[[green1]INFO[/]] are you mentioning to these chats?: [yellow]{possible_chat}[/]." if len(possible_chat) > 1 else \
               f"[[red1]ERROR[/]] [cyan]'{chat}'[/] was not found.\n[[green1]INFO[/]] are you mentioning to this chat?: [yellow]'{possible_chat[0]}'[/]."
            console.print(error)
    if print_chat and chat != None:
        display_chat_as_tables(conversations_dict[chat])
    elif print_chat_element != None and chat != None:
        index = print_chat_element if math_tools.is_even(print_chat_element) else print_chat_element+1
        try:
            # console.print(display_as_table(conversations_dict[chat][index], Markdown(conversations_dict[chat][index+1])))
            print(index, index+1)
        except IndexError:
            console.print(f"[[red1]ERROR[/]] there is no element for index: [cyan]'{print_chat_element}'[/].")
    elif display_all and chat == None:
        for title in titles:
            console.print(f"[green1]{title}[/]")
            display_chat_as_tables(conversations_dict[title])
            print('\n')
    elif list_names and chat == None:
        console.print('\n'.join(titles))
    elif save_as_json and chat != None:
        json_file =  f"{''.join(chat.split('.'))}.json"
        json.dump(conversation_with_talker_dict[chat], open(json_file, 'w', encoding="utf-8"))
        display = f"your chat: [cyan]'{chat}'[/] has been [green1]successfully[/] saved in: [yellow]'{path_tools.get_full_path(json_file)}'[/] file path."
        console.print(display)
    elif save_all_as_json != None and chat == None:
        json_file = ''.join(save_all_as_json.split('.')[0:-1]) if save_all_as_json.endswith('.json') else f"{''.join(save_all_as_json.split('.'))}.json"
        json.dump(conversation_with_talker_dict, open(json_file, 'w', encoding="utf-8"))
        display = f"all your chats has been [green1]successfully[/] saved in: [yellow]'{path_tools.get_full_path(json_file)}'[/] file path."
        console.print(display)
    elif markdown_chat and chat != None:
        markdown_file =  f"{''.join(chat.split('.'))}.md"
        open(markdown_file, 'w', encoding="utf-8").write('\n'.join(conversations_dict[chat]))
        display = f"your chat: [cyan]'{chat}'[/] has been [green1]successfully[/] saved in: [yellow]'{path_tools.get_full_path(markdown_file)}'[/] file path."
        console.print(display)
    elif markdown_chats != None and chat == None:
        markdown_file = ''.join(markdown_chats.split('.')[0:-1]) if markdown_chats.endswith('.md') else f"{''.join(markdown_chats.split('.'))}.md"
        open(markdown_file, 'w', encoding="utf-8").write("")
        for title in titles:
            open(markdown_file, 'a', encoding="utf-8").write('\n'.join(conversations_dict[title]))
        display = f"all your chats has been [green1]successfully[/] saved in: [yellow]'{path_tools.get_full_path(json_file)}'[/] file path."
        console.print(display)

if __name__ == "__main__":
    main()
