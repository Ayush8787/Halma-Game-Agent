import math

list1 = []
list2 = []
list1_pos = ""
parent_child = {}
B_dict = {}
W_dict = {}
relation = {}
oldextra = []
allmoves = {}
relation_updated = {}
parent_child_updated = {}
leaf = {}
final_dis = 0
final_dic_at_leaf = {}
final_dic_at_leaf2 = {}
inout_dic = {}
inin_dic = {}
outout_dic = {}
distance = {}
goal_dic = {}
distance1 = {}
final_list2 = {}
allmoves= {}
in_triangle_B = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4, (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 4,
                 (1, 4): 5, (2, 0): 2, (2, 1): 3, (2, 2): 4, (2, 3): 5, (3, 0): 3, (3, 1): 4, (3, 2): 5, (4, 0): 4,
                 (4, 1): 5}

in_triangle_W = {(11, 14): 1, (11, 15): 2, (12, 13): 1, (12, 14): 2, (12, 15): 3, (13, 12): 1, (13, 13): 2, (13, 14): 3,
                 (13, 15): 4, (14, 11): 1, (14, 12): 2, (14, 13): 3, (14, 14): 4, (14, 15): 5, (15, 11): 2, (15, 12): 3,
                 (15, 13): 4, (15, 14): 5, (15, 15): 6 }

evalution_dic_J_inout = {}
evalution_dic_E_inout = {}
evalution_dic_J_inin = {}
evalution_dic_E_inin = {}
evalution_dic_J_outout = {}
evalution_dic_E_outout = {}
dis_dic = {}
n = -1

White_i_des = 15
White_j_des = 15
f = open("input.txt", "r")


# Mode
mode = (f.readline()).split()


# Color
color = (f.readline()).split()


# Time
Time = (f.readline()).split()


    # for iter2 in range(16):
    #     list1_pos = f.readline().split()
    #     x = list1_pos[0]
    #     print(x)
    #     bm = [x[j] for j in range(0,len(x))]
    #     list1.append(bm)
    #     print(list1)

for iter2 in range(16):
    list1_pos = f.readline().rstrip('\n')
    results1 = [i for i in list1_pos]
    list1.append(results1)

def getreport():
    B_dict.clear()
    W_dict.clear()

    for i in range(16):
        for j in range(16):
            if list1[i][j] == "W":
                W_dict.update({(i, j): 1})
            elif list1[i][j] == "B":
                B_dict.update({(i, j): 1})
    flag = 0

def search_neighbour(i, j, flag):
    extra = [[i, j]]

    if 0 <= j + 1 < 16 and i >= 0 and (list1[i][j + 1] != "W" and list1[i][j + 1] != "B"):
        parent_child.update({((i, j), (i, j + 1)): ['E', [[i, j], [i, j + 1]]]})
    if 0 <= j + 1 < 16 and i >= 0 and (list1[i][j + 1] == "W" or list1[i][j + 1] == "B"):
        if 0 <= j + 2 < 16 and i >= 0 and (list1[i][j + 2] != "W" and list1[i][j + 2] != "B"):
            extra.append([i, j + 2])
            relation.update({((i, j), (i, j + 2)): ["J", extra]})
            search(i, j + 2, i, j, extra[:])

    extra = [[i, j]]

    if i >= 0 and j - 1 >= 0 and (list1[i][j - 1] != "W" and list1[i][j - 1] != "B"):
        parent_child.update({((i, j), (i, j - 1)): ['E', [[i, j], [i, j - 1]]]})
    if i >= 0 and j - 1 >= 0 and (list1[i][j - 1] == "W" or list1[i][j - 1] == "B"):
        if i >= 0 and j - 2 >= 0 and (list1[i][j - 2] != "W" and list1[i][j - 2] != "B"):
            extra.append([i, j - 2])
            relation.update({((i, j), (i, j - 2)): ["J", extra]})
            search(i, j - 2, i, j, extra[:])

    extra = [[i, j]]
    if 0 <= i + 1 < 16 and j >= 0 and (list1[i + 1][j] != "W" and list1[i + 1][j] != "B"):
        parent_child.update({((i, j), (i + 1, j)): ['E', [[i, j], [i + 1, j]]]})
    if 0 <= i + 1 < 16 and j >= 0 and (list1[i + 1][j] == "W" or list1[i + 1][j] == "B"):
        if 0 <= i + 2 < 16 and j >= 0 and (list1[i + 2][j] != "W" and list1[i + 2][j] != "B"):
            extra.append([i + 2, j])
            relation.update({((i, j), (i + 2, j)): ["J", extra]})
            search(i + 2, j, i, j, extra[:])

    extra = [[i, j]]
    if i - 1 >= 0 and j >= 0 and (list1[i - 1][j] != "W" and list1[i - 1][j] != "B"):
        parent_child.update({((i, j), (i - 1, j)): ['E', [[i, j], [i - 1, j]]]})
    if i - 1 >= 0 and j >= 0 and (list1[i - 1][j] == "W" or list1[i - 1][j] == "B"):
        if i - 2 >= 0 and j >= 0 and (list1[i - 2][j] != "W" and list1[i - 2][j] != "B"):
            extra.append([i - 2, j])
            relation.update({((i, j), (i - 2, j)): ["J", extra]})
            search(i - 2, j, i, j, extra[:])

    extra = [[i, j]]
    if i - 1 >= 0 and 0 <= j + 1 < 16 and (list1[i - 1][j + 1] != "W" and list1[i - 1][j + 1] != "B"):
        parent_child.update({((i, j), (i - 1, j + 1)): ['E', [[i, j], [i - 1, j + 1]]]})
    if i - 1 >= 0 and 0 <= j + 1 < 16 and (list1[i - 1][j + 1] == "W" or list1[i - 1][j + 1] == "B"):
        if i - 2 >= 0 and 0 <= j + 2 < 16 and (list1[i - 2][j + 2] != "W" and list1[i - 2][j + 2] != "B"):
            extra.append([i - 2, j + 2])
            relation.update({((i, j), (i - 2, j + 2)): ["J", extra]})
            search(i - 2, j + 2, i, j, extra[:])

    extra = [[i, j]]
    if 0 <= i + 1 < 16 and 0 <= j + 1 < 16 and (list1[i + 1][j + 1] != "W" and list1[i + 1][j + 1] != "B"):
        parent_child.update({((i, j), (i + 1, j + 1)): ['E', [[i, j], [i + 1, j + 1]]]})
    if 0 <= i + 1 < 16 and 0 <= j + 1 < 16 and (list1[i + 1][j + 1] == "W" or list1[i + 1][j + 1] == "B"):
        if 0 <= i + 2 < 16 and 0 <= j + 2 < 16 and (list1[i + 2][j + 2] != "W" and list1[i + 2][j + 2] != "B"):
            extra.append([i + 2, j + 2])
            relation.update({((i, j), (i + 2, j + 2)): ["J", extra]})
            search(i + 2, j + 2, i, j, extra[:])

    extra = [[i, j]]
    if 0 <= i + 1 < 16 and j - 1 >= 0 and (list1[i + 1][j - 1] != "W" and list1[i + 1][j - 1] != "B"):
        parent_child.update({((i, j), (i + 1, j - 1)): ['E', [[i, j], [i + 1, j - 1]]]})
    if 0 <= i + 1 < 16 and j - 1 >= 0 and (list1[i + 1][j - 1] == "W" or list1[i + 1][j - 1] == "B"):
        if 0 <= i + 2 < 16 and j - 2 >= 0 and (list1[i + 2][j - 2] != "W" and list1[i + 2][j - 2] != "B"):
            extra.append([i + 2, j - 2])
            relation.update({((i, j), (i + 2, j - 2)): ["J", extra]})
            search(i + 2, j - 2, i, j, extra[:])

    extra = [[i, j]]
    if i - 1 >= 0 and j - 1 >= 0 and (list1[i - 1][j - 1] != "W" and list1[i - 1][j - 1] != "B"):
        parent_child.update({((i, j), (i - 1, j - 1)): ['E', [[i, j], [i - 1, j - 1]]]})
    if i - 1 >= 0 and j - 1 >= 0 and (list1[i - 1][j - 1] == "W" or list1[i - 1][j - 1] == "B"):
        if i - 2 >= 0 and j - 2 >= 0 and (list1[i - 2][j - 2] != "W" and list1[i - 2][j - 2] != "B"):
            extra.append([i - 2, j - 2])
            relation.update({((i, j), (i - 2, j - 2)): ["J", extra]})
            search(i - 2, j - 2, i, j, extra[:])


def search(i, j, ip, jp, extra11):
    extra1 = extra11[:]
    if 0 <= j + 1 < 16 and i >= 0 and (list1[i][j + 1] == "W" or list1[i][j + 1] == "B"):
        if 0 <= j + 2 < 16 and i >= 0 and (list1[i][j + 2] != "W" and list1[i][j + 2] != "B"):
            if [i, j + 2] not in extra1:
                extra1.append([i, j + 2])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i, j + 2)): ["J", extra1]})
                search(i, j + 2, i, j, extra1[:])

    extra1 = extra11[:]
    if i >= 0 and j - 1 >= 0 and (list1[i][j - 1] == "W" or list1[i][j - 1] == "B"):
        if i >= 0 and j - 2 >= 0 and (list1[i][j - 2] != "W" and list1[i][j - 2] != "B"):
            if [i, j - 2] not in extra1:
                extra1.append([i, j - 2])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i, j - 2)): ["J", extra1]})
                search(i, j - 2, i, j, extra1[:])

    extra1 = extra11[:]
    if 0 <= i + 1 < 16 and j >= 0 and (list1[i + 1][j] == "W" or list1[i + 1][j] == "B"):
        if 0 <= i + 2 < 16 and j >= 0 and (list1[i + 2][j] != "W" and list1[i + 2][j] != "B"):
            if [i + 2, j] not in extra1:
                extra1.append([i + 2, j])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i + 2, j)): ["J", extra1]})
                search(i + 2, j, i, j, extra1[:])

    extra1 = extra11[:]
    if i - 1 >= 0 and j >= 0 and (list1[i - 1][j] == "W" or list1[i - 1][j] == "B"):
        if i - 2 >= 0 and j >= 0 and (list1[i - 2][j] != "W" and list1[i - 2][j] != "B"):
            if [i - 2, j] not in extra1:
                extra1.append([i - 2, j])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i - 2, j)): ["J", extra1]})
                search(i - 2, j, i, j, extra1[:])

    extra1 = extra11[:]
    if i - 1 >= 0 and 0 <= j + 1 < 16 and (list1[i - 1][j + 1] == "W" or list1[i - 1][j + 1] == "B"):
        if i - 2 >= 0 and 0 <= j + 2 < 16 and (list1[i - 2][j + 2] != "W" and list1[i - 2][j + 2] != "B"):
            if [i - 2, j + 2] not in extra1:
                extra1.append([i - 2, j + 2])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i - 2, j + 2)): ["J", extra1]})
                search(i - 2, j + 2, i, j, extra1[:])

    extra1 = extra11[:]
    if 0 <= i + 1 < 16 and 0 <= j + 1 < 16 and (list1[i + 1][j + 1] == "W" or list1[i + 1][j + 1] == "B"):
        if 0 <= i + 2 < 16 and 0 <= j + 2 < 16 and (list1[i + 2][j + 2] != "W" and list1[i + 2][j + 2] != "B"):
            if [i + 2, j + 2] not in extra1:
                extra1.append([i + 2, j + 2])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i + 2, j + 2)): ["J", extra1]})
                search(i + 2, j + 2, i, j, extra1[:])

    extra1 = extra11[:]
    if 0 <= i + 1 < 16 and j - 1 >= 0 and (list1[i + 1][j - 1] == "W" or list1[i + 1][j - 1] == "B"):
        if 0 <= i + 2 < 16 and j - 2 >= 0 and (list1[i + 2][j - 2] != "W" and list1[i + 2][j - 2] != "B"):
            if [i + 2, j - 2] not in extra1:
                extra1.append([i + 2, j - 2])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i + 2, j - 2)): ["J", extra1]})
                search(i + 2, j - 2, i, j, extra1[:])

    extra1 = extra11[:]
    if i - 1 >= 0 and j - 1 >= 0 and (list1[i - 1][j - 1] == "W" or list1[i - 1][j - 1] == "B"):
        if i - 2 >= 0 and j - 2 >= 0 and (list1[i - 2][j - 2] != "W" and list1[i - 2][j - 2] != "B"):
            if [i - 2, j - 2] not in extra1:
                extra1.append([i - 2, j - 2])
                ip1 = extra1[0][0]
                jp1 = extra1[0][1]
                relation.update({((ip1, jp1), (i - 2, j - 2)): ["J", extra1]})
                search(i - 2, j - 2, i, j, extra1[:])


def Generate_neighbour(col):
    if col == "WHITE":
        relation.clear()
        parent_child.clear()
        for k in W_dict.keys():
            i = k[0]
            j = k[1]
            search_neighbour(i, j, 0)

    if col == "BLACK":
        relation.clear()
        parent_child.clear()
        for k in B_dict.keys():
            i = k[0]
            j = k[1]
            search_neighbour(i, j, 0)
        # print(relation)
        # print(parent_child)

def for_path(move):

    output = allmoves[move]

    out_str = ""
    if output[0] == "E":

        out_str = str(output[0]) + " " + str(move[0][1]) + "," + str(move[0][0]) + " " + str(move[1][1]) + "," + str(move[1][0])
    else:
        for iter_r in range(len(output[1]) - 1):
            if output[1][iter_r][0] == move[1][0] and output[1][iter_r][1] == move[1][1]:
                break;
            else:
                out_str += str(output[0]) + " " + str(output[1][iter_r][1]) + "," + str(output[1][iter_r][0]) + " "
                out_str += str(output[1][iter_r + 1][1]) + "," + str(output[1][iter_r + 1][0])
                if output[1][iter_r + 1][0] != move[0][0] or output[1][iter_r + 1][1] != move[0][1]:
                    out_str += "\n"
    print(out_str)
    out_file = open('output.txt','w',encoding='utf-8')
    out_file.write(out_str)
    out_file.close()

def minmax(aa, bb, aaa, bbb,alpha,beta):

    getreport()
    goal_pos_x = 15
    goal_pos_y = 15
    if list1[15][15] == "B":
        goal_pos_x = 15
        goal_pos_y = 14
        if list1[15][14] == "B":
            goal_pos_x = 14
            goal_pos_y = 14
            if list1[14][14] == "B":
                goal_pos_x = 13
                goal_pos_y = 14
                if list1[13][14] == "B":
                    goal_pos_x = 12
                    goal_pos_y = 14
                    if list1[12][14] == "B":
                        goal_pos_x = 11
                        goal_pos_y = 14
                        if list1[11][14] == "B":
                            goal_pos_x = 13
                            goal_pos_y = 12
                            if list1[13][12] == "B":
                                goal_pos_x = 14
                                goal_pos_y = 12
                                if list1[14][12] == "B":
                                    goal_pos_x = 15
                                    goal_pos_y = 12
                                    if list1[15][12] == "B":
                                        goal_pos_x = 13
                                        goal_pos_y = 15
                                        if list1[13][15] == "B":
                                            goal_pos_x = 14
                                            goal_pos_y = 15
                                            if list1[14][15] == "B":
                                                goal_pos_x = 12
                                                goal_pos_y = 15
                                                if list1[12][15] == "B":
                                                    goal_pos_x = 11
                                                    goal_pos_y = 15
                                                    if list1[11][15] == "B":
                                                        goal_pos_x = 12
                                                        goal_pos_y = 13
                                                        if list1[12][13] == "B":
                                                            goal_pos_x = 14
                                                            goal_pos_y = 13
                                                            if list1[14][13] == "B":
                                                                goal_pos_x = 15
                                                                goal_pos_y = 13
                                                                if list1[15][13] == "B":
                                                                    goal_pos_x = 13
                                                                    goal_pos_y = 13
                                                                    if list1[13][13] == "B":
                                                                        goal_pos_x = 15
                                                                        goal_pos_y = 11
                                                                        if list1[15][11] == "B":
                                                                            goal_pos_x = 14
                                                                            goal_pos_y = 11
                                                                            if list1[14][11] == "B":
                                                                                return 0



    list1[aa][bb] = "."
    list1[aaa][bbb] = "B"
    # print("before",list1)
    getreport()
    leaf.clear()
    Generate_neighbour("WHITE")
    allmoves = parent_child.copy()
    allmoves.update(relation)

    for ii in allmoves.keys():
        a = ii[0][0]
        b = ii[0][1]
        c = ii[1][0]
        d = ii[1][1]
        list1[a][b] = "."
        list1[c][d] = "W"
        getreport()
        if alpha >= beta:
            # print("in pruning condition")
            flag = 32;
            list1[a][b] = "W"
            list1[c][d] = "."
            list1[aa][bb] = "B"
            list1[aaa][bbb] = "."
            break;
        for i in W_dict:
            aa1 = i[0]
            bb1 = i[1]
            dis = math.sqrt((aa1 - 0) ** 2 + (bb1 - 0) ** 2)
            distance.update({(aa1, bb1): dis})
        for i in B_dict:
            aa1 = i[0]
            bb1 = i[1]
            dis = math.sqrt((aa1 - goal_pos_x) ** 2 + (bb1 - goal_pos_y) ** 2)
            distance1.update({(aa1, bb1): dis})
        dis1 = math.sqrt((aaa-goal_pos_x)**2 + (bbb-goal_pos_y)**2)
        final_diss = (sum(distance.values()) - sum(distance1.values()))
        temp_value1 = final_diss
        if temp_value1 < beta:
            beta = temp_value1
        leaf.update({((aaa, bbb), (a, b)): (final_diss)})
        distance.clear()
        distance1.clear()
        list1[a][b] = "W"
        list1[c][d] = "."
    list1[aa][bb] = "B"
    list1[aaa][bbb] = "."
    # print("every time",list1)

    return leaf, alpha, beta


def start():
    allmoves = parent_child.copy()
    allmoves.update(relation)
    for q in allmoves.keys():
        getreport()
        fl = 0
        if list1[15][15] == "B":
            fl = 1
            if q[0] == (15,15):
                goal_dic.update({(15,15) : 1})
        if list1[15][14] == "B" and fl == 1:
            fl = 2
            if q[0] == (15, 14):
                goal_dic.update({(15, 14): 1})
        if list1[14][14] == "B" and fl == 2:
            fl = 3
            if q[0] == (14, 14):
                goal_dic.update({(14, 14): 1})
        if list1[13][14] == "B" and fl == 3:
            fl = 4
            if q[0] == (13, 14):
                 goal_dic.update({(13, 14): 1})
        if list1[12][14] == "B" and fl == 4:
            fl = 5
            if q[0] == (12, 14):
                goal_dic.update({(12, 14): 1})
        if list1[11][14] == "B" and fl == 5:
            fl = 6
            if q[0] == (11, 14):
                goal_dic.update({(11, 14): 1})
        if list1[13][12] == "B" and fl == 6:
            fl = 7
            if q[0] == (13, 12):
                goal_dic.update({(13, 12): 1})
        if list1[14][12] == "B" and fl == 7:
            fl = 8
            if q[0] == (14, 12):
                goal_dic.update({(14, 12): 1})
        if list1[15][12] == "B" and fl == 8:
            fl = 9
            if q[0] == (15, 12):
                goal_dic.update({(15, 12): 1})
        if list1[13][15] == "B" and fl == 9:
            fl = 10
            if q[0] == (13, 15):
                goal_dic.update({(13, 15): 1})
        if list1[14][15] == "B" and fl == 10:
            fl = 11
            if q[0] == (14, 15):
                goal_dic.update({(14, 15): 1})
        if list1[12][15] == "B" and fl == 11:
            fl = 12
            if q[0] == (12, 15):
                goal_dic.update({(12, 15): 1})
        if list1[11][15] == "B" and fl == 12:
            fl = 13
            if q[0] == (11, 15):
                goal_dic.update({(11, 15): 1})
        if list1[12][13] == "B" and fl == 13:
            fl = 14
            if q[0] == (12, 13):
                goal_dic.update({(12, 13): 1})
        if list1[14][13] == "B" and fl == 14:
            fl = 15
            if q[0] == (14, 13):
                goal_dic.update({(14, 13): 1})
        if list1[15][13] == "B" and fl == 15:
            fl = 16
            if q[0] == (15, 13):
                goal_dic.update({(15, 13): 1})
        if list1[13][13] == "B" and fl == 16:
            fl = 17
            if q[0] == (13, 13):
                goal_dic.update({(13, 13): 1})
        if list1[15][11] == "B" and fl == 17:
            fl = 18
            if q[0] == (15, 11):
                goal_dic.update({(15, 11): 1})
        if list1[14][11] == "B" and fl == 18:
            fl = 19
            if q[0] == (14, 11):
                goal_dic.update({(14, 11): 1})
    alpha = -5000000
    beta = 5000000
    for i in allmoves.keys():
        if i[0] not in goal_dic.keys():

            # print(i)
            aa = i[0][0]
            bb = i[0][1]
            aaa = i[1][0]
            bbb = i[1][1]
            # print(aa,bb,aaa,bbb)
            ans, alpha1, beta1 = minmax(aa, bb, aaa, bbb, alpha, beta)
            final_dic_at_leaf.update(ans)
            # print("final dic",final_dic_at_leaf)
            # print(final_dic_at_leaf)
            alpha = max(alpha1, alpha, beta1)
            final_dic_at_leaf.update(ans)
            r1 = min(final_dic_at_leaf.values())
            for key in final_dic_at_leaf.keys():
                if final_dic_at_leaf[key] == r1:
                    r2 = key
                    break;
            if (aa, bb) in in_triangle_B.keys() and (r2[0]) in in_triangle_B.keys() :
                if aa <= r2[0][0] and bb <= r2[0][1]:
                    con = -1
                    r1 = r1 + in_triangle_B[r2[0]]
                else:
                    con = -23
            elif (aa, bb) in in_triangle_B.keys() and (r2[0]) not in in_triangle_B.keys():
                con = 1
            elif (aa, bb) not in in_triangle_B.keys() and (r2[0]) not in in_triangle_B.keys():
                con = 0
            elif (aa, bb) not in in_triangle_B.keys() and (r2[0]) in in_triangle_B.keys():
                con = -22
            final_dic_at_leaf2.update({((aa, bb), r2[0], r2[1], 10): [con, r1]})

            # print(final_dic_at_leaf2)
            # print("this is final",final_dic_at_leaf2)
            final_dic_at_leaf.clear()

    return final_dic_at_leaf2


if color[0] == "BLACK":
    if (mode[0] == "GAME"):
        getreport()
        Generate_neighbour(color[0])
        final_list = start()

        for k in final_list.keys():
            if final_list[k][0] == 1:
                inout_dic.update({k: [1, final_list[k][1]]})
            elif final_list[k][0] == 0:
                outout_dic.update({k: [0, final_list[k][1]]})
            elif final_list[k][0] == -1:
                inin_dic.update({k: [-1, final_list[k][1]]})

        # print("inin",inin_dic)
        # print("inout",inout_dic)
        # print("outout",outout_dic)
        # print(inin_dic)
        if inout_dic != {}:
            r10 = max(inout_dic.values())
            for key1 in inout_dic.keys():
                if inout_dic[key1] == r10:
                    locate = key1
                    break;
            getreport()
            Generate_neighbour("BLACK")
            allmoves = parent_child.copy()
            allmoves.update(relation)
            locate1 = locate[0]
            locate2 = locate[1]

            location = (locate1, locate2)
            for_path(location)

        elif inin_dic != {}:

            r11 = max(inin_dic.values())
            for key1 in inin_dic.keys():
                if inin_dic[key1] == r11:
                    locate1 = key1
                    break;
            getreport()
            Generate_neighbour("BLACK")
            allmoves = parent_child.copy()
            allmoves.update(relation)
            locate11 = locate1[0]
            locate22 = locate1[1]

            location = (locate11, locate22)
            for_path(location)

        else:
            r12 = max(outout_dic.values())
            for key1 in outout_dic.keys():
                if outout_dic[key1] == r12:
                    locate21 = key1
                    break;
            getreport()
            Generate_neighbour("BLACK")
            allmoves = parent_child.copy()
            allmoves.update(relation)
            locate111 = locate21[0]
            locate222 = locate21[1]

            location = (locate111, locate222)
            for_path(location)



# __________________________________________________________________________________________________________________________________________


def minmax1(aa, bb, aaa, bbb,alpha,beta):
    getreport()
    goal_pos_x = 0
    goal_pos_y = 0
    if list1[0][0] == "W":
        goal_pos_x = 1
        goal_pos_y = 0
        if list1[1][0] == "W":
            goal_pos_x = 1
            goal_pos_y = 1
            if list1[1][1] == "W":
                goal_pos_x = 1
                goal_pos_y = 2
                if list1[1][2] == "W":
                    goal_pos_x = 1
                    goal_pos_y = 3
                    if list1[1][3] == "W":
                        goal_pos_x = 1
                        goal_pos_y = 4
                        if list1[1][4] == "W":
                            goal_pos_x = 3
                            goal_pos_y = 2
                            if list1[3][2] == "W":
                                goal_pos_x = 3
                                goal_pos_y = 1
                                if list1[3][1] == "W":
                                    goal_pos_x = 3
                                    goal_pos_y = 0
                                    if list1[3][0] == "W":
                                        goal_pos_x = 0
                                        goal_pos_y = 2
                                        if list1[0][2] == "W":
                                            goal_pos_x = 0
                                            goal_pos_y = 1
                                            if list1[0][1] == "W":
                                                goal_pos_x = 0
                                                goal_pos_y = 3
                                                if list1[0][3] == "W":
                                                    goal_pos_x = 0
                                                    goal_pos_y = 4
                                                    if list1[0][4] == "W":
                                                        goal_pos_x = 2
                                                        goal_pos_y = 3
                                                        if list1[2][3] == "W":
                                                            goal_pos_x = 2
                                                            goal_pos_y = 1
                                                            if list1[2][1] == "W":
                                                                goal_pos_x = 2
                                                                goal_pos_y = 0
                                                                if list1[2][0] == "W":
                                                                    goal_pos_x = 2
                                                                    goal_pos_y = 2
                                                                    if list1[2][2] == "W":
                                                                        goal_pos_x = 4
                                                                        goal_pos_y = 0
                                                                        if list1[4][0] == "W":
                                                                            goal_pos_x = 4
                                                                            goal_pos_y = 1
                                                                            if list1[14][11] == "W":
                                                                                return 0



    list1[aa][bb] = "."
    list1[aaa][bbb] = "W"
    # print("before",list1)
    getreport()
    leaf.clear()
    Generate_neighbour("BLACK")
    allmoves = parent_child.copy()
    allmoves.update(relation)

    for ii in allmoves.keys():
        a = ii[0][0]
        b = ii[0][1]
        c = ii[1][0]
        d = ii[1][1]
        list1[a][b] = "."
        list1[c][d] = "B"
        getreport()
        if alpha >= beta:
            # print("in pruning condition")
            flag = 32;
            list1[a][b] = "B"
            list1[c][d] = "."
            list1[aa][bb] = "W"
            list1[aaa][bbb] = "."
            break;
        for i in W_dict:
            aa1 = i[0]
            bb1 = i[1]
            dis = math.sqrt((aa1 - goal_pos_x) ** 2 + (bb1 - goal_pos_y) ** 2)
            distance1.update({(aa1, bb1): dis})
        for i in B_dict:
            aa1 = i[0]
            bb1 = i[1]
            dis = math.sqrt((aa1 - 15) ** 2 + (bb1 - 15) ** 2)
            distance.update({(aa1, bb1): dis})
        dis1 = math.sqrt((aaa - goal_pos_x) ** 2 + (bbb - goal_pos_y) ** 2)
        final_diss = (sum(distance.values()) - sum(distance1.values()))
        temp_value1 = final_diss
        if temp_value1 < beta:
            beta = temp_value1
        # dis1 = math.sqrt((aaa - goal_pos_x) ** 2 + (bbb - goal_pos_y) ** 2)
        leaf.update({((aaa, bbb), (a, b)): final_diss})
        distance.clear()
        distance1.clear()
        list1[a][b] = "B"
        list1[c][d] = "."
    list1[aa][bb] = "W"
    list1[aaa][bbb] = "."
    # print("every time",list1)

    return leaf, alpha, beta


def start1():
    allmoves = parent_child.copy()
    allmoves.update(relation)

    for q in allmoves.keys():
        getreport()
        fl = 0
        if list1[0][0] == "W":
            fl = 1
            if q[0] == (0,0):
                goal_dic.update({(0,0) : 1})
        if list1[1][0] == "W" and fl == 1:
            fl = 2
            if q[0] == (1, 0):
                goal_dic.update({(1, 0): 1})
        if list1[1][1] == "W" and fl == 2:
            fl = 3
            if q[0] == (1, 1):
                goal_dic.update({(1, 1): 1})
        if list1[1][2] == "W" and fl == 3:
            fl = 4
            if q[0] == (1, 2):
                 goal_dic.update({(1, 2): 1})
        if list1[1][3] == "W" and fl == 4:
            fl = 5
            if q[0] == (1, 3):
                goal_dic.update({(1, 3): 1})
        if list1[1][4] == "W" and fl == 5:
            fl = 6
            if q[0] == (1, 4):
                goal_dic.update({(1, 4): 1})
        if list1[3][2] == "W" and fl == 6:
            fl = 7
            if q[0] == (3, 2):
                goal_dic.update({(3, 2): 1})
        if list1[3][1] == "W" and fl == 7:
            fl = 8
            if q[0] == (3, 1):
                goal_dic.update({(3, 1): 1})
        if list1[3][0] == "W" and fl == 8:
            fl = 9
            if q[0] == (3, 0):
                goal_dic.update({(3, 0): 1})
        if list1[0][2] == "W" and fl == 9:
            fl = 10
            if q[0] == (0, 2):
                goal_dic.update({(0, 2): 1})
        if list1[0][1] == "W" and fl == 10:
            fl = 11
            if q[0] == (0, 1):
                goal_dic.update({(0, 1): 1})
        if list1[0][3] == "W" and fl == 11:
            fl = 12
            if q[0] == (0, 3):
                goal_dic.update({(0, 3): 1})
        if list1[0][4] == "W" and fl == 12:
            fl = 13
            if q[0] == (0, 4):
                goal_dic.update({(0, 4): 1})
        if list1[2][3] == "W" and fl == 13:
            fl = 14
            if q[0] == (2, 3):
                goal_dic.update({(2, 3): 1})
        if list1[2][1] == "W" and fl == 14:
            fl = 15
            if q[0] == (2,1):
                goal_dic.update({(2, 1): 1})
        if list1[2][0] == "W" and fl == 15:
            fl = 16
            if q[0] == (2, 0):
                goal_dic.update({(2, 0): 1})
        if list1[2][2] == "W" and fl == 16:
            fl = 17
            if q[0] == (2, 2):
                goal_dic.update({(2, 2): 1})
        if list1[4][0] == "W" and fl == 17:
            fl = 18
            if q[0] == (4, 0):
                goal_dic.update({(4, 0): 1})
        if list1[4][1] == "W" and fl == 18:
            fl = 19
            if q[0] == (4, 1):
                goal_dic.update({(4, 1): 1})
    alpha = -5000
    beta = 5000

    getreport()

    for i in allmoves.keys():

        if i[0] not in goal_dic.keys():

            aa = i[0][0]
            bb = i[0][1]
            aaa = i[1][0]
            bbb = i[1][1]
            # print(aa,bb,aaa,bbb)
            ans, alpha1, beta1 = minmax1(aa, bb, aaa, bbb, alpha, beta)
            final_dic_at_leaf.update(ans)
            # print("final dic",final_dic_at_leaf)
            # print(final_dic_at_leaf)
            alpha = max(alpha1, alpha, beta1)
            final_dic_at_leaf.update(ans)
            r1 = min(final_dic_at_leaf.values())
            for key in final_dic_at_leaf.keys():
                if final_dic_at_leaf[key] == r1:
                    r2 = key
                    break;
            if (aa, bb) in in_triangle_W.keys() and (r2[0]) in in_triangle_W.keys() :
                if aa>= r2[0][0] and bb >= r2[0][1]:
                    con = -1
                    r1 = r1 + in_triangle_W[r2[0]] * -1
                else:
                    con = -23
            elif (aa, bb) in in_triangle_W.keys() and (r2[0]) not in in_triangle_W.keys():
                con = 1
            elif (aa, bb) not in in_triangle_W.keys() and (r2[0]) not in in_triangle_W.keys():
                con = 0
            elif (aa, bb) not in in_triangle_W.keys() and (r2[0]) in in_triangle_W.keys():
                con = -22
            final_dic_at_leaf2.update({((aa, bb), r2[0], r2[1], 10): [con, r1]})
            # print("this is final",final_dic_at_leaf2)
            # print(final_dic_at_leaf2)
            # print("this is final",final_dic_at_leaf2)
            final_dic_at_leaf.clear()
    return final_dic_at_leaf2
        # print(i)


if color[0] == "WHITE":
    if (mode[0] == "GAME"):
        getreport()
        Generate_neighbour(color[0])
        final_list12 = start1()

        for k in final_list12.keys():
            if final_list12[k][0] == 1:
                inout_dic.update({k: [1, final_list12[k][1]]})
            elif final_list12[k][0] == 0:
                outout_dic.update({k: [0, final_list12[k][1]]})
            elif final_list12[k][0] == -1:
                inin_dic.update({k: [-1, final_list12[k][1]]})

        # print("inin",inin_dic)
        # print("inout",inout_dic)
        # print("outout",outout_dic)
        # print("inin",inin_dic)
        if inout_dic != {}:
            r10 = max(inout_dic.values())
            for key1 in inout_dic.keys():
                if inout_dic[key1] == r10:
                    locate = key1
                    break;
            getreport()
            Generate_neighbour("WHITE")
            allmoves = parent_child.copy()
            allmoves.update(relation)
            locate1 = locate[0]
            locate2 = locate[1]

            location = (locate1, locate2)
            for_path(location)

        elif inin_dic != {}:

            r11 = max(inin_dic.values())
            for key1 in inin_dic.keys():
                if inin_dic[key1] == r11:
                    locate1 = key1
                    break;
            getreport()
            Generate_neighbour("WHITE")
            allmoves = parent_child.copy()
            allmoves.update(relation)
            locate11 = locate1[0]
            locate22 = locate1[1]

            location = (locate11, locate22)
            for_path(location)

        else:
            r12 = max(outout_dic.values())
            for key1 in outout_dic.keys():
                if outout_dic[key1] == r12:
                    locate21 = key1
                    break;
            getreport()
            Generate_neighbour("WHITE")
            allmoves = parent_child.copy()
            allmoves.update(relation)
            locate111 = locate21[0]
            locate222 = locate21[1]

            location = (locate111, locate222)
            for_path(location)


if mode[0] == "SINGLE":

    list1 = []
    list2 = []
    list1_pos = ""
    parent_child = {}
    B_dict = {}
    W_dict = {}
    relation = {}
    oldextra = []
    allmoves = {}
    relation_updated = {}
    parent_child_updated = {}
    leaf = {}
    final_dis = 0
    final_dic_at_leaf = {}
    final_dic_at_leaf2 = {}
    inout_dic = {}
    inin_dic = {}
    outout_dic = {}
    distance = {}
    goal_dic = {}
    distance1 = {}
    final_list2 = {}
    best_move = []
    best_move_inin = []
    best_move_outout = []
    evalution_dic_J_inout = {}
    evalution_dic_E_inout = {}
    evalution_dic_J_inin = {}
    evalution_dic_E_inin = {}
    evalution_dic_J_outout = {}
    evalution_dic_E_outout = {}
    dis_dic = {}
    in_triangle_B = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (1, 0): 1, (1, 1): 1, (1, 2): 1, (1, 3): 1,
                     (1, 4): 1, (2, 0): 1, (2, 1): 1, (2, 2): 1, (2, 3): 1, (3, 0): 1, (3, 1): 1, (3, 2): 1, (4, 0): 1,
                     (4, 1): 1}

    in_triangle_W = {(11, 14): 1, (11, 15): 1, (12, 13): 1, (12, 14): 1, (12, 15): 1, (13, 12): 1, (13, 13): 1,
                     (13, 14): 1,
                     (13, 15): 1, (14, 11): 1, (14, 12): 1, (14, 13): 1, (14, 14): 1, (14, 15): 1, (15, 11): 1,
                     (15, 12): 1,
                     (15, 13): 1, (15, 14): 1, (15, 15): 1}


    n = -1

    White_i_des = 15
    White_j_des = 15
    Black_i_des = 0
    Black_j_des = 0
    f = open("input.txt", "r")

    # Mode
    mode = (f.readline()).split()


    # Color
    color = (f.readline()).split()


    # Time
    Time = (f.readline()).split()

    # for iter2 in range(16):
    #     list1_pos = f.readline().split()
    #     x = list1_pos[0]
    #     print(x)
    #     bm = [x[j] for j in range(0,len(x))]
    #     list1.append(bm)
    #     print(list1)

    for iter2 in range(16):
        list1_pos = f.readline().rstrip('\n')
        results1 = [i for i in list1_pos]
        list1.append(results1)


    # if (mode == )
    def getreport():
        B_dict.clear()
        W_dict.clear()

        for i in range(16):
            for j in range(16):
                if list1[i][j] == "W":
                    W_dict.update({(i, j): 1})
                elif list1[i][j] == "B":
                    B_dict.update({(i, j): 1})
        flag = 0


    def search_neighbour(i, j, flag):
        extra = [[i, j]]

        if 0 <= j + 1 < 16 and i >= 0 and (list1[i][j + 1] != "W" and list1[i][j + 1] != "B"):
            parent_child.update({((i, j), (i, j + 1)): ['E', [[i, j], [i, j + 1]]]})
        if 0 <= j + 1 < 16 and i >= 0 and (list1[i][j + 1] == "W" or list1[i][j + 1] == "B"):
            if 0 <= j + 2 < 16 and i >= 0 and (list1[i][j + 2] != "W" and list1[i][j + 2] != "B"):
                extra.append([i, j + 2])
                relation.update({((i, j), (i, j + 2)): ["J", extra]})
                search(i, j + 2, i, j, extra[:])

        extra = [[i, j]]

        if i >= 0 and j - 1 >= 0 and (list1[i][j - 1] != "W" and list1[i][j - 1] != "B"):
            parent_child.update({((i, j), (i, j - 1)): ['E', [[i, j], [i, j - 1]]]})
        if i >= 0 and j - 1 >= 0 and (list1[i][j - 1] == "W" or list1[i][j - 1] == "B"):
            if i >= 0 and j - 2 >= 0 and (list1[i][j - 2] != "W" and list1[i][j - 2] != "B"):
                extra.append([i, j - 2])
                relation.update({((i, j), (i, j - 2)): ["J", extra]})
                search(i, j - 2, i, j, extra[:])

        extra = [[i, j]]
        if 0 <= i + 1 < 16 and j >= 0 and (list1[i + 1][j] != "W" and list1[i + 1][j] != "B"):
            parent_child.update({((i, j), (i + 1, j)): ['E', [[i, j], [i + 1, j]]]})
        if 0 <= i + 1 < 16 and j >= 0 and (list1[i + 1][j] == "W" or list1[i + 1][j] == "B"):
            if 0 <= i + 2 < 16 and j >= 0 and (list1[i + 2][j] != "W" and list1[i + 2][j] != "B"):
                extra.append([i + 2, j])
                relation.update({((i, j), (i + 2, j)): ["J", extra]})
                search(i + 2, j, i, j, extra[:])

        extra = [[i, j]]
        if i - 1 >= 0 and j >= 0 and (list1[i - 1][j] != "W" and list1[i - 1][j] != "B"):
            parent_child.update({((i, j), (i - 1, j)): ['E', [[i, j], [i - 1, j]]]})
        if i - 1 >= 0 and j >= 0 and (list1[i - 1][j] == "W" or list1[i - 1][j] == "B"):
            if i - 2 >= 0 and j >= 0 and (list1[i - 2][j] != "W" and list1[i - 2][j] != "B"):
                extra.append([i - 2, j])
                relation.update({((i, j), (i - 2, j)): ["J", extra]})
                search(i - 2, j, i, j, extra[:])

        extra = [[i, j]]
        if i - 1 >= 0 and 0 <= j + 1 < 16 and (list1[i - 1][j + 1] != "W" and list1[i - 1][j + 1] != "B"):
            parent_child.update({((i, j), (i - 1, j + 1)): ['E', [[i, j], [i - 1, j + 1]]]})
        if i - 1 >= 0 and 0 <= j + 1 < 16 and (list1[i - 1][j + 1] == "W" or list1[i - 1][j + 1] == "B"):
            if i - 2 >= 0 and 0 <= j + 2 < 16 and (list1[i - 2][j + 2] != "W" and list1[i - 2][j + 2] != "B"):
                extra.append([i - 2, j + 2])
                relation.update({((i, j), (i - 2, j + 2)): ["J", extra]})
                search(i - 2, j + 2, i, j, extra[:])

        extra = [[i, j]]
        if 0 <= i + 1 < 16 and 0 <= j + 1 < 16 and (list1[i + 1][j + 1] != "W" and list1[i + 1][j + 1] != "B"):
            parent_child.update({((i, j), (i + 1, j + 1)): ['E', [[i, j], [i + 1, j + 1]]]})
        if 0 <= i + 1 < 16 and 0 <= j + 1 < 16 and (list1[i + 1][j + 1] == "W" or list1[i + 1][j + 1] == "B"):
            if 0 <= i + 2 < 16 and 0 <= j + 2 < 16 and (list1[i + 2][j + 2] != "W" and list1[i + 2][j + 2] != "B"):
                extra.append([i + 2, j + 2])
                relation.update({((i, j), (i + 2, j + 2)): ["J", extra]})
                search(i + 2, j + 2, i, j, extra[:])

        extra = [[i, j]]
        if 0 <= i + 1 < 16 and j - 1 >= 0 and (list1[i + 1][j - 1] != "W" and list1[i + 1][j - 1] != "B"):
            parent_child.update({((i, j), (i + 1, j - 1)): ['E', [[i, j], [i + 1, j - 1]]]})
        if 0 <= i + 1 < 16 and j - 1 >= 0 and (list1[i + 1][j - 1] == "W" or list1[i + 1][j - 1] == "B"):
            if 0 <= i + 2 < 16 and j - 2 >= 0 and (list1[i + 2][j - 2] != "W" and list1[i + 2][j - 2] != "B"):
                extra.append([i + 2, j - 2])
                relation.update({((i, j), (i + 2, j - 2)): ["J", extra]})
                search(i + 2, j - 2, i, j, extra[:])

        extra = [[i, j]]
        if i - 1 >= 0 and j - 1 >= 0 and (list1[i - 1][j - 1] != "W" and list1[i - 1][j - 1] != "B"):
            parent_child.update({((i, j), (i - 1, j - 1)): ['E', [[i, j], [i - 1, j - 1]]]})
        if i - 1 >= 0 and j - 1 >= 0 and (list1[i - 1][j - 1] == "W" or list1[i - 1][j - 1] == "B"):
            if i - 2 >= 0 and j - 2 >= 0 and (list1[i - 2][j - 2] != "W" and list1[i - 2][j - 2] != "B"):
                extra.append([i - 2, j - 2])
                relation.update({((i, j), (i - 2, j - 2)): ["J", extra]})
                search(i - 2, j - 2, i, j, extra[:])


    def search(i, j, ip, jp, extra11):
        extra1 = extra11[:]
        if 0 <= j + 1 < 16 and i >= 0 and (list1[i][j + 1] == "W" or list1[i][j + 1] == "B"):
            if 0 <= j + 2 < 16 and i >= 0 and (list1[i][j + 2] != "W" and list1[i][j + 2] != "B"):
                if [i, j + 2] not in extra1:
                    extra1.append([i, j + 2])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i, j + 2)): ["J", extra1]})
                    search(i, j + 2, i, j, extra1[:])

        extra1 = extra11[:]
        if i >= 0 and j - 1 >= 0 and (list1[i][j - 1] == "W" or list1[i][j - 1] == "B"):
            if i >= 0 and j - 2 >= 0 and (list1[i][j - 2] != "W" and list1[i][j - 2] != "B"):
                if [i, j - 2] not in extra1:
                    extra1.append([i, j - 2])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i, j - 2)): ["J", extra1]})
                    search(i, j - 2, i, j, extra1[:])

        extra1 = extra11[:]
        if 0 <= i + 1 < 16 and j >= 0 and (list1[i + 1][j] == "W" or list1[i + 1][j] == "B"):
            if 0 <= i + 2 < 16 and j >= 0 and (list1[i + 2][j] != "W" and list1[i + 2][j] != "B"):
                if [i + 2, j] not in extra1:
                    extra1.append([i + 2, j])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i + 2, j)): ["J", extra1]})
                    search(i + 2, j, i, j, extra1[:])

        extra1 = extra11[:]
        if i - 1 >= 0 and j >= 0 and (list1[i - 1][j] == "W" or list1[i - 1][j] == "B"):
            if i - 2 >= 0 and j >= 0 and (list1[i - 2][j] != "W" and list1[i - 2][j] != "B"):
                if [i - 2, j] not in extra1:
                    extra1.append([i - 2, j])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i - 2, j)): ["J", extra1]})
                    search(i - 2, j, i, j, extra1[:])

        extra1 = extra11[:]
        if i - 1 >= 0 and 0 <= j + 1 < 16 and (list1[i - 1][j + 1] == "W" or list1[i - 1][j + 1] == "B"):
            if i - 2 >= 0 and 0 <= j + 2 < 16 and (list1[i - 2][j + 2] != "W" and list1[i - 2][j + 2] != "B"):
                if [i - 2, j + 2] not in extra1:
                    extra1.append([i - 2, j + 2])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i - 2, j + 2)): ["J", extra1]})
                    search(i - 2, j + 2, i, j, extra1[:])

        extra1 = extra11[:]
        if 0 <= i + 1 < 16 and 0 <= j + 1 < 16 and (list1[i + 1][j + 1] == "W" or list1[i + 1][j + 1] == "B"):
            if 0 <= i + 2 < 16 and 0 <= j + 2 < 16 and (list1[i + 2][j + 2] != "W" and list1[i + 2][j + 2] != "B"):
                if [i + 2, j + 2] not in extra1:
                    extra1.append([i + 2, j + 2])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i + 2, j + 2)): ["J", extra1]})
                    search(i + 2, j + 2, i, j, extra1[:])

        extra1 = extra11[:]
        if 0 <= i + 1 < 16 and j - 1 >= 0 and (list1[i + 1][j - 1] == "W" or list1[i + 1][j - 1] == "B"):
            if 0 <= i + 2 < 16 and j - 2 >= 0 and (list1[i + 2][j - 2] != "W" and list1[i + 2][j - 2] != "B"):
                if [i + 2, j - 2] not in extra1:
                    extra1.append([i + 2, j - 2])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i + 2, j - 2)): ["J", extra1]})
                    search(i + 2, j - 2, i, j, extra1[:])

        extra1 = extra11[:]
        if i - 1 >= 0 and j - 1 >= 0 and (list1[i - 1][j - 1] == "W" or list1[i - 1][j - 1] == "B"):
            if i - 2 >= 0 and j - 2 >= 0 and (list1[i - 2][j - 2] != "W" and list1[i - 2][j - 2] != "B"):
                if [i - 2, j - 2] not in extra1:
                    extra1.append([i - 2, j - 2])
                    ip1 = extra1[0][0]
                    jp1 = extra1[0][1]
                    relation.update({((ip1, jp1), (i - 2, j - 2)): ["J", extra1]})
                    search(i - 2, j - 2, i, j, extra1[:])


    def best_path_out1(best_move1):
        result_out = allmoves[best_move1]
        out_str = ""
        if result_out[0] == "E":

            out_str = str(result_out[0]) + " " + str(best_move1[0][1]) + "," + str(best_move1[0][0]) + " " + str(best_move1[1][1]) + "," + str(best_move1[1][0])
        else:
            for iter_r in range(len(result_out[1]) - 1):
                if result_out[1][iter_r][0] == best_move1[1][0] and result_out[1][iter_r][1] == best_move1[1][1]:
                    break;
                else:
                    out_str += str(result_out[0]) + " " + str(result_out[1][iter_r][1]) + "," + str(
                        result_out[1][iter_r][0]) + " "
                    out_str += str(result_out[1][iter_r + 1][1]) + "," + str(result_out[1][iter_r + 1][0])
                    if result_out[1][iter_r + 1][0] != best_move1[0][0] or result_out[1][iter_r + 1][1] != best_move1[0][
                        1]:
                        out_str += "\n"
        print(out_str)
        out_file = open('output.txt', 'w', encoding='utf-8')
        out_file.write(out_str)
        out_file.close()


    def Generate_neighbour(col):
        if col == "WHITE":
            relation.clear()
            parent_child.clear()
            for k in W_dict.keys():
                i = k[0]
                j = k[1]
                search_neighbour(i, j, 0)

        if col == "BLACK":
            relation.clear()
            parent_child.clear()
            for k in B_dict.keys():
                i = k[0]
                j = k[1]
                search_neighbour(i, j, 0)
            # print(relation)
            # print(parent_child)


    # One_in_Two_out

    if color[0] == "BLACK":
        def evalution_func_inout(ii, jj, ii1, jj1, value):
            if value == 1:
                distance = (ii1 - White_i_des) ** 2 + (jj1 - White_j_des) ** 2
                evalution_dic_J_inout.update({((ii, jj), (ii1, jj1)): distance})
            if value == 0:
                distance = (ii1 - White_i_des) ** 2 + (jj1 - White_j_des) ** 2
                evalution_dic_E_inout.update({((ii, jj), (ii1, jj1)): distance})


        if (mode[0] == "SINGLE"):
            getreport()
            Generate_neighbour(color[0])

            # One_in_Two_out
            for i in parent_child.keys():
                if i[0] in in_triangle_B and i[1] not in in_triangle_B:
                    best_move.append((i[0], i[1]))
                    evalution_func_inout(i[0][0], i[0][1], i[1][0], i[1][1], 0)

            # One_in_Two_out
            for i in relation.keys():
                if i[0] in in_triangle_B and i[1] not in in_triangle_B:
                    best_move.append((i[0], i[1]))
                    evalution_func_inout(i[0][0], i[0][1], i[1][0], i[1][1], 1)

            ###################################################################################

            if evalution_dic_J_inout != {}:
                key_min_J_inout = min(evalution_dic_J_inout.keys(), key=(lambda k: evalution_dic_J_inout[k]))
                temp_J = evalution_dic_J_inout[key_min_J_inout]
            else:
                temp_J = 0
            if evalution_dic_E_inout != {}:
                key_min_E_inout = min(evalution_dic_E_inout.keys(), key=(lambda k: evalution_dic_E_inout[k]))
                temp_E = evalution_dic_E_inout[key_min_E_inout]
            else:
                temp_E = 0
            if temp_J == 0 and temp_E == 0:
                final_inout = n
            elif temp_E == temp_J:
                final_inout = relation[key_min_J_inout]
            elif temp_E == 0 and temp_J != 0:
                final_inout = relation[key_min_J_inout]
            elif temp_J == 0 and temp_E != 0:
                final_inout = parent_child[key_min_E_inout]
            elif temp_E < temp_J and temp_E != 0:
                final_inout = parent_child[key_min_E_inout]
            elif temp_E > temp_J and temp_J != 0:
                final_inout = relation[key_min_J_inout]


            ###########################################################################################################################################
            # One_in_Two_in
            def evalution_func_inin(iii, jjj, iii1, jjj1, value1):
                if value1 == 1:
                    distance = (iii1 - White_i_des) ** 2 + (jjj1 - White_j_des) ** 2
                    evalution_dic_J_inin.update({((iii, jjj), (iii1, jjj1)): distance})
                if value1 == 0:
                    distance = (iii1 - White_i_des) ** 2 + (jjj1 - White_j_des) ** 2
                    evalution_dic_E_inin.update({((iii, jjj), (iii1, jjj1)): distance})


            # One_in_Two_in
            for i in parent_child.keys():
                if i[0] in in_triangle_B and i[1] in in_triangle_B and (i[0][0]<= i[1][0] and i[0][1] <= i[1][1]):
                    best_move_inin.append((i[0], i[1]))
                    evalution_func_inin(i[0][0], i[0][1], i[1][0], i[1][1], 0)

            # One_in_Two_in
            for i in relation.keys():
                if i[0] in in_triangle_B and i[1] in in_triangle_B and (i[0][0]<= i[1][0] and i[0][1] <= i[1][1]):
                    best_move_inin.append((i[0], i[1]))
                    evalution_func_inin(i[0][0], i[0][1], i[1][0], i[1][1], 1)
            #########################################################################
            if evalution_dic_J_inin != {}:
                key_min_J_inin = min(evalution_dic_J_inin.keys(), key=(lambda k: evalution_dic_J_inin[k]))
                temp_J = evalution_dic_J_inin[key_min_J_inin]
            else:
                temp_J = 0
            if evalution_dic_E_inin != {}:
                key_min_E_inin = min(evalution_dic_E_inin.keys(), key=(lambda k: evalution_dic_E_inin[k]))
                temp_E = evalution_dic_E_inin[key_min_E_inin]

            else:
                temp_E = 0

            if temp_J == 0 and temp_E == 0:
                final_inin = n
            elif temp_E == temp_J:
                final_inin = relation[key_min_J_inin]
            elif temp_E == 0 and temp_J != 0:
                final_inin = relation[key_min_J_inin]
            elif temp_J == 0 and temp_E != 0:
                final_inin = parent_child[key_min_E_inin]
            elif temp_E < temp_J and temp_E != 0:
                final_inin = parent_child[key_min_E_inin]
            elif temp_E > temp_J and temp_J != 0:
                final_inin = relation[key_min_J_inin]

            ######################################################################################################################################################
            # One_out_Two_out
            def getgoalW():
                for i in in_triangle_W.keys():
                    if list1[i[0]][i[1]] == '.':
                        ele = i
                        break;
                return ele
            goal = getgoalW()
            for i in parent_child.keys():
                if i[0] not in in_triangle_B and i[1] not in in_triangle_B and i[0] not in in_triangle_W:

                    ii = i[0][0]
                    jj = i[0][1]
                    max1 = 500
                    for j in parent_child.keys():
                        if i[0] not in in_triangle_B and i[1] not in in_triangle_B and i[0] not in in_triangle_W:
                            if ii == j[0][0] and jj == j[0][1]:
                                if ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2) < max1:
                                    max1 = ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2)
                                    parent_child_updated.clear()
                                    parent_child_updated.update({((i[0][0], i[0][1]), (j[1][0], j[1][1])): max1})
                    evalution_dic_E_outout.update(parent_child_updated)

            for i in relation.keys():
                if i[0] not in in_triangle_B and i[1] not in in_triangle_B and i[0] not in in_triangle_W:
                    ii = i[0][0]
                    jj = i[0][1]
                    max1 = 500
                    for j in relation.keys():
                        if i[0] not in in_triangle_B and i[1] not in in_triangle_B:
                            if ii == j[0][0] and jj == j[0][1]:
                                if ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2) < max1:
                                    max1 = ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2)
                                    relation_updated.clear()
                                    relation_updated.update({((i[0][0], i[0][1]), (j[1][0], j[1][1])): max1})
                    evalution_dic_J_outout.update(relation_updated)

            #########################################################################
            if evalution_dic_J_outout != {}:
                r = max(evalution_dic_J_outout.values())
                for key in evalution_dic_J_outout:
                    if evalution_dic_J_outout[key] == r:
                        key_min_J_outout = key
                        break;
                temp_J = r
            else:
                temp_J = -1

            if evalution_dic_E_outout != {}:

                r = max(evalution_dic_E_outout.values())
                for key in evalution_dic_E_outout.keys():
                    if evalution_dic_E_outout[key] == r:
                        key_min_E_outout = key
                        break;
                temp_E = r
            else:
                temp_E = -1

            if temp_J == -1 and temp_E == -1:
                final_outout = n
            elif temp_E == temp_J:
                final_outout = relation[key_min_J_outout]
            elif temp_E == -1 and temp_J != -1:
                final_outout = relation[key_min_J_outout]
            elif temp_J == -1 and temp_E != -1:
                final_outout = parent_child[key_min_E_outout]
            elif temp_E < temp_J and temp_E != -1:
                final_outout = parent_child[key_min_E_outout]
            elif temp_E > temp_J and temp_J != -1:
                final_outout = relation[key_min_J_outout]


            def priority(inin, inout, outout):

                if inin != -1 and inout != -1 and outout != -1:
                    output = inout
                elif inout != -1 and inin == -1 and outout == -1:
                    output = inout
                elif inout != -1 and inin != -1 and outout == -1:
                    output = inout
                elif inout != -1 and inin == -1 and outout != -1:
                    output = inout
                elif inout == -1 and inin != -1 and outout != -1:
                    output = inin
                elif inout == -1 and inin != -1 and outout == -1:
                    output = inin
                elif inout == -1 and inin == -1 and outout != -1:
                    output = outout
                return output

            allmoves = parent_child.copy()
            allmoves.update(relation)
            ans = priority(final_inin, final_inout, final_outout)

            for i in allmoves.keys():
                if allmoves[i] == ans:
                    best_path_out1(i)
                    break;


    if color[0] == "WHITE":
        if (mode[0] == "SINGLE"):
            getreport()
            Generate_neighbour(color[0])


            def evalution_func_inout(ii, jj, ii1, jj1, value):
                if value == 1:
                    distance = (ii1 - Black_i_des) ** 2 + (jj1 - Black_j_des) ** 2
                    evalution_dic_J_inout.update({((ii, jj), (ii1, jj1)): distance})
                if value == 0:
                    distance = (ii1 - Black_i_des) ** 2 + (jj1 - Black_j_des) ** 2
                    evalution_dic_E_inout.update({((ii, jj), (ii1, jj1)): distance})

            # One_in_Two_out
            for i in parent_child.keys():
                if i[0] in in_triangle_W and i[1] not in in_triangle_W:
                    best_move.append((i[0], i[1]))
                    evalution_func_inout(i[0][0], i[0][1], i[1][0], i[1][1], 0)

            # One_in_Two_out
            for i in relation.keys():
                if i[0] in in_triangle_W and i[1] not in in_triangle_W:
                    best_move.append((i[0], i[1]))
                    evalution_func_inout(i[0][0], i[0][1], i[1][0], i[1][1], 1)

            ###################################################################################

            if evalution_dic_J_inout != {}:
                key_min_J_inout = min(evalution_dic_J_inout.keys(), key=(lambda k: evalution_dic_J_inout[k]))
                temp_J = evalution_dic_J_inout[key_min_J_inout]
            else:
                temp_J = 0
            if evalution_dic_E_inout != {}:
                key_min_E_inout = min(evalution_dic_E_inout.keys(), key=(lambda k: evalution_dic_E_inout[k]))
                temp_E = evalution_dic_E_inout[key_min_E_inout]
            else:
                temp_E = 0
            if temp_J == 0 and temp_E == 0:
                final_inout = n
            elif temp_E == temp_J:
                final_inout = relation[key_min_J_inout]
            elif temp_E == 0 and temp_J != 0:
                final_inout = relation[key_min_J_inout]
            elif temp_J == 0 and temp_E != 0:
                final_inout = parent_child[key_min_E_inout]
            elif temp_E < temp_J and temp_E != 0:
                final_inout = parent_child[key_min_E_inout]
            elif temp_E > temp_J and temp_J != 0:
                final_inout = relation[key_min_J_inout]


            ###########################################################################################################################################
            # One_in_Two_in
            def evalution_func_inin(iii, jjj, iii1, jjj1, value1):
                if value1 == 1:
                    distance = (iii1 - Black_i_des) ** 2 + (jjj1 - Black_j_des) ** 2
                    evalution_dic_J_inin.update({((iii, jjj), (iii1, jjj1)): distance})
                if value1 == 0:
                    distance = (iii1 - Black_i_des) ** 2 + (jjj1 - Black_j_des) ** 2
                    evalution_dic_E_inin.update({((iii, jjj), (iii1, jjj1)): distance})


            # One_in_Two_in
            for i in parent_child.keys():

                if i[0] in in_triangle_W and i[1] in in_triangle_W and (i[0][0]<= i[1][0] and i[0][1] <= i[1][1]):
                    best_move_inin.append((i[0], i[1]))
                    evalution_func_inin(i[0][0], i[0][1], i[1][0], i[1][1], 0)

            # One_in_Two_in
            for i in relation.keys():
                if i[0] in in_triangle_W and i[1] in in_triangle_W and (i[0][0]<= i[1][0] and i[0][1] <= i[1][1]):
                    best_move_inin.append((i[0], i[1]))
                    evalution_func_inin(i[0][0], i[0][1], i[1][0], i[1][1], 1)
            #########################################################################
            if evalution_dic_J_inin != {}:
                key_min_J_inin = min(evalution_dic_J_inin.keys(), key=(lambda k: evalution_dic_J_inin[k]))
                temp_J = evalution_dic_J_inin[key_min_J_inin]
            else:
                temp_J = 0
            if evalution_dic_E_inin != {}:
                key_min_E_inin = min(evalution_dic_E_inin.keys(), key=(lambda k: evalution_dic_E_inin[k]))
                temp_E = evalution_dic_E_inin[key_min_E_inin]

            else:
                temp_E = 0

            if temp_J == 0 and temp_E == 0:
                final_inin = n
            elif temp_E == temp_J:
                final_inin = relation[key_min_J_inin]
            elif temp_E == 0 and temp_J != 0:
                final_inin = relation[key_min_J_inin]
            elif temp_J == 0 and temp_E != 0:
                final_inin = parent_child[key_min_E_inin]
            elif temp_E < temp_J and temp_E != 0:
                final_inin = parent_child[key_min_E_inin]
            elif temp_E > temp_J and temp_J != 0:
                final_inin = relation[key_min_J_inin]

            ######################################################################################################################################################
            # One_out_Two_out
            def getgoalB():
                for i in in_triangle_B.keys():
                    if list1[i[0]][i[1]] == '.':
                        ele = i
                        break;
                return ele
            goal = getgoalB()
            for i in parent_child.keys():

                if i[0] not in in_triangle_W and i[1] not in in_triangle_W and i[0] not in in_triangle_B:

                    ii = i[0][0]
                    jj = i[0][1]
                    max1 = 500
                    for j in parent_child.keys():
                        if i[0] not in in_triangle_W and i[1] not in in_triangle_W and i[0] not in in_triangle_B:
                            if ii == j[0][0] and jj == j[0][1]:
                                if ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2) < max1:
                                    max1 = ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2)
                                    parent_child_updated.clear()
                                    parent_child_updated.update({((i[0][0], i[0][1]), (j[1][0], j[1][1])): max1})
                    evalution_dic_E_outout.update(parent_child_updated)

            for i in relation.keys():

                if i[0] not in in_triangle_W and i[1] not in in_triangle_W and i[0] not in in_triangle_B:

                    ii = i[0][0]
                    jj = i[0][1]
                    max1 = 500
                    for j in relation.keys():
                        if i[0] not in in_triangle_W and i[1] not in in_triangle_W and i[0] not in in_triangle_B:
                            if ii == j[0][0] and jj == j[0][1]:
                                if ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2) < max1:

                                    max1 = ((j[1][0] - goal[0]) ** 2 + (j[1][1] - goal[1]) ** 2)


                                    relation_updated.clear()
                                    relation_updated.update({((i[0][0], i[0][1]), (j[1][0], j[1][1])): max1})
                    evalution_dic_J_outout.update(relation_updated)


            #########################################################################
            if evalution_dic_J_outout != {}:
                r = max(evalution_dic_J_outout.values())
                for key in evalution_dic_J_outout:
                    if evalution_dic_J_outout[key] == r:
                        key_min_J_outout = key
                        break;
                temp_J = r

            else:
                temp_J = -1

            if evalution_dic_E_outout != {}:

                r = max(evalution_dic_E_outout.values())
                for key in evalution_dic_E_outout.keys():
                    if evalution_dic_E_outout[key] == r:
                        key_min_E_outout = key
                        break;
                temp_E = r

            else:
                temp_E = -1

            if temp_J == -1 and temp_E == -1:
                final_outout = n

            elif temp_E == temp_J:
                final_outout = relation[key_min_J_outout]

            elif temp_E == -1 and temp_J != -1:
                final_outout = relation[key_min_J_outout]

            elif temp_J == -1 and temp_E != -1:
                final_outout = parent_child[key_min_E_outout]

            elif temp_E < temp_J and temp_E != -1:
                final_outout = parent_child[key_min_E_outout]

            elif temp_E > temp_J and temp_J != -1:
                final_outout = relation[key_min_J_outout]



            def priority(inin, inout, outout):

                if inin != -1 and inout != -1 and outout != -1:
                    output = inout
                elif inout != -1 and inin == -1 and outout == -1:
                    output = inout
                elif inout != -1 and inin != -1 and outout == -1:
                    output = inout
                elif inout != -1 and inin == -1 and outout != -1:
                    output = inout
                elif inout == -1 and inin != -1 and outout != -1:
                    output = inin
                elif inout == -1 and inin != -1 and outout == -1:
                    output = inin
                elif inout == -1 and inin == -1 and outout != -1:
                    output = outout
                return output

            allmoves = parent_child.copy()
            allmoves.update(relation)
            ans = priority(final_inin, final_inout, final_outout)
            for i in allmoves.keys():
                if allmoves[i] == ans:
                    best_path_out1(i)
                    break;











