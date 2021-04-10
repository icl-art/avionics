# adapted from https://github.com/larsks/py-mpu6050

# constants extracted from
# https://github.com/jrowberg/i2cdevlib/blob/master/Arduino/MPU6050/MPU6050.h

MPU6050_ADDRESS_AD0_LOW               = 0x68
MPU6050_ADDRESS_AD0_HIGH              = 0x69
MPU6050_DEFAULT_ADDRESS               = MPU6050_ADDRESS_AD0_LOW
MPU6050_RA_XG_OFFS_TC                 = 0x00
MPU6050_RA_YG_OFFS_TC                 = 0x01
MPU6050_RA_ZG_OFFS_TC                 = 0x02
MPU6050_RA_X_FINE_GAIN                = 0x03
MPU6050_RA_Y_FINE_GAIN                = 0x04
MPU6050_RA_Z_FINE_GAIN                = 0x05
MPU6050_RA_XA_OFFS_H                  = 0x06
MPU6050_RA_XA_OFFS_L_TC               = 0x07
MPU6050_RA_YA_OFFS_H                  = 0x08
MPU6050_RA_YA_OFFS_L_TC               = 0x09
MPU6050_RA_ZA_OFFS_H                  = 0x0A
MPU6050_RA_ZA_OFFS_L_TC               = 0x0B
MPU6050_RA_SELF_TEST_X                = 0x0D
MPU6050_RA_SELF_TEST_Y                = 0x0E
MPU6050_RA_SELF_TEST_Z                = 0x0F
MPU6050_RA_SELF_TEST_A                = 0x10
MPU6050_RA_XG_OFFS_USRH               = 0x13
MPU6050_RA_XG_OFFS_USRL               = 0x14
MPU6050_RA_YG_OFFS_USRH               = 0x15
MPU6050_RA_YG_OFFS_USRL               = 0x16
MPU6050_RA_ZG_OFFS_USRH               = 0x17
MPU6050_RA_ZG_OFFS_USRL               = 0x18
MPU6050_RA_SMPLRT_DIV                 = 0x19
MPU6050_RA_CONFIG                     = 0x1A
MPU6050_RA_GYRO_CONFIG                = 0x1B
MPU6050_RA_ACCEL_CONFIG               = 0x1C
MPU6050_RA_FF_THR                     = 0x1D
MPU6050_RA_FF_DUR                     = 0x1E
MPU6050_RA_MOT_THR                    = 0x1F
MPU6050_RA_MOT_DUR                    = 0x20
MPU6050_RA_ZRMOT_THR                  = 0x21
MPU6050_RA_ZRMOT_DUR                  = 0x22
MPU6050_RA_FIFO_EN                    = 0x23
MPU6050_RA_INT_PIN_CFG                = 0x37
MPU6050_RA_INT_ENABLE                 = 0x38
MPU6050_RA_DMP_INT_STATUS             = 0x39
MPU6050_RA_INT_STATUS                 = 0x3A
MPU6050_RA_ACCEL_XOUT_H               = 0x3B
MPU6050_RA_ACCEL_XOUT_L               = 0x3C
MPU6050_RA_ACCEL_YOUT_H               = 0x3D
MPU6050_RA_ACCEL_YOUT_L               = 0x3E
MPU6050_RA_ACCEL_ZOUT_H               = 0x3F
MPU6050_RA_ACCEL_ZOUT_L               = 0x40
MPU6050_RA_TEMP_OUT_H                 = 0x41
MPU6050_RA_TEMP_OUT_L                 = 0x42
MPU6050_RA_GYRO_XOUT_H                = 0x43
MPU6050_RA_GYRO_XOUT_L                = 0x44
MPU6050_RA_GYRO_YOUT_H                = 0x45
MPU6050_RA_GYRO_YOUT_L                = 0x46
MPU6050_RA_GYRO_ZOUT_H                = 0x47
MPU6050_RA_GYRO_ZOUT_L                = 0x48
MPU6050_RA_MOT_DETECT_STATUS          = 0x61
MPU6050_RA_SIGNAL_PATH_RESET          = 0x68
MPU6050_RA_MOT_DETECT_CTRL            = 0x69
MPU6050_RA_USER_CTRL                  = 0x6A
MPU6050_RA_PWR_MGMT_1                 = 0x6B
MPU6050_RA_PWR_MGMT_2                 = 0x6C
MPU6050_RA_BANK_SEL                   = 0x6D
MPU6050_RA_MEM_START_ADDR             = 0x6E
MPU6050_RA_MEM_R_W                    = 0x6F
MPU6050_RA_DMP_CFG_1                  = 0x70
MPU6050_RA_DMP_CFG_2                  = 0x71
MPU6050_RA_FIFO_COUNTH                = 0x72
MPU6050_RA_FIFO_COUNTL                = 0x73
MPU6050_RA_FIFO_R_W                   = 0x74
MPU6050_RA_WHO_AM_I                   = 0x75
MPU6050_TC_PWR_MODE_BIT               = 7
MPU6050_TC_OFFSET_BIT                 = 6
MPU6050_TC_OFFSET_LENGTH              = 6
MPU6050_TC_OTP_BNK_VLD_BIT            = 0
MPU6050_VDDIO_LEVEL_VLOGIC            = 0
MPU6050_VDDIO_LEVEL_VDD               = 1
MPU6050_CFG_EXT_SYNC_SET_BIT          = 5
MPU6050_CFG_EXT_SYNC_SET_LENGTH       = 3
MPU6050_CFG_DLPF_CFG_BIT              = 2
MPU6050_CFG_DLPF_CFG_LENGTH           = 3
MPU6050_DLPF_BW_256                   = 0x00
MPU6050_DLPF_BW_188                   = 0x01
MPU6050_DLPF_BW_98                    = 0x02
MPU6050_DLPF_BW_42                    = 0x03
MPU6050_DLPF_BW_20                    = 0x04
MPU6050_DLPF_BW_10                    = 0x05
MPU6050_DLPF_BW_5                     = 0x06
MPU6050_GCONFIG_FS_SEL_BIT            = 4
MPU6050_GCONFIG_FS_SEL_LENGTH         = 2
MPU6050_GYRO_FS_250                   = 0x00
MPU6050_GYRO_FS_500                   = 0x01
MPU6050_GYRO_FS_1000                  = 0x02
MPU6050_GYRO_FS_2000                  = 0x03
MPU6050_ACONFIG_XA_ST_BIT             = 7
MPU6050_ACONFIG_YA_ST_BIT             = 6
MPU6050_ACONFIG_ZA_ST_BIT             = 5
MPU6050_ACONFIG_AFS_SEL_BIT           = 4
MPU6050_ACONFIG_AFS_SEL_LENGTH        = 2
MPU6050_ACONFIG_ACCEL_HPF_BIT         = 2
MPU6050_ACONFIG_ACCEL_HPF_LENGTH      = 3
MPU6050_ACCEL_FS_2                    = 0x00
MPU6050_ACCEL_FS_4                    = 0x01
MPU6050_ACCEL_FS_8                    = 0x02
MPU6050_ACCEL_FS_16                   = 0x03
MPU6050_DHPF_RESET                    = 0x00
MPU6050_DHPF_5                        = 0x01
MPU6050_DHPF_2P5                      = 0x02
MPU6050_DHPF_1P25                     = 0x03
MPU6050_DHPF_0P63                     = 0x04
MPU6050_DHPF_HOLD                     = 0x07
MPU6050_TEMP_FIFO_EN_BIT              = 7
MPU6050_XG_FIFO_EN_BIT                = 6
MPU6050_YG_FIFO_EN_BIT                = 5
MPU6050_ZG_FIFO_EN_BIT                = 4
MPU6050_ACCEL_FIFO_EN_BIT             = 3
MPU6050_INTCFG_INT_LEVEL_BIT          = 7
MPU6050_INTCFG_INT_OPEN_BIT           = 6
MPU6050_INTCFG_LATCH_INT_EN_BIT       = 5
MPU6050_INTCFG_INT_RD_CLEAR_BIT       = 4
MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT    = 3
MPU6050_INTCFG_FSYNC_INT_EN_BIT       = 2
MPU6050_INTCFG_CLKOUT_EN_BIT          = 0
MPU6050_INTMODE_ACTIVEHIGH            = 0x00
MPU6050_INTMODE_ACTIVELOW             = 0x01
MPU6050_INTDRV_PUSHPULL               = 0x00
MPU6050_INTDRV_OPENDRAIN              = 0x01
MPU6050_INTLATCH_50USPULSE            = 0x00
MPU6050_INTLATCH_WAITCLEAR            = 0x01
MPU6050_INTCLEAR_STATUSREAD           = 0x00
MPU6050_INTCLEAR_ANYREAD              = 0x01
MPU6050_INTERRUPT_FF_BIT              = 7
MPU6050_INTERRUPT_MOT_BIT             = 6
MPU6050_INTERRUPT_ZMOT_BIT            = 5
MPU6050_INTERRUPT_FIFO_OFLOW_BIT      = 4
MPU6050_INTERRUPT_PLL_RDY_INT_BIT     = 2
MPU6050_INTERRUPT_DMP_INT_BIT         = 1
MPU6050_INTERRUPT_DATA_RDY_BIT        = 0
MPU6050_DMPINT_5_BIT                  = 5
MPU6050_DMPINT_4_BIT                  = 4
MPU6050_DMPINT_3_BIT                  = 3
MPU6050_DMPINT_2_BIT                  = 2
MPU6050_DMPINT_1_BIT                  = 1
MPU6050_DMPINT_0_BIT                  = 0
MPU6050_MOTION_MOT_XNEG_BIT           = 7
MPU6050_MOTION_MOT_XPOS_BIT           = 6
MPU6050_MOTION_MOT_YNEG_BIT           = 5
MPU6050_MOTION_MOT_YPOS_BIT           = 4
MPU6050_MOTION_MOT_ZNEG_BIT           = 3
MPU6050_MOTION_MOT_ZPOS_BIT           = 2
MPU6050_MOTION_MOT_ZRMOT_BIT          = 0
MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT = 7
MPU6050_PATHRESET_GYRO_RESET_BIT      = 2
MPU6050_PATHRESET_ACCEL_RESET_BIT     = 1
MPU6050_PATHRESET_TEMP_RESET_BIT      = 0
MPU6050_DETECT_ACCEL_ON_DELAY_BIT     = 5
MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH  = 2
MPU6050_DETECT_FF_COUNT_BIT           = 3
MPU6050_DETECT_FF_COUNT_LENGTH        = 2
MPU6050_DETECT_MOT_COUNT_BIT          = 1
MPU6050_DETECT_MOT_COUNT_LENGTH       = 2
MPU6050_DETECT_DECREMENT_RESET        = 0x0
MPU6050_DETECT_DECREMENT_1            = 0x1
MPU6050_DETECT_DECREMENT_2            = 0x2
MPU6050_DETECT_DECREMENT_4            = 0x3
MPU6050_USERCTRL_DMP_EN_BIT           = 7
MPU6050_USERCTRL_FIFO_EN_BIT          = 6
MPU6050_USERCTRL_DMP_RESET_BIT        = 3
MPU6050_USERCTRL_FIFO_RESET_BIT       = 2
MPU6050_USERCTRL_SIG_COND_RESET_BIT   = 0
MPU6050_PWR1_DEVICE_RESET_BIT         = 7
MPU6050_PWR1_SLEEP_BIT                = 6
MPU6050_PWR1_CYCLE_BIT                = 5
MPU6050_PWR1_TEMP_DIS_BIT             = 3
MPU6050_PWR1_CLKSEL_BIT               = 2
MPU6050_PWR1_CLKSEL_LENGTH            = 3
MPU6050_CLOCK_INTERNAL                = 0x00
MPU6050_CLOCK_PLL_XGYRO               = 0x01
MPU6050_CLOCK_PLL_YGYRO               = 0x02
MPU6050_CLOCK_PLL_ZGYRO               = 0x03
MPU6050_CLOCK_PLL_EXT32K              = 0x04
MPU6050_CLOCK_PLL_EXT19M              = 0x05
MPU6050_CLOCK_KEEP_RESET              = 0x07
MPU6050_PWR2_LP_WAKE_CTRL_BIT         = 7
MPU6050_PWR2_LP_WAKE_CTRL_LENGTH      = 2
MPU6050_PWR2_STBY_XA_BIT              = 5
MPU6050_PWR2_STBY_YA_BIT              = 4
MPU6050_PWR2_STBY_ZA_BIT              = 3
MPU6050_PWR2_STBY_XG_BIT              = 2
MPU6050_PWR2_STBY_YG_BIT              = 1
MPU6050_PWR2_STBY_ZG_BIT              = 0
MPU6050_WAKE_FREQ_1P25                = 0x0
MPU6050_WAKE_FREQ_2P5                 = 0x1
MPU6050_WAKE_FREQ_5                   = 0x2
MPU6050_WAKE_FREQ_10                  = 0x3
MPU6050_WHO_AM_I_BIT                  = 6
MPU6050_WHO_AM_I_LENGTH               = 6
MPU_SCL_PIN                           = 13
MPU_SDA_PIN                           = 12
MPU_DATA_RDY_PIN                      = 14
MPU_ADDR                              = MPU6050_DEFAULT_ADDRESS

from machine import Pin, I2C
import utime
from ustruct import unpack

accel_range = [2, 4, 8, 16]
gyro_range = [250, 500, 1000, 2000]

class MPU6050Data:
    def __init__(self):
        self.Gx=0
        self.Gy=0
        self.Gz=0
        self.Temperature=0
        self.Gyrox=0
        self.Gyroy=0
        self.Gyroz=0

class MPU6050(object):
    def __init__(self, bus=0, scl=13, sda=12, rate=0x20):

        self.scl = scl
        self.sda = sda
        self.rate = rate

        self.address = MPU6050_DEFAULT_ADDRESS

        self.buffer = bytearray(16)
        self.bytebuf = memoryview(self.buffer[0:1])
        self.wordbuf = memoryview(self.buffer[0:2])
        self.sensors = bytearray(14)

        self.bus = I2C(bus, scl=self.scl, sda=self.sda)
        
        self.gyro_lookup = {250: MPU6050_GYRO_FS_250, 500: MPU6050_GYRO_FS_500, 
        1000: MPU6050_GYRO_FS_1000, 2000: MPU6050_GYRO_FS_2000}

        self.acc_lookup = {2: MPU6050_ACCEL_FS_2, 4: MPU6050_ACCEL_FS_4, 
        8: MPU6050_ACCEL_FS_8, 16: MPU6050_ACCEL_FS_16}

        self.acc_rng = 16
        self.gyro_rng = 500

        self.init_device()

    def write_byte(self, reg, val):
        self.bytebuf[0] = val
        self.bus.writeto_mem(self.address, reg, self.bytebuf)

    def read_byte(self, reg):
        self.bus.readfrom_mem_into(self.address, reg, self.bytebuf)
        return self.bytebuf[0]

    def set_bitfield(self, reg, pos, length, val):
        old = self.read_byte(reg)
        shift = pos - length + 1
        mask = (2**length - 1) << shift
        new = (old & ~mask) | (val << shift)
        self.write_byte(reg, new)

    # def read_word(self, reg):
    #     self.bus.readfrom_mem_into(self.address, reg, self.wordbuf)
    #     return unpack('>H', self.wordbuf)[0]

    # def read_word2(self, reg):
    #     self.bus.readfrom_mem_into(self.address, reg, self.wordbuf)
    #     return unpack('>h', self.wordbuf)[0]
        
    def identify(self):
        val = self.read_byte(MPU6050_RA_WHO_AM_I)
        if val != MPU6050_ADDRESS_AD0_LOW:
            raise OSError("No mpu6050 at address {}".format(self.address))

    def reset(self):
        print('* reset')
        self.write_byte(MPU6050_RA_PWR_MGMT_1, (
            (1 << MPU6050_PWR1_DEVICE_RESET_BIT)
        ))
        utime.sleep_ms(100)

        self.write_byte(MPU6050_RA_SIGNAL_PATH_RESET, (
            (1 << MPU6050_PATHRESET_GYRO_RESET_BIT) |
            (1 << MPU6050_PATHRESET_ACCEL_RESET_BIT) |
            (1 << MPU6050_PATHRESET_TEMP_RESET_BIT)
        ))
        utime.sleep_ms(100)

    def init_device(self):
        self.identify()

        # disable sleep mode and select clock source
        self.write_byte(MPU6050_RA_PWR_MGMT_1, MPU6050_CLOCK_PLL_XGYRO)

        # enable all sensors
        self.write_byte(MPU6050_RA_PWR_MGMT_2, 0)

        # set sampling rate
        self.write_byte(MPU6050_RA_SMPLRT_DIV, self.rate)

        # enable dlpf
        self.write_byte(MPU6050_RA_CONFIG, 1)

        # explicitly set accel/gyro range
        self.set_accel_range(self.acc_rng)
        self.set_gyro_range(self.gyro_rng)

    def set_gyro_range(self, rng):
        self.gyro_range = rng
        fsr = self.gyro_lookup[rng]

        self.set_bitfield(MPU6050_RA_GYRO_CONFIG,
                          MPU6050_GCONFIG_FS_SEL_BIT,
                          MPU6050_GCONFIG_FS_SEL_LENGTH,
                          fsr)

    def set_accel_range(self, rng):

        self.accel_range = rng
        fsr = self.acc_lookup[rng]

        self.set_bitfield(MPU6050_RA_ACCEL_CONFIG,
                          MPU6050_ACONFIG_AFS_SEL_BIT,
                          MPU6050_ACONFIG_AFS_SEL_LENGTH,
                          fsr)

    def read_sensors(self):
        self.bus.readfrom_mem_into(self.address,
                                   MPU6050_RA_ACCEL_XOUT_H,
                                   self.sensors)

        data = unpack('>hhhhhhh', self.sensors)

        return [data[i] for i in range(7)]

    def read_sensors_scaled(self):
        data = self.read_sensors()
        data[0:3] = [x/(65536//self.accel_range//2) for x in data[0:3]]
        data[4:7] = [x/(65536//self.gyro_range//2) for x in data[4:7]]
        return data
    
    def read(self):
        data = MPU6050Data()
        unpacked = self.read_sensors_scaled()

        data.Gx = unpacked[0]
        data.Gy = unpacked[1]
        data.Gz = unpacked[2]
        data.Temperature = unpacked[3]
        data.Gyrox = unpacked[4]
        data.Gyroy = unpacked[5]
        data.Gyroz = unpacked[6]

        return data
    

    