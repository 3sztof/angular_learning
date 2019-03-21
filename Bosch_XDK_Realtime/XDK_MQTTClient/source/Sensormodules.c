/*
 * Sensormodules.c
 *
 *  Created on: Aug 28, 2018
 *      Author: FUQ1DON
 */

/* own header files */
#include "XdkSensorHandle.h"
#include "BCDS_Retcode.h"
/* system header files */
#include <stdio.h>
#include "BCDS_Basics.h"
#include "BCDS_Assert.h"
#include "BCDS_CmdProcessor.h"
#include "Sensormodules.h"

/**
 * @brief To initialize environmental BME280 sensor driver
 *
 */
void InitEnvironmentalSensor(void)
{
    Retcode_T retcode = Environmental_init(xdkEnvironmental_BME280_Handle);
    if (RETCODE_OK != retcode)
    {
        printf("Environmental_init is failed \n\r");
        Retcode_RaiseError(retcode);
    }
}
/**
 * @brief To initialize Accelerometer BMA280 sensor driver
 *
 */
void InitAcceleromterSensor(void)
{
    Retcode_T retcode = Accelerometer_init(xdkAccelerometers_BMA280_Handle);
    if (RETCODE_OK == retcode)
    {
    	retcode=Accelerometer_setBandwidth(xdkAccelerometers_BMA280_Handle, ACCELEROMETER_BMA280_BANDWIDTH_125HZ);
    }
    if (RETCODE_OK == retcode)
    {
    	retcode=Accelerometer_setRange(xdkAccelerometers_BMA280_Handle, ACCELEROMETER_BMA280_RANGE_2G);
    }
    if (RETCODE_OK == retcode)
    {
    	retcode=Accelerometer_setMode(xdkAccelerometers_BMA280_Handle, ACCELEROMETER_BMA280_POWERMODE_NORMAL);
    }
    if (RETCODE_OK != retcode)
    {
        printf("Accelerometer_init is failed \n\r");
        Retcode_RaiseError(retcode);
    }
}
/**
 * @brief To initialize Gyroscope BMG160 sensor driver
 *
 */
void InitGyroscopeSensor(void)
{
    Retcode_T retcode = Gyroscope_init(xdkGyroscope_BMG160_Handle);
    if (RETCODE_OK == retcode)
    {
    	retcode=Gyroscope_setBandwidth(xdkGyroscope_BMG160_Handle, GYROSCOPE_BMG160_BANDWIDTH_116HZ);
    }
    if (RETCODE_OK == retcode)
    {
    	retcode=Gyroscope_setRange(xdkGyroscope_BMG160_Handle, GYROSCOPE_BMG160_RANGE_250s);
    }
    if (RETCODE_OK == retcode)
    {
    	retcode=Gyroscope_setMode(xdkGyroscope_BMG160_Handle, GYROSCOPE_BMG160_POWERMODE_NORMAL);
    }
    if (RETCODE_OK != retcode)
    {
        printf("Gyroscope_init is failed \n\r");
        Retcode_RaiseError(retcode);
    }
}
/**
 * @brief To initialize Light_MAX44009 sensor driver
 *
 */
void InitLightSensor(void)
{
	Retcode_T retcode =LightSensor_init(xdkLightSensor_MAX44009_Handle);
	if (RETCODE_OK == retcode)
	{
		retcode=LightSensor_setContinuousMode(xdkLightSensor_MAX44009_Handle, LIGHTSENSOR_MAX44009_ENABLE_MODE);
	}
    if (RETCODE_OK != retcode)
    {
        printf("LightSensor_init is failed \n\r");
        Retcode_RaiseError(retcode);
    }
}
/**
 * @brief To read environmental sensor data
 *
 * @return Environmental sensor data in standard units
 */
Environmental_Data_T ReadEnvironmentSensor(void)
{

    Environmental_Data_T bme280 = { 0, 0, 0 };
    Retcode_T retcode = Environmental_readCompensatedData(xdkEnvironmental_BME280_Handle, &bme280);
    if (RETCODE_OK != retcode)
    {
        bme280.humidity = 0;
        bme280.pressure = 0;
        bme280.temperature = 0;
    }
    return bme280;
}
/**
 * @brief To read Accelerometer sensor data
 *
 * @return Accelerometer sensor data in standard units
 */
Accelerometer_XyzData_T ReadAccelerometerSensor(void)
{

	Accelerometer_XyzData_T bma280 = { 0, 0, 0 };
    Retcode_T retcode = Accelerometer_readXyzGValue(xdkAccelerometers_BMA280_Handle, &bma280);
    if (RETCODE_OK != retcode)
    {
        bma280.xAxisData = 0;
        bma280.yAxisData = 0;
        bma280.zAxisData = 0;
    }
    return bma280;
}
/**
 * @brief To read Gyroscope sensor data
 *
 * @return Gyroscope sensor data in standard units
 */
Gyroscope_XyzData_T ReadGyroscopeSensor(void)
{

	Gyroscope_XyzData_T bmg160 = { 0, 0, 0 };
    Retcode_T retcode = Gyroscope_readXyzDegreeValue(xdkGyroscope_BMG160_Handle,&bmg160);
    if (RETCODE_OK != retcode)
    {
        bmg160.xAxisData = 0;
        bmg160.yAxisData = 0;
        bmg160.zAxisData = 0;
    }
    return bmg160;
}

/**
 * @brief To read Light sensor data
 *
 * @return Light sensor data in standard units
 */
uint32_t ReadLightSensor(void)
{

	uint32_t max44009 = 0;
    Retcode_T retcode = LightSensor_readLuxData (xdkLightSensor_MAX44009_Handle,&max44009);
    if (RETCODE_OK != retcode)
    {
    	max44009=0;
    }
    return max44009;
}
