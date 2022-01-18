
from functions import tilecoordytt
from functions import tilecoordybt
from functions import tiles


# The pre existing text in the file is erased
# the modified list is written into
# the file thereby replacing the old text

def updatetilestxt():
    tiles.truncate(0)
    tiles.seek(0)
    tiles.flush()

    z=""

    print(tilecoordybt[1][1])
    for s in range(len(tilecoordybt)):
        if s >0:
            z = "["
            for i in range(len(tilecoordybt[s])):
                if i < 9:
                    z = z +'"'+ tilecoordybt[s][i] +'",'
                else:
                    z = z +'"'+ tilecoordybt[s][i]+'"]'

            tiles.writelines(z + "\n")

    for s in range(len(tilecoordytt)):
        if s >0 and s < 9:
            z = "("
            for i in range(len(tilecoordytt[s])):
                if i < 9:
                    z = z +'"'+ tilecoordytt[s][i] +'",'
                else:
                    z = z +'"'+ tilecoordytt[s][i]+'")'

            tiles.writelines(z + "\n")

    tiles.writelines(tilecoordytt[9])
