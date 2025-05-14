import re


class LogAnalyer:

    def __init__(self,logAnalyzerTk,entry):
        self.entry = entry
        self.logAnalyzerTk = logAnalyzerTk

    def get_entry(self):
        pass


    # 读取整个日志的内容
    def get_log_file(self):
        print(self.logAnalyzerTk)
        path = self.logAnalyzerTk.get_Entry(self.entry)
        with open(path, 'r',encoding='utf-8') as file:
            log_lines = file.readlines()
        print(type(log_lines))
        return log_lines

    # 清空日志
    def truncate_file(self):
        path = self.logAnalyzerTk.get_Entry(self.entry)
        with open(path, 'r+') as file:
            file.truncate()
        print(path + "已清空")

    # 读取战斗日志
    def get_battle_log(self):
        return self.pattern_search("攻击者|受击者")

    # 读取技能日志
    def get_skill_log(self):
        return self.pattern_search(r"release skill")

    # 读取buff日志
    def get_buff_log(self):
        return self.pattern_search(r"(buff)$")

    # 读取法术伤害
    def get_magic_log(self):
        return self.pattern_search(r"法术伤害")

    # 读取replay
    def get_replay_log(self):
        return self.pattern_search(r"BattleReplay fileName:")


    # 正则搜索
    def pattern_search(self,pattern):
        res = ""
        log_lines=self.get_log_file()
       # print(log_lines)
        try:
            m_pattern = re.compile(pattern)
            for i in log_lines:
                result = m_pattern.findall(i)
                if result:
                    print (i),
                    res += i
        except:
            print("pattern 为空")
        return res


    # 单行匹配
    def line_pattern_search(self,pattern,line):
        res =  re.search(pattern,line)
        return  res

    #搜索进攻者和防御者
    def search_atk_def(self,atk_atr_dic,def_atr_dic,atk_name="",def_name="",atk_bool=False,def_bool=False,):
        search_res=""
        log_lines=self.get_log_file()
        atk_name = atk_name.replace('(', '\(').replace(')', '\)')
        def_name = def_name.replace('(', '\(').replace(')', '\)')

        for index,line in enumerate(log_lines):
             if "攻击者" in line:
                 line = line.replace('\n','\t\t\t\t\t\t\t')+log_lines[index+1]
                 print("-------",atk_name,def_name)
                 pattern = "攻击者= {0}(.*)受击者= {1}(.*)最终伤害.*".format(atk_name, def_name)
                 res = self.line_pattern_search(pattern, line)

                 if(res):
                     #攻击者部分
                     if atk_bool:
                         del_str = line[line.index(')')+1:line.index("受击者")]
                         line = line.replace(del_str,"\t\t\t\t\t\t")
                     else:
                         #筛选属性
                         for name,value in atk_atr_dic.items():
                           # print("name",name)
                            if(value.get()==False):
                                name = name.replace('(','\(').replace(')','\)')
                                pattern = name + ":-?\d+\.?\d*";
                                #print("----->",pattern)
                                attribute = self.line_pattern_search(pattern, line).group(0)
                                #print("attribute",attribute)
                                line = line.replace(attribute,"",1)

                     if def_bool:
                         start_index = line.index("受击者")
                         del_str = line[line.index(')',start_index)+1:line.index("最终伤害")]
                         line = line.replace(del_str,"\t\t\t\t\t\t")

                     else:
                         line_def = line[line.index("受击者"):]
                         for name, value in def_atr_dic.items():
                             # print("name",name)
                             if (value.get() == False):
                                 name = name.replace('(', '\(').replace(')', '\)')
                                 pattern = name + ":-?\d+\.?\d*";
                                 print("----->", pattern)
                                 print("----->",line_def)
                                 attribute = self.line_pattern_search(pattern, line_def).group(0)
                                 print("attribute", attribute)
                                 if(attribute):
                                    line_def = line_def.replace(attribute, "", 1)

                         line = line[0:line.index("受击者")]+line_def
                     search_res += line

        return search_res




