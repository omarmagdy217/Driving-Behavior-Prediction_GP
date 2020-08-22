#ifndef __SYSTICK_H__
#define	__SYSTICK_H__

#include "micro_config.h"
void systick_init(void);
void systick_wait(uint32_t delay);
void _delay_ms(uint32_t time);

#endif