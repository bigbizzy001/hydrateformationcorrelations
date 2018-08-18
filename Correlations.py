import math


class HFCorrelations:

    def hammerschmidt(self, p_start, p_end):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i,  round(8.9 * ((i)**0.285), 4)
            result.append([a, t])
        return result

    def bahadori_and_vuthaluru(self, p_start, p_end, g_gravity):
        A, B, C = 194.681789, 0.044232, 0.189829
        result = []

        for i in range(p_start, p_end+1):
            a, t = i, round((A*(g_gravity**B)*((math.log(i))**C)), 4)
            result.append([a, t])
        return result

    def towler_and_mokhatab(self, p_start, p_end, g_gravity):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i, round(((13.47*math.log(i)) + (34.27*math.log(g_gravity)) - (1.675*math.log(g_gravity)*math.log(i)) - 20.35), 4)
            result.append([a, t])
        return result


    def berge(self, p_start, p_end, g_gravity):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i, round((((80.61 * i) - (2.1*10**4) - (1.22 * (10**3/(g_gravity - 0.535))) -
                        (1.23*10**4) + (171 * (10**3/(g_gravity-0.509))))/(i - (-260.42) - (15.18/(g_gravity - 0.535)))), 4)
            result.append([a, t])
        return result


    def holder_et_al(self, p_start, p_end):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i, round(((-8533.80)/(math.log(i) - 38.9803)), 4)
            result.append([a, t])
        return result


    def motiee(self, p_start, p_end, g_gravity):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i, round((-238.24469 + (78.99667 * math.log(i)) - (5.352544 * (math.log(i))**2) +
                       (349.473877 * g_gravity) - (150.854675 * (g_gravity)**2) - (27.604065 * g_gravity * math.log(i))), 4)
            result.append([a, t])
        return result


    def aut(self, p_start, p_end, g_gravity):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i, round((20.928 + (13.623*math.log(i)) + (29.67 * math.log(g_gravity)) - (0.006 * i * (g_gravity**2)) +
                       (4.14 * (10**-4) * (i**2) * (g_gravity**3)) + (0.979 * math.log(i) * math.log(g_gravity)) +
                       (0.19 * i * g_gravity) + (1.25*10**-20 * i**6 * g_gravity**8) + (0.001 * (math.log(i))**5) +
                       (281.743 * (math.log(g_gravity))**7) + (1.25*10**-27 * i**8 * g_gravity**8) +
                       (7.24*10**-28 * i**8 * g_gravity**7) + (0.002 * (math.log(i))**6 * (math.log(g_gravity))**8) +
                       (1.84*10**-5 * (math.log(i))**7 * (math.log(g_gravity))**4) +
                       (0.792 * (math.log(i)) * (math.log(g_gravity))**3)), 4)
            result.append([a, t])
        return result


    def kobayashi_et_al(self, p_start, p_end, g_gravity):
        result = []
        for i in range(p_start, p_end+1):
            a, t = i, round(((-20.928 + (13.623 * math.log(g_gravity)) + (29.67 * math.log(i)) -
                                (0.006 * (math.log(g_gravity))**2) + (4.14*10**-6 * math.log(g_gravity) * math.log(i)) -
                                (0.779 * (math.log(i))**2) - (0.19 * (math.log(g_gravity))**3) -
                                (1.25*10**-20 * (math.log(g_gravity))**2 * math.log(i)) +
                                (0.001 * (math.log(i))**2 * math.log(g_gravity)) + (281.743 * (math.log(i))**3) +
                                (1.25*10**-27 * (math.log(g_gravity))**4) -
                                (7.24*10**-28 * (math.log(g_gravity))**3 * math.log(i)) +
                                (0.002 * (math.log(g_gravity))**2 * (math.log(i))**2) -
                                (1.84*10**-5 * math.log(g_gravity) * (math.log(i))**3 +
                                (0.792 * (math.log(i))**4)))), 4)
            result.append([a, t])
        return result

