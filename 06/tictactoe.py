def TicTacDraw(board):
    tictacmap={0:' O ',1:' X ',2:'   '}
    k=0
    for i in board:
        k+=1
        string=''
        for j in i:
            string+=tictacmap[j]
            string+='|'
        row=string[:-1]
        print(row)
        if k<len(board):
            print('----'*len(board))
