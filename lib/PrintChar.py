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
    # print congrats in terminal
    def print_congrate(self):
        print("*****************************************")
        print("*****************************************")
        print("**                                     **")
        print("**                 ccccc               **")
        print("**              ccc                    **")
        print("**             ccc                     **")
        print("**            ccc                      **")
        print("**           ccc                       **")
        print("**          ccc                        **")
        print("**         ccc                         **")
        print("**          ccc                        **")
        print("**            ccc                      **")
        print("**              ccc                    **")
        print("**                ccc                  **")
        print("**                   cccc              **")
        print("**                                     **")
        print("**                                     **")
        print("**                                     **")
        print("**             ooooo                   **")
        print("**          ooo     ooo                **")
        print("**        ooo         ooo              **")
        print("**       ooo           ooo             **")
        print("**      ooo             ooo            **")
        print("**     ooo               ooo           **")
        print("**    ooo                 ooo          **")
        print("**     ooo               ooo           **")
        print("**      ooo             ooo            **")
        print("**        ooo          ooo             **")
        print("**          ooo      ooo               **")
        print("**             oooooo                  **")
        print("**                                     **")
        print("**        nnnnn          nnn           **")
        print("**        nnnnnn         nnn           **")
        print("**        nnn nnn        nnn           **")
        print("**        nnn  nnn       nnn           **")
        print("**        nnn   nnn      nnn           **")
        print("**        nnn    nnn     nnn           **")
        print("**        nnn     nnn    nnn           **")
        print("**        nnn      nnn   nnn           **")
        print("**        nnn       nnn  nnn           **")
        print("**        nnn        nnn nnn           **")
        print("**        nnn        nnnnnnn           **")
        print("**        nnn        nnnnnnn           **")
        print("**                                     **")
        print("**            GGGGGGGGGGGG             **")
        print("**          GGG         GGG            **")
        print("**         GGG           GGG           **")
        print("**        GGG                          **")
        print("**       GGG                           **")
        print("**       GGG                           **")
        print("**       GGG        GGGGGGGGGG         **")
        print("**        GGG      GGG      GGG        **")
        print("**         GGG              GGG        **")
        print("**          GGG             GGG        **")
        print("**           GG             GGG        **")
        print("**             GGGGGGGGGGGGGGG         **")
        print("**                                     **")
        print("**           RRRRRRRRRRRR              **")
        print("**           RRR        RRR            **")
        print("**           RRR         RRR           **")
        print("**           RRR        RRR            **")
        print("**           RRR       RRR             **")
        print("**           RRR      RRR              **")
        print("**           RRRRRRRRR    GG           **")
        print("**           RRR    RRR                **")
        print("**           RRR     RRR               **")
        print("**           RRR      RRR              **")
        print("**           RRR       RRR             **")
        print("**           RRR        RRR            **")
        print("**                                     **")
        print("**                 AAA                 **")
        print("**                AAAAA                **")
        print("**              AAA   AAA              **")
        print("**             AAA     AAA             **")
        print("**            AAA       AAA            **")
        print("**           AAA         AAA           **")
        print("**          AAAAAAAAAAAAAAAAA          **")
        print("**         AAAAAAAAAAAAAAAAAAA         **")
        print("**        AAA               AAA        **")
        print("**       AAA                 AAA       **")
        print("**      AAA                   AAA      **")
        print("**     AAA                     AAA     **")
        print("**                                     **")
        print("**        TTTTTTTTTTTTTTTTTTTTT        **")
        print("**        TTTTTTTTTTTTTTTTTTTTT        **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                 TTT                 **")
        print("**                                     **")
        print("**            SSSSSSSSSSS              **")
        print("**          SSS        SSS             **")
        print("**        SSS                          **")
        print("**       SSS                           **")
        print("**         SSS                         **")
        print("**           SSS                       **")
        print("**             SSS                     **")
        print("**               SSS                   **")
        print("**                  SSS                **")
        print("**                    SSS              **")
        print("**       SSS        SSS                **")
        print("**        SSSSSSSSSSS                  **")
        print("**                                     **")
        print("**                                     **")        
        print("*****************************************")
        print("*****************************************")

    def print_win(self,X_OR_O):
        print("**************************************************************************************")
        print("**************************************************************************************")
        print("*                                                                                   **")
        if(X_OR_O== "x" or X_OR_O == "X") :
            print("**  xxx        xxx             WWW                WWW    i    NNNNNN         NNN   **")
            print("**   xxx      xxx              WWW                WWW   III   NNN NNN        NNN   **")
            print("**    xxx    xxx                WWW              WWW    III   NNN  NNN       NNN   **")
            print("**     xxx  xxx                 WWW              WWW    III   NNN   NNN      NNN   **")
            print("**      xxxxxx                   WWW    WWW     WWW     III   NNN    NNN     NNN   **")
            print("**     xxx  xxx                  WWW  WWW  WWW  WWW     III   NNN     NNN    NNN   **")
            print("**    xxx    xxx                  WWW WWW  WWW WWW      III   NNN      NNN   NNN   **")
            print("**   xxx      xxx                  WWWW     WWWW        III   NNN       NNN  NNN   **")
            print("**  xxx        xxx                  WWW       WWW       III   NNN        NNNNNN    **")
        else:
            print("**           OOO                  WWW                WWW    i    NNNNNN         NNN   **")
            print("**         OOO OOO                WWW                WWW   III   NNN NNN        NNN   **")
            print("**       OOO     OOO               WWW              WWW    III   NNN  NNN       NNN   **")
            print("**     OOO         OOO             WWW              WWW    III   NNN   NNN      NNN   **")
            print("**   OOO             OOO            WWW    WWW     WWW     III   NNN    NNN     NNN   **")
            print("**     OOO         OOO              WWW  WWW  WWW  WWW     III   NNN     NNN    NNN   **")
            print("**       OOO      OOO                WWW WWW  WWW WWW      III   NNN      NNN   NNN   **")
            print("**         OOO  OOO                   WWWW     WWWW        III   NNN       NNN  NNN   **")
            print("**            OOO                      WWW       WWW       III   NNN        NNNNNN    **")            
        print("**                                                                                  **")
        print("**************************************************************************************")
        print("**************************************************************************************")