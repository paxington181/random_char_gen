
def hc_stat_update(current_stats):
    str_update(current_stats[0][0])
    print(current_stats[0][0])
    dex_update(current_stats[1][0])
    con_update(current_stats[2][0])
    int_update(current_stats[3][0])
    wis_update(current_stats[4][0])
    cha_update(current_stats[5][0])
    mass_stat_button("", "", "", "", "", "")

# def reset_stats():
#     str_update(10)
#     dex_update(10)
#     con_update(10)
#     int_update(10)
#     wis_update(10)
#     cha_update(10)
#     stats_gen_selector.set("Standard")
    #mass_stat_button("", "", "", "", "", "")

def str_button_config(value1, value2, value3, value4, value5, value6):
    str_button_1.configure(text = f"{(value1)}", command = str_update(value1))
    str_button_2.configure(text = f"{(value2)}", command = str_update(value2))
    str_button_3.configure(text = f"{(value3)}", command = str_update(value3))
    str_button_4.configure(text = f"{(value4)}", command = str_update(value4))
    str_button_5.configure(text = f"{(value5)}", command = str_update(value5))
    str_button_6.configure(text = f"{(value6)}", command = str_update(value6))

def dex_button_config(value1, value2, value3, value4, value5, value6):
    dex_button_1.configure(text = f"{(value1)}", command = dex_update(value1))
    dex_button_2.configure(text = f"{(value2)}", command = dex_update(value2))
    dex_button_3.configure(text = f"{(value3)}", command = dex_update(value3))
    dex_button_4.configure(text = f"{(value4)}", command = dex_update(value4))
    dex_button_5.configure(text = f"{(value5)}", command = dex_update(value5))
    dex_button_6.configure(text = f"{(value6)}", command = dex_update(value6))

def con_button_config(value1, value2, value3, value4, value5, value6):
    con_button_1.configure(text = f"{(value1)}", command = con_update(value1))
    con_button_2.configure(text = f"{(value2)}", command = con_update(value2))
    con_button_3.configure(text = f"{(value3)}", command = con_update(value3))
    con_button_4.configure(text = f"{(value4)}", command = con_update(value4))
    con_button_5.configure(text = f"{(value5)}", command = con_update(value5))
    con_button_6.configure(text = f"{(value6)}", command = con_update(value6))

def int_button_config(value1, value2, value3, value4, value5, value6):
    int_button_1.configure(text = f"{(value1)}", command = int_update(value1))
    int_button_2.configure(text = f"{(value2)}", command = int_update(value2))
    int_button_3.configure(text = f"{(value3)}", command = int_update(value3))
    int_button_4.configure(text = f"{(value4)}", command = int_update(value4))
    int_button_5.configure(text = f"{(value5)}", command = int_update(value5))
    int_button_6.configure(text = f"{(value6)}", command = int_update(value6))

def wis_button_config(value1, value2, value3, value4, value5, value6):
    wis_button_1.configure(text = f"{(value1)}", command = wis_update(value1))
    wis_button_2.configure(text = f"{(value2)}", command = wis_update(value2))
    wis_button_3.configure(text = f"{(value3)}", command = wis_update(value3))
    wis_button_4.configure(text = f"{(value4)}", command = wis_update(value4))
    wis_button_5.configure(text = f"{(value5)}", command = wis_update(value5))
    wis_button_6.configure(text = f"{(value6)}", command = wis_update(value6))

def cha_button_config(value1, value2, value3, value4, value5, value6):
    cha_button_1.configure(text = f"{(value1)}", command = cha_update(value1))
    cha_button_2.configure(text = f"{(value2)}", command = cha_update(value2))
    cha_button_3.configure(text = f"{(value3)}", command = cha_update(value3))
    cha_button_4.configure(text = f"{(value4)}", command = cha_update(value4))
    cha_button_5.configure(text = f"{(value5)}", command = cha_update(value5))
    cha_button_6.configure(text = f"{(value6)}", command = cha_update(value6))

def mass_stat_button(value1, value2, value3, value4, value5, value6):
    str_button_config(value1, value2, value3, value4, value5, value6)
    dex_button_config(value1, value2, value3, value4, value5, value6)
    con_button_config(value1, value2, value3, value4, value5, value6)
    int_button_config(value1, value2, value3, value4, value5, value6)
    wis_button_config(value1, value2, value3, value4, value5, value6)
    cha_button_config(value1, value2, value3, value4, value5, value6)


str_button_1 = ttk.Button(main, text = "", command = None)
str_button_2 = ttk.Button(main, text = "", command = None)
str_button_3 = ttk.Button(main, text = "", command = None)
str_button_4 = ttk.Button(main, text = "", command = None)
str_button_5 = ttk.Button(main, text = "", command = None)
str_button_6 = ttk.Button(main, text = "", command = None)

dex_button_1 = ttk.Button(main, text = "", command = None)
dex_button_2 = ttk.Button(main, text = "", command = None)
dex_button_3 = ttk.Button(main, text = "", command = None)
dex_button_4 = ttk.Button(main, text = "", command = None)
dex_button_5 = ttk.Button(main, text = "", command = None)
dex_button_6 = ttk.Button(main, text = "", command = None)

con_button_1 = ttk.Button(main, text = "", command = None)
con_button_2 = ttk.Button(main, text = "", command = None)
con_button_3 = ttk.Button(main, text = "", command = None)
con_button_4 = ttk.Button(main, text = "", command = None)
con_button_5 = ttk.Button(main, text = "", command = None)
con_button_6 = ttk.Button(main, text = "", command = None)

int_button_1 = ttk.Button(main, text = "", command = None)
int_button_2 = ttk.Button(main, text = "", command = None)
int_button_3 = ttk.Button(main, text = "", command = None)
int_button_4 = ttk.Button(main, text = "", command = None)
int_button_5 = ttk.Button(main, text = "", command = None)
int_button_6 = ttk.Button(main, text = "", command = None)

wis_button_1 = ttk.Button(main, text = "", command = None)
wis_button_2 = ttk.Button(main, text = "", command = None)
wis_button_3 = ttk.Button(main, text = "", command = None)
wis_button_4 = ttk.Button(main, text = "", command = None)
wis_button_5 = ttk.Button(main, text = "", command = None)
wis_button_6 = ttk.Button(main, text = "", command = None)

cha_button_1 = ttk.Button(main, text = "", command = None)
cha_button_2 = ttk.Button(main, text = "", command = None)
cha_button_3 = ttk.Button(main, text = "", command = None)
cha_button_4 = ttk.Button(main, text = "", command = None)
cha_button_5 = ttk.Button(main, text = "", command = None)
cha_button_6 = ttk.Button(main, text = "", command = None)

# def str_update(current_stat):
#     str_stat.configure(text = f"{current_stat}")
#     print(current_stat)
#     str_modifier.configure(text = f"{modifier_update(current_stat)}")

# def dex_update(current_stat):
#     dex_stat.configure(text = f"{current_stat}")
#     dex_modifier.configure(text = f"{modifier_update(current_stat)}")

# def con_update(current_stat):
#     con_stat.configure(text = f"{current_stat}")
#     con_modifier.configure(text = f"{modifier_update(current_stat)}")

# def int_update(current_stat):
#     int_stat.configure(text = f"{current_stat}")
#     int_modifier.configure(text = f"{modifier_update(current_stat)}")

# def wis_update(current_stat):
#     wis_stat.configure(text = f"{current_stat}")
#     wis_modifier.configure(text = f"{modifier_update(current_stat)}")

# def cha_update(current_stat):
#     cha_stat.configure(text = f"{current_stat}")
#     cha_modifier.configure(text = f"{modifier_update(current_stat)}")

str_button_1.grid(row = 2, column = 3, sticky = "nswe")
str_button_2.grid(row = 2, column = 4, sticky = "nswe")
str_button_3.grid(row = 2, column = 5, sticky = "nswe")
str_button_4.grid(row = 2, column = 6, sticky = "nswe")
str_button_5.grid(row = 2, column = 7, sticky = "nswe")
str_button_6.grid(row = 2, column = 8, sticky = "nswe")

dex_button_1.grid(row = 3, column = 3, sticky = "nswe")
dex_button_2.grid(row = 3, column = 4, sticky = "nswe")
dex_button_3.grid(row = 3, column = 5, sticky = "nswe")
dex_button_4.grid(row = 3, column = 6, sticky = "nswe")
dex_button_5.grid(row = 3, column = 7, sticky = "nswe")
dex_button_6.grid(row = 3, column = 8, sticky = "nswe")

con_button_1.grid(row = 4, column = 3, sticky = "nswe")
con_button_2.grid(row = 4, column = 4, sticky = "nswe")
con_button_3.grid(row = 4, column = 5, sticky = "nswe")
con_button_4.grid(row = 4, column = 6, sticky = "nswe")
con_button_5.grid(row = 4, column = 7, sticky = "nswe")
con_button_6.grid(row = 4, column = 8, sticky = "nswe")

int_button_1.grid(row = 5, column = 3, sticky = "nswe")
int_button_2.grid(row = 5, column = 4, sticky = "nswe")
int_button_3.grid(row = 5, column = 5, sticky = "nswe")
int_button_4.grid(row = 5, column = 6, sticky = "nswe")
int_button_5.grid(row = 5, column = 7, sticky = "nswe")
int_button_6.grid(row = 5, column = 8, sticky = "nswe")

wis_button_1.grid(row = 6, column = 3, sticky = "nswe")
wis_button_2.grid(row = 6, column = 4, sticky = "nswe")
wis_button_3.grid(row = 6, column = 5, sticky = "nswe")
wis_button_4.grid(row = 6, column = 6, sticky = "nswe")
wis_button_5.grid(row = 6, column = 7, sticky = "nswe")
wis_button_6.grid(row = 6, column = 8, sticky = "nswe")

cha_button_1.grid(row = 7, column = 3, sticky = "nswe")
cha_button_2.grid(row = 7, column = 4, sticky = "nswe")
cha_button_3.grid(row = 7, column = 5, sticky = "nswe")
cha_button_4.grid(row = 7, column = 6, sticky = "nswe")
cha_button_5.grid(row = 7, column = 7, sticky = "nswe")
cha_button_6.grid(row = 7, column = 8, sticky = "nswe")