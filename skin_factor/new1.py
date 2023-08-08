from skin import *
from tkinter import *
from time import *
from PIL import Image, ImageTk
import ttkbootstrap as tb
import os
import sys
import pygame
import pyautogui



screen = pyautogui.size()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app=tb.Window(themename="darkly")
app.title('Skin Analysis')
if screen == (1920, 1080):
    app.geometry('750x1001+200+0')
app.resizable(False, True)
app.iconbitmap(resource_path("logo.ico"))


#variables

s=tk.BooleanVar()
muskatvar=IntVar()
play_pause_var=IntVar()
play_pause_var.set(1)

# Images

muskat_top_image=Image.open(resource_path('muskat_top.png')).resize((300, 250))
muskat_top_image=ImageTk.PhotoImage(muskat_top_image)
muskat_middle_image=Image.open(resource_path('muskat_middle.png')).resize((300, 250))
muskat_middle_image=ImageTk.PhotoImage(muskat_middle_image)
furui_image=Image.open(resource_path('furui.png')).resize((300, 250))
furui_image=ImageTk.PhotoImage(furui_image)
golan_image=Image.open(resource_path('golan.png')).resize((300, 250))
golan_image=ImageTk.PhotoImage(golan_image)
odeh_image=Image.open(resource_path('odeh.png')).resize((300, 250))
odeh_image=ImageTk.PhotoImage(odeh_image)
papatzacos_image=Image.open(resource_path('papatzacos.png')).resize((300, 250))
papatzacos_image=ImageTk.PhotoImage(papatzacos_image)
perforation_image=Image.open(resource_path('perforation.png')).resize((300, 250))
perforation_image=ImageTk.PhotoImage(perforation_image)
slanted_image=Image.open(resource_path('slanted.png')).resize((300, 250))
slanted_image=ImageTk.PhotoImage(slanted_image)
plus_image=Image.open(resource_path('plus.png')).resize((20, 20))
plus_image=ImageTk.PhotoImage(plus_image)
uni_image=Image.open(resource_path('logo_en.png')).resize((200, 200))
uni_image=ImageTk.PhotoImage(uni_image)
play_image=Image.open(resource_path('play.png')).resize((40, 40))
play_image=ImageTk.PhotoImage(play_image)


## menu items

perforation_menu_items=['Karakas & Tariq(1988)',]
perforation_menu_var=StringVar()
gravel_menu_items=['Golan and Whitson (1991)', 'Furui (2004)']
gravel_menu_var=StringVar()
slanted_menu_items=['Cinco et al. (1975)', 'Besson (1990)']
slanted_menu_var=StringVar()
partial_menu_items=['Muskat (1946)', 'Odeh (1980)', 'Papatzacos (1987)']
partial_menu_var=StringVar()
phasing_menu_items=[0, 45, 60, 90, 120, 180]
phasing_menu_var=IntVar()
gravel_mesh_size_menu_items=['40/60', '20/40', '10/20', '8/12']
gravel_mesh_size_menu_var=StringVar()
non_darcy_mesh_size_menu_var=StringVar()

## menu variables

Perforation_Yes_Novar=IntVar()
Gravel_Yes_Novar=IntVar()
Slanted_Yes_Novar=IntVar()
Partial_Yes_Novar=IntVar()
Non_darcy_Yes_Novar=IntVar()
Gas_Oilvar=IntVar()

## default values

DefaultPayZoneThickness=''
DefaultWellRadius=''
DefaultAnisotropy=''
DefaultPerforationLength=''
DefaultSpf=''
DefaultPerforationTunnelRadius=''
DefaultPhasingAng='Select an Angle'
DefaultPermeability=''
DefaultMeshSize='Select a size'



## python variables

count=0

## circle variables

circle=list(range((len(Skin(2).all_skins))))

empty_circle=(Image.open(resource_path('empty_circle.png'))).resize((15,15))
empty_circle=ImageTk.PhotoImage(empty_circle)
solid_circle=(Image.open(resource_path('solid_circle.png'))).resize((18, 15))
solid_circle=ImageTk.PhotoImage(solid_circle)


## Perforation initial values

global perforation_skin_value, slanted_skin_value, gravel_skin_value, non_darcy_skin_value, partial_skin_value, resbutton, ent_oil_fvf

perforation_skin_value = 0
slanted_skin_value = 0
gravel_skin_value = 0
non_darcy_skin_value = 0
partial_skin_value = 0


#functions

def perforation():

    global left_frame

    ############################# right frame  ###############################

    right_frame=Frame(take_frame)
    right_frame.grid_propagate(0)
    right_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='right')

    ############################# vertical separator ########################

    sep1=tb.Separator(take_frame, bootstyle='danger', orient='vertical')
    sep1.pack(fill='both', pady=50, side='right', expand=False)

    ############################# left frame  #############################

    left_frame=Frame(take_frame)
    left_frame.grid_propagate(0)
    left_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='left')

    ############################# top frame  #############################

    top_frame=Frame(left_frame, height=30)
    top_frame.grid_propagate(0)
    top_frame.pack(ipadx=10, ipady=10, fill='both', side='top')

    ############################# down frame  #############################

    down_frame=Frame(left_frame)
    down_frame.grid_propagate(0)
    down_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='bottom')

    ############################# menu button  ############################

    method_menu=tb.Menubutton(top_frame, bootstyle='warning outline', text='Method of Calculation')
    method_menu.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    method_menu_inside=tb.Menu(method_menu)

    for x in perforation_menu_items:
        method_menu_inside.add_radiobutton(label=x, variable=perforation_menu_var, command=lambda x=x: menu(x))
        
    method_menu['menu']=method_menu_inside

    #############################     Method of Calculation   #################################
    
    def Tariq():
    
        global ent_Well_Radius, ent_perforation_length, phasing_menu_var, ent_spf, ent_Anisotropy, ent_damage_ratio, ent_crushed_ratio, ent_Damage_zone_radius, ent_crushed_zone_radius, ent_perforation_tunnel_radius

    
        label_Well_Radius=tb.Label(down_frame, text='Well Radius (in.)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_perforation_length=tb.Label(down_frame, text='Perforation Length (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_length.grid(row=2, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_length=tb.Entry(down_frame, width=12)
        ent_perforation_length.insert(END, DefaultPerforationLength)
        ent_perforation_length.grid(row=2, column=1, padx=10, pady=12)

        label_phasing_angel=tb.Label(down_frame, text='Phasing Angel (degree)= ', bootstyle='danger', anchor='e')
        label_phasing_angel.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        # ent_phasing_angel=tb.Entry(down_frame, width=12)
        # ent_phasing_angel.insert(END, DefaultPhasingAng)
        # ent_phasing_angel.grid(row=3, column=1, padx=10, pady=12)
        phasing_menu=tb.Menubutton(down_frame, bootstyle='danger outlined', width=50, text=DefaultPhasingAng)
        phasing_menu.grid(row=3, column=1, padx=10, pady=12)

        method_menu_inside=tb.Menu(phasing_menu)

        for x in phasing_menu_items:
            method_menu_inside.add_radiobutton(label=x, variable=phasing_menu_var, command=lambda x=x: phasing(x))
            
        phasing_menu['menu']=method_menu_inside
        
        def phasing(x):
            phasing_menu_var.set(x)
            phasing_menu.config(text=int(x))
            

        label_spf=tb.Label(down_frame, text='SPF= ', bootstyle='danger', anchor='e')
        label_spf.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_spf=tb.Entry(down_frame, width=12)
        ent_spf.insert(END, DefaultSpf)
        ent_spf.grid(row=4, column=1, padx=10, pady=12)

        label_Anisotropy=tb.Label(down_frame, text='Anisotropy (Kv/Kh)= ', bootstyle='danger', anchor='e')
        label_Anisotropy.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_Anisotropy=tb.Entry(down_frame, width=12)
        ent_Anisotropy.insert(END, DefaultAnisotropy)
        ent_Anisotropy.grid(row=5, column=1, padx=10, pady=12)

        label_damage_ratio=tb.Label(down_frame, text='Kd/K= ', bootstyle='danger', anchor='e')
        label_damage_ratio.grid(row=6, column=0, padx=10, pady=12, sticky='w')
        ent_damage_ratio=tb.Entry(down_frame, width=12)
        ent_damage_ratio.grid(row=6, column=1, padx=10, pady=12)

        label_crushed_ratio=tb.Label(down_frame, text='Kc/K= ', bootstyle='danger', anchor='e')
        label_crushed_ratio.grid(row=7, column=0, padx=10, pady=12, sticky='w')
        ent_crushed_ratio=tb.Entry(down_frame, width=12)
        ent_crushed_ratio.grid(row=7, column=1, padx=10, pady=12)

        label_Damage_zone_radius=tb.Label(down_frame, text='Damage Zone Radius (in.)= ', bootstyle='danger', anchor='e')
        label_Damage_zone_radius.grid(row=8, column=0, padx=10, pady=12, sticky='w')
        ent_Damage_zone_radius=tb.Entry(down_frame, width=12)
        ent_Damage_zone_radius.grid(row=8, column=1, padx=10, pady=12)

        label_crushed_zone_radius=tb.Label(down_frame, text='Crushed Zone Radius (in.)= ', bootstyle='danger', anchor='e')
        label_crushed_zone_radius.grid(row=9, column=0, padx=10, pady=12, sticky='w')
        ent_crushed_zone_radius=tb.Entry(down_frame, width=12)
        ent_crushed_zone_radius.grid(row=9, column=1, padx=10, pady=12)

        label_perforation_tunnel_radius=tb.Label(down_frame, text='Perforation Tunnel Radius (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_tunnel_radius.grid(row=10, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_tunnel_radius=tb.Entry(down_frame, width=12)
        ent_perforation_tunnel_radius.insert(END, DefaultPerforationTunnelRadius)
        ent_perforation_tunnel_radius.grid(row=10, column=1, padx=10, pady=12)
        
        perforation_image_label=tb.Label(right_frame, image=perforation_image, bootstyle='danger', anchor='e')
        perforation_image_label.grid(row=0, column=0, padx=20, pady=200)
        
        
    Tariq()
    def menu(x):
    
        for widget in down_frame.winfo_children():
                widget.destroy()
        method_menu.config(text=x)
        if x==perforation_menu_items[0]:
            Tariq()

    ##########################################################################
    ##########################################################################
    
    
def gravel():

    ############################# right frame  ###############################

    right_frame=Frame(take_frame)
    right_frame.grid_propagate(0)
    right_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='right')

    ############################# vertical separator ########################

    sep1=tb.Separator(take_frame, bootstyle='danger', orient='vertical')
    sep1.pack(fill='both', pady=50, side='right', expand=False)

    ############################# left frame  #############################

    left_frame=Frame(take_frame)
    left_frame.grid_propagate(0)
    left_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='left')

    ############################# top frame  #############################

    top_frame=Frame(left_frame, height=30)
    top_frame.grid_propagate(0)
    top_frame.pack(ipadx=10, ipady=10, fill='both', side='top')

    ############################# down frame  #############################

    down_frame=Frame(left_frame)
    down_frame.grid_propagate(0)
    down_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='bottom')

    ############################# menu button  ############################

    method_menu=tb.Menubutton(top_frame, bootstyle='warning outline', text='Method of Calculation')
    method_menu.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    method_menu_inside=tb.Menu(method_menu)

    for x in gravel_menu_items:
        method_menu_inside.add_radiobutton(label=x, variable=gravel_menu_var, command=lambda x=x: menu(x))
        
    method_menu['menu']=method_menu_inside

    #############################     Method of Calculation   #################################
    
    def Golan():
    
        global ent_perforation_length, ent_permeability, ent_pay_zone_thickness, ent_spf

    
        label_perforation_length=tb.Label(down_frame, text='Perforation Length (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_length.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_length=tb.Entry(down_frame, width=12)
        ent_perforation_length.insert(END, DefaultPerforationLength)
        ent_perforation_length.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)
    
    
        label_permeability=tb.Label(down_frame, text='Permeability (mD)= ', bootstyle='danger', anchor='e')
        label_permeability.grid(row=2, column=0, padx=10, pady=12, sticky='w')
        ent_permeability=tb.Entry(down_frame, width=12)
        ent_permeability.insert(END, DefaultPermeability)
        ent_permeability.grid(row=2, column=1, padx=10, pady=12)
        

        label_pay_zone_thickness=tb.Label(down_frame, text='Pay Zone Thickness (ft)= ', bootstyle='danger')
        label_pay_zone_thickness.grid(row=3, column=0, padx=10, pady=12, sticky='w' )
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=3, column=1, padx=10, pady=12)

        label_spf=tb.Label(down_frame, text='SPF= ', bootstyle='danger', anchor='e')
        label_spf.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_spf=tb.Entry(down_frame, width=12)
        ent_spf.insert(END, DefaultSpf)
        ent_spf.grid(row=4, column=1, padx=10, pady=12)
        
        golan_image_label=tb.Label(right_frame, image=golan_image, bootstyle='danger', anchor='e')
        golan_image_label.grid(row=0, column=0, padx=20, pady=200)


        label_mesh_size=tb.Label(down_frame, text='Mesh Size= ', bootstyle='danger', anchor='e')
        label_mesh_size.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        mesh_menu=tb.Menubutton(down_frame, bootstyle='danger outlined', width=50, text=DefaultMeshSize)
        mesh_menu.grid(row=5, column=1, padx=10, pady=12)

        method_menu_inside=tb.Menu(mesh_menu)

        for x in gravel_mesh_size_menu_items:
            method_menu_inside.add_radiobutton(label=x, variable=gravel_mesh_size_menu_var, command=lambda x=x: mesh(x))
            
        mesh_menu['menu']=method_menu_inside

        
    def Furui():
        
        global ent_perforation_length, ent_perforation_tunnel_radius, ent_casing_thickness, ent_spf, phasing_menu_var, ent_permeability, ent_Well_Radius, gravel_mesh_size_menu_var
        
        label_perforation_length=tb.Label(down_frame, text='Perforation Length (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_length.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_length=tb.Entry(down_frame, width=12)
        ent_perforation_length.insert(END, DefaultPerforationLength)
        ent_perforation_length.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)
    
        label_perforation_tunnel_radius=tb.Label(down_frame, text='Perforation Tunnel Radius (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_tunnel_radius.grid(row=2, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_tunnel_radius=tb.Entry(down_frame, width=12)
        ent_perforation_tunnel_radius.insert(END, DefaultPerforationTunnelRadius)
        ent_perforation_tunnel_radius.grid(row=2, column=1, padx=10, pady=12)
    
        label_casing_thickness=tb.Label(down_frame, text='Casing Thickness (in.)= ', bootstyle='danger', anchor='e')
        label_casing_thickness.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        ent_casing_thickness=tb.Entry(down_frame, width=12)
        ent_casing_thickness.grid(row=3, column=1, padx=10, pady=12)
        
        label_spf=tb.Label(down_frame, text='SPF= ', bootstyle='danger', anchor='e')
        label_spf.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_spf=tb.Entry(down_frame, width=12)
        ent_spf.insert(END, DefaultSpf)
        ent_spf.grid(row=4, column=1, padx=10, pady=12)

        label_phasing_angel=tb.Label(down_frame, text='Phasing Angel (degree)= ', bootstyle='danger', anchor='e')
        label_phasing_angel.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        # ent_phasing_angel=tb.Entry(down_frame, width=12)
        # ent_phasing_angel.insert(END, DefaultPhasingAng)
        # ent_phasing_angel.grid(row=5, column=1, padx=10, pady=12)
        phasing_menu=tb.Menubutton(down_frame, bootstyle='danger outlined', width=50, text=DefaultPhasingAng)
        phasing_menu.grid(row=5, column=1, padx=10, pady=12)

        method_menu_inside=tb.Menu(phasing_menu)

        for x in phasing_menu_items:
            method_menu_inside.add_radiobutton(label=x, variable=phasing_menu_var, command=lambda x=x: phasing(x))
            
        phasing_menu['menu']=method_menu_inside
        
        def phasing(x):
            phasing_menu_var.set(x)
            phasing_menu.config(text=int(x))


        label_permeability=tb.Label(down_frame, text='Permeability (mD)= ', bootstyle='danger', anchor='e')
        label_permeability.grid(row=6, column=0, padx=10, pady=12, sticky='w')
        ent_permeability=tb.Entry(down_frame, width=12)
        ent_permeability.insert(END, DefaultPermeability)
        ent_permeability.grid(row=6, column=1, padx=10, pady=12)
        
        label_Well_Radius=tb.Label(down_frame, text='Well Radius (in.)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=7, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=7, column=1, padx=10, pady=12)
        
        furui_image_label=tb.Label(right_frame, image=furui_image, bootstyle='danger', anchor='e')
        furui_image_label.grid(row=0, column=0, padx=20, pady=200)


        label_mesh_size=tb.Label(down_frame, text='Mesh Size= ', bootstyle='danger', anchor='e')
        label_mesh_size.grid(row=8, column=0, padx=10, pady=12, sticky='w')
        mesh_menu=tb.Menubutton(down_frame, bootstyle='danger outlined', width=50, text=DefaultMeshSize)
        mesh_menu.grid(row=8, column=1, padx=10, pady=12)

        method_menu_inside=tb.Menu(mesh_menu)

        for x in gravel_mesh_size_menu_items:
            method_menu_inside.add_radiobutton(label=x, variable=gravel_mesh_size_menu_var, command=lambda x=x: mesh(x))
            
        mesh_menu['menu']=method_menu_inside
        def mesh(x):
            gravel_mesh_size_menu_var.set(x)
            mesh_menu.config(text=x)
        
    Furui()
    
    
    
    def menu(x):
        for widget in down_frame.winfo_children():
                widget.destroy()
        method_menu.config(text=x)
        if x==gravel_menu_items[0]:
            Golan()
            
        if x==gravel_menu_items[1]:
            Furui()

def slanted_well():

    ############################# right frame  ###############################

    right_frame=Frame(take_frame)
    right_frame.grid_propagate(0)
    right_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='right')

    ############################# vertical separator ########################

    sep1=tb.Separator(take_frame, bootstyle='danger', orient='vertical')
    sep1.pack(fill='both', pady=50, side='right', expand=False)

    ############################# left frame  #############################

    left_frame=Frame(take_frame)
    left_frame.grid_propagate(0)
    left_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='left')

    ############################# top frame  #############################

    top_frame=Frame(left_frame, height=30)
    top_frame.grid_propagate(0)
    top_frame.pack(ipadx=10, ipady=10, fill='both', side='top')

    ############################# down frame  #############################

    down_frame=Frame(left_frame)
    down_frame.grid_propagate(0)
    down_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='bottom')

    ############################# menu button  ############################

    method_menu=tb.Menubutton(top_frame, bootstyle='warning outline', text='Method of Calculation')
    method_menu.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    method_menu_inside=tb.Menu(method_menu)

    for x in slanted_menu_items:
        method_menu_inside.add_radiobutton(label=x, variable=slanted_menu_var, command=lambda x=x: menu(x))
        
    method_menu['menu']=method_menu_inside

    #############################     Method of Calculation   #################################
    
    def Cinco():
    
        global ent_pay_zone_thickness, ent_completion_thickness, ent_Well_Radius, ent_Anisotropy, ent_deviation_angel

    
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)


        label_Well_Radius=tb.Label(down_frame, text='Well Radius (ft)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=3, column=1, padx=10, pady=12)
        
        label_Anisotropy=tb.Label(down_frame, text='Anisotropy (Kv/Kh)= ', bootstyle='danger', anchor='e')
        label_Anisotropy.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_Anisotropy=tb.Entry(down_frame, width=12)
        ent_Anisotropy.insert(END, DefaultAnisotropy)
        ent_Anisotropy.grid(row=4, column=1, padx=10, pady=12)
        

        label_deviation_angel=tb.Label(down_frame, text='Deviation Angel= ', bootstyle='danger', anchor='e')
        label_deviation_angel.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_deviation_angel=tb.Entry(down_frame, width=12)
        ent_deviation_angel.grid(row=5, column=1, padx=10, pady=12)
        
        slanted_image_label=tb.Label(right_frame, image=slanted_image, bootstyle='danger', anchor='e')
        slanted_image_label.grid(row=0, column=0, padx=20, pady=200)

        
    def Besson():
    
        global ent_pay_zone_thickness, ent_completion_thickness, ent_Well_Radius, ent_Anisotropy, ent_deviation_angel

    
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)


        label_Well_Radius=tb.Label(down_frame, text='Well Radius (ft)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=3, column=1, padx=10, pady=12)
        
        label_Anisotropy=tb.Label(down_frame, text='Anisotropy (Kv/Kh)= ', bootstyle='danger', anchor='e')
        label_Anisotropy.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_Anisotropy=tb.Entry(down_frame, width=12)
        ent_Anisotropy.insert(END, DefaultAnisotropy)
        ent_Anisotropy.grid(row=4, column=1, padx=10, pady=12)
        

        label_deviation_angel=tb.Label(down_frame, text='Deviation Angel= ', bootstyle='danger', anchor='e')
        label_deviation_angel.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_deviation_angel=tb.Entry(down_frame, width=12)
        ent_deviation_angel.grid(row=5, column=1, padx=10, pady=12)
        
        slanted_image_label=tb.Label(right_frame, image=slanted_image, bootstyle='danger', anchor='e')
        slanted_image_label.grid(row=0, column=0, padx=20, pady=200)
        
    Besson()
    
    def menu(x):
        for widget in down_frame.winfo_children():
                widget.destroy()
        method_menu.config(text=x)
        if x==slanted_menu_items[0]:
            Cinco()
                    
        if x==slanted_menu_items[1]:
            Besson()
    
def partial():

    ############################# right frame  ###############################

    right_frame=Frame(take_frame)
    right_frame.grid_propagate(0)
    right_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='right')

    ############################# vertical separator ########################

    sep1=tb.Separator(take_frame, bootstyle='danger', orient='vertical')
    sep1.pack(fill='both', pady=50, side='right', expand=False)

    ############################# left frame  #############################

    left_frame=Frame(take_frame)
    left_frame.grid_propagate(0)
    left_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='left')

    ############################# top frame  #############################

    top_frame=Frame(left_frame, height=30)
    top_frame.grid_propagate(0)
    top_frame.pack(ipadx=10, ipady=10, fill='both', side='top')

    ############################# down frame  #############################

    down_frame=Frame(left_frame)
    down_frame.grid_propagate(0)
    down_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='bottom')

    ############################# menu button  ############################

    method_menu=tb.Menubutton(top_frame, bootstyle='warning outline', text='Method of Calculation')
    method_menu.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    method_menu_inside=tb.Menu(method_menu)

    for x in partial_menu_items:
        method_menu_inside.add_radiobutton(label=x, variable=partial_menu_var, command=lambda x=x: menu(x))
        
    method_menu['menu']=method_menu_inside

    #############################     Method of Calculation   #################################
    
    def Papatzacos():
    
        global ent_pay_zone_thickness, ent_completion_thickness, ent_Well_Radius, ent_Anisotropy, ent_completion_position

    
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_completion_thickness=tb.Label(down_frame, text='Completion Thickness (ft)= ', bootstyle='danger')
        label_completion_thickness.grid(row=2, column=0, padx=10, pady=12, sticky='w' )
        ent_completion_thickness=tb.Entry(down_frame, width=12)
        ent_completion_thickness.grid(row=2, column=1, padx=10, pady=12)


        label_Well_Radius=tb.Label(down_frame, text='Well Radius (ft)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=3, column=1, padx=10, pady=12)
        
        label_Anisotropy=tb.Label(down_frame, text='Anisotropy (Kv/Kh)= ', bootstyle='danger', anchor='e')
        label_Anisotropy.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_Anisotropy=tb.Entry(down_frame, width=12)
        ent_Anisotropy.insert(END, DefaultAnisotropy)
        ent_Anisotropy.grid(row=4, column=1, padx=10, pady=12)
        

        label_completion_position=tb.Label(down_frame, text='completion position (h1)= ', bootstyle='danger', anchor='e')
        label_completion_position.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_completion_position=tb.Entry(down_frame, width=12)
        ent_completion_position.grid(row=5, column=1, padx=10, pady=12)
        
        papatzacos_image_label=tb.Label(right_frame, image=papatzacos_image, bootstyle='danger', anchor='e')
        papatzacos_image_label.grid(row=0, column=0, padx=20, pady=200)
        
        
    def Odeh():
        
        global ent_pay_zone_thickness, ent_completion_thickness, ent_Well_Radius, ent_Anisotropy, ent_completion_position

        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_completion_thickness=tb.Label(down_frame, text='Completion Thickness (ft)= ', bootstyle='danger')
        label_completion_thickness.grid(row=2, column=0, padx=10, pady=12, sticky='w' )
        ent_completion_thickness=tb.Entry(down_frame, width=12)
        ent_completion_thickness.grid(row=2, column=1, padx=10, pady=12)


        label_Well_Radius=tb.Label(down_frame, text='Well Radius (ft)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=3, column=1, padx=10, pady=12)
        
        label_Anisotropy=tb.Label(down_frame, text='Anisotropy (Kv/Kh)= ', bootstyle='danger', anchor='e')
        label_Anisotropy.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_Anisotropy=tb.Entry(down_frame, width=12)
        ent_Anisotropy.insert(END, DefaultAnisotropy)
        ent_Anisotropy.grid(row=4, column=1, padx=10, pady=12)
        

        label_completion_position=tb.Label(down_frame, text='completion position (Zm)= ', bootstyle='danger', anchor='e')
        label_completion_position.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_completion_position=tb.Entry(down_frame, width=12)
        ent_completion_position.grid(row=5, column=1, padx=10, pady=12)
        
        odeh_image_label=tb.Label(right_frame, image=odeh_image, bootstyle='danger', anchor='e')
        odeh_image_label.grid(row=0, column=0, padx=20, pady=200)
        
    def Muskat():
        
        global ent_pay_zone_thickness, ent_completion_thickness, ent_Well_Radius, ent_Drainage_Radius
        
        def Muskat_top(value):
        
            if value==1:
                muskat_middle_image_label.grid_forget()
                muskat_top_image_label.grid(row=0, column=0, padx=20, pady=200)
            elif value==2:
                muskat_top_image_label.grid_forget()
                muskat_middle_image_label.grid(row=0, column=0, padx=20, pady=200)
            
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_completion_thickness=tb.Label(down_frame, text='Completion Thickness (ft)= ', bootstyle='danger')
        label_completion_thickness.grid(row=2, column=0, padx=10, pady=12, sticky='w' )
        ent_completion_thickness=tb.Entry(down_frame, width=12)
        ent_completion_thickness.grid(row=2, column=1, padx=10, pady=12)


        label_Well_Radius=tb.Label(down_frame, text='Well Radius (ft)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=3, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=3, column=1, padx=10, pady=12)
        
        label_Drainage_Radius=tb.Label(down_frame, text='Drainage Radius (ft)= ', bootstyle='danger', anchor='e')
        label_Drainage_Radius.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_Drainage_Radius=tb.Entry(down_frame, width=12)
        ent_Drainage_Radius.grid(row=4, column=1, padx=10, pady=12)
        
        muskat_top=tb.Radiobutton(down_frame, text='Top of the pay zone is perfrorated', bootstyle='danger', variable=muskatvar, value=1, command=lambda: Muskat_top(muskatvar.get()))
        muskat_top.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        muskat_middle=tb.Radiobutton(down_frame, text='Middle of the pay zone is perfrorated', bootstyle='danger', variable=muskatvar, value=2, command=lambda: Muskat_top(muskatvar.get()))
        muskat_middle.grid(row=6, column=0, padx=10, pady=12, sticky='w')
        
        muskat_top_image_label=tb.Label(right_frame, image=muskat_top_image, bootstyle='danger', anchor='e')
        muskat_top_image_label.grid(row=0, column=0, padx=20, pady=(50,25))
        muskat_middle_image_label=tb.Label(right_frame, image=muskat_middle_image, bootstyle='danger', anchor='e')
        muskat_middle_image_label.grid(row=1, column=0, padx=20, pady=(25,100))

        
        
    Papatzacos()
    
    def menu(x):
        for widget in down_frame.winfo_children():
                widget.destroy()
                
        for widget in right_frame.winfo_children():
                widget.destroy()
                
        method_menu.config(text=x)
        if x==partial_menu_items[0]:
            Muskat()
                    
        if x==partial_menu_items[1]:
            Odeh()
                    
        if x==partial_menu_items[2]:
            Papatzacos()
    
    
def non_darcy():

    global ent_oil_fvf,ent_oil_density
    
    ############################# right frame  ###############################

    right_frame=Frame(take_frame)
    right_frame.grid_propagate(0)
    right_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='right')

    ############################# vertical separator ########################

    sep1=tb.Separator(take_frame, bootstyle='danger', orient='vertical')
    sep1.pack(fill='both', pady=50, side='right', expand=False)

    ############################# left frame  #############################

    left_frame=Frame(take_frame)
    left_frame.grid_propagate(0)
    left_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='left')

    ############################# top frame  #############################

    top_frame=Frame(left_frame, height=30)
    top_frame.grid_propagate(0)
    top_frame.pack(ipadx=10, ipady=10, fill='both', side='top')

    ############################# down frame  #############################

    down_frame=Frame(left_frame)
    down_frame.grid_propagate(0)
    down_frame.pack(ipadx=10, ipady=10, fill='both', expand=True, side='bottom')

    ############################# menu button  ############################
    
    def gas_oil():
        global Gas_Oilvar
        if Gas_Oilvar.get()==0:
            for widget in down_frame.winfo_children():
                widget.destroy()
            Non_darcy_cased_gas()
            
        elif Gas_Oilvar.get()==1:
            for widget in down_frame.winfo_children():
                widget.destroy()
            Non_darcy_cased_oil()
    
    if Perforation_Yes_Novar.get()==0:
        Gas_Oil=tb.Checkbutton(top_frame, text="This is an Oil well", bootstyle='danger', variable=Gas_Oilvar, onvalue=1, offvalue=0, command=gas_oil)
        Gas_Oil.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    #############################     Method of Calculation   #################################
    
    def Non_darcy_open():
    
        global ent_pay_zone_thickness, ent_completion_thickness, ent_gas_gravity, ent_permeability, ent_Well_Radius, ent_gas_viscosity, ent_gas_flow_rate
        
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_completion_thickness=tb.Label(down_frame, text='Completion Thickness (ft)= ', bootstyle='danger')
        label_completion_thickness.grid(row=2, column=0, padx=10, pady=12, sticky='w' )
        ent_completion_thickness=tb.Entry(down_frame, width=12)
        ent_completion_thickness.grid(row=2, column=1, padx=10, pady=12)
        
        label_gas_gravity=tb.Label(down_frame, text='Gas Gravity (γg)= ', bootstyle='danger')
        label_gas_gravity.grid(row=3, column=0, padx=10, pady=12, sticky='w' )
        ent_gas_gravity=tb.Entry(down_frame, width=12)
        ent_gas_gravity.grid(row=3, column=1, padx=10, pady=12)
        
        label_permeability=tb.Label(down_frame, text='Permeability (mD)= ', bootstyle='danger', anchor='e')
        label_permeability.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_permeability=tb.Entry(down_frame, width=12)
        ent_permeability.insert(END, DefaultPermeability)
        ent_permeability.grid(row=4, column=1, padx=10, pady=12)
        
        label_Well_Radius=tb.Label(down_frame, text='Well Radius (in.)= ', bootstyle='danger', anchor='e')
        label_Well_Radius.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_Well_Radius=tb.Entry(down_frame, width=12)
        ent_Well_Radius.insert(END, DefaultWellRadius)
        ent_Well_Radius.grid(row=5, column=1, padx=10, pady=12)
        
        label_gas_viscosity=tb.Label(down_frame, text='Viscosity (cp)= ', bootstyle='danger', anchor='e')
        label_gas_viscosity.grid(row=6, column=0, padx=10, pady=12, sticky='w')
        ent_gas_viscosity=tb.Entry(down_frame, width=12)
        ent_gas_viscosity.grid(row=6, column=1, padx=10, pady=12)
        
        label_gas_flow_rate=tb.Label(down_frame, text='Gas Flow Rate (Mscf)= ', bootstyle='danger', anchor='e')
        label_gas_flow_rate.grid(row=7, column=0, padx=10, pady=12, sticky='w')
        ent_gas_flow_rate=tb.Entry(down_frame, width=12)
        ent_gas_flow_rate.grid(row=7, column=1, padx=10, pady=12)
        
    def Non_darcy_cased_gas():
        
        global ent_pay_zone_thickness, ent_completion_thickness, ent_gas_gravity, ent_permeability, ent_perforation_length, ent_gas_viscosity, ent_spf, ent_gas_flow_rate, non_darcy_mesh_size_menu_var
        
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_completion_thickness=tb.Label(down_frame, text='Completion Thickness (ft)= ', bootstyle='danger')
        label_completion_thickness.grid(row=2, column=0, padx=10, pady=12, sticky='w' )
        ent_completion_thickness=tb.Entry(down_frame, width=12)
        ent_completion_thickness.grid(row=2, column=1, padx=10, pady=12)
        
        label_gas_gravity=tb.Label(down_frame, text='Gas Gravity (γg)= ', bootstyle='danger')
        label_gas_gravity.grid(row=3, column=0, padx=10, pady=12, sticky='w' )
        ent_gas_gravity=tb.Entry(down_frame, width=12)
        ent_gas_gravity.grid(row=3, column=1, padx=10, pady=12)
        
        label_permeability=tb.Label(down_frame, text='Permeability (mD)= ', bootstyle='danger', anchor='e')
        label_permeability.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_permeability=tb.Entry(down_frame, width=12)
        ent_permeability.insert(END, DefaultPermeability)
        ent_permeability.grid(row=4, column=1, padx=10, pady=12)
        
        label_perforation_length=tb.Label(down_frame, text='Perforation Length (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_length.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_length=tb.Entry(down_frame, width=12)
        ent_perforation_length.insert(END, DefaultPerforationLength)
        ent_perforation_length.grid(row=5, column=1, padx=10, pady=12)
        
        label_gas_viscosity=tb.Label(down_frame, text='Gas Viscosity (cp)= ', bootstyle='danger', anchor='e')
        label_gas_viscosity.grid(row=6, column=0, padx=10, pady=12, sticky='w')
        ent_gas_viscosity=tb.Entry(down_frame, width=12)
        ent_gas_viscosity.grid(row=6, column=1, padx=10, pady=12)
        
        label_spf=tb.Label(down_frame, text='SPF= ', bootstyle='danger', anchor='e')
        label_spf.grid(row=7, column=0, padx=10, pady=12, sticky='w')
        ent_spf=tb.Entry(down_frame, width=12)
        ent_spf.insert(END, DefaultSpf)
        ent_spf.grid(row=7, column=1, padx=10, pady=12)
        
        label_mesh_size=tb.Label(down_frame, text='Mesh Size= ', bootstyle='danger', anchor='e')
        label_mesh_size.grid(row=8, column=0, padx=10, pady=12, sticky='w')
        mesh_menu=tb.Menubutton(down_frame, bootstyle='danger outlined', width=50, text=DefaultMeshSize)
        mesh_menu.grid(row=8, column=1, padx=10, pady=12)

        method_menu_inside=tb.Menu(mesh_menu)

        for x in gravel_mesh_size_menu_items:
            method_menu_inside.add_radiobutton(label=x, variable=non_darcy_mesh_size_menu_var, command=lambda x=x: mesh(x))
            
        mesh_menu['menu']=method_menu_inside
        
        label_gas_flow_rate=tb.Label(down_frame, text='Gas Flow Rate (Mscf)= ', bootstyle='danger', anchor='e')
        label_gas_flow_rate.grid(row=9, column=0, padx=10, pady=12, sticky='w')
        ent_gas_flow_rate=tb.Entry(down_frame, width=12)
        ent_gas_flow_rate.grid(row=9, column=1, padx=10, pady=12)
        
        def mesh(x):
            mesh_menu.config(text=x)
            gravel_mesh_size_menu_var.set(x)
            
    def Non_darcy_cased_oil():
        
        global ent_pay_zone_thickness, ent_completion_thickness, ent_permeability, ent_perforation_length, ent_oil_viscosity, ent_spf, ent_oil_flow_rate, non_darcy_mesh_size_menu_var, ent_oil_fvf, ent_oil_density
        
        label_pay_zone_thickness=tb.Label(down_frame, text='Pay zone thickness (ft)= ', bootstyle='danger', anchor='e')
        label_pay_zone_thickness.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        ent_pay_zone_thickness=tb.Entry(down_frame, width=12)
        ent_pay_zone_thickness.insert(END, DefaultPayZoneThickness)
        ent_pay_zone_thickness.grid(row=1, column=1, padx=10, pady=12)
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)

        label_completion_thickness=tb.Label(down_frame, text='Completion Thickness (ft)= ', bootstyle='danger')
        label_completion_thickness.grid(row=2, column=0, padx=10, pady=12, sticky='w' )
        ent_completion_thickness=tb.Entry(down_frame, width=12)
        ent_completion_thickness.grid(row=2, column=1, padx=10, pady=12)
        
        label_oil_density=tb.Label(down_frame, text='Oil density (lbm/ft3)= ', bootstyle='danger')
        label_oil_density.grid(row=3, column=0, padx=10, pady=12, sticky='w' )
        ent_oil_density=tb.Entry(down_frame, width=12)
        ent_oil_density.grid(row=3, column=1, padx=10, pady=12)
        
        label_permeability=tb.Label(down_frame, text='Permeability (mD)= ', bootstyle='danger', anchor='e')
        label_permeability.grid(row=4, column=0, padx=10, pady=12, sticky='w')
        ent_permeability=tb.Entry(down_frame, width=12)
        ent_permeability.insert(END, DefaultPermeability)
        ent_permeability.grid(row=4, column=1, padx=10, pady=12)
        
        label_perforation_length=tb.Label(down_frame, text='Perforation Length (in.)= ', bootstyle='danger', anchor='e')
        label_perforation_length.grid(row=5, column=0, padx=10, pady=12, sticky='w')
        ent_perforation_length=tb.Entry(down_frame, width=12)
        ent_perforation_length.insert(END, DefaultPerforationLength)
        ent_perforation_length.grid(row=5, column=1, padx=10, pady=12)
        
        label_oil_viscosity=tb.Label(down_frame, text='Oil Viscosity (cp)= ', bootstyle='danger', anchor='e')
        label_oil_viscosity.grid(row=6, column=0, padx=10, pady=12, sticky='w')
        ent_oil_viscosity=tb.Entry(down_frame, width=12)
        ent_oil_viscosity.grid(row=6, column=1, padx=10, pady=12)
        
        label_spf=tb.Label(down_frame, text='SPF= ', bootstyle='danger', anchor='e')
        label_spf.grid(row=7, column=0, padx=10, pady=12, sticky='w')
        ent_spf=tb.Entry(down_frame, width=12)
        ent_spf.insert(END, DefaultSpf)
        ent_spf.grid(row=7, column=1, padx=10, pady=12)
        
        label_mesh_size=tb.Label(down_frame, text='Mesh Size= ', bootstyle='danger', anchor='e')
        label_mesh_size.grid(row=8, column=0, padx=10, pady=12, sticky='w')
        mesh_menu=tb.Menubutton(down_frame, bootstyle='danger outlined', width=50, text=DefaultMeshSize)
        mesh_menu.grid(row=8, column=1, padx=10, pady=12)

        method_menu_inside=tb.Menu(mesh_menu)

        for x in gravel_mesh_size_menu_items:
            method_menu_inside.add_radiobutton(label=x, variable=non_darcy_mesh_size_menu_var, command=lambda x=x: mesh(x))
            
        mesh_menu['menu']=method_menu_inside
        
        label_oil_flow_rate=tb.Label(down_frame, text='Gas Flow Rate (Mscf)= ', bootstyle='danger', anchor='e')
        label_oil_flow_rate.grid(row=9, column=0, padx=10, pady=12, sticky='w')
        ent_oil_flow_rate=tb.Entry(down_frame, width=12)
        ent_oil_flow_rate.grid(row=9, column=1, padx=10, pady=12)
        
        label_oil_fvf=tb.Label(down_frame, text='Oil FVF (BBL/STB)= ', bootstyle='danger', anchor='e')
        label_oil_fvf.grid(row=10, column=0, padx=10, pady=12, sticky='w')
        ent_oil_fvf=tb.Entry(down_frame, width=12)
        ent_oil_fvf.grid(row=10, column=1, padx=10, pady=12)
        
        def mesh(x):
            mesh_menu.config(text=x)
            gravel_mesh_size_menu_var.set(x)
    
        
    if Perforation_Yes_Novar.get()==1:
        Non_darcy_open()
        
    elif Gravel_Yes_Novar.get()==0:
        if Gas_Oilvar.get()==0:
            for widget in down_frame.winfo_children():
                widget.destroy()
            Non_darcy_cased_gas()
            
        elif Gas_Oilvar.get()==1:
            for widget in down_frame.winfo_children():
                widget.destroy()
            Non_darcy_cased_oil()
        
    else:
        label_no_nondarcy=tb.Label(down_frame, text='There is no Non-Darcy effect for this well', bootstyle='danger', anchor='e')
        label_no_nondarcy.grid(row=1, column=0, padx=10, pady=12, sticky='w')
        down_frame.grid_rowconfigure(1, weight=0)
        down_frame.grid_columnconfigure(1, weight=6)
        Gas_Oil.grid_forget()
        


                
            
def Reset(event=None):

    global Perforation_Yes_Novar, Gravel_Yes_Novar, Slanted_Yes_Novar, Partial_Yes_Novar, Non_darcy_Yes_Novar, Gas_Oilvar
    global DefaultAnisotropy, DefaultPayZoneThickness, DefaultWellRadius, DefaultPerforationLength, DefaultSpf, DefaultPerforationTunnelRadius
    global DefaultPhasingAng, DefaultPermeability, DefaultMeshSize, DefaultPhasingAng
    
    Perforation_Yes_Novar.set(0)
    Gravel_Yes_Novar.set(0)
    Slanted_Yes_Novar.set(0)
    Partial_Yes_Novar.set(0)
    Non_darcy_Yes_Novar.set(0)
    Gas_Oilvar.set(0)

    ## default values

    DefaultPayZoneThickness=''
    DefaultWellRadius=''
    DefaultAnisotropy=''
    DefaultPerforationLength=''
    DefaultSpf=''
    DefaultPerforationTunnelRadius=''
    DefaultPhasingAng='Select an Angle'
    DefaultPermeability=''
    DefaultMeshSize='Select a size'
    
    perforation_skin_value = 0
    slanted_skin_value = 0
    gravel_skin_value = 0
    non_darcy_skin_value = 0
    partial_skin_value = 0
    

def nothing(event=None):
    pass


def result():
    global count, perforation_skin_value, slanted_skin_value, gravel_skin_value, non_darcy_skin_value, partial_skin_value, label5, label6, resbutton
    
    label5.grid_forget()
    label5=tb.Label(result_frame, text='Total skin : ', font=('Helvetica', 16,'bold'), bootstyle='danger')
    label5.grid(row=0, column=0, padx=10)
    result_frame.columnconfigure(1, minsize=860)
    
    label6.destroy()
    label6=tb.Label(result_frame, text=str(float("%0.4f" % (perforation_skin_value+slanted_skin_value+gravel_skin_value+non_darcy_skin_value+partial_skin_value))), font=('Helvetica', 16, 'bold'), bootstyle='light')
    label6.grid(row=0, column=1, padx=10)
    result_frame.grid_columnconfigure(1, weight=5)
    
    resbutton=tb.Button(cal_frame, text='Reset', bootstyle='danger', width=10, command=Reset)
    resbutton.grid(row=0, column=0, sticky='w', padx=20, pady=5)
    
    uni_label = tb.Label(take_frame, image=uni_image)
    uni_label.pack(padx=30, pady=30)
    
    uni_name=Label(take_frame, text='AmirKabir University of Technology \n(Tehran PolyTechnic)', font=('Helvetica', 16,'bold'), fg='white')
    uni_name.pack(pady=10, padx=10)
    
    total_frame = Frame(take_frame, height=300, width=720)
    total_frame.grid_propagate(0)
    total_frame.pack(padx=10)
    
    total_label1=tb.Label(total_frame, text='Total skin = Perforation Skin + Gravel Skin + \n\t     Slanted-Well Skin + Non-Darcy Skin + \n\t     Partial-Penetration Skin', font=('Helvetica', 16), bootstyle='danger')
    total_label1.grid(row=0, column=0, padx=10, pady=(100,10))
    
    total_label2=tb.Label(total_frame, text='= {Perforation} + {Gravel} + {Slanted} + {Non_Darcy} + {Partial}'.format(Perforation=perforation_skin_value, Gravel=gravel_skin_value, Slanted=slanted_skin_value, Non_Darcy=non_darcy_skin_value, Partial=partial_skin_value), font=('Helvetica', 16,'bold'), bootstyle='light')
    total_label2.grid(row=1, column=0, padx=0, pady=40)


def next(event=None):
    global count, label6
    
    for widget in take_frame.winfo_children():
        widget.destroy()
    
    label6.grid_forget()
    app.bind('<Left>', back)
    
    backbutton.configure(state='active')
    
    if count==Skin(2).all_skins.index('gravel')-1:
        frame1.config(text='Gravel Pack Skin')
        Yes_No.config(text='We have not set gravel pack', variable=Gravel_Yes_Novar)
        gravel()
        
    if count==Skin(2).all_skins.index('slanted well')-1:
        frame1.config(text='Slanted Well Skin')
        Yes_No.config(text='The well is horizontal', variable=Slanted_Yes_Novar)
        slanted_well()
        
    if count==Skin(2).all_skins.index('partial')-1:
        frame1.config(text='Partial Penetration Skin')
        Yes_No.config(text='The well is fully penetrated', variable=Partial_Yes_Novar)
        partial()
        
        
    if count==Skin(2).all_skins.index('non Darcy')-1:
        frame1.config(text='Non-Darcy Skin')
        Yes_No.config(text='There is NO Non-Darcy effect', variable=Non_darcy_Yes_Novar)
        non_darcy()
        
    if count==Skin(2).all_skins.index('result')-1:
        frame1.config(text='Result & output')
        Yes_No.grid_forget()
        result()
        
        
    if count > len(circle)-3:
        Nextbutton.configure(state='disabled')
    
    count += 1
    
    for i in circle:
        j=i
        if i==count:
            j=Label(circle_frame, image=solid_circle, highlightbackground='#adacb1')
            j.grid(row=0, column=i)
        else:
            j=Label(circle_frame, image=empty_circle, highlightbackground='#adacb1')
            j.grid(row=0, column=i)
            
    
    
    if count<=4:
        app.bind('<Right>', next)
    else:
        app.bind('<Right>', nothing)
    

def back(event=None):

    global count, label5, label6, resbutton
    
    for widget in take_frame.winfo_children():
        widget.destroy()
        
    label6.grid_forget()
    if count==Skin(2).all_skins.index('result'):
        resbutton.destroy()
    app.bind('<Right>', next)
    
    Nextbutton.configure(state='active')
    if count ==Skin(2).all_skins.index('perforation')+1:
        backbutton.configure(state='disabled')
        frame1.config(text='Perforation Skin')
        Yes_No.config(text="The well is NOT perforated ! It's openhole", variable=Perforation_Yes_Novar)
        perforation()
        
    if count==Skin(2).all_skins.index('perforation')+2:
        frame1.config(text='Gravel Pack Skin')
        Yes_No.config(text='We have not set gravel pack', variable=Gravel_Yes_Novar)
        gravel()
        
    if count==Skin(2).all_skins.index('slanted well')+1:
        frame1.config(text='Slanted Well Skin')
        Yes_No.config(text='The well is horizontal', variable=Slanted_Yes_Novar)
        slanted_well()
        
    if count==Skin(2).all_skins.index('partial')+1:
        frame1.config(text='Partial Penetration Skin')
        Yes_No.config(text='The well is fully penetrated', variable=Partial_Yes_Novar)
        partial()
        

    if count==Skin(2).all_skins.index('non Darcy')+1:
        frame1.config(text='Non-Darcy Skin')
        Yes_No.config(text='There is NO Non-Darcy effect', variable=Non_darcy_Yes_Novar)
        non_darcy()
    
    if count==Skin(2).all_skins.index('non Darcy')+1:
        # frame1.config(text='Non-Darcy Skin')
        # Yes_No.config(text='There is NO Non-Darcy effect', variable=Non_darcy_Yes_Novar)
        # non_darcy()
        label5.config(text='Relavant Skin')
        Yes_No.grid(row=0, column=0, sticky='w', padx=20, pady=5)
        
    
    if count>=2:
        app.bind('<Left>', back)
    else:
        app.bind('<Left>', nothing)
    
    count -= 1
    
    
    for i in circle:
        j=i
        if i==count:
            j=Label(circle_frame, image=solid_circle, highlightbackground='#adacb1')
            j.grid(row=0, column=i)
        else:
            j=Label(circle_frame, image=empty_circle, highlightbackground='#adacb1')
            j.grid(row=0, column=i)
    
    
def calculate(event=None):
    global label6, PayZoneThickness, DefaultPayZoneThickness, DefaultWellRadius, DefaultAnisotropy, DefaultPerforationLength, DefaultSpf, DefaultPerforationTunnelRadius, DefaultPhasingAng, DefaultPermeability, DefaultMeshSize
    global perforation_skin_value, slanted_skin_value, gravel_skin_value, non_darcy_skin_value, partial_skin_value, ent_oil_fvf, ent_Well_Radius
    
    if count ==Skin(2).all_skins.index('perforation'):
        a = Skin(ent_Well_Radius.get())
        perforation_skin_value=0
        try:
            if Perforation_Yes_Novar.get()==0:
                perforation_skin_value = a.perforation(ent_perforation_length.get(), phasing_menu_var.get(), ent_spf.get(), ent_Damage_zone_radius.get(), ent_crushed_zone_radius.get(), ent_perforation_tunnel_radius.get(), ent_Anisotropy.get(), ent_damage_ratio.get(), ent_crushed_ratio.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())
                DefaultPerforationLength=str(ent_perforation_length.get())
                DefaultSpf=str(ent_spf.get())
                DefaultPerforationTunnelRadius=str(ent_perforation_tunnel_radius.get())
                DefaultPhasingAng=str(phasing_menu_var.get())
            elif Perforation_Yes_Novar.get()==1:
                perforation_skin_value=0
        except:
            perforation_skin_value='Not Defined Angel'
            
        label6.grid_forget()
        label6=tb.Label(result_frame, text=str(float("%0.4f" % (perforation_skin_value))), font=('Helvetica', 12, 'bold'), bootstyle='light')
        label6.grid(row=0, column=1, padx=10, pady=10)
        
    if count ==Skin(2).all_skins.index('perforation')+1:
        gravel_skin_value=0
        if Gravel_Yes_Novar.get()==0:
            if gravel_menu_var.get()=='Golan and Whitson (1991)':
                a = Skin(2)
                gravel_skin_value = a.golan(ent_perforation_length.get(), ent_permeability.get(), ent_pay_zone_thickness.get(), ent_spf.get(), gravel_mesh_size_menu_var.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultPerforationLength=str(ent_perforation_length.get())
                DefaultSpf=str(ent_spf.get())
                DefaultPermeability=str(ent_permeability.get())
                DefaultMeshSize=str(gravel_mesh_size_menu_var.get())
            elif gravel_menu_var.get()=='Furui (2004)':
                a = Skin(ent_Well_Radius.get())
                gravel_skin_value=a.furui(ent_perforation_length.get(), ent_perforation_tunnel_radius.get(), ent_casing_thickness.get(), ent_spf.get(), phasing_menu_var.get(), ent_permeability.get(), ent_Well_Radius.get(), gravel_mesh_size_menu_var.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPerforationLength=str(ent_perforation_length.get())
                DefaultSpf=str(ent_spf.get())
                DefaultPerforationTunnelRadius=str(ent_perforation_tunnel_radius.get())
                DefaultPhasingAng=str(phasing_menu_var.get())
                DefaultPermeability=str(ent_permeability.get())
                DefaultMeshSize=str(gravel_mesh_size_menu_var.get())
            else:
                a = Skin(ent_Well_Radius.get())
                gravel_skin_value=a.furui(ent_perforation_length.get(), ent_perforation_tunnel_radius.get(), ent_casing_thickness.get(), ent_spf.get(), phasing_menu_var.get(), ent_permeability.get(), ent_Well_Radius.get(), gravel_mesh_size_menu_var.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPerforationLength=str(ent_perforation_length.get())
                DefaultSpf=str(ent_spf.get())
                DefaultPerforationTunnelRadius=str(ent_perforation_tunnel_radius.get())
                DefaultPhasingAng=str(phasing_menu_var.get())
                DefaultPermeability=str(ent_permeability.get())
                DefaultMeshSize=str(gravel_mesh_size_menu_var.get())

        elif Gravel_Yes_Novar.get()==1:
            gravel_skin_value=0
           
        label6.grid_forget()
        label6=tb.Label(result_frame, text=str(float("%0.4f" % (gravel_skin_value))), font=('Helvetica', 12, 'bold'), bootstyle='light')
        label6.grid(row=0, column=1, padx=10, pady=10)
    
    if count ==Skin(2).all_skins.index('perforation')+2:
        a = Skin(ent_Well_Radius.get())
        slanted_skin_value=0
        if Slanted_Yes_Novar.get()==0:
            if slanted_menu_var.get()=='Cinco et al. (1975)':
                slanted_skin_value = a.cinco(ent_pay_zone_thickness.get(), ent_Well_Radius.get(), ent_Anisotropy.get(), ent_deviation_angel.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())

            elif slanted_menu_var.get()=='Besson (1990)':
                slanted_skin_value = a.besson(ent_pay_zone_thickness.get(), ent_Well_Radius.get(), ent_Anisotropy.get(), ent_deviation_angel.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())
            
            else:
                slanted_skin_value = a.besson(ent_pay_zone_thickness.get(), ent_Well_Radius.get(), ent_Anisotropy.get(), ent_deviation_angel.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())
        elif Slanted_Yes_Novar.get()==1:
            slanted_skin_value=0
        
        label6.grid_forget()
        label6=tb.Label(result_frame, text=str(float("%0.4f" % (slanted_skin_value))), font=('Helvetica', 12, 'bold'), bootstyle='light')
        label6.grid(row=0, column=1, padx=10, pady=10)
    
    if count ==Skin(2).all_skins.index('perforation')+3:
        a = Skin(ent_Well_Radius.get())
        partial_skin_value=0
        if Partial_Yes_Novar.get()==0:
            if partial_menu_var.get()=='Muskat (1946)':
                if muskatvar.get()==1:
                    partial_skin_value = a.muskat_top(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_Well_Radius.get(), ent_Drainage_Radius.get())
                elif muskatvar.get()==2:
                    partial_skin_value = a.muskat_middle(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_Well_Radius.get(), ent_Drainage_Radius.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())

                
            elif partial_menu_var.get()=='Odeh (1980)':
                partial_skin_value = a.odeh(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_Well_Radius.get(), ent_Anisotropy.get(), ent_completion_position.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())

            elif partial_menu_var.get()=='Papatzacos (1987)':
                partial_skin_value = a.papatzacos(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_Well_Radius.get(), ent_Anisotropy.get(), ent_completion_position.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())
                
            else:
                partial_skin_value = a.papatzacos(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_Well_Radius.get(), ent_Anisotropy.get(), ent_completion_position.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultAnisotropy=str(ent_Anisotropy.get())
                
        elif Partial_Yes_Novar.get()==1:
            partial_skin_value=0
            
        label6.grid_forget()
        label6=tb.Label(result_frame, text=str(float("%0.4f" % (partial_skin_value))), font=('Helvetica', 12, 'bold'), bootstyle='light')
        label6.grid(row=0, column=1, padx=10, pady=10)
    
    if count ==Skin(2).all_skins.index('perforation')+4:       
        non_darcy_skin_value=0
        if Non_darcy_Yes_Novar.get()==0:
            if Perforation_Yes_Novar.get()==1:
                a = Skin(ent_Well_Radius.get())
                non_darcy_skin_value = a.non_darcy_open(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_gas_gravity.get(), ent_permeability.get(), ent_Well_Radius.get(), ent_gas_viscosity.get(), ent_gas_flow_rate.get())
                DefaultWellRadius=str(ent_Well_Radius.get())
                DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                DefaultPermeability=str(ent_permeability.get())
                DefaultMeshSize=str(gravel_mesh_size_menu_var.get())
                
            elif Perforation_Yes_Novar.get()==0:
                a = Skin(2)
                if Gas_Oilvar.get()==0:
                    non_darcy_skin_value = a.non_darcy_gas_cased(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_gas_gravity.get(), ent_permeability.get(), ent_perforation_length.get(), ent_gas_viscosity.get(), ent_spf.get(), non_darcy_mesh_size_menu_var.get(), ent_gas_flow_rate.get())
                    DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                    DefaultPermeability=str(ent_permeability.get())
                    DefaultMeshSize=str(gravel_mesh_size_menu_var.get())
                    
                if Gas_Oilvar.get()==1:
                    non_darcy_skin_value = a.non_darcy_oil_cased(ent_pay_zone_thickness.get(), ent_completion_thickness.get(), ent_oil_fvf.get(), ent_oil_density.get(), ent_permeability.get(), ent_perforation_length.get(), ent_oil_viscosity.get(), ent_spf.get(), non_darcy_mesh_size_menu_var.get(), ent_oil_flow_rate.get())
                    DefaultPayZoneThickness=str(ent_pay_zone_thickness.get())
                    DefaultPermeability=str(ent_permeability.get())
                    DefaultMeshSize=str(gravel_mesh_size_menu_var.get())
 
        elif Non_darcy_Yes_Novar.get()==1:
            non_darcy_skin_value=0
            
        label6.grid_forget()
        label6=tb.Label(result_frame, text=str(float("%0.4f" % (non_darcy_skin_value))), font=('Helvetica', 12, 'bold'), bootstyle='light')
        label6.grid(row=0, column=1, padx=10, pady=10)
  

def play(event=None):
    global play_pause_var
    
    if play_pause_var.get()==1:
        pygame.mixer.music.pause()
        play_pause_var.set(0)
    elif play_pause_var.get()==0:
        pygame.mixer.music.play(loops=1)
        play_pause_var.set(1)
    
    
    


#objects

pygame.mixer.init()
pygame.mixer.music.load(resource_path('music.mp3'))
pygame.mixer.music.play(loops=1)

frame1=LabelFrame(app, text='Perforation Skin', width=720, height=970)
frame1.pack_propagate(0)
frame1.place(x=15, y=15)

frame2=Frame(frame1, height=750, width=720)
frame2.pack(padx=5, pady=10)
frame2.pack_propagate(0)

############################### Play ######################################

play_button = tb.Button(frame1, image=play_image, bootstyle='darkly', command=play)
play_button.place(x=645, y=0)

############################### Take Frame  ###############################

take_frame=Frame(frame2, height=700, width=720)
take_frame.pack(ipadx=5, ipady=5, fill='both', expand=True)

##########################################################################
##########################################################################


perforation()


############################### Cal Frame  ###############################

cal_frame=Frame(frame2, height=50, width=720)
cal_frame.grid_propagate(0)
cal_frame.pack(ipadx=5, ipady=5)
cal_frame.grid_columnconfigure(0, weight=1)
calbutton=tb.Button(cal_frame, text='Calculate', bootstyle='danger', width=10, command=calculate)
calbutton.grid(row=0, column=1, sticky='e', padx=20, pady=5)

Yes_No=tb.Checkbutton(cal_frame, text="The well is NOT perforated ! It's openhole", bootstyle='danger', variable=Perforation_Yes_Novar, onvalue=1, offvalue=0)
Yes_No.grid(row=0, column=0, sticky='w', padx=20, pady=5)
############################### separator  ###############################

sep2=tb.Separator(frame1, bootstyle='danger', orient='horizontal')
sep2.pack(fill='x', padx=50)

############################### result frame  ############################

frame3=Frame(frame1, height=200, width=720)
frame3.grid_propagate(0)
frame3.pack(pady=10)

result_frame=Frame(frame3, height=110, width=720)
result_frame.grid_propagate(0)
result_frame.pack()

label5=tb.Label(result_frame, text='Relevant skin : ', font=('Helvetica', 16,'bold'), bootstyle='danger')
label5.grid(row=0, column=0, padx=10)
result_frame.columnconfigure(1, minsize=810)

label6=tb.Label(result_frame, text='', width=10, font=('Helvetica', 16,'bold'), bootstyle='light')
label6.grid(row=0, column=1, padx=10, sticky='e')
result_frame.grid_columnconfigure(1, weight=6)


############################### bottom Frame  ###############################

buttom_frame=Frame(frame3, height=50, width=720)
buttom_frame.grid_propagate(0)
buttom_frame.pack()
buttom_frame.grid_columnconfigure(0, weight=1)
buttom_frame.grid_columnconfigure(1, weight=1)
buttom_frame.grid_columnconfigure(2, weight=1)

backbutton=tb.Button(buttom_frame, text='Back', bootstyle='warning-outlined', state='disable', width=10, command=back)
backbutton.grid(row=0, column=0, sticky='w', padx=20)

Nextbutton=tb.Button(buttom_frame, text='Next', bootstyle='warning-outlined', width=10, command=next)
Nextbutton.grid(row=0, column=2, sticky='e', padx=20)

right = tb.Label(buttom_frame, text='® All right reserved by H u s s e i n  M o h a m m a d i  R o o z b a h a n i', bootstyle='light', font=('Helvetica', 5))
right.grid(row=1, column=0, columnspan=3)

############################### circle Frame  ###############################

circle_frame=Frame(buttom_frame, height=50)
circle_frame.grid(row=0, column=1)



for i in circle:
    j=i
    if i==count:
        j=Label(circle_frame, image=solid_circle, highlightbackground='#adacb1')
        j.grid(row=0, column=i)
    else:
        j=Label(circle_frame, image=empty_circle, highlightbackground='#adacb1')
        j.grid(row=0, column=i)


### Binding


app.bind("<Right>", next)
app.bind("<Left>", back)
app.bind("<Return>", calculate)
app.bind("<space>", play)
app.bind("<Escape>", Reset)


if screen != (1920, 1080):
    app.geometry('750x900+200+0')
    for widget in take_frame.winfo_children():
        widget.destroy()
    warning_label=tb.Label(take_frame, text='Note that this app Only works on screen size of 1920 * 1080', font=('Helvetica', 16), bootstyle='danger')
    warning_label.pack(padx=10, pady=(100,10))

app.mainloop()