# aqi v1.0

class AqiCal:
    def __init__(self, pm_va, co_va, co2_va):
        self.pm_val = pm_va
        self.co_val= co_va
        self.co2_val = co2_va
        self.pm_aqi = 0
        self.co_aqi = 0
        self.co2_aqi = 0

    # iaqi计算公式
    def aqi_cal_formula(self, hi, lo, bplo, bphi, val):
        aqi_cal = (hi - lo) * (val - bplo) / (bphi - bplo) + lo
        return aqi_cal

    # 计算pm2.5的iaqi
    def pm_aqi_cal(self):
        if 0 < self.pm_val <= 35:
            pm_aqi = self.aqi_cal_formula(0, 50, 0, 35, self.pm_val)
        elif 35 < self.pm_val <= 75:
            pm_aqi = self.aqi_cal_formula(50, 100, 35, 75, self.pm_val)
        elif 75 < self.pm_val <= 115:
            self.pm_aqi = self.aqi_cal_formula(100, 150, 75, 115, self.pm_val)
        elif 115 < self.pm_val <= 150:
            self.pm_aqi = self.aqi_cal_formula(100, 150, 115, 150, self.pm_val)
        elif 150 < self.pm_val <= 250:
            self.pm_aqi = self.aqi_cal_formula(150, 250, 150, 250, self.pm_val)
        elif 250 < self.pm_val <= 350:
            self.pm_aqi = self.aqi_cal_formula(300, 400, 250, 350, self.pm_val)
        elif 350 < self.pm_val <= 500:
            self.pm_aqi = self.aqi_cal_formula(400, 500, 350, 500, self.pm_val)

        return pm_aqi

    def co_aqi_cal(self):
        if 0 < self.co_val <= 35:
            self.co_aqi = self.aqi_cal_formula(0, 50, 0, 35, self.pm_val)
        elif 35 < self.pm_val <= 75:
            self.co_aqi = self.aqi_cal_formula(50, 100, 35, 75, self.pm_val)
        elif 75 < self.pm_val <= 115:
            self.pm_aqi = self.aqi_cal_formula(100, 150, 75, 115, self.pm_val)
        elif 115 < self.pm_val <= 150:
            self.pm_aqi = self.aqi_cal_formula(100, 150, 115, 150, self.pm_val)
        elif 150 < self.pm_val <= 250:
            self.pm_aqi = self.aqi_cal_formula(150, 250, 150, 250, self.pm_val)
        elif 250 < self.pm_val <= 350:
            self.pm_aqi = self.aqi_cal_formula(300, 400, 250, 350, self.pm_val)
        elif 350 < self.pm_val <= 500:
            self.pm_aqi = self.aqi_cal_formula(400, 500, 350, 500, self.pm_val)
        return self.co_aqi

    def co2_aqi_cal(self):
        if 0 < self.co_val <= 35:
            self.co2_aqi = self.aqi_cal_formula(0, 50, 0, 35, self.pm_val)
        elif 35 < self.pm_val <= 75:
            self.co_aqi = self.aqi_cal_formula(50, 100, 35, 75, self.pm_val)
        elif 75 < self.pm_val <= 115:
            self.pm_aqi = self.aqi_cal_formula(100, 150, 75, 115, self.pm_val)
        elif 115 < self.pm_val <= 150:
            self.pm_aqi = self.aqi_cal_formula(100, 150, 115, 150, self.pm_val)
        elif 150 < self.pm_val <= 250:
            self.pm_aqi = self.aqi_cal_formula(150, 250, 150, 250, self.pm_val)
        elif 250 < self.pm_val <= 350:
            self.pm_aqi = self.aqi_cal_formula(300, 400, 250, 350, self.pm_val)
        elif 350 < self.pm_val <= 500:
            self.pm_aqi = self.aqi_cal_formula(400, 500, 350, 500, self.pm_val)
        return self.co2_aqi


    def aqical(self):
        iaqi_list = []
        pm_aqi = self.pm_aqi_cal()
        co_aqi = self.co_aqi_cal()
        co2_aqi = self.co2_aqi_cal()
        iaqi_list.append(pm_aqi)
        iaqi_list.append(co_aqi)
        iaqi_list.append(co2_aqi)

        self.aqi = max(iaqi_list)
        return self.aqi


# 计算aqi值的函数
def aqiVal(pm_val, co_val, co2_val):
    # 实例化AqiCal
    aqiCal = AqiCal(pm_val, co_val, co2_val)

    aqi_val = aqiCal.aqical()
    return aqi_val


def main():
    print('请分别输入今日测量的PM2.5、CO、CO2的值：')
    input_str = input('（如29.3、30、55）')
    str_list = input_str.split("、")
    pm_val = float(str_list[0])
    co_val = float(str_list[1])
    co2_val = float(str_list[2])

    # 调用函数，计算aqi的值
    aqi_val = aqiVal(pm_val, co_val, co2_val)

    print('今天的AQI为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
