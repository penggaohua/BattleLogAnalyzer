#coding=utf-8
from tkinter import *
from LogAnalyser import LogAnalyer
from LogAnalyserTK import LogAnalyerTK
from tkinter import StringVar
import configparser







if __name__=='__main__':
   # path = StringVar()
    #path.set(r"C:\Users\NING MEI\AppData\Local\Unity\Editor\Editor.log")
    cf = configparser.ConfigParser()
    cf.read("config.ini")
    path = cf.get("log_path", "log_path")

    # logAnalyerTk = LogAnalyerTK(r"C:\Users\JM\AppData\Local\Unity\Editor\Editor.log")
    logAnalyerTk = LogAnalyerTK(path)
    #攻击者属性列表
    atk_atr_dic = {
                 "生命":BooleanVar(),
                "当前血量":BooleanVar(),
                "攻击":BooleanVar(),
                "闪避":BooleanVar(),
                "护甲":BooleanVar(),
                "暴击":BooleanVar(),
                "吸血":BooleanVar(),
                "穿透":BooleanVar(),
                "无视闪避":BooleanVar(),
                "移动速度":BooleanVar(),
                "攻速":BooleanVar(),
                "混扽效果(伤害降低)":BooleanVar(),
                "攻城伤害":BooleanVar(),
                "魔法伤害系数":BooleanVar(),
                "单次伤害系数":BooleanVar()
                }
   #受击者属性列表
    def_atr_dic  ={
               "生命": BooleanVar(),
               "当前血量": BooleanVar(),
               "攻击": BooleanVar(),
               "闪避": BooleanVar(),
               "护甲": BooleanVar(),
               "暴击": BooleanVar(),
               "吸血": BooleanVar(),
               "穿透": BooleanVar(),
               "移动速度": BooleanVar(),
               "远程抗性": BooleanVar(),
               "法术抗性": BooleanVar(),
               "陷阱抗性": BooleanVar(),
               "暴击抗性": BooleanVar(),
               "所有抗性": BooleanVar(),
               "生命护盾值": BooleanVar()

    }

    for value in atk_atr_dic.values():
           value.set(True)
    for value in def_atr_dic.values():
           value.set(True)

    check_button_value_atk = BooleanVar()
    check_button_value_def = BooleanVar()



    frame1 = logAnalyerTk.set_frame()
    frame2 = logAnalyerTk.set_frame()
    frame3 = logAnalyerTk.set_frame()
    frame4 = logAnalyerTk.set_frame()
    frame5 = logAnalyerTk.set_frame()

    #frame1
    log_entry = logAnalyerTk.set_Entry(frame1,65,logAnalyerTk.path)
    logAnalyer = LogAnalyer(logAnalyerTk,log_entry)

    print(log_entry.get())
    btn_get_log= logAnalyerTk.set_button(frame1,"读取日志",lambda :logAnalyerTk.show_in_text(logAnalyer.get_log_file(),text_output))
    btn_truncate_log= logAnalyerTk.set_button(frame1,"清除日志",logAnalyer.truncate_file,bg="LightCoral")
    btn_battle_log= logAnalyerTk.set_button(frame1,"读取战斗日志",lambda :logAnalyerTk.show_in_text(logAnalyer.get_battle_log(),text_output))
    btn_skill_log= logAnalyerTk.set_button(frame1,"读取技能日志",lambda :logAnalyerTk.show_in_text(logAnalyer.get_skill_log(),text_output))
    btn_buff_log= logAnalyerTk.set_button(frame1,"读取buff日志",lambda :logAnalyerTk.show_in_text(logAnalyer.get_buff_log(),text_output))
    btn_magic_log= logAnalyerTk.set_button(frame1,"读取法术日志",lambda :logAnalyerTk.show_in_text(logAnalyer.get_magic_log(),text_output))
    btn_replay_log= logAnalyerTk.set_button(frame1,"读取战报日志",lambda :logAnalyerTk.show_in_text(logAnalyer.get_replay_log(),text_output))


    frame1.grid(row=0 ,column=0,sticky=W)
    log_entry.pack(padx=15,side=LEFT)
    btn_get_log.pack(padx=15,side=LEFT)
    btn_truncate_log.pack(padx=15,side=LEFT)
    btn_battle_log.pack(padx=15,side=LEFT)
    btn_skill_log.pack(padx=15,side=LEFT)
    btn_buff_log.pack(padx=15,side=LEFT)
    btn_magic_log.pack(padx=15,side=LEFT)
    btn_replay_log.pack(padx=15,side=LEFT)

    #frame2
    label_atk= logAnalyerTk.set_lable(frame2,"攻击者:")
    entry_atk= logAnalyerTk.set_Entry(frame2,30)
    check_atk = logAnalyerTk.set_check_button(frame2,"仅显示攻击者名称",check_button_value_atk)



    label_atk.pack(padx=15,side=LEFT)
    entry_atk.pack(padx=15,side=LEFT)
    check_atk.pack(padx=15,side=LEFT)

    list_check_atk = [logAnalyerTk.set_check_button(frame2, key, value).pack(padx=5, side=LEFT) for key, value in atk_atr_dic.items()]

    #全选 /取消
    btn_select_all_atk = logAnalyerTk.set_button(frame2,"全选/取消",lambda :logAnalyerTk.select_all(atk_atr_dic))
    btn_select_all_atk.pack(padx=15,side=LEFT)

    frame2.grid(row=1 ,column=0 ,pady=5,sticky=W)
    #frame3
    label_def= logAnalyerTk.set_lable(frame3,"受击者:")
    entry_def= logAnalyerTk.set_Entry(frame3,30)
    check_def = logAnalyerTk.set_check_button(frame3,"仅显示受击者名称",check_button_value_def)
    label_def.pack(padx=15,side=LEFT)
    entry_def.pack(padx=15,side=LEFT)
    check_def.pack(padx=15,side=LEFT)
    frame3.grid(row=2 ,column=0 ,pady=10,sticky=W)

    list_check_def = [logAnalyerTk.set_check_button(frame3, key, value).pack(padx=5, side=LEFT) for key, value in  def_atr_dic.items()]
    btn_select_all_def = logAnalyerTk.set_button(frame3,"全选/取消",lambda :logAnalyerTk.select_all(def_atr_dic))
    btn_select_all_def.pack(padx=15,side=LEFT)

    #frame4
    entry_regex=logAnalyerTk.set_Entry(frame4,65,"请输入要搜索的内容，支持正则表达式")
    btn_reg_search= logAnalyerTk.set_button(frame4,"正则搜索",lambda :logAnalyerTk.show_in_text(logAnalyer.pattern_search(entry_regex.get()),text_output))
    btn_search= logAnalyerTk.set_button(frame4,"搜索日志",lambda :logAnalyerTk.show_in_text(logAnalyer.search_atk_def(atk_atr_dic,def_atr_dic,entry_atk.get(),entry_def.get(),check_button_value_atk.get(),check_button_value_def.get()),text_output),bg="skyblue")
    btn_truncate_res=  logAnalyerTk.set_button(frame4,"清空搜索",lambda :logAnalyerTk.clean_text(text_output))

    entry_regex.pack(padx=15,side=LEFT)
    btn_reg_search.pack(padx=15,side=LEFT)
    btn_search.pack(padx=15,side=LEFT)
    btn_truncate_res.pack(padx=15,side=LEFT)
    frame4.grid(row=3 ,column=0 ,pady=5,sticky=W)

    #frame5
    text_output = logAnalyerTk.set_scroll_text(frame5,260,40)
    label_compare= logAnalyerTk.set_lable(frame5,"对比池:")
    text_output_compare = logAnalyerTk.set_scroll_text(frame5,260,20)
    text_output.grid(row=0,column=0,sticky=W,pady=10,padx=10)
    label_compare.grid(row=1,column=0,sticky=W,padx=10)
    text_output_compare.grid(row=2,column=0,sticky=N)
    frame5.grid(row=4 ,column=0 ,pady=5,sticky=N)

    #button2.pack(padx=15,side=LEFT)
    #button3.pack(padx=15,side=LEFT)

    logAnalyerTk.main()
