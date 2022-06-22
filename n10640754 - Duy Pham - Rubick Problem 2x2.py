
# Functions to simulate moves interact to the Rubick
def B(pos):
    return (pos[9],  pos[10], pos[2], pos[3],
            pos[4],  pos[5], pos[6], pos[7],
            pos[8],  pos[22], pos[23], pos[11],
            pos[15],  pos[12], pos[13], pos[14],
            pos[1],  pos[17], pos[18], pos[0],
            pos[20],  pos[21], pos[19], pos[16]
            )


def Bi(pos):
    return(pos[19],  pos[16], pos[2], pos[3],
           pos[4],  pos[5], pos[6], pos[7],
           pos[8],  pos[0], pos[1], pos[11],
           pos[13],  pos[14], pos[15], pos[12],
           pos[23],  pos[17], pos[18], pos[22],
           pos[20],  pos[21], pos[9], pos[10]
           )


def D(pos):
    return(pos[0],  pos[1], pos[2], pos[3],
           pos[4],  pos[5], pos[10], pos[11],
           pos[8],  pos[9], pos[14], pos[15],
           pos[12],  pos[13], pos[18], pos[19],
           pos[16],  pos[17], pos[6], pos[7],
           pos[21],  pos[22], pos[23], pos[20]
           )


def Di(pos):
    return(pos[0],  pos[1], pos[2], pos[3],
           pos[4],  pos[5], pos[18], pos[19],
           pos[8],  pos[9], pos[6], pos[7],
           pos[12],  pos[13], pos[10], pos[11],
           pos[16],  pos[17], pos[14], pos[15],
           pos[23],  pos[20], pos[22], pos[21]
           )

def R(pos):
    return (pos[0],  pos[5], pos[6], pos[3],
            pos[4],  pos[21], pos[22], pos[7],
            pos[11],  pos[8], pos[9], pos[10],
            pos[2],  pos[13], pos[14], pos[1],
            pos[16],  pos[17], pos[18], pos[19],
            pos[20],  pos[15], pos[12], pos[23]
            )


def Ri(pos):
    return (pos[0],  pos[15], pos[12], pos[3],
            pos[4],  pos[1], pos[2], pos[7],
            pos[9],  pos[10], pos[11], pos[8],
            pos[22],  pos[13], pos[14], pos[21],
            pos[16],  pos[17], pos[18], pos[19],
            pos[20],  pos[5], pos[6], pos[23]
            )

legalMoves = {B, Bi, D, Di, R, Ri}

# method to apply moves into a cube config to find its' neighbours
def findConfigs(v):
    return {move(v) for move in legalMoves}

# Method to check if the cube config is solved or not.
def checkCubeStatus(tuple):
    cubeStatus= False
    if(
        tuple[0] == tuple[1] == tuple[2] == tuple[3] and
        tuple[4] == tuple[5] == tuple[6] == tuple[7] and
        tuple[8] == tuple[9] == tuple[10] == tuple[11] and
        tuple[12] == tuple[13] == tuple[14] == tuple[15] and
        tuple[16] == tuple[17] == tuple[18] == tuple[19] and
        tuple[20] == tuple[21] == tuple[22] == tuple[23]
    ):
        cubeStatus = True
    return cubeStatus


# Modified from graphys.py obtained from CAB203 Blackboard
def breadthFirst(u):
    D = [{u}]  # D[0] = D_0 = {u}
    if(checkCubeStatus(u)):
        return D
    return breadthFirstR(D, u)


def breadthFirstR(D, u):
    # variable to store all vertices in the current depth
    vD = set()
    for cubeConfig in D[-1]:
            vD = vD | findConfigs(cubeConfig)
    Dnew = D + [vD]# D_{j} = N_{V_j}(D_{j-1})
    for cubeConfig in Dnew[-1]:
            if checkCubeStatus(cubeConfig) == True:
                return Dnew
    return breadthFirstR(Dnew, u)

# Modified from project example.
def solution(instance):
    D = breadthFirst(instance)
    return D


def print_solution(solution):
    print(testData)
    print("Solving this cube...")
    print("Number of moves made to solve the cube: ")
    print(len(solution)-1)

testData = (
    "G", "G", "W", "O",
    "Y", "G", "O", "Y",
    "R", "Y", "W", "G",
    "R", "W", "W", "O",
    "O", "B", "B", "B",
    "R", "Y", "B", "R")

print_solution(solution(testData))
