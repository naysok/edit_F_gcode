class Analysis_String():


    def open_file(self, path):
        with open(path) as f:
            l = f.readlines()
        # print(type(l))
        # print(len(l))
        # print(l)
        return l


    def check_element(self, gcode, msg):

        c_xy = 0
        c_xx = 0
        c_yy = 0
        c_oo = 0
        c_gg = 0

        for i in range(len(msg)):
            # print("{} : {}".format(msg[i], gcode[i]))

            if msg[i] == "XY":
                c_xy += 1
            elif msg[i] == "XX":
                c_xx += 1
            elif msg[i] == "YY":
                c_yy += 1
            elif msg[i] == "OO":
                c_oo += 1
            elif msg[i] == "GG":
                c_gg += 1

        sum_number = c_xy + c_xx + c_yy + c_oo + c_gg
        
        print("- - - - - -")
        print("gcode length  : {}\nstatus length : {}".format(len(gcode), len(msg)))
        print("xy : {}, xx : {}, yy : {}, oo : {}, gg : {} / SUM : {}".format(c_xy, c_xx, c_yy, c_oo, c_gg, sum_number))
        print("- - - - - -")


    def analysis_element(self, path):

        gcode = self.open_file(path)
        
        msg = []

        # for i in range(20):
        for i in range(len(gcode)):
            str_ = gcode[i]
            
            if ("X" in str_) and ("Y" in str_):
                if ("G1" in str_):
                    msg.append("XY")
                else:
                    msg.append("GG")
            
            elif ("X" in str_) and ("Y" not in str_):
                msg.append("XX")
            
            elif ("X" not in str_) and ("Y" in str_):
                msg.append("YY")
            
            else:
                msg.append("OO")
        
        self.check_element(gcode, msg)

