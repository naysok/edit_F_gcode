from module_gcode import analysis_string, operate_string

aa = analysis_string.Analysis_String()
oo = operate_string.Operate_String()


path_src = "./data/gcode_original/face3_3_F.txt"

off_vector = (225, 300)
count = (7, 4)

##### canvas_size = (1700, 1300)
##### max_count = (7, 4)

### Analysis
#aa.analysis_element(path_src)

### Edit GCode, duplicete
oo.duplicate_path(path_src, count, off_vector)