# edit_F_gcode  


某 F 向けの gcode の編集と、確認のための描画を行うプログラム。  

編集部分は Python 3系、描画部分には Rhino + Grasshopper を用いるため Python 2系。  


## 構成  

- module_gcode  
  - analysis_string  
  - operate_string  
  - util  
  - gcode_for_gh // ghPython Component  


## 雑感  

元の文字列が綺麗のなので、例外も無く助かった。  

XY ベクトルを渡してパスを移動させる関数を作って、それをループで回して複製。考えれば当たり前の実装であるが、迷わずにきちんと作れたので良かった。  
