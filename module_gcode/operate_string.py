from . import util
ut = util.Util()


class Operate_String():

    def open_file(self, path):
        with open(path) as f:
            l = f.readlines()
        return l
    

    def flatten_array_2d(self, array_2d):
        items = []
        for i in range(len(array_2d)):
            sub = array_2d[i]
            for j in range(len(sub)):
                items.append(sub[j])
        return items


    def offset_xy(self, path, vector):
        
        gcode = self.open_file(path)
        gcode_edited = []

        for i in range(len(gcode)):
            tmp_string = gcode[i]

            if ("X" in tmp_string) and ("Y" in tmp_string):
                ### split elements
                elements = tmp_string.split()
                
                for j in range(len(elements)):
                    e = elements[j]
                    
                    if ("X" in e):
                        tmp_x = e.split("X")
                    
                    if ("Y" in e):
                        tmp_y = e.split("Y")
                
                new_x = '{:.08f}'.format(float(tmp_x[1]) + float(vector[0]))
                new_y = '{:.08f}'.format(float(tmp_y[1]) + float(vector[1]))
                new_string = "G1 X{} Y{}".format(new_x, new_y)

                gcode_edited.append(new_string)

            else:
                new_string = tmp_string.replace('\n', '')
                gcode_edited.append(new_string)
        
        return gcode_edited



    def duplicate_path(self, path, count, vector):
        
        dup = []
        body_count = 1

        for j in range(count[1]):
            for i in range(count[0]):
                offset_vector = (vector[0] * i, vector[1] * j)
                print(offset_vector)
                export = self.offset_xy(path, offset_vector)
                
                ### add message
                comment = []
                c = "(nnnnnnnnnnnnnnnnnnnnnnnn body count {} nnnnnnnnnnnnnnnnnnnnnnnn)".format(body_count)
                comment.append(c)
                body_count += 1

                dup.append(comment)
                dup.append(export)
        
        gcode_edited = self.flatten_array_2d(dup)

        
        ### Export File
        now = ut.get_current_time()
        path_current_time = "./data/gcode_out/" + now + ".txt"
        
        with open(path_current_time, mode='w') as f:
            f.write('\n'.join(gcode_edited))
        print("- - - - - -")
        print("Export : {}".format(path_current_time))
        print("Count : {}".format(count))
        print("- - - - - -")

        