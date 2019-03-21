/*
 * InitSensor.h
 *
 *  Created on: Aug 28, 2018
 *      Author: FUQ1DON
 */

#ifndef SOURCE_SENSORMODULES_H_
#define SOURCE_SENSORMODULES_H_
#include "BCDS_Retcode.h"
#include "XdkSensorHandle.h"


extern void InitEnvironmentalSensor(void);
extern void InitAcceleromterSensor(void);
extern void InitGyroscopeSensor(void);
extern void InitLightSensor(void);
extern Environmental_Data_T ReadEnvironmentSensor(void);
extern Accelerometer_XyzData_T ReadAccelerometerSensor(void);
extern Gyroscope_XyzData_T ReadGyroscopeSensor(void);
extern uint32_t ReadLightSensor(void);


#endif /* SOURCE_SENSORMODULES_H_ */
