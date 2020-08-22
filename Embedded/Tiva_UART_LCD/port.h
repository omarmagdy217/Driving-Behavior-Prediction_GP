#ifndef PORT_H_
#define PORT_H_

#include "micro_config.h"

typedef enum
{
	PORT_PIN_IN , PORT_PIN_OUT
}Port_PinDirectionType;

/*******************************************************************************
 *                      Functions Prototypes                                   *
 *******************************************************************************/

void Port_Init(uint8_t port_index);
void Port_SetPinDirection(uint8_t port_index , uint8_t pins_mask , Port_PinDirectionType pins_direction);
void Port_SetPinPullDown( uint8_t port_index , uint8_t pins_mask ,uint8_t enable);
void Port_SetPinPullUp( uint8_t port_index , uint8_t pins_mask ,uint8_t enable);

#endif