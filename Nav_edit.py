#Nav_edit.py
import tkinter as tk
import tkinter.filedialog as tkf
import linecache
import math

def test_float(content):
    try:
        float(content)
        return True
    except ValueError:
        return False
    
def test_int(content):
    try:
        int(content)
        return True
    except ValueError:
        return False

class Nav_edit:
    def __init__(self, root=tk.Tk()):
        self.__file_item_yield = ""
        self.__main_win = root       #build window
        test_float_TMD = self.__main_win.register(test_float)   #register function test_digit
        test_int_TMD = self.__main_win.register(test_int)   #register function test_int
        
        self.__main_win.title("Nav_edit")
        
        self.__frame_main = tk.Frame(self.__main_win)   # build frame
        self.__frame_main.grid(row=0)

        tk.Button(self.__frame_main, text="input_file", command=self._open_file_dialg).grid(row=0, column=0)  #build button open file
        tk.Button(self.__frame_main, text="output_file", command=self._save_file_dialg).grid(row=1, column=0)  #build button save file

        self.__button_open_file = tk.StringVar()
        self.__label_open_file = tk.Label(self.__frame_main, textvariable=self.__button_open_file)  #build label open file
        self.__label_open_file.grid(row=0, column=1, columnspan=3)

        self.__button_save_file = tk.StringVar()
        self.__label_save_file = tk.Label(self.__frame_main, textvariable=self.__button_save_file)  #build label save file
        self.__label_save_file.grid(row=1, column=1, columnspan=3)

        tk.Label(self.__frame_main, text="start_num").grid(row=2, column=0)   # build label start_num
        tk.Label(self.__frame_main, text="end_num").grid(row=3, column=0)   # build label end_num

        self.__entry_start_num_str = tk.StringVar()
        self.__entry_start_num = tk.Entry(self.__frame_main, width=10, textvariable=self.__entry_start_num_str, validate="focusout", validatecommand=(test_int_TMD, '%P'), invalidcommand=self._entry_invalid_start_num)             # build entry X_adj
        self.__entry_start_num.grid(row=2, column=1, padx=5, pady=5)
        self.__entry_start_num.insert(0,"1")

        self.__entry_end_num_str = tk.StringVar()
        self.__entry_end_num = tk.Entry(self.__frame_main, width=10, textvariable=self.__entry_end_num_str, validate="focusout", validatecommand=(test_int_TMD, '%P'), invalidcommand=self._entry_invalid_end_num)             # build entry Y_adj
        self.__entry_end_num.grid(row=3, column=1, padx=5, pady=5)
        self.__entry_end_num.insert(0,"5000")
        
        tk.Label(self.__frame_main, text="X_adj (um)").grid(row=2, column=2)   # build label X_adj
        tk.Label(self.__frame_main, text="Y_adj (um)").grid(row=3, column=2)   # build label Y_adj
        tk.Label(self.__frame_main, text="Z_adj (um)").grid(row=4, column=2)   # build label Z_adj

        self.__entry_X_adj_str = tk.StringVar()
        self.__entry_X_adj = tk.Entry(self.__frame_main, width=10,textvariable=self.__entry_X_adj_str, validate="focusout", validatecommand=(test_float_TMD, '%P'), invalidcommand=self._entry_invalid_X)             # build entry X_adj
        self.__entry_X_adj.grid(row=2, column=3, padx=5, pady=5)
        self.__entry_X_adj.insert(0,"0")

        self.__entry_Y_adj_str = tk.StringVar()
        self.__entry_Y_adj = tk.Entry(self.__frame_main, width=10, textvariable=self.__entry_Y_adj_str, validate="focusout", validatecommand=(test_float_TMD, '%P'), invalidcommand=self._entry_invalid_Y)             # build entry Y_adj
        self.__entry_Y_adj.grid(row=3, column=3, padx=5, pady=5)
        self.__entry_Y_adj.insert(0,"0")
        
        self.__entry_Z_adj_str = tk.StringVar()
        self.__entry_Z_adj = tk.Entry(self.__frame_main, width=10, textvariable=self.__entry_Z_adj_str, validate="focusout", validatecommand=(test_float_TMD, '%P'), invalidcommand=self._entry_invalid_Z)             # build entry Y_adj
        self.__entry_Z_adj.grid(row=4, column=3, padx=5, pady=5)
        self.__entry_Z_adj.insert(0,"0")
        
        tk.Label(self.__frame_main, text="focus_start").grid(row=2, column=4)   # build label focus_start
        tk.Label(self.__frame_main, text="focus_end").grid(row=3, column=4)   # build label focus_end

        self.__entry_focus_start_str = tk.StringVar()
        self.__entry_focus_start = tk.Entry(self.__frame_main, width=10,textvariable=self.__entry_focus_start_str, validate="focusout", validatecommand=(test_int_TMD, '%P'), invalidcommand=self._entry_invalid_focus_start)             # build entry focus_start
        self.__entry_focus_start.grid(row=2, column=5, padx=5, pady=5)
        self.__entry_focus_start.insert(0,"0")

        self.__entry_focus_end_str = tk.StringVar()
        self.__entry_focus_end = tk.Entry(self.__frame_main, width=10, textvariable=self.__entry_focus_end_str, validate="focusout", validatecommand=(test_int_TMD, '%P'), invalidcommand=self._entry_invalid_focus_end)             # build entry focus_end
        self.__entry_focus_end.grid(row=3, column=5, padx=5, pady=5)
        self.__entry_focus_end.insert(0,"0")

        self.__OptionM_grpNum_str = tk.StringVar()
        self.__OptionM_grpNum_str.set("0")
        self.__OptionM_grpNum = tk.OptionMenu(self.__frame_main, self.__OptionM_grpNum_str, "0", "5", "10", "15", "20", "25", "30")
        self.__OptionM_grpNum.grid(row=5, column=0)

        tk.Label(self.__frame_main, text="groups").grid(row=5, column=1)   # build label groups

        self.__OptionM_markA_str = tk.StringVar()
        self.__OptionM_markA_str.set("All acquire")
        self.__OptionM_markA = tk.OptionMenu(self.__frame_main, self.__OptionM_markA_str, "All acquire", "acquire focus", "not acquire")   # build optionmenu markA
        self.__OptionM_markA.grid(row=5, column=2)
        
        self.__button_run = tk.Button(self.__frame_main, text="edit Nav file", fg="blue", width=10, command=self._edit)    # build button edit Nav file
        self.__button_run.grid(row=5, column=3)
        
        self.__button_map = tk.Button(self.__frame_main, text="edit map file", fg="blue", width=10, command=self._edit_map)    # build button edit map file
        self.__button_map.grid(row=5, column=5)

        self.__button_next_set = tk.Button(self.__frame_main, text="edit next set", fg="blue", width=10, command=self._edit_next_set)    # build button edit next set
        self.__button_next_set.grid(row=6, column=0, columnspan=2)

        self.__OptionM_markB_str = tk.StringVar()
        self.__OptionM_markB_str.set("manual_pick")
        self.__OptionM_markB = tk.OptionMenu(self.__frame_main, self.__OptionM_markB_str, "manual_pick", "auto_pick")   # build optionmenu markB
        self.__OptionM_markB.grid(row=6, column=2)        

    def _edit(self):
        if self.__button_open_file.get() == self.__button_save_file.get():
            print("input file name = output file name")
            return
        elif self.__button_save_file.get() == "":
            print("Please name the output flile.")
            return
        elif self.__button_open_file.get() == "":
            print("Please give the input flile.")
            return
        elif int(self.__entry_start_num_str.get()) > int(self.__entry_end_num_str.get()):
            print("start_num > end_num!")
            return
        elif int(self.__entry_start_num_str.get()) == 0:
            print("start_num = 0")
            return
        elif int(self.__entry_end_num_str.get()) == 0:
            print("end_num = 0")
            return

        print("input parameters:")
        print("input file:", self.__open_filename)
        print("output file:", self.__save_filename)
        print("from", self.__entry_start_num_str.get(), "to", self.__entry_end_num_str.get())
        print("X_adj =", self.__entry_X_adj_str.get(), ", Y_adj =", self.__entry_Y_adj_str.get(), ", Z_adj =", self.__entry_Z_adj_str.get())
        print(self.__OptionM_markA_str.get(), ", groups", self.__OptionM_grpNum_str.get())
        print(self.__OptionM_markB_str.get(), " mode")
        print("start")

        self._file_edit()
        print("done")
        
    def _edit_next_set(self):

        if self.__file_item_yield != "":
            if self.__button_open_file.get()==self.__button_save_file.get():
                print("input file name = output file name")
            elif self.__button_open_file.get()!= self.__button_save_file.get() != "":
                self.__file_item_yield_a=self.__file_item_yield.split(sep=" = ")       #according yield edit start_num
                self.__file_item_yield_b=self.__file_item_yield_a[1].split(sep="]\n")
                self.__entry_start_num.delete(0, tk.END)
                self.__entry_start_num.insert(0,self.__file_item_yield_b[0])
                self.__file_item_yield = ""
                    
                print("input parameters:")
                print("input file:", self.__open_filename)
                print("output file:", self.__save_filename)
                print("from", self.__entry_start_num_str.get(), "to", self.__entry_end_num_str.get())
                print("X_adj =", self.__entry_X_adj_str.get(), ", Y_adj =", self.__entry_Y_adj_str.get(), ", Z_adj =", self.__entry_Z_adj_str.get())
                print(self.__OptionM_markA_str.get(), ", groups", self.__OptionM_grpNum_str.get())
                print(self.__OptionM_markB_str.get(), " mode")
                print("start")
 
                self._file_edit()
                print("done")
            else:
                print("file name error.")
        else:
            print("no previous set!")

    def _file_edit(self):
        self.__button_next_set.config(state="disabled", fg="gray")
        self.__button_run.config(state="disabled", fg="gray")
        self.__button_map.config(state="disabled", fg="gray")
        with open(self.__button_save_file.get(), mode="w") as self.__save_file:
            self.__save_file.writelines("AdocVersion = 2.00\n\n")
        self.__file_item_grpID_old = "0"
        self.__file_item_grpID_new = "0"
        self.__file_item_grp_num = 0
        self.__entry_num = list()
        if self.__OptionM_markB_str.get() == "manual_pick":
            for self.__entry_num_index in range(int(self.__entry_start_num_str.get()), int(self.__entry_end_num_str.get())+1):
                self.__entry_num.append("[Item = " + str(self.__entry_num_index) + "]\n")
        elif self.__OptionM_markB_str.get() == "auto_pick":
            for self.__entry_num_index in range(int(self.__entry_start_num_str.get()), int(self.__entry_end_num_str.get())+1):
                for self.__item_add_num in range(1, 50):
                    self.__entry_num.append("[Item = " + str(self.__entry_num_index) + "-" + str(self.__item_add_num) + "]\n")
        with open(self.__button_open_file.get(), mode="r") as self.__open_file:
            for self.__each_line in self.__open_file:
                if self.__each_line in self.__entry_num:
                    self.__file_item = list()
                    self.__file_item.append(self.__each_line) #put target in list 
                    for self.__file_item_index in range(20):
                        self.__file_item_a = self.__open_file.readline()
                        if " = " in self.__file_item_a:
                            self.__file_item_b = self.__file_item_a.split(sep=" = ")
                            if self.__file_item_b[0] == "StageXYZ":                   #edit StageXYZ, make StageXYZ = (X + X_adj), (Y + Y_adj), Z\n
                                self.__file_item_c = self.__file_item_b[1].split(sep=" ")
                                self.__file_item_c[0] = str("%.3f" % (float(self.__file_item_c[0]) + float(self.__entry_X_adj_str.get())))
                                self.__file_item_c[1] = str("%.3f" % (float(self.__file_item_c[1]) + float(self.__entry_Y_adj_str.get())))
                                self.__file_item_z = self.__file_item_c[2].split(sep="\n")
                                self.__file_item_z[0] = str("%.3f" % (float(self.__file_item_z[0]) + float(self.__entry_Z_adj_str.get())))
                                self.__file_item_a = "StageXYZ = " + self.__file_item_c[0] + " " + self.__file_item_c[1] + " " + self.__file_item_z[0] + "\n"
                            elif self.__file_item_b[0] == "Type":
                                self.__file_item_t = self.__file_item_b[1].split(sep="\n")
                                if int(self.__file_item_t[0]) != 0:
                                    self.__file_item_del = True
                                else:
                                    self.__file_item_del = False
                            elif self.__file_item_b[0] == "Note":
                                self.__file_item_a = ""
                            elif self.__file_item_b[0] == "GroupID":
                                self.__file_item_d = self.__file_item_b[1].split(sep="\n")
                                self.__file_item_grpID_new = self.__file_item_d[0]
                                if self.__file_item_grpID_new != self.__file_item_grpID_old:
                                    self.__file_item_grp_start = True
                                    self.__file_item_grpID_old = self.__file_item_grpID_new
                                    self.__file_item_grp_num += 1
                                else:
                                    self.__file_item_grp_start = False
                                   # print(self.__file_item_grp_start)
                            elif self.__file_item_b[0] == "Acquire":
                                self.__file_item_a = ""
                            elif self.__file_item_b[0] == "PtsX":
                                self.__file_item_a = "PtsX = " + self.__file_item_c[0] + "\n"
                            elif self.__file_item_b[0] == "PtsY":
                                self.__file_item_a = "PtsY = " + self.__file_item_c[1] + "\n"
                        else:
                            break
                        self.__file_item.append(self.__file_item_a)        #put target in list 
                  
                    if self.__file_item_grp_num > int(self.__OptionM_grpNum_str.get()) != 0:
                        self.__file_item_yield = self.__file_item[0]
                        del self.__file_item
                        break
                    if self.__file_item_del == True:                 #delete polygon and map 
                        del self.__file_item
                        continue
                    if "Acquire = 1\n" not in self.__file_item:
                        if self.__OptionM_markA_str.get() == "All acquire":
                            self.__file_item.insert(9, "Acquire = 1\n")
                        elif self.__OptionM_markA_str.get() == "acquire focus" and self.__file_item_grp_start == True:
                            self.__file_item.insert(9, "Acquire = 1\n")
                    if self.__file_item_grp_start == True:
                        self.__file_item.insert(6, "Note = 1\n")
                    else:
                        self.__file_item.insert(6, "Note = 2\n")
                    with open(self.__button_save_file.get(), mode="a") as self.__save_file:
                        self.__save_file.writelines("".join(self.__file_item))
                        self.__save_file.writelines("\n")
                    del self.__file_item
        del self.__entry_num
        self.__button_run.config(state="normal", fg="blue")
        self.__button_next_set.config(state="normal", fg="blue")
        self.__button_map.config(state="normal", fg="blue")
    
    def _edit_map(self):
        if self.__button_open_file.get() == self.__button_save_file.get():
            print("input file name = output file name")
            return
        elif self.__button_save_file.get() == "":
            print("Please name the output flile.")
            return
        elif self.__button_open_file.get() == "":
            print("Please give the input flile.")
            return
        elif int(self.__entry_start_num_str.get()) > int(self.__entry_end_num_str.get()):
            print("start_num > end_num!")
            return
        elif int(self.__entry_start_num_str.get()) == 0:
            print("start_num = 0")
            return
        elif int(self.__entry_end_num_str.get()) == 0:
            print("end_num = 0")
            return
        elif int(self.__entry_focus_start_str.get()) > int(self.__entry_focus_end_str.get()):
            print("focus_start > focus_end!")
            return
        elif int(self.__entry_focus_start_str.get()) == 0:
            print("focus_start = 0")
            return
        elif int(self.__entry_focus_end_str.get()) == 0:
            print("focus_end = 0")
            return
        elif int(self.__entry_start_num_str.get()) <= int(self.__entry_focus_start_str.get()) <= int(self.__entry_end_num_str.get()):
            print("detect overlap between position edit points and focus points!")
            return
        elif int(self.__entry_start_num_str.get()) <= int(self.__entry_focus_end_str.get()) <= int(self.__entry_end_num_str.get()):
            print("detect overlap between position edit points and focus points!")
            return        
        

        print("input parameters:")
        print("input file:", self.__open_filename)
        print("output file:", self.__save_filename)
        print("from", self.__entry_start_num_str.get(), "to", self.__entry_end_num_str.get())
        print("X_adj =", self.__entry_X_adj_str.get(), ", Y_adj =", self.__entry_Y_adj_str.get())
        print("map group from:", self.__entry_focus_start_str.get(), "to", self.__entry_focus_end_str.get())
        print(self.__OptionM_markA_str.get(), ", groups", self.__OptionM_grpNum_str.get())
        print("start")

        self.__entry_map_num = dict()      
        self.__map_item_position = dict()
        self.__map_item_grp_num = 0
        for self.__entry_map_num_index in range(int(self.__entry_focus_start_str.get()), int(self.__entry_focus_end_str.get())+1):
            self.__entry_map_num[str("[Item = " + str(self.__entry_map_num_index) + "]\n")] = self.__entry_map_num_index
            
        with open(self.__button_open_file.get(), mode="r") as self.__open_map_file:
            for self.__map_index, self.__map_line in enumerate(self.__open_map_file):
                if self.__map_line in self.__entry_map_num.keys():
#                      self.__map_item_position[self.__entry_map_num[self.__map_line]] = self.__map_index + 1
                    self.__map_item_position[self.__map_item_grp_num] = self.__map_index + 1
                    self.__map_item_grp_num += 1
        
        self.__map_item_point_check = True
        
        self._file_map_edit()
            
        self.__entry_map_num.clear()
        self.__map_item_position.clear()
        print("done")

        

    def _file_map_point_edit(self):
        if self.__map_item_position.get(self.__file_item_grp_num, "N") == "N":
            self.__map_item_point_check = False
            return
        self.__map_point_item = list()
        for self.__map_point_item_index in range(20):
            self.__map_point_item_num = int(self.__map_item_position.get(self.__file_item_grp_num)) + self.__map_point_item_index - 1
            
            self.__map_point_item_a = linecache.getline(self.__button_open_file.get(), self.__map_point_item_num)
            
            if " = " in self.__map_point_item_a:
                self.__map_point_item_b = self.__map_point_item_a.split(sep=" = ")
                if self.__map_point_item_b[0] == "GroupID":
                    self.__map_point_item_a = "GroupID = " + str(self.__file_item_grpID_new) + "\n"
                elif self.__map_point_item_b[0] == "Note":
                    self.__map_point_item_a = ""
                elif self.__map_point_item_b[0] == "Acquire":
                    self.__map_point_item_a = ""
                elif self.__map_point_item_b[0] == "StageXYZ":
                    self.__map_point_item_c = self.__map_point_item_b[1].split(sep=" ")
                    self.__map_point_item_z = self.__map_point_item_c[2].split(sep="\n")
                    self.__map_point_item_z[0] = str("%.3f" % (float(self.__map_point_item_z[0]) + float(self.__entry_Z_adj_str.get())))
                    self.__map_point_item_a = "StageXYZ = " + self.__map_point_item_c[0] + " " + self.__map_point_item_c[1] + " " + self.__map_point_item_z[0] + "\n"
                    
                    self.__focus_inner_check_x = float(self.__map_point_item_c[0])
                    self.__focus_inner_check_y = float(self.__map_point_item_c[1])
                
                    
                elif self.__map_point_item_b[0] == "Type":
                    self.__map_point_item_t = self.__map_point_item_b[1].split(sep="\n")
                    if int(self.__map_point_item_t[0]) != 0:
                        print("Map Group ", self.__file_item_grp_num, linecache.getline(self.__button_open_file.get(), int(self.__map_item_position.get(self.__file_item_grp_num))), " is not a point!")
                        self.__map_point_item_del = True
                        self.__map_item_point_check = False
                    else:
                        self.__map_point_item_del = False                        
            else:
                break
            self.__map_point_item.append(self.__map_point_item_a)

        if self.__map_point_item_del == True:
            del self.__map_point_item
            print("detect non focus point in focus point range!")
            return
        if "Acquire = 1\n" not in self.__map_point_item:
            self.__map_point_item.insert(9, "Acquire = 1\n")
        if "Note = 1\n" not in self.__map_point_item:
            self.__map_point_item.insert(6, "Note = 1\n")
        with open(self.__button_save_file.get(), mode="a") as self.__save_file:
            self.__save_file.writelines("".join(self.__map_point_item))
            self.__save_file.writelines("\n")
        del self.__map_point_item
    
        
        
            
    def _file_map_edit(self):
        self.__button_next_set.config(state="disabled", fg="gray")
        self.__button_run.config(state="disabled", fg="gray")
        self.__button_map.config(state="disabled", fg="gray")
        with open(self.__button_save_file.get(), mode="w") as self.__save_file:
            self.__save_file.writelines("AdocVersion = 2.00\n\n")
        self.__file_item_grpID_old = "0"
        self.__file_item_grpID_new = "0"
        self.__file_item_grp_num = 0
        self.__entry_num = list()
        
        if self.__OptionM_markB_str.get() == "manual_pick":
            for self.__entry_num_index in range(int(self.__entry_start_num_str.get()), int(self.__entry_end_num_str.get())+1):
                self.__entry_num.append("[Item = " + str(self.__entry_num_index) + "]\n")
        elif self.__OptionM_markB_str.get() == "auto_pick":
            for self.__entry_num_index in range(int(self.__entry_start_num_str.get()), int(self.__entry_end_num_str.get())+1):
                for self.__item_add_num in range(1, 50):
                    self.__entry_num.append("[Item = " + str(self.__entry_num_index) + "-" + str(self.__item_add_num) + "]\n")

        with open(self.__button_open_file.get(), mode="r") as self.__open_file:
            for self.__each_line in self.__open_file:
                if self.__each_line in self.__entry_num:
                    self.__file_item = list()
                    self.__file_item.append(self.__each_line) #put target in list 
                    for self.__file_item_index in range(20):
                        self.__file_item_a = self.__open_file.readline()
                        
                        if " = " in self.__file_item_a:
                            self.__file_item_b = self.__file_item_a.split(sep=" = ")
                            if self.__file_item_b[0] == "StageXYZ":                   #edit StageXYZ, make StageXYZ = (X + X_adj), (Y + Y_adj), Z\n
                                self.__file_item_c = self.__file_item_b[1].split(sep=" ")
                                self.__file_item_c[0] = str("%.3f" % (float(self.__file_item_c[0]) + float(self.__entry_X_adj_str.get())))
                                self.__file_item_c[1] = str("%.3f" % (float(self.__file_item_c[1]) + float(self.__entry_Y_adj_str.get())))
                                self.__file_item_z = self.__file_item_c[2].split(sep="\n")
                                self.__file_item_z[0] = str("%.3f" % (float(self.__file_item_z[0]) + float(self.__entry_Z_adj_str.get())))
                                self.__file_item_a = "StageXYZ = " + self.__file_item_c[0] + " " + self.__file_item_c[1] + " " + self.__file_item_z[0] + "\n"
                                
                                self.__focus_inner_check_x_file = float(self.__file_item_c[0])
                                self.__focus_inner_check_y_file = float(self.__file_item_c[1])                                 
                            elif self.__file_item_b[0] == "Type":
                                self.__file_item_t = self.__file_item_b[1].split(sep="\n")
                                if int(self.__file_item_t[0]) != 0:
                                    self.__file_item_del = True
                                    break                                    
                                else:
                                    self.__file_item_del = False
                            elif self.__file_item_b[0] == "Note":
                                self.__file_item_a = ""
                            elif self.__file_item_b[0] == "GroupID":
                                self.__file_item_d = self.__file_item_b[1].split(sep="\n")
                                self.__file_item_grpID_new = self.__file_item_d[0]
                                if self.__file_item_grpID_new != self.__file_item_grpID_old:
                                    self._file_map_point_edit()     #insert point for RealigntoNavitem as the first point in group
                                    if self.__map_item_point_check == False:
                                        break
                                    print("current point:", self.__focus_inner_check_x_file, self.__focus_inner_check_y_file)
                                    print("map point:", self.__focus_inner_check_x, self.__focus_inner_check_y)
                                    self.__focus_inner_check_x -= self.__focus_inner_check_x_file
                                    self.__focus_inner_check_y -= self.__focus_inner_check_y_file
                                    
                                    if math.fabs(self.__focus_inner_check_x) > 2 or math.fabs(self.__focus_inner_check_y) > 2:
                                        print("distance between two point", self.__focus_inner_check_x, self.__focus_inner_check_y)
                                        
                                        print("focus points chaos at ", linecache.getline(self.__button_open_file.get(), int(self.__map_item_position.get(self.__file_item_grp_num))))
                                        self.__map_item_point_check = False
                                        
                                        break
                                    
                                    self.__file_item_grpID_old = self.__file_item_grpID_new
                                    self.__file_item_grp_num += 1
                            elif self.__file_item_b[0] == "Acquire":
                                self.__file_item_a = ""
                            elif self.__file_item_b[0] == "PtsX":
                               self.__file_item_a = "PtsX = " + self.__file_item_c[0] + "\n"
                            elif self.__file_item_b[0] == "PtsY":
                                self.__file_item_a = "PtsY = " + self.__file_item_c[1] + "\n"
                        else:
                            break
                        self.__file_item.append(self.__file_item_a)
                    if self.__file_item_del == True:
                        del self.__file_item
                        continue
                    if self.__map_item_point_check == False:
                        del self.__file_item
                        break
                    if self.__OptionM_markA_str.get() == "All acquire":
                        self.__file_item.insert(9, "Acquire = 1\n")
                    
                    self.__file_item.insert(6, "Note = 2\n")
                    with open(self.__button_save_file.get(), mode="a") as self.__save_file:
                        self.__save_file.writelines("".join(self.__file_item))
                        self.__save_file.writelines("\n")
                    del self.__file_item
                if self.__map_item_point_check == False:
                    break
        
        self.__button_run.config(state="normal", fg="blue")
        self.__button_next_set.config(state="normal", fg="blue")
        self.__button_map.config(state="normal", fg="blue")                            
#        print(self.__map_item_position.items())
#        print(self.__entry_focus_start_str.get())
#        print(self.__map_item_position.get(int(self.__entry_focus_end_str.get())))
#        self.__picked_line = linecache.getline(self.__button_open_file.get(), int(self.__map_item_position.get(int(self.__entry_focus_end_str.get()))))
#        print (self.__picked_line)

    def _entry_invalid_X(self):
        self.__entry_X_adj.delete(0, tk.END)
        self.__entry_X_adj.insert(0,"0")
    def _entry_invalid_Y(self):
        self.__entry_Y_adj.delete(0, tk.END)
        self.__entry_Y_adj.insert(0,"0")
    def _entry_invalid_Z(self):
        self.__entry_Z_adj.delete(0, tk.END)
        self.__entry_Z_adj.insert(0,"0")
    def _entry_invalid_start_num(self):
        self.__entry_start_num.delete(0, tk.END)
        self.__entry_start_num.insert(0,"0")
    def _entry_invalid_end_num(self):
        self.__entry_end_num.delete(0, tk.END)
        self.__entry_end_num.insert(0,"0")      
    def _entry_invalid_focus_start(self):
        self.__entry_focus_start.delete(0, tk.END)
        self.__entry_focus_start.insert(0,"0")
    def _entry_invalid_focus_end(self):
        self.__entry_focus_end.delete(0, tk.END)
        self.__entry_focus_end.insert(0,"0")    

    def _open_file_dialg(self):
        self.__open_filename = tkf.askopenfilename(filetypes=[("NAV", ".nav")])

        self.__button_open_file.set(self.__open_filename)
    def _save_file_dialg(self):
        self.__save_filename = tkf.asksaveasfilename(filetypes=[("NAV", ".nav")])
 
        self.__button_save_file.set(self.__save_filename)
    def mainloop(self):
        self.__main_win.mainloop()

        
def test_Nav_edit():
    win = Nav_edit()
    win.mainloop()
if __name__ == '__main__':
    test_Nav_edit()