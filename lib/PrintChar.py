class PrintChar():
    def __init__(self) -> None:
        pass
    def print_full_char(self,char:str,num:int):
        str_ = ""
        for i in range(0 ,num):
            str_ += char
        return str_
    def print_x(self , num):
        match(num):
            case 1:
                return "  xx       xx  "
            case 2:
                return "   xx     xx   "
            case 3:
                return "    xx   xx    "
            case 4:
                return "      xxx      "
            case 5:
                return "    xx   xx    "
            case 6:
                return "   xx      xx  "
            case 7:
                return "  xx        xx "
                
    def print_o(self , num):
        match(num):
            case 1:
                return "      ooo      "
            case 2:
                return "    oo   oo    "
            case 3:
                return "   oo     oo   "
            case 4:
                return "  oo       oo  "
            case 5:
                return "   oo     oo   "
            case 6:
                return "    oo   oo    "
            case 7:
                return "      ooo      "
