#ifndef __UART_H__
#define	__UART_H__

#include "micro_config.h"

void UART_Init(uint8_t index);

uint8_t UART_Available(uint8_t index);

uint8_t UART_Read(uint8_t index);
void UART_Write(uint8_t index,uint8_t data);
void UART_sendString(const uint8_t *Str);

void UART_receiveString(uint8_t *Str);


#endif // __UART_H__