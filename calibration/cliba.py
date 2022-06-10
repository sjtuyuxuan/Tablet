import numpy as np
from scipy.optimize import minimize
def fun(datas):
    def res(x):
        rtn = 0
        # rsa = np.array([[np.cos(x[4]), -np.sin(x[4])], [np.sin(x[4]), np.cos(x[4])]])
        tsa = np.array([[x[0]], [x[1]]])
        for data in datas:
            uv = 5.9259 * (np.array([[180 * np.cos(-data[0]-x[2]) + 180 * np.cos(-data[1]-x[3])],[180 * np.sin(-data[0]-x[2]) + 180 * np.sin(-data[1]-x[3])]]) + tsa)
            rtn += np.linalg.norm(np.array([uv[0, 0] - data[2], uv[1, 0] + data[3]])) ** 2
        return rtn
    return res


# datas = [[-0.071137518*2*np.pi/12.5, 1.765595375*2*np.pi/12.5, 301-640, 543-400],
# [1.41952607*2*np.pi/12.5, 2.661650715*2*np.pi/12.5, 941-640, 353-400],
# [0.617646187*2*np.pi/12.5, 2.399628697*2*np.pi/12.5, 594-640, 490-400],
# [0.568695992*2*np.pi/12.5, 1.543608723*2*np.pi/12.5, 362-640, 132-400],
# [1.892851799*2*np.pi/12.5, 2.484648762*2*np.pi/12.5, 1146-640, 142-400],
# [1.773100823*2*np.pi/12.5, 3.41751009*2*np.pi/12.5, 1103-640, 642-400],
# [-0.376616508*2*np.pi/12.5, 1.556733189*2*np.pi/12.5, 203-640, 613-400],
# #[0.601470023*2*np.pi/12.5, 2.714629231*2*np.pi/12.5, 637-640, 644-400],
# [1.317046254*2*np.pi/12.5, 2.121977864*2*np.pi/12.5, 813-640, 93-400],
# [0.181670278*2*np.pi/12.5, 1.076201497*2*np.pi/12.5, 85-640, 166-400]]

datas = [[0.19891806, 0.723233592, -358, -214],
[-0.262871546, 0.654572612, -538, 216],
[-0.014612096, 0.659326994, -501, -53],
[0.863868022, 1.441534477, 459, 0],
[0.961951712, 1.720534903, 533, 238],
[0.990881631, 1.27439193, 551, -242],
[0.548083696, 0.99895034, 46, -282],
[0.25306851, 0.723601747, -327, -272],
[0.529951084, 1.494887288, 162, 214],
[-0.071137518*2*np.pi/12.5, 1.765595375*2*np.pi/12.5, 301-640, 543-400],
[1.41952607*2*np.pi/12.5, 2.661650715*2*np.pi/12.5, 941-640, 353-400],
[0.617646187*2*np.pi/12.5, 2.399628697*2*np.pi/12.5, 594-640, 490-400],
[0.568695992*2*np.pi/12.5, 1.543608723*2*np.pi/12.5, 362-640, 132-400],
[1.892851799*2*np.pi/12.5, 2.484648762*2*np.pi/12.5, 1146-640, 142-400],
[1.773100823*2*np.pi/12.5, 3.41751009*2*np.pi/12.5, 1103-640, 642-400],
[-0.376616508*2*np.pi/12.5, 1.556733189*2*np.pi/12.5, 203-640, 613-400],
[1.317046254*2*np.pi/12.5, 2.121977864*2*np.pi/12.5, 813-640, 93-400],
[0.181670278*2*np.pi/12.5, 1.076201497*2*np.pi/12.5, 85-640, 166-400],
[0.844417145, 1.221254836, 390, -247],
[0.400085229, 0.996650328, -67, -168],
[0.215975896, 0.821531081, -273, -148]]



x0 = [-27.5774532, -173.347459,  3.419349446427077, 4.7671385367866606]
res = minimize(fun(datas), x0, method='SLSQP')
print("result is ")
print(res)


import math
dis_ = math.sqrt(27.5774374 ** 2 + 173.34744929 ** 2) 
total = np.pi - math.atan2(173.34744929, 27.5774374)
big = math.acos((dis_ * dis_) / (2 * 180 * dis_))
(total - big - 0.2774533464102067) / 2 / np.pi * 12.5


validation_data_screen = []
validation_data_projection = []
x = res.x
for data in datas:
    uv = 5.95238 * (np.array([[180 * np.cos(-data[0]-x[2]) + 180 * np.cos(-data[1]-x[3])],[180 * np.sin(-data[0]-x[2]) + 180 * np.sin(-data[1]-x[3])]]) + np.array([[x[0]], [x[1]]]))
    validation_data_screen.append(data[2:4])
    validation_data_projection.append([uv[0, 0], -uv[1, 0]])

from matplotlib import pyplot as plt
plt.scatter(np.array(validation_data_screen).T[0],np.array(validation_data_screen).T[1], color = 'blue')
plt.scatter(np.array(validation_data_projection).T[0],np.array(validation_data_projection).T[1], color = 'red')
plt.show()